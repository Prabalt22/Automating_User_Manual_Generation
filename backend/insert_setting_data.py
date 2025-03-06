from backend.connection_db import db_connect_func

CONN,C = db_connect_func()

def insert_data(data):
    global CONN,C
    
    C.execute(
        """
        INSERT OR REPLACE INTO setting_data (id, cursor_name, image_storage_dir, color_R, color_G, color_B)
        VALUES (1, ?, ?, ?, ?, ?) 
        """,
        data
    )
        
    CONN.commit()
    