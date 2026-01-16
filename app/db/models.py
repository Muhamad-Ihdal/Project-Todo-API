from .sesion import foreign_key_on
from ..common.exception import *
import sqlite3

# ----------------------------------------------------------------- user 
def add_user_db(hashed_pwd:str,email:str,created_at):
    conn = foreign_key_on()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email,password,created_at) VALUES (?,?,?)",
            (email,hashed_pwd,created_at)
        )
    except sqlite3.IntegrityError:
        conn.close()
        raise UniqueError()


    conn.commit()
    conn.close()


def get_user_by_id(user_id:int):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = ? ",
        (user_id,)
    )
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise UserNotFoudError()

    user = dict(row)
    user["is_active"] = bool(user["is_active"])

    conn.close()
    return user


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

    user = dict(row)
    user["is_active"] = bool(user["is_active"])

    conn.close()
    return user

def change_role_db(user_id:int,role:str):
    conn = foreign_key_on()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE users
            SET role = ?
            WHERE id = ?""",
            (role,user_id)
        )
    except sqlite3.IntegrityError:
        conn.close()
        raise DatabaseError()
    
    affacted_row = cursor.rowcount
    if not affacted_row:
        conn.close()
        raise UserNotFoudError()
    
    user = get_user_by_id(user_id=user_id)
    
    conn.commit()
    conn.close()
    return dict(user)


def update_is_active_db(user_id:int,is_active:int):
    conn = foreign_key_on()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE users
            SET is_active = ?
            WHERE id = ?""",
            (is_active,user_id)
        )
    except sqlite3.IntegrityError:
        conn.close()
        raise DatabaseError()
    
    affacted_row = cursor.rowcount
    if not affacted_row:
        conn.close()
        raise UserNotFoudError()
    
    user = get_user_by_id(user_id=user_id)
    
    conn.commit()
    conn.close()
    return dict(user)


# ----------------------------------------------------------------- user end

# ----------------------------------------------------------------- refresh token
def add_refresh_token_db(owner_id,token,expired_at):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO ref_token (owner_id,token,expired_at) VALUES (?,?,?)",
        (owner_id,token,expired_at)
    )


    conn.commit()
    conn.close()


def check_and_get_token_db(token):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM ref_token WHERE token = ?",
        (token,)
    )

    row = cursor.fetchone()
    if not row:
        conn.close()
        raise DatabaseError()

    conn.close()
    return dict(row)

def delete_refresh_token_db(token):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM ref_token WHERE token = ?",
        (token,)
    )

    conn.commit()
    conn.close()

# ----------------------------------------------------------------- refresh token end

# ----------------------------------------------------------------- todo

def create_todo_db(owner_id,title,description,created_at):

    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO todos (owner_id,title,descroption,created_at) VALUES (?,?,?,?)",
        (owner_id,title,description,created_at)
    )
    row = cursor.rowcount
    if not row:
        conn.close()
        raise UserNotFoudError()
    
    todo = get_todo_by_title_db(title)

    conn.commit()
    conn.close()
    return todo


def get_todo_by_title_db(title):

    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM todos WHERE title = ? AND delete_at = null",
        (title,)
    )

    row = cursor.fetchone()
    if not row:
        conn.close()
        raise DatabaseError()

    conn.close()
    return dict(row)

def get_todo_by_id_db(id):

    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM todos WHERE id = ? AND delete_at = null",
        (id,)
    )

    row = cursor.fetchone()
    if not row:
        conn.close()
        raise DatabaseError()

    conn.close()
    return dict(row)


def get_todos_db(owner_id):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM todos WHERE owner_id = ? AND delete_at = null",
        (owner_id,)
    )
    
    rows = cursor.fetchall()
    if not rows:
        conn.close()
        return rows

    rows = [dict(row) for row in rows]

    conn.close()
    return rows

def edit_todo_db(title,description,status,updated_at):
    conn = foreign_key_on()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE todos
            SET title = ?
            WHERE id = ?""",
            (title,description,status,updated_at)
        )
    except sqlite3.IntegrityError:
        conn.close()
        raise DatabaseError()
    
    affacted_row = cursor.rowcount
    if not affacted_row:
        conn.close()
        raise DatabaseError(detail="todo tidak ditemukan")
    
    user = get_todo_by_title_db(title=title)
    
    conn.commit()
    conn.close()
    return dict(user)

# ----------------------------------------------------------------- todo end