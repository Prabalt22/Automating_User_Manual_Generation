from flet import Page
import flet as ft
from flet_contrib.color_picker import ColorPicker

def main(page: Page):
        
    def check_color(e):
        print(color_picker1.r.value)
        print(color_picker1.g.value)
        print(color_picker1.b.value)
        
    color_picker1 = ColorPicker()
    sample_button = ft.ElevatedButton("ok", on_click=check_color)
    
    page.add(color_picker1,sample_button)

ft.app(target=main)