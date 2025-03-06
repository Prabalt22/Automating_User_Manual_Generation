import flet as ft
from components.image_operations import ImageOperations
from components.side_toolbar import SideToolbar
from components.step_details import StepDetails
from components.steps_list import StepsList
from components.top_bar import TopBar
from components.text_formatter import TextFormater

class StepGuideCreator(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.curr_guide_name = "Untitled-24-02-25"
        self.steps_data = {
            1: {'title': 'hello', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_1.png'},
            2: {'title': 'hy bro', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_2.png'},
            3: {'title': 'what are you doin', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_3.png'},
            4: {'title': 'salo earth', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_4.png'},
            5: {'title': 'yoyo huny singh', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_5.png'}
        }
        
        self.cnt = 5
        self.selected_image_index = None
        self.image_containers = []
        self.create_image_containers()
        
        self.image_column = ft.Column(
            self.image_containers,
            alignment=ft.alignment.center
        )
        
        # Initialize components
        self.image_operations = ImageOperations(self)
        self.top_bar_component = TopBar(self)
        self.side_toolbar_component = SideToolbar()
        self.steps_list_component = StepsList(self)
        self.step_details_component = StepDetails(self)
        
    def create_image_containers(self):
        self.image_containers = []
        for i in range(1, self.cnt+1):
            image = ft.Image(
                src=f"{self.steps_data[i]['screenshot_path']}",
                width=500,
                height=500,
                fit=ft.ImageFit.CONTAIN,
            )
            
            # Create a container that can be styled differently when selected
            container = ft.Container(
                content=image,
                border_radius=10,
                padding=5,
                data=i,  # Store the index in the data attribute
                on_click=self.on_image_click,
            )
            self.image_containers.append(container)
    
    def on_image_click(self, e):
        clicked_index = e.control.data
        
        # Deselect all images first
        for container in self.image_containers:
            container.border = None
            container.bgcolor = None
        
        # If clicking on already selected image, deselect it
        if self.selected_image_index == clicked_index:
            self.selected_image_index = None
        else:
            # Select the clicked image
            self.selected_image_index = clicked_index
            e.control.border = ft.border.all(3, ft.Colors.BLUE)
            e.control.bgcolor = ft.Colors.BLUE_100
            
            # Update the step details panel with the selected image details
            title = self.steps_data[clicked_index]["title"]
            description = self.steps_data[clicked_index]["description"]
            self.update_step_details(clicked_index, title, description)
        
        # Update the image operation controls visibility
        self.image_operations.update_image_operations_visibility()
        
        # Update the UI
        self.page.update()
    
    def update_step_details(self, clicked_index, current_index_title, current_index_description):
        
        self.step_details_component.update_details(clicked_index, current_index_title, current_index_description)
    
    def select_step(self, index):
        """Handle step selection from the steps list"""
        # Simulate a click on the corresponding image container
        pass

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
                    # Add image operation controls before the images
                    self.image_operations.controls,
                    self.image_column
                ],
                scroll="always",
            ),
            expand=True,
            bgcolor="#F0F0F0",
        )

    def build(self):
        self.controls = [
            self.top_bar_component,
            ft.Row(
                [
                    self.side_toolbar_component,
                    self.steps_list_component.build(),
                    self.main_content(),
                    self.step_details_component,
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
                expand=True,
            ),
        ]
        self.expand = True