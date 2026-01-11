from ..common.response import *
from ..db.models import change_role_db
from ..common.exception import *


def change_role_service(user_id,role):
    try:
        user = change_role_db(user_id=user_id,role=role)
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)
    
    # user["is_active"] = (True if user["is_active"] else False)
    user["is_active"] = bool(user["is_active"])

    return success(data=user,message="berhasil mengubah role ke admin")
