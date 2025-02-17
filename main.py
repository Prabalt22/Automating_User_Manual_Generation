import flet as ft
from backend.connection_db import db_connect_func
from backend.get_data_db import get_data
from frontend.pages.starting_ui_fld.starting_ui import WorkflowGuideApp
from frontend.components.setting_alertdialog import CheckSetting


def main(page: ft.Page):
    page.title = "Screenshot App"
    page.window.width =  900  
    page.window.height = 600  
    page.theme_mode =    "light"

    def back_click():
        page.clean()
        page.add(WorkflowGuideApp(page, back_click))
        page.update()
        
    def check_setting():
        val = get_data()
        if val is None:
            CheckSetting(page)
            page.update()

    check_setting()
    page1 = WorkflowGuideApp(page, back_click)
    page.add(
        page1
    )

db_connect_func()
ft.app(target=main)