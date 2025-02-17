import flet as ft
import os
from backend.get_data_db import get_data
   
class StepGuideCreator(ft.Column):
    def __init__(self, page, curr_guide_name):
        super().__init__()
        self.page = page
        self.setting_cursor_name, self.setting_screenshot_dir = get_data()
        
        # self.screenshot_dir = r"C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\User_Manuel\backend\screenshots\{curr_guide_name}"
        self.screenshot_dir = f"{self.setting_screenshot_dir}\\{curr_guide_name}"
        self.cnt = self.get_file_count()
        self.image_column = ft.Column(
                [
                ft.Image(
                        src=f"{self.setting_screenshot_dir}\\{curr_guide_name}\\screenshot_{i}.png",
                        width=500,
                        height=500,
                        fit=ft.ImageFit.CONTAIN,
                    ) for i in range(1, self.cnt+1)
                ],
                 alignment=ft.alignment.center
        )
        
        
    def get_file_count(self):
        if not os.path.exists(self.screenshot_dir):
            return 0 
        existing_files = os.listdir(self.screenshot_dir)
        screenshot_count = len([file for file in existing_files if file.endswith('.png')])
        return screenshot_count
       
    def top_bar(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.MENU, tooltip="Menu"),
                    ft.Text("Untitled - " + "07-02-2025", size=16, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Export PDF",
                                icon=ft.Icons.DOWNLOAD,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.GREEN,
                                    color=ft.Colors.WHITE,
                                )
                            ),
                            ft.Dropdown(
                                width=100,
                                options=[
                                    ft.dropdown.Option("Red"),
                                    ft.dropdown.Option("Green"),
                                    ft.dropdown.Option("Blue"),
                                ],
                            ),
                        ],
                        spacing=10,
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.BLACK12)),
        )

    def side_toolbar(self):
        tools = [
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
        
        return ft.Container(
            content=ft.Column(
                controls=tools,
                spacing=5,
            ),
            width=50,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(right=ft.BorderSide(1, ft.Colors.BLACK12)),
        )

    def steps_list(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Add step",
                            icon=ft.Icons.ADD,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.WHITE,
                                color=ft.Colors.BLACK,
                            ),
                        ),
                        padding=10,
                    ),
                    ft.ListView(
                        controls=[
                            ft.ListTile(
                                leading=ft.Text(f"{i}."),
                                title=ft.Text("hello world" if i == 1 else f"Step {i}"),
                                dense=True,
                            ) for i in range(1, 4+1)
                        ],
                        spacing=2,
                    ),
                ],
            ),
            width=200,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(right=ft.BorderSide(1, ft.Colors.BLACK12)),
        )

    def main_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Step image actions",
                                icon=ft.Icons.IMAGE,
                            ),
                            ft.ElevatedButton(
                                "Export image",
                                icon=ft.Icons.UPLOAD,
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text("Focused view"),
                                ft.IconButton(icon=ft.Icons.HELP),
                                ft.Text("1.5"),
                                ft.IconButton(icon=ft.Icons.REMOVE),
                                ft.IconButton(icon=ft.Icons.ADD),
                                ft.Switch(),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        bgcolor="#FFA500",
                        border_radius=10,
                        padding=10,
                        width=400
                    ),
                    self.image_column
                ],
                scroll="always",
            ),
            expand=True,
            bgcolor="#F0F0F0",
        )

    def step_details(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Step Details", size=16, weight=ft.FontWeight.BOLD),
                            ft.IconButton(icon=ft.Icons.KEYBOARD_ARROW_UP),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Dropdown(
                        options=[
                            ft.dropdown.Option("Red"),
                            ft.dropdown.Option("Green"),
                            ft.dropdown.Option("Blue"),
                        ],
                        width=200,
                    ),
                    ft.TextField(
                        label="Title",
                        value="hello world",
                    ),
                    ft.TextField(
                        label="Description",
                        multiline=True,
                        min_lines=3,
                    ),
                ],
                spacing=20,
            ),
            width=300,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(left=ft.BorderSide(1, ft.Colors.BLACK12)),
        )

    def build(self):
        self.controls = [
            self.top_bar(),
            ft.Row(
                [
                    self.side_toolbar(),
                    self.steps_list(),
                    self.main_content(),
                    self.step_details(),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
                expand=True,
            ),
        ]
        self.expand = True
        self.page.window.width =  900  
        self.page.window.height = 600 
        

def main(page: ft.Page):
    page.theme_mode = "light"
    page.add(
        StepGuideCreator(page)
    )

# ft.app(target=main) 