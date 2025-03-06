from PIL import Image, ImageGrab
import os
import pygetwindow as gw
import threading
import time
from backend.get_data_db import get_data
from config import SCALE_FACTOR
from backend.window_state_manager import WindowStateManager

class ScreenshotManager:
    
    def __init__(self, curr_guide_name):
        self.curr_guide_name = curr_guide_name
        self.setting_cursor_name, self.setting_screenshot_dir = get_data()
        
        # Initialize window manager
        self.window_manager = WindowStateManager()
        
        self.screenshot_dir = self.get_screenshot_dir()
        self.cursor_image = self.get_cursor_image()
        
        
        self.active_window = None
        self.window_bound = None
        
        # Start tracking the active window in the background
        self._lock = threading.Lock()
        self._start_window_tracking()
        
    def _start_window_tracking(self):
        # start window tracking
        self.window_track_thread = threading.Thread(target=self._track_active_window, daemon=True)
        self.window_track_thread.start()
    
    def _track_active_window(self): 
        while True:
            try:
                new_window = gw.getActiveWindow()
                if new_window and new_window != self.active_window:
                    with self._lock:    
                        self.active_window = new_window
                        self.window_bound = self.get_active_window_bounds(new_window)
            except Exception as e:
                print(f" Error tracking window: {e}")
            time.sleep(0.1)
    
    def get_active_window_bounds(self, active_window):
        return (
            active_window.left, 
            active_window.top, 
            active_window.left + active_window.width, 
            active_window.top + active_window.height
        )
    
    def get_filename(self):
        existing_files = os.listdir(self.screenshot_dir)
        screenshot_count = len([file for file in existing_files if file.endswith('.png')])
        filename_path = os.path.join(self.screenshot_dir, f"screenshot_{screenshot_count + 1}.png")
        return filename_path
    
    
    def get_screenshot_dir(self) -> str:
        base_dir = self.setting_screenshot_dir or "backend/screenshots"
        screenshot_dir = os.path.join(base_dir, self.curr_guide_name)
        os.makedirs(screenshot_dir, exist_ok=True)
        return screenshot_dir
    
    def get_cursor_image(self) -> Image.Image:
        cursur_name = self.setting_cursor_name or "click_color2.png"
        cursur_path = f"backend/image_folder/{cursur_name}"
        return Image.open(cursur_path).convert("RGBA")

        
    def take_screenshot(self, x, y) -> str | None:
        max_retiries = 3
        retry_count = 0
        
        if not self.active_window.title:
            print("No active window found.")
            return None
        
        while retry_count < max_retiries:
            try:
                # Add lock to prevent multiple screenshots at once
                with self._lock:
                    left, top, right, bottom = self.window_bound
                
                # Adjust for DPI scaling if necessary
                scale_factor = SCALE_FACTOR  # Example scale factor, adjust as needed
                left         = int(left * scale_factor)
                top          = int(top * scale_factor)
                right        = int(right * scale_factor)
                bottom       = int(bottom * scale_factor)
                
                # Take screenshot with the app minimized
                self.window_manager.minimize()
                time.sleep(0.1)
                    
                screenshot = ImageGrab.grab(bbox=(left, top, right, bottom)).convert("RGBA")

                cursor_x = x - left
                cursor_y = y - top

                screenshot.paste(self.cursor_image, (int(cursor_x), int(cursor_y)), self.cursor_image)

                filename_path = self.get_filename()
                screenshot.save(filename_path)
                screenshot.close()  # Explicitly close the image
                return filename_path
            except Exception as e:
                retry_count += 1
                print(f"Screenshot attempt {retry_count} failed: {e}")
                time.sleep(0.5)  # Wait before retry
            finally:
                # Ensure cleanup happens
                self.window_manager.restore()
                time.sleep(0.1)
    
        print("Failed to take screenshot after all retries")
        return None
    