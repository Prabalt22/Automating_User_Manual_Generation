import flet as ft
from frontend.pages.create_guide_fld.create_guide import CreatGuide
from frontend.pages.setting_page_fld.setting_page import SettingsPage

class WorkflowGuideApp(ft.Column):
    def __init__(self, page, main_instance_function_back):
        super().__init__()
        self.page = page
        self.main_instance_function_back = main_instance_function_back
        

    def top_bar(self):
        return ft.Container(
            content = ft.Row(
                [
                    ft.ElevatedButton("Menu", icon=ft.Icons.MENU),
                    ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, tooltip="Profile"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                height=50,
            ),
            bgcolor="#FFDD67",
            padding=ft.padding.only(left=10, right=10)
        )

    def action_buttons(self):
        button_container = ft.Row(
                controls=[
                    ft.Container(
                        ft.ElevatedButton(
                            text="Create Guide",
                            icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                            on_click=self.create_guide,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                bgcolor=ft.Colors.WHITE,
                                color=ft.Colors.BLACK,
                                padding=20
                            ),
                        ),
                        border=ft.border.all(1, "black"),
                        border_radius=10,
                        padding=10,
                        width=200,
                        height=70
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            text="Backup",
                            icon=ft.Icons.BACKUP,
                            on_click=lambda e: print("Backup Clicked"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                bgcolor=ft.Colors.WHITE,
                                color=ft.Colors.BLACK,
                                padding=20
                            ),
                        ),
                        border=ft.border.all(1, "black"),
                        border_radius=10,
                        padding=10,
                        width=200,
                        height=70
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            text="Restore",
                            icon=ft.Icons.RESTORE,
                            on_click=lambda e: print("Restore Clicked"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                bgcolor=ft.Colors.WHITE,
                                color=ft.Colors.BLACK,
                                padding=20
                            ),
                        ),
                        border=ft.border.all(1, "black"),
                        border_radius=10,
                        padding=10,
                        width=200,
                        height=70
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            text="Settings",
                            icon=ft.Icons.SETTINGS_OUTLINED,
                            on_click=self.setting_button,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                bgcolor=ft.Colors.WHITE,
                                color=ft.Colors.BLACK,
                                padding=20
                            ),
                        ),
                        border=ft.border.all(1, "black"),
                        border_radius=10,
                        padding=10,
                        width=200,
                        height=70
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                spacing=10
            )
        
        return ft.Container(
            content=button_container,
            padding=ft.padding.only(top=10),
            alignment=ft.alignment.center,
        )

    def guides_header_with_search(self):
        return ft.Column(
            [
                ft.Divider(thickness=1, color="gray"),  
                ft.Row(
                    [
                        ft.Text("Your Guides", weight=ft.FontWeight.BOLD, size=14),
                        ft.Container(
                            ft.TextField(
                                hint_text="Search...",
                                prefix_icon=ft.Icons.SEARCH,
                                height=40,       
                                border_radius=8,  # Rounded corners
                            ),
                            width=250,  
                        ),
                        ft.Text(" ", weight=ft.FontWeight.BOLD, size=14)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  
                )
            ]
        )


    def guide_list(self):
        return ft.Row(
        # expand=True,
        alignment=ft.MainAxisAlignment.CENTER,  # Center align the DataTable
        controls=[
            ft.Container(  # Wrap the DataTable in a Container
                expand= True,
                content=ft.DataTable(
                    width=self.page.width,
                    heading_row_height=50,
                    column_spacing=200,
                    show_checkbox_column=False,
                    columns=[
                        ft.DataColumn(ft.Text("Title"), numeric=False),
                        ft.DataColumn(ft.Text("Updated")),
                        ft.DataColumn(ft.Text("Created")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(
                                    ft.Row(
                                        [ft.Checkbox(), ft.Text("prabal-1")],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=40,
                                    )
                                ),
                                ft.DataCell(ft.Text("2 days ago")),
                                ft.DataCell(ft.Text("8 days ago")),
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(
                                    ft.Row(
                                        [ft.Checkbox(), ft.Text("prabal-2")],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=40,
                                    )
                                ),
                                ft.DataCell(ft.Text("5 days ago")),
                                ft.DataCell(ft.Text("10 days ago")),
                            ]
                        ),
                    ],
                ),
                alignment=ft.alignment.center,  # Center-align the DataTable
            )
        ]
    )
        
    def create_guide(self, e):
        print("Guide Created")
        creatGuide_btn = CreatGuide(self.page, self.main_instance_function_back)
        self.page.clean()
        self.page.add(creatGuide_btn)
        
    def setting_button(self, e):
        setting_btn = SettingsPage(self.page, self.main_instance_function_back)
        self.page.clean()
        self.page.add(setting_btn)

    def backup_guides(self, e):
        print("Backup Clicked")

    def restore_guides(self, e):
        print("Restore Clicked")

    def build(self):
        self.controls = [
            self.top_bar(),
            self.action_buttons(),
            self.guides_header_with_search(),
            self.guide_list(),
        ]
        self.spacing = 10,
        self.expand = True
        