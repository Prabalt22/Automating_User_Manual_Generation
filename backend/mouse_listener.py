from pynput import mouse
import pygetwindow as gw


class MouseListener:
    def __init__(self, screenshot_manager):
        self.screenshot_manager = screenshot_manager
        self.selected_window_titles = None
        self.listener = None
        self.current_window = None

        
    def update_active_window(self) -> str | None:
        try:
            new_window = gw.getActiveWindowTitle()
            if new_window and new_window != self.current_window:
                self.current_window = new_window
            return self.current_window
        except Exception as e:
            print(f"Error getting active window: {e}")
            return None
            
    def on_click(self, x, y, button, pressed):
        
        if not pressed:
            return
        
        current_window = self.update_active_window()
        if not current_window:
            return 
          
        window = current_window.split(" - ")[-1] if " - " in current_window else current_window
         
        
        if self.selected_window_titles == window:
            # self.minimiza_window()
            self.screenshot_manager.take_screenshot(x, y)
    
            
    def minimiza_window(self):
        try:
            window = gw.getWindowsWithTitle("Screenshot App")[0]
            window.minimize() 
        except IndexError:
            print("❌ Window not found.")
               
    def begin(self, selected_title):
        
        if self.listener and self.listener.running:
            print("🛑 Stopping existing listener before starting a new one.")
            self.end()
            
        self.selected_window_titles = selected_title
        
        try:
            # Listening Mouse
            
            self.listener = mouse.Listener(on_click = self.on_click)
            self.listener.start()
        except Exception as e:
            print(f"❌ Error starting listener: {e}")
            self.end()
            
                
        
    def end(self):
        if self.listener:
            self.listener.stop()
            self.listener = None