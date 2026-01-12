from ..common.response import *
from ..db.models import change_role_db,update_is_active_db
from ..common.exception import *


def change_role_service(user_id,role):
    try:
        user = change_role_db(user_id=user_id,role=role)
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)
    except PermissionDenail:
        error(status_code=PermissionDenail.status_code,message=PermissionDenail.detail)
    except DatabaseError:
        error(status_code=DatabaseError.status_code,message=DatabaseError.detail)
    
    # user["is_active"] = (True if user["is_active"] else False)
    user["is_active"] = bool(user["is_active"])
    
    return success(data=user,message="berhasil mengubah role ke admin")


def ban_user_service(user_id):
    try:
        user = update_is_active_db(user_id=user_id,is_active=0)
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)
    except PermissionDenail:
        error(status_code=PermissionDenail.status_code,message=PermissionDenail.detail)
    except DatabaseError:
        error(status_code=DatabaseError.status_code,message=DatabaseError.detail)

    user["is_active"] = bool(user["is_active"])

    return success(data=user,message="ban user berhasil")

