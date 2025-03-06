import flet as ft

class SideToolbar(ft.Container):
    def __init__(self):
        super().__init__()
        self.tools = [
            ft.IconButton(icon=ft.Icons.VIEW_LIST, tooltip="List View"),
            ft.IconButton(icon=ft.Icons.ARROW_BACK, tooltip="Back"),
            ft.IconButton(icon=ft.Icons.ARROW_FORWARD, tooltip="Forward"),
            ft.IconButton(icon=ft.Icons.MOUSE, tooltip="Select"),
            ft.IconButton(icon=ft.Icons.CHAT, tooltip="Comment"),
            ft.IconButton(icon=ft.Icons.TEXT_FIELDS, tooltip="Text"),
            ft.IconButton(icon=ft.Icons.PAN_TOOL, tooltip="Hand Tool"),
            ft.IconButton(icon=ft.Icons.TIMER, tooltip="Timer"),
            ft.IconButton(icon=ft.Icons.WATER_DROP, tooltip="Draw"),
            ft.IconButton(icon=ft.Icons.EDIT, tooltip="Edit"),
            ft.IconButton(icon=ft.Icons.CREATE, tooltip="Pencil"),
            ft.IconButton(icon=ft.Icons.SCREENSHOT_MONITOR, tooltip="Screenshot"),
            ft.IconButton(icon=ft.Icons.REFRESH, tooltip="Reset"),
            ft.IconButton(icon=ft.Icons.SYNC, tooltip="Sync"),
        ]
    
    def build(self):
    
        self.content=ft.Column(
            controls=self.tools,
            spacing=5,
        )
        self.width=50
        self.bgcolor=ft.Colors.WHITE
        self.border=ft.border.only(right=ft.BorderSide(1, ft.Colors.BLACK12))
    