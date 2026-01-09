from fastapi import FastAPI,HTTPException,APIRouter
from .db.sesion import delete_table,create_table_refresh_token,create_table_todo,create_table_users
from .auth.router import router
# create_table_users()
# create_table_todo()
# create_table_refresh_token()
# delete_table()

app = FastAPI()

app.include_router(router=router)

