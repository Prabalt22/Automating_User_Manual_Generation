import pygetwindow as gw

class WindowManager:
    def __init__(self):
        
        # List of system windows that should be ignored
        self.SYSTEM_WINDOWS = [
            "Settings", "Windows Input Experience", "Program Manager", 
            "Search", "explorer", "Task Manager", "Application Frame Host", 
            "Windows Shell Experience Host", "File Explorer", "Screenshot App"
        ]
        
        # Get all open windows
        self.open_windows = gw.getAllTitles()
        self.open_windows = list(set([title for title in self.open_windows if title]))
        
        
        self.filtered_windows = self.get_clean_app_names()

    def get_clean_app_names(self):
        clean_names = []
        
        for title in self.open_windows:
            # Skip system windows
            if any(system_window in title for system_window in self.SYSTEM_WINDOWS):
                continue
            
            # Extract application name based on common patterns
            if " - Google Chrome" in title:
                clean_names.append("Google Chrome")
            elif " - Visual Studio Code" in title:
                clean_names.append("Visual Studio Code")
            elif "DB Browser for SQLite" in title:
                clean_names.append("DB Browser for SQLite")
            
        return list(set(clean_names))  # Remove duplicates
    
    def focus_window(self, window_title):
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            print(windows)
            window = windows[0]
            print(windows[0])
            try:
                if window.isMinimized:
                    window.restore()  
                else:
                    window.restore()
                # window.bringToFront()  
            except Exception as e:
                print(f"Error focusing on window: {e}")
        else:
            print(f"No window found with title: {window_title}")
    
    def get_filtered_windows(self):
        return self.filtered_windows
