from db.models import delete_refresh_token_db,add_user_db,get_user_by_id,get_user_by_email,add_refresh_token_db,check_and_get_token_db
from core.security import hash_password,verify_password,create_access_token,create_refresh_token,verify_token
from ..common.time import now
from ..common.response import *
from ..common.exception import *
from datetime import datetime,timedelta,timezone
from utils import get_user_by_email_utils, get_user_by_id_utils
# belajar init dan moduls duluuu woyyyy <----------------------------------|

def register_service(email,password):
    time_now = str(now())
    hashed_password = hash_password(password=password)
    try:
        add_user_db(hashed_pwd=hashed_password,email=email,created_at=time_now)
    except UniqueError:
        error(status_code=400,message=f"{email} Telah di guakan")

    return success(message="Registrasi berhasil, silakan login kembali.")


def login_service(email,password):
    user = get_user_by_email_utils(email=email)
    if not verify_password(plain_password=password,hashed_password=user["hashed_password"]):
        error(status_code=400,message="invalid email or password")

    access_token = create_access_token(user_id=user["id"],email=user["email"],role=user["role"])
    refresh_token = create_refresh_token(user_id=user["id"])
    expierd_at = now() + timedelta(days=7)
    try:
        add_refresh_token_db(owner_id=user["id"],token=refresh_token,expired_at=expierd_at)
    except DatabaseError:
        error(status_code=DatabaseError.status_code,message="Database error")
    
    return success(
        data={
            "access_token":access_token,
            "refresh_token":refresh_token,
            "type":"bearer"
        }, 
        message="login berhasil"
    )

def refresh_token_service(token):
    try:
        data_token = check_and_get_token_db(token=token)
        delete_refresh_token_db(data_token["token"])
        if data_token["revoked_at"]:
            raise PermissionDenail()
    except FileNotFoundError:
        error(status_code=404,message="Token tidak terdaftar")
    except PermissionDenail:
        error(status_code=401,message="Token telah di band")
   
    expired_at = datetime.fromisoformat(data_token["expired_at"])
    if expired_at < datetime.now(timezone.utc):
        error(message="Token telah expired")
    
    payload = verify_token(token=data_token["token"])
    user_id = int(payload["sub"])
    
    user = get_user_by_id_utils(user_id=user_id)
    
    access_token = create_access_token(user_id=user["id"],email=user["email"],role=user["role"])
    refresh_token = create_refresh_token(user_id=user["id"])
    expierd_at = now() + timedelta(days=7)
    try:
        add_refresh_token_db(owner_id=user["id"],token=refresh_token,expired_at=expierd_at)
    except DatabaseError:
        error(status_code=DatabaseError.status_code,message=DatabaseError.detail)
    
    data_response,m = {
        "access_token":access_token,
        "refresh_token":refresh_token,
        "type":"Bearer"
    }

    return success(data=data_response,message="refresh token berhasil")


def logout_service(token):
    pass
