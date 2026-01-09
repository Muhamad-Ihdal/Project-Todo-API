from fastapi import APIRouter
from schemas import RegisterRequest,LoginRequest,RefreshRequest
from service import register_service,login_service,refresh_token_service,logout_service
router = APIRouter()

@router.post("/auth/register")
def register(user : RegisterRequest):
    email = user.email
    password = user.password
    return register_service(email,password)

@router.post("/auth/login")
def login(user : LoginRequest):
    email = user.email
    password = user.password
    return login_service(email,password)

@router.post("/auth/refresh")
def refresh_token(token : RefreshRequest):
    return refresh_token_service(token.refresh_token)

@router.post("/auth/logout")
def logout(token : RefreshRequest):
    return refresh_token_service(token)

