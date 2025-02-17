from backend.connection_db import db_connect_func

CONN,C = db_connect_func()

def insert_data(data):
    global CONN,C
    
    C.execute(
        """
        INSERT OR REPLACE INTO setting_data (id, cursor_name, image_storage_dir)
        VALUES (1, ?, ?) 
        """,
        data
    )
        
    CONN.commit()
    