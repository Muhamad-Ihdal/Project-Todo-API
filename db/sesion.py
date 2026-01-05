import sqlite3

def foreign_key_on():
    conn = sqlite3.connect("db/todo.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

def delete_table():
    conn = foreign_key_on() 
    cursor = conn.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS users;
    """)
    cursor.execute("""
    DROP TABLE IF EXISTS ref_token;
    """)
    cursor.execute("""
    DROP TABLE IF EXISTS todos;
    """)

    
    conn.commit()
    conn.close()


def create_table_users():
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIPARY KEY,
            email TEXT UNIQUE,
            hashed_password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user',
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL
            )""")

    conn.commit()
    conn.close()
    return


def create_table_todo():
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL,
            update_at TEXT NOT NULL,
            deleted_at TEXT DEFAULT null,
            owner_id INTEGER NOT NULL, 
            FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
            )""")

    conn.commit()
    conn.close()
    return


def create_table_refresh_token():
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ref_token (
            id INTEGER PRIMARY KEY,
            token TEXT NOT NULL,
            revoked_at EXT DEFAULT null,
            expired_at TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )""")

    conn.commit()
    conn.close()
    return



