from mouse_listener import MouseListener
from screenshot import ScreenshotManager
from window_manager import WindowManager
import flet as ft
import time

def main(page: ft.Page):
    page.title = "Screenshot App"
    page.window.width  = 400
    page.window.height = 400
    
    # class and inststances
    screenshot_manager = ScreenshotManager()                           # initalixe the manager
    mouse_listener = MouseListener(screenshot_manager)  
    window_manager = WindowManager()                                   # window manager
    filtered_windows = window_manager.get_filtered_windows()
    
    
    # page element functionality
    options = [ft.dropdown.Option(title) for title in filtered_windows] # active window option
    print("=", options)
    def start_mouse_listener(e):                                        # start button
        selected_title = dd.value
        if selected_title:
            window_manager.focus_window(selected_title)
        else:
            print("Please select a window title first")
        time.sleep(1)
        mouse_listener.begin(selected_title)
            
    def stop_mouse_listener(e):                                         # end button
        mouse_listener.end()                                            
    
    # page element
    start_button = ft.ElevatedButton(
        text="Start Listening",
        on_click=start_mouse_listener
    )
    stop_button = ft.ElevatedButton(
        text="Stop Listening",
        on_click=stop_mouse_listener
    )
    dd = ft.Dropdown(
        width=300,
        options=options
    )
    
    page.add(
        ft.Row([dd, start_button,stop_button]),
    )
    

ft.app(target=main)