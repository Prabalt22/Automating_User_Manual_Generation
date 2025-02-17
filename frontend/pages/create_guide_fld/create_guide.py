import flet as ft
from datetime import datetime
from frontend.pages.small_window_fld.small_window import ScreenshotApp

class CreatGuide(ft.Column):
    def __init__(self, page, main_instance_function_back):
        super().__init__()
        self.page = page
        self.main_instance_function_back = main_instance_function_back
        self.defaut_guide_name = self.formate_untitle_date()
        self.create_guide_name = ft.TextField(value=self.defaut_guide_name, text_align=ft.TextAlign.CENTER, width=300)
    
    
    def formate_untitle_date(self):
        # get current date
        current_date = datetime.now()
        
        # formate the date
        formate_date = f"Untitled - {current_date.strftime('%d-%m-%y')}"
        
        return formate_date     
          
    def top_bar(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                on_click=self.backButton,
                                )
                            ],
                            spacing=10
                        ),
                    ft.Row(
                        controls=[
                            ft.Text(value=self.defaut_guide_name, size=14, weight=ft.FontWeight.BOLD),
                            ft.Icon(ft.Icons.EDIT, size=16)
                        ]
                    ),
                    ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, tooltip="Profile"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#FFD966",                              # Yellow background
            height=50,
            padding=ft.padding.symmetric(horizontal=15),
        )

    def center_content(self):
        return ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Icon(ft.Icons.WAVING_HAND, size=60),  # Hand wave emoji
                    ft.Text("Start building your guide.", size=24, weight=ft.FontWeight.BOLD),
                    self.create_guide_name,
                    ft.Text("Your guide has no steps yet. Add new steps from:", size=14),
                    self.action_buttons()
                ]
            )
        )

    def start_capture(self, e):
        curr_guide_name = self.create_guide_name.value
       
        self.page.clean()
        self.page.add(ScreenshotApp(self.page, curr_guide_name))
        self.page.update()
        
    def import_images(self, e):
        print("Import Images Clicked")

    def empty_step(self, e):
        print("Empty Step Clicked")
        
    def action_buttons(self):
        button_labels = {
        "Capture screenshots with mouse clicks":self.start_capture,
        "Import any images as new steps": self.import_images,
        "Empty step":self.empty_step,
        }

        return ft.Column(
            controls=[
                ft.ElevatedButton(
                    text=label,
                    bgcolor="#606060",  # Dark gray buttons
                    color="white",
                    width=300,
                    height=40,
                    on_click=action,
                )
                for label,action in button_labels.items()
            ],
            spacing=10
        )

    def backButton(self,e):
        self.main_instance_function_back()
        
    
    def build(self):
        self.controls = [
            self.top_bar(),
            self.center_content(),
        ]
        self.spacing = 10,
        # self.expand = True
