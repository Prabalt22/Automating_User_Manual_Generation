import flet as ft

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
        
        # Add image operation controls
        self.image_operation_controls = self.create_image_operation_controls()
        
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
            self.update_step_details(clicked_index)
        
        # Update the image operation controls visibility
        self.update_image_operations_visibility()
        
        # Update the UI
        self.page.update()
    
    def update_step_details(self, index):
        """Update the step details panel with the selected image info"""
        # This is where you would update the text fields in the step details panel
        pass
    
    def create_image_operation_controls(self):
        """Create controls for image operations"""
        return ft.Column([
            ft.Row([
                ft.ElevatedButton(
                    "Crop",
                    icon=ft.Icons.CROP,
                    on_click=self.crop_image,
                    visible=False,
                ),
                ft.ElevatedButton(
                    "Rotate",
                    icon=ft.Icons.ROTATE_RIGHT,
                    on_click=self.rotate_image,
                    visible=False,
                ),
                ft.ElevatedButton(
                    "Delete",
                    icon=ft.Icons.DELETE,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.RED_400,
                        color=ft.Colors.WHITE,
                    ),
                    on_click=self.delete_image,
                    visible=False,
                ),
            ], spacing=10)
        ], visible=False)
    
    def update_image_operations_visibility(self):
        """Show or hide image operation controls based on selection state"""
        visible = self.selected_image_index is not None
        self.image_operation_controls.visible = visible
        for control in self.image_operation_controls.controls[0].controls:
            control.visible = visible
        
    def crop_image(self, e):
        if self.selected_image_index:
            # Implement cropping functionality
            self.snack_bar = ft.SnackBar(
                content=ft.Text(f"Cropping image {self.selected_image_index}"),
                action="Close"
            )
            self.page.overlay.append(self.snack_bar)
            self.snack_bar.open = True
            self.page.update()
    
    def rotate_image(self, e):
        if self.selected_image_index:
            # Implement rotation functionality
            self.snack_bar = ft.SnackBar(
                content=ft.Text(f"Rotating image {self.selected_image_index}"),
                action="Close"
            )
            self.page.overlay.append(self.snack_bar)
            self.snack_bar.open = True
            self.page.update()
    
    def delete_image(self, e):
        if self.selected_image_index:
            # Show confirmation dialog
            def confirm_delete(e):
                # Delete the image
                del self.steps_data[self.selected_image_index]
                
                # Renumber the remaining steps
                new_steps_data = {}
                index = 1
                for i in sorted(self.steps_data.keys()):
                    new_steps_data[index] = self.steps_data[i]
                    index += 1
                
                self.steps_data = new_steps_data
                self.cnt = len(self.steps_data)
                
                # Recreate the image containers
                self.create_image_containers()
                self.image_column.controls = self.image_containers
                
                # Reset selection
                self.selected_image_index = None
                self.update_image_operations_visibility()
                
                # Close the dialog
                self.dialog.open = False
                self.page.update()
            
            def cancel_delete(e):
                self.dialog.open = False
                self.page.update()
            
            self.dialog = ft.AlertDialog(
                title=ft.Text("Confirm Deletion"),
                content=ft.Text(f"Are you sure you want to delete image {self.selected_image_index}?"),
                actions=[
                    ft.TextButton("Yes", on_click=confirm_delete),
                    ft.TextButton("No", on_click=cancel_delete),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            
            self.page.overlay.append(self.dialog)
            self.dialog.open = True
            self.page.update()

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
                                title=ft.Text(self.steps_data[i]["title"]),
                                dense=True,
                                on_click=lambda e, idx=i: self.select_step(idx),
                            ) for i in range(1, self.cnt+1)
                        ],
                        spacing=2,
                    ),
                ],
            ),
            width=200,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(right=ft.BorderSide(1, ft.Colors.BLACK12)),
        )
    
    def select_step(self, index):
        """Handle step selection from the steps list"""
        # Simulate a click on the corresponding image container
        # fake_event = type("Event", (), {
        #     "control": self.image_containers[index - 1],
        #     "data": index,
        #     "page": self.page
        # })()
        
        # self.on_image_click(fake_event)
        # self.on_image_click(ft.ControlEvent(self.image_containers[index-1], None))

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
                    self.image_operation_controls,
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
        # self.page.window.width = 900  
        # self.page.window.height = 600 


def main(page: ft.Page):
    page.theme_mode = "light"
    # page.window.width = 1200
    # page.window.height = 700
    page.add(StepGuideCreator(page))
    
ft.app(target=main)