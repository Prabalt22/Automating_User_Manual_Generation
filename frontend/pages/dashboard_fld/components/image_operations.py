import flet as ft

class ImageOperations:
    def __init__(self, parent):
        self.parent = parent
        self.controls = self.create_image_operation_controls()
    
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
        visible = self.parent.selected_image_index is not None
        self.controls.visible = visible
        for control in self.controls.controls[0].controls:
            control.visible = visible
        
    def crop_image(self, e):
        if self.parent.selected_image_index:
            # Implement cropping functionality
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Cropping image {self.parent.selected_image_index}"),
                action="Close"
            )
            self.parent.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.parent.page.update()
    
    def rotate_image(self, e):
        if self.parent.selected_image_index:
            # Implement rotation functionality
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Rotating image {self.parent.selected_image_index}"),
                action="Close"
            )
            self.parent.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.parent.page.update()
    
    def delete_image(self, e):
        if self.parent.selected_image_index:
            # Show confirmation dialog
            def confirm_delete(e):
                # Delete the image
                del self.parent.steps_data[self.parent.selected_image_index]
                
                # Renumber the remaining steps
                new_steps_data = {}
                index = 1
                for i in sorted(self.parent.steps_data.keys()):
                    new_steps_data[index] = self.parent.steps_data[i]
                    index += 1
                
                self.parent.steps_data = new_steps_data
                self.parent.cnt = len(self.parent.steps_data)
                
                # Recreate the image containers
                self.parent.create_image_containers()
                self.parent.image_column.controls = self.parent.image_containers
                
                # Reset selection
                self.parent.selected_image_index = None
                self.update_image_operations_visibility()
                
                # Close the dialog
                dialog.open = False
                self.parent.page.update()
            
            def cancel_delete(e):
                dialog.open = False
                self.parent.page.update()
            
            dialog = ft.AlertDialog(
                title=ft.Text("Confirm Deletion"),
                content=ft.Text(f"Are you sure you want to delete image {self.parent.selected_image_index}?"),
                actions=[
                    ft.TextButton("Yes", on_click=confirm_delete),
                    ft.TextButton("No", on_click=cancel_delete),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            
            self.parent.page.overlay.append(dialog)
            dialog.open = True
            self.parent.page.update()