import sqlite3

CONN = None
C = None

def db_connect_func():
    global CONN,C
    try:
        CONN = sqlite3.connect("UserManual.sqlite",check_same_thread=False)
        C = CONN.cursor()
        return CONN,C
    except Exception as e:
        raise e

def create_table():
    global CONN,C
    query = """
    CREATE TABLE IF NOT EXISTS setting_data 
    (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        cursor_name TEXT NOT NULL,
        image_storage_dir TEXT
    )
    """
    C.execute(query)
    CONN.commit()


    

