from fastapi import APIRouter,Depends
from ..core.dependencies import require_role
from .schemas import IdRequest,UserResponse
from .service import change_role_service,update_is_active_db
router = APIRouter()


@router.post("/admin/users/create_admin",response_model=UserResponse)
def change_to_admin(user_id : IdRequest,creator = Depends(require_role(required_role="admin"))):
    return change_role_service(user_id,role="admin")

@router.post("/admin/users/ban_user",response_model=UserResponse)
def ban_user(user_id :IdRequest ,admin = Depends(require_role("admin"))):
    return update_is_active_db(user_id=user_id,is_active=0)
    



