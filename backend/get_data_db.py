from backend.connection_db import db_connect_func

CONN,C = db_connect_func()

def get_data():
    try:    
        query = """
            SELECT cursor_name, image_storage_dir
            FROM setting_data AS s 
            WHERE s.id = 1
        """
        
        data = C.execute(query).fetchone()
        if data:
            return data
        else:
            # ("click_color2.png","C:\\Users\\Prabal Arvind Tiwari\\OneDrive\\Desktop\\User_Manuel\\backend\\screenshots")
            return None
    except Exception as e:
        raise e
    

def get_color_data():
    try:    
        query = """
            SELECT color_R, color_G, color_B
            FROM setting_data AS s 
            WHERE s.id = 1
        """
        
        data = C.execute(query).fetchone()
        if data:
            return data
        else:
            # ("click_color2.png","C:\\Users\\Prabal Arvind Tiwari\\OneDrive\\Desktop\\User_Manuel\\backend\\screenshots")
            return None
    except Exception as e:
        raise e

