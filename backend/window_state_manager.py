import pygetwindow as gw
from time import sleep

class WindowStateManager:
    def __init__(self, app_window_name="Screenshot App"):
        self.app_window_name = app_window_name
        self._transition_delay = 0.2
        
    def get_app_window(self):
        try:
            return gw.getWindowsWithTitle(self.app_window_name)[0]
        except (IndexError, Exception) as e:
            print(f"❌ Could not find window '{self.app_window_name}': {e}")
            return None
            
    def minimize(self):
        if window := self.get_app_window():
            try:
                if not window.isMinimized:
                    window.minimize()
                    sleep(self._transition_delay)
                return True
            except Exception as e:
                print(f"❌ Error minimizing window: {e}")
        return False
        
    def restore(self):
        if window := self.get_app_window():
            try:
                if window.isMinimized:
                    window.restore()
                    sleep(self._transition_delay)
                return True
            except Exception as e:
                print(f"❌ Error restoring window: {e}")
        return False