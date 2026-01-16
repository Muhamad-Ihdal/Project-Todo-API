from ..common.time import now,str_to_datetime
from ..db.models import edit_todo_db,get_todo_by_id_db,create_todo_db,get_todo_by_title_db,get_user_by_id,get_todos_db
from ..common.exception import *
from ..common.response import *
from ..common.utils import normalize



def create_todo_service(user:dict, spec:dict | object):
    created_at = now()
    try:
        todo = create_todo_db(owner_id=user["id"],title=spec["title"],description=spec["description"],created_at=created_at)
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)

    user["todo"] = todo
    return success(data=user,message="todo berhasil dibuat.")

def get_todos_service(user:dict):
    try:
        list_todos = get_todos_db(owner_id=user["id"])
    except DatabaseError:
        error(status_code=DatabaseError.status_code,message=DatabaseError.detail)
    
    user["todos"] = list_todos
    return success(data=user)

def get_todo_by_id_service(todo_id:int,user:dict):

    try:
        todo = get_todo_by_id_db(id=todo_id)
        owner = get_user_by_id(user_id=todo["owner_id"])
        if user["id"] != todo["owner_id"] and user["role"] != "admin":
            raise PermissionDenail()
    except DatabaseError:
        error(status_code=DatabaseError.status_code,message=DatabaseError.detail)
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)
    except PermissionDenail:
        error(status_code=PermissionDenail.status_code,message=PermissionDenail.detail)
        
    owner["todo"] = todo
    return success(data=owner)
    
def edit_todo_service(edit:object,todo_id:int,user:dict):
    try:
        todo = get_todo_by_id_db(todo_id)
        if todo["status"] == "archived":
            raise PermissionDenail("tidak bisa menedit todo dengan status 'archived'.")
        
        updated_at = now()
        match edit.status:
            case "pending": status = "pending"
            case "done": status = "done"
            case "archived": status = "archived"
            case _ : status = todo["status"] 

        edited_todo = edit_todo_db(title=edit.title,description=edit.description,status=status,updated_at=updated_at)

    except DatabaseError:
        error(status_code=DatabaseError.status_code,message=DatabaseError.detail)
    except UserNotFoudError:
        error(status_code=UserNotFoudError.status_code,message=UserNotFoudError.detail)
    except PermissionDenail:
        error(status_code=PermissionDenail.status_code,message=PermissionDenail.detail)
    
    return success(data=edited_todo,message="Update berhasil.")




    




