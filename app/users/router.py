from fastapi import APIRouter,Depends
from ..core.dependencies import require_role
from .schemas import ToAdminRequest
from .service import change_role_service
router = APIRouter()


@router.post("/admin/users/create_admin")
def to_admin(creator = Depends(require_role(required_role="admin")),user_id = ToAdminRequest):
    return change_role_service(user_id,role="admin")


