from ..common.time import now,str_to_datetime
from ..db.models import create_todo_db,get_todo_by_title_db,get_user_by_id
from ..common.exception import *
from ..common.response import *



def create_todo_service(user:dict, spec:dict | object):
    created_at = now()
    try:
        todo = create_todo_db(owner_id=user["id"],title=spec["title"],description=spec["description"],created_at=created_at)
    except UserNotFoudError:
        error(status_code=404,message="user not found")

    user["todo"] = todo
    return success(data=user,message="todo berhasil dibuat.")


    




