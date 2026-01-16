from fastapi import APIRouter,Depends
from ..core.dependencies import require_role
from .schemas import UserResponse
from .service import change_role_service,update_is_active_db
router = APIRouter()


@router.patch("/admin/users/{id}",response_model=UserResponse)
def change_to_admin(id ,admin = Depends(require_role(required_role="admin"))):
    return change_role_service(user_id=id,role="admin")

@router.post("/admin/users/{id}",response_model=UserResponse)
def ban_user(id,admin = Depends(require_role("admin"))):
    return update_is_active_db(user_id=id)

# coba tanya chat gpt cara bikin restful api yang bener, contonya kode di atas
    



