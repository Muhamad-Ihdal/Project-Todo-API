from fastapi import APIRouter,Depends
from .schemas import SuccessTodoResponse,SuccessTodosResponse,CreateTodoRequest
from ..core.dependencies import get_current_user,require_role
from .service import create_todo_service
from .service import get_todos_service
router = APIRouter()

@router.post("todos/",response_model=SuccessTodoResponse)
def create_todo(spec:CreateTodoRequest,user = Depends(get_current_user)):
    return create_todo_service(user,spec)
    
@router.get("todos/",response_model=SuccessTodosResponse)
def get_todos(user = Depends(get_current_user)):
    return get_todos_service(user)