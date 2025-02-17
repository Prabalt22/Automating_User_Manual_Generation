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
        self.page.window.width = 500
        self.page.window.height = 360
        
        # Initialize components
        self.window_manager = WindowManager()
        self.screenshot_manager = ScreenshotManager(curr_guide_name)
        self.mouse_listener = MouseListener(self.screenshot_manager)
        
        
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
        self.finish_button = ft.ElevatedButton(text="finish Listening",
                                               style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=10),
                                                    padding=20
                                                ),
                                               on_click=self.finish_screenshot_bottom)
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
        if 1 == 1:
            self.controls =[ 
                ft.Container(
                    content = ft.Column([
                        ft.Text("What to capture", size=20, weight=ft.FontWeight.BOLD),
                        self.dd, 
                        ft.Row([
                            self.start_button, 
                            self.stop_button, 
                            self.finish_button
                        ])
                    ]),
                    width=500,
                    height = 300,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(1, "black"),
                    padding=20
                )
            ]
        
