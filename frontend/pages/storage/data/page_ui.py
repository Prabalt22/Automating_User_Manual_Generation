import flet as ft
from page1.starting_ui import WorkflowGuideApp

def main(page: ft.Page):
    page.title = "Workflow Guide Manager"
    page.window.width =  900  
    page.window.height = 600  
    page.theme_mode =    "light"

    def back_click():
        page.clean()
        page.add(WorkflowGuideApp(page,back_click))
        page.update()

    page1 = WorkflowGuideApp(page,back_click)
    page.add(
        page1
    )

ft.app(target=main)