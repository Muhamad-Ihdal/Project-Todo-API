from ..db.models import get_user_by_email,get_user_by_id
from ..common.exception import PermissionDenail,UserNotFoudError
from ..common.response import error



def get_user_by_id_utils(user_id):
    try:
        user = get_user_by_id(user_id=user_id)
        if not user["is_active"]:
            raise PermissionDenail()
    except UserNotFoudError:
        error(status_code=404,message="User not found")
    except PermissionDenail:
        error(status_code=403,message="User sudah dinonaktifkan")

    return user


def get_user_by_email_utils(email):
    try:
        user = get_user_by_email(email=email)
        if not user["is_active"]:
            raise PermissionDenail()
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message="invalid email or password")
    except PermissionDenail:
        error(status_code=403,message="User sudah dinonaktifkan")
    
    return user