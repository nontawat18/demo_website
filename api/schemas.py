from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    firstname : str
    lastname : str
    age : int
    email : str
    phone : int
    position : str
    currentSalary : str
    expectedSalary : str
    address : str
    dateSubmit : str
    status : str
    
class AdminSchema(BaseModel):
    id: int
    username : str
    password : str
 