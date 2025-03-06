import flet as ft
from views.step_guide import StepGuideCreator

def main(page: ft.Page):
    page.theme_mode = "light"
    page.add(StepGuideCreator(page))

ft.app(target=main)