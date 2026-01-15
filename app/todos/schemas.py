from pydantic import BaseModel,EmailStr


class UserResponse(BaseModel):
    id:int
    email:str
    role:str
    is_active: bool | int | str
    created_at: str
    todo: list | dict | None = None

class SuccessResponse(BaseModel):
    success: bool
    message:str
    data: UserResponse

class CreateTodoRequest(BaseModel):
    title:str
    description:str