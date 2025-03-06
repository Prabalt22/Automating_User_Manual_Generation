import flet as ft
import os
from flet_contrib.color_picker import ColorPicker
from config import CURSOR_DIRECTORY_PATH
from backend.insert_setting_data import insert_data

class SettingsPage(ft.Column):
    def __init__(self, page, main_instance_function_back):
        super().__init__()
        self.page = page
        self.main_instance_function_back = main_instance_function_back
        
        # setting element
        # getting type of cursor
        self.cursor_directory_path = CURSOR_DIRECTORY_PATH
        cursor_list = self.get_png_files_dropdown(self.cursor_directory_path)
        self.dropdown_options = [ft.dropdown.Option(title) for title in cursor_list]
        self.cursor_type = ft.Dropdown(
            width=200,
            options=self.dropdown_options,
            value="Windows Pointer"
        )
        
        # selecting the folder path
        self.setup_file_picker()
        self.color_picker = ColorPicker()
        # selectin the directory path
        self.selected_directory_path = ""
        
        
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
                    ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, tooltip="Profile"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#FFD966",                              # Yellow background
            height=50,
            padding=ft.padding.symmetric(horizontal=15),
        )
        
    def get_png_files_dropdown(self, directory_path):
        
        if not os.path.exists(directory_path):
            return []
        try:
            png_file = [file for file in os.listdir(directory_path) if file.endswith('.png')]
            return png_file
        except Exception as e:
            raise e
            
    def setup_file_picker(self):
        self.selected_directory = ft.Text()
        self.pick_files_dialog = ft.FilePicker(
            on_result=self.on_directory_picked
        )
        self.page.overlay.append(self.pick_files_dialog)
        
        self.directory_picker = ft.Card(
            content=ft.Container(
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.GREY_100,
                content=ft.Column([
                    ft.Text("Select Screenshot Folder", size=18, weight=ft.FontWeight.W_600),
                    ft.Text("Choose where screenshots will be saved.", size=14, color=ft.Colors.GREY_600),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Select Directory",
                                icon=ft.Icons.FOLDER_OPEN,
                                bgcolor=ft.Colors.BLUE_500,
                                color=ft.Colors.WHITE,
                                on_click=lambda _: self.pick_files_dialog.get_directory_path()
                            ),
                            self.selected_directory,  # Display selected folder
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ], spacing=10),
            ),
            elevation=3  # Subtle shadow
        )
    
    def on_directory_picked(self, e: ft.FilePickerResultEvent):
        self.selected_directory.value = e.path if e.path else "No directory selected"
        self.selected_directory_path = e.path if e.path else "No directory selected"
        self.selected_directory.update()
    
    def backButton(self,e):
        self.main_instance_function_back()
    
    def add_to_database(self):
        try:
            insert_data((self.cursor_type.value, self.selected_directory_path, self.color_picker.r.value, self.color_picker.g.value, self.color_picker.b.value))
            print("data inseted")
        except Exception as e:
            raise e
        
    def color_pickers(self):
        pass
        # color_picker1 = ColorPicker()
              
    
    def build(self):
        self.controls = [
            self.top_bar(),
            ft.Column([            
                
                # Show cursor
                ft.Row([
                    ft.Column([
                        ft.Text("Show cursor", size=16, weight=ft.FontWeight.W_500),
                        ft.Text(
                            "Spot where you clicked will have a cursor icon",
                            size=12,
                            color=ft.Colors.GREY_700
                        )
                    ], expand=True),
                    self.cursor_type
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                
                # Directory selection
                self.directory_picker,

                # color picker
                self.color_picker,   
                
                # Mode
                ft.ElevatedButton("Submit",
                    bgcolor="blue", 
                    on_click=lambda _:self.add_to_database()
                )
                
                ], 
                spacing=20,
                scroll=ft.ScrollMode.ALWAYS,
                expand=True
            ) 
        ]

