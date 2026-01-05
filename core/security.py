from passlib.context import CryptContext
from jose import jwt,JWTError,ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRED_IN_MINUTES,REFRESH_TOKEN_EXPIRED_IN_DAYS
from datetime import datetime,timedelta,timezone


# ----------------------------------hash 
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)
# ----------------------------------hash end

# ------------------------------------ jwt
def create_access_token(user_id:int,email,role):
    payload = {
        "sub":str(user_id),
        "email":email,
        "role":role,
        "type":"access",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def create_refresh_token(user_id:int):
    payload = {
        "sub":str(user_id),
        "type":"refresh",
        "exp": datetime.now(timezone.utc) + timedelta(days=7)
    }
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token:str):
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        pass
# ------------------------------------ jwt end 