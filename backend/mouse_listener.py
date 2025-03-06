from pynput import mouse
import pygetwindow as gw
import threading
import time

class MouseListener:
    def __init__(self, screenshot_manager, step_details):
        self.screenshot_manager = screenshot_manager
        self.selected_window_titles = None
        self.listener = None
        self.current_window = None
        self.step_details = step_details
        self.is_taking_screenshot = False
        self._Screenshot_lock = threading.Lock()
        
    def update_active_window(self) -> str | None:
        
        with self._Screenshot_lock:
            if self.is_taking_screenshot:
                return
            self.is_taking_screenshot = True
        
        try:
            new_window = gw.getActiveWindowTitle()
            if new_window and new_window != self.current_window:
                self.current_window = new_window
            return self.current_window
        except Exception as e:
            print(f"Error getting active window: {e}")
            return None
        finally:
            with self._Screenshot_lock:
                self.is_taking_screenshot = False
    
    
    def handle_screenshot(self, x, y):
        try:
            screenshot_path = self.screenshot_manager.take_screenshot(x, y)
            if screenshot_path:
                self.step_details.update_counter(screenshot_path)
        except Exception as e:
            print(f"Error in handle_screenshot: {e}")
            return None
        
    def on_click(self, x, y, button, pressed):
        
        if not pressed:
            return
        time.sleep(0.15)
        
        current_window = self.update_active_window()
        
        if not current_window:
            return 
        
        window = current_window.split(" - ")[-1] if " - " in current_window else current_window
        
        if self.selected_window_titles == window:
            # Take screenshot directly in the main thread
            self.handle_screenshot(x, y)
            
               
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
       
    def begin1(self):
        
        if self.listener and self.listener.running:
            print("🛑 Stopping existing listener before starting a new one.")
            self.end()
        
        try:
            if self.selected_window_titles:
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
            print("Listener stopped")  # Better message than "hi2"
