from fastapi import APIRouter,Depends
from .schemas import SuccessResponse,CreateTodoRequest
from ..core.dependencies import get_current_user,require_role
from .service import create_todo_service
router = APIRouter()

@router.post("todos/",response_model=SuccessResponse)
def create_todo(spec:CreateTodoRequest,user = Depends(get_current_user)):
    return create_todo_service(user,spec)
    
