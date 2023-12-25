from fastapi import FastAPI, HTTPException,Depends, File, UploadFile, HTTPException,status
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import sqlite3
import csv
from models import User, Base, Admin
from schemas import UserSchema
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from fastapi_login import LoginManager
from fastapi.middleware.cors import CORSMiddleware
import csv
from io import StringIO
import csv
import io
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

Base.metadata.create_all(bind=engine)

app = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:3000",  
    "http://localhost:5173",  
    "http://127.0.0.1:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Item(BaseModel):
    description: str
    

@app.post("/submit-work")
async def add_user(request:UserSchema, db: Session = Depends(get_db)):
    user = User(firstname=request.firstname, lastname=request.lastname, age=request.age, email=request.email, phone=request.phone, position=request.position,currentSalary=request.currentSalary,expectedSalary=request.expectedSalary,address=request.address,dateSubmit=request.dateSubmit,status=request.status)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.put("/update-work/{id}")
async def delete_work(id,updated_user:UserSchema,db: Session = Depends(get_db)):

    updated_post = db.query(User).filter(User.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'update wite such id: {id} does not exist')
    else:
        updated_post.update(updated_user.dict(), synchronize_session=False)
        db.commit()
    return updated_post.first()

@app.get("/get-all/")
async def get_all(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return  users

@app.delete("/submit-work/{id}")
async def delete_work(id,db: Session = Depends(get_db)):
    delete_work = db.query(User).filter(User.id == id)
    delete_work.delete(synchronize_session=False)
    db.commit()
    return  "success!"

@app.get("/submit-work/{date}")
async def get_by_date(date,db: Session = Depends(get_db)):
    delete_work = db.query(User).filter(User.dateSubmit == date).all()
    
    return  delete_work


SECRET_KEY = b'your-secret-key'
manager = LoginManager(SECRET_KEY, token_url="/token", use_cookie=True)
users_db = {
    "testuser": {
        "username": "testuser",
        "password": "testpassword",
    }
}

class Username(BaseModel):
    username: str
    password: str

@manager.user_loader()
def load_user(username: str):
    user_data = users_db.get(username)
    if user_data:
        return User(username=user_data["username"])

@app.post("/token")
async def login(data: Username):
    user_data = users_db.get(data.username)
    if user_data and data.password == user_data["password"]:
        access_token = manager.create_access_token(
            data=dict(sub=data.username),
        )
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Invalid credentials")



def get_data_from_database(db: Session):
    data = db.query(User).all()
    return data

def generate_csv(data):
    csv_data = io.StringIO()
    csv_writer = csv.writer(csv_data)

    header = User.__table__.columns.keys()
    csv_writer.writerow(header)

    for item in data:
        row = [str(getattr(item, column)) for column in header]
        csv_writer.writerow(row)

    return csv_data.getvalue()

@app.get("/export/csv")
def export_to_csv(db: Session = Depends(get_db)):
    data = get_data_from_database(db)
    csv_content = generate_csv(data)
    with open("exported_data.csv", "w") as file:
        file.write(csv_content)
   
    headers = {
        "Content-Disposition": "attachment;filename=data.csv",
        "Content-Type": "text/csv",
    }

    return FileResponse("exported_data.csv", filename="exported_data.csv")
