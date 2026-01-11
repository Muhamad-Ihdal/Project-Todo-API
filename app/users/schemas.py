from pydantic import BaseModel,EmailStr

class ToAdminRequest(BaseModel):
    id:int

class UserResponse(BaseModel):
    email:str
    role:str
    is_active: bool | str