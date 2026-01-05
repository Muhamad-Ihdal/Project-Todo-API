from sesion import foreign_key_on
from ..common.exception import UserNotFoudError,ForbiddenError

def add_user_db(hased_pwd,email,created_at,role='user'):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "INSESRT INTO users (email,password,created_at,role) VALUES (?,?,?,?)",
        (email,hased_pwd,created_at,role)
    )

    conn.commit()
    conn.close()


def get_user_by_id(user_id:int):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise UserNotFoudError()

    conn.close()
    return dict(row)


def get_user_by_email(email:str):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise UserNotFoudError()

    conn.close()
    return dict(row)

