from sesion import foreign_key_on
from ..common.exception import UserNotFoudError,PermissionDenail,UniqueError,DatabaseError
import sqlite3



# ----------------------------------------------------------------- user 
def add_user_db(hashed_pwd,email,created_at):
    conn = foreign_key_on()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSESRT INTO users (email,password,created_at) VALUES (?,?,?)",
            (email,hashed_pwd,created_at)
        )
    except sqlite3.IntegrityError:
        raise UniqueError()


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


# ----------------------------------------------------------------- user end


# ----------------------------------------------------------------- refresh token


def add_refresh_token_db(owner_id,token,expired_at):
    conn = foreign_key_on()
    cursor = conn.cursor()


    cursor.execute(
        "INSESRT INTO users (owner_id,token,expired_at) VALUES (?,?,?)",
        (owner_id,token,expired_at)
    )

    affected_row = cursor.rowcount
    if not affected_row:
        raise DatabaseError()


    conn.commit()
    conn.close()







# ----------------------------------------------------------------- refresh token end