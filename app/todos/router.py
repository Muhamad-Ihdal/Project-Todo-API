from fastapi import APIRouter,Depends
from .schemas import SuccessTodoResponse,SuccessTodosResponse,CreateTodoRequest,EditTodoRequest
from ..core.dependencies import get_current_user,require_role
from .service import delete_todo_service,create_todo_service,get_todos_service,get_todo_by_id_service,edit_todo_service
router = APIRouter()

@router.post("todos/",response_model=SuccessTodoResponse)
def create_todo(spec:CreateTodoRequest,user = Depends(get_current_user)):
    return create_todo_service(user,spec)
    
@router.get("todos/",response_model=SuccessTodosResponse)
def get_todos(user = Depends(get_current_user)):
    return get_todos_service(user)

@router.get("todos/{id}",response_model=SuccessTodoResponse)
def get_todo_by_id_router(id:int,user = Depends(get_current_user)):
    return get_todo_by_id_service(id,user)

@router.patch("todos/{id}",response_model=SuccessTodoResponse)
def edit_todo(edit:EditTodoRequest,id:int,user = Depends(get_current_user)):
    return edit_todo_service(edit=edit,todo_id=id,user=user)

@router.delete("todos/{id}",response_model=SuccessTodoResponse)
def edit_todo(id:int,user = Depends(get_current_user)):
    return delete_todo_service(todo_id=id,user=user)