from sqlalchemy import Column, Integer, String
from database import Base



class User(Base):
    __tablename__ = "people_submit_work"
    
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    email = Column(String)
    phone = Column(String)
    position = Column(String)
    currentSalary = Column(String)
    expectedSalary = Column(String)
    address = Column(String)
    dateSubmit = Column(String)
    status = Column(String)
    
    
class Admin(Base):
    __tablename__ = "admin"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    






    