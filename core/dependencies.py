from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from security import verify_password,verify_token
from common.response import success,error
from db.models import get_user_by_id
from common.exception import UserNotFoudError


oauth2_sheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token = Depends(oauth2_sheme),token_type="access"):
    payload = verify_token(token)
    if payload["type"] != token_type:
        error(status_code=400,message="tipe token tidak sesuai")
    user_id = int(payload['sub'])

    try:
        user = get_user_by_id(user_id)
    except UserNotFoudError:
        error(status_code=404,message=f"user dengan id {user_id} tidak ditemukan ")
    
    return user

def require_active_user(user = Depends(get_current_user)):
    if not user['is_active']:
        error(status_code=403,message="accound sudah di non aktivkan")
    return user

def require_role(required_role:str="admin"):    
    def checker(user = Depends(require_active_user)):
        if user["role"] != required_role:
            error(
                status_code=403,
                message="Forbidden"
            )
        return user
    return checker


