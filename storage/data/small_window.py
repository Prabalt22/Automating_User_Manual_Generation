import flet as ft
import time
from backend.mouse_listener import MouseListener
from backend.screenshot import ScreenshotManager
from backend.window_manager import WindowManager
from frontend.pages.dashboard_fld.dashboard import StepGuideCreator


class ScreenshotApp(ft.Column):
    def __init__(self, page, curr_guide_name):
        super().__init__()
        self.page = page
        self.curr_guide_name = curr_guide_name
        self.page.title = "Screenshot App"
        self.page.window.width = 410
        self.page.window.height = 350
        
        # Initialize components
        self.screenshot_manager = ScreenshotManager(curr_guide_name)
        self.mouse_listener = MouseListener(self.screenshot_manager)
        self.window_manager = WindowManager()
        
        # Get filtered window titles
        self.filtered_windows = self.window_manager.get_filtered_windows()
        self.options = [ft.dropdown.Option(title) for title in self.filtered_windows]
        
        # UI Elements
        self.dd = ft.Dropdown(width=300, options=self.options)
        self.start_button = ft.ElevatedButton(text="Start Listening", on_click=self.start_mouse_listener)
        self.stop_button = ft.ElevatedButton(text="Stop Listening", on_click=self.stop_mouse_listener)
        self.finish_button = ft.ElevatedButton(text="finish Listening", on_click=self.finish_screenshot_bottom)
        # Add elements to page
    
    def start_mouse_listener(self, e):
        selected_title = self.dd.value
        if selected_title:
            self.window_manager.focus_window(selected_title)
            time.sleep(1)
            self.mouse_listener.begin(selected_title)
        else:
            print("Please select a window title first")
    
    def stop_mouse_listener(self, e):
        self.mouse_listener.end()
    
    def finish_screenshot_bottom(self, e):
        self.page.clean()
        self.page.add(StepGuideCreator(self.page, self.curr_guide_name))
        self.page.update()

    def build(self):
        self.controls = [self.dd, self.start_button, self.stop_button, self.finish_button]
