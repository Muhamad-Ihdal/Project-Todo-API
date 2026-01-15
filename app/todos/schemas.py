from pydantic import BaseModel,EmailStr


class TodoResponse(BaseModel):
    id :int 
    owner_id : int 
    title :str
    description :str
    status : str
    created_at : any
    deleted_at : any
    update_at : any


class UserWithTodoResponse(BaseModel):
    id:int
    email:str
    role:str
    is_active: bool | int | str
    created_at: str
    todo: TodoResponse

class UserWithTodosResponse(BaseModel):
    id:int
    email:str
    role:str
    is_active: bool | int | str
    created_at: str
    todos: list[TodoResponse]

class SuccessTodoResponse(BaseModel):
    success: bool
    message:str
    data: UserWithTodoResponse
    
class SuccessTodosResponse(BaseModel):
    success: bool
    message:str
    data: UserWithTodosResponse

class CreateTodoRequest(BaseModel):
    title:str
    description:str