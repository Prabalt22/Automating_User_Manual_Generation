import flet as ft
import time
from backend.mouse_listener import MouseListener
from backend.screenshot import ScreenshotManager
from backend.window_manager import WindowManager
from frontend.pages.small_window_fld.small_window_start_taking_image import CapturingPage

class ScreenshotApp(ft.Column):
    def __init__(self, page, curr_guide_name):
        super().__init__()
        self.page = page
        self.curr_guide_name = curr_guide_name
        self.page.title = "Screenshot App"
        self.page.window.width = 500
        self.page.window.height = 360
        
        # Initialize components
        self.selected_window_title = None
        self.window_page        = None
        self.window_manager     = WindowManager()
        self.screenshot_manager = ScreenshotManager(curr_guide_name)
        self.mouse_listener     = MouseListener(self.screenshot_manager, self.window_page)
        self.window_page        = CapturingPage(self.page, self.curr_guide_name, self.mouse_listener)
        self.mouse_listener.step_details = self.window_page
        
        # Get filtered window titles
        self.filtered_windows = self.window_manager.get_filtered_windows()
        self.options = [ft.dropdown.Option(title) for title in self.filtered_windows]
        
        # UI Elements
        self.dd = ft.Dropdown(width=300, options=self.options, padding=20)
        self.start_button = ft.ElevatedButton(text="Start Listening", 
                                              style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=10),
                                                    bgcolor=ft.Colors.GREEN,
                                                    color=ft.Colors.WHITE,
                                                    padding=20
                                                ),
                                              on_click=self.start_mouse_listener)
        self.stop_button = ft.ElevatedButton(text="Stop Listening",
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=20
                                            ),
                                             on_click=self.stop_mouse_listener)
        
        
    def start_mouse_listener(self, e):
        self.selected_window_title = self.dd.value
        if not self.selected_window_title:
            print("Please select a window title first")
            return
        try:
            self.window_manager.focus_window(self.selected_window_title)
            time.sleep(0.5)
            self.mouse_listener.begin(self.selected_window_title)
            self.page.clean()
            self.page.add(self.window_page)
            self.page.update()
        except Exception as e:
            print(f"Error starting mouse listener: {e}")
    
  
    def first_ui_small_window(self):
        return ft.Container(
                    content = ft.Column([
                        ft.Text("What to capture", size=20, weight=ft.FontWeight.BOLD),
                        self.dd, 
                        ft.Row([
                            self.start_button, 
                            self.stop_button
                        ])
                    ]),
                    width=500,
                    height = 300,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(1, "black"),
                    padding=20
                )
        
    def stop_mouse_listener(self, e):
        self.mouse_listener.end()
        print("chi")   
    
    def build(self):
        self.controls = [ 
            self.first_ui_small_window()
        ]
