from fastapi import APIRouter
from schemas import RegisterRequest,LoginRequest,RefreshRequest,SuccessResponse
from service import register_service,login_service,refresh_token_service,logout_service
router = APIRouter()

@router.post("/auth/register",response_model=SuccessResponse)
def register(user : RegisterRequest):
    email = user.email
    password = user.password
    return register_service(email,password)

@router.post("/auth/login",response_model=SuccessResponse)
def login(user : LoginRequest):
    email = user.email
    password = user.password
    return login_service(email,password)

@router.post("/auth/refresh",response_model=SuccessResponse)
def refresh_token(token : RefreshRequest):
    return refresh_token_service(token.refresh_token)

@router.post("/auth/logout",response_model=SuccessResponse)
def logout(token : RefreshRequest):
    return refresh_token_service(token.refresh_token)

