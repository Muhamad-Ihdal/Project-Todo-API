from ..common.exception import *
from ..common.response import *


from fastapi import Depends




def check_and_get_user(user_id,permission_denail_massage = "Akses ditolak",database_error_message = "Database error"):
    try:
        pass
        # data_token = check_and_get_token_db(token=token)
        # if data_token["revoked_at"]:
            # raise PermissionDenail()
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)
    except PermissionDenail:
        error(status_code=PermissionDenail.status_code,message=permission_denail_massage)
    except DatabaseError:
        error(status_code=404,message=database_error_message)

def normalize(x:str):
    return x.srtip().lower().replace(" ","")