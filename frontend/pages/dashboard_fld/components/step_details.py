import flet as ft
import re

class StepDetails(ft.Container):
    def __init__(self, main_instance):
        super().__init__()
        self.main_instance = main_instance
        
        self.title_field = ft.TextField(
            label="Title",
            value=" ",
            on_change=self.edit_title
        )
        self.description_field = ft.TextField(
            label="Description",
            multiline=True,
            min_lines=3,
            on_change=self.edit_description
        )
        self.style_dropdown = ft.Dropdown(
            width=120,
            options=[
                ft.dropdown.Option("Normal"),
                ft.dropdown.Option("Heading 1"),
                ft.dropdown.Option("Heading 2"),
                ft.dropdown.Option("Heading 3"),
            ],
            value="Normal",
            on_change=self.on_style_change
        )
        self.select_image_index = None
        self.is_bold = False
        self.is_italic = False
        self.is_underlined = False
        self.is_strikethrough = False
        self.is_quote = False
        self.is_code = False
        self.is_bullet_list = False
        self.is_numbered_list = False
        self.is_checklist = False
        
    def toggle_bold(self, e):
        if self.main_instance.selected_image_index:
            
            self.is_bold = not self.is_bold
            
            if self.is_bold:
                self.description_field.text_style = ft.TextStyle(weight=ft.FontWeight.BOLD)
                e.control.style = ft.ButtonStyle(
                    bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
                )
            else:
                self.description_field.text_style = ft.TextStyle(weight=ft.FontWeight.NORMAL)
                e.control.style = ft.ButtonStyle(
                    bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
                )

            self.description_field.update()
    
    def toggle_italic(self, e):
        self.is_italic = not self.is_italic
        
        if self.is_italic:
            self.description_field.text_style = ft.TextStyle(italic=True)
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            self.description_field.text_style = ft.TextStyle(italic=False)
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def toggle_underline(self, e):
        self.is_underlined = not self.is_underlined
        
        if self.is_underlined:
            self.description_field.text_style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            self.description_field.text_style = ft.TextStyle(decoration=ft.TextDecoration.NONE)
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def toggle_strikethrough(self, e):
        self.is_strikethrough = not self.is_strikethrough
        
        if self.is_strikethrough:
            self.description_field.text_style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            self.description_field.text_style = ft.TextStyle(decoration=ft.TextDecoration.NONE)
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def on_style_change(self, e):
        if self.main_instance.selected_image_index:
            selected_style = e.control.value
            # Apply different text sizes based on selection
            if selected_style == "Normal":
                sizes = 14
            elif selected_style == "Heading 1":
                sizes = 16
            elif selected_style == "Heading 2":
                sizes = 20
            elif selected_style == "Heading 3":
                sizes = 24
            
            self.description_field.text_style = ft.TextStyle(size=sizes)
            
            self.description_field.update()                                    
    
    def toggle_quote(self, e):
        self.is_quote = not self.is_quote
        
        if self.is_quote:
            # Apply quote formatting
            current_text = self.description_field.value
            self.description_field.value = f"> {current_text}"
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            # Remove quote formatting
            current_text = self.description_field.value
            if current_text.startswith("> "):
                self.description_field.value = current_text[2:]
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def toggle_code(self, e):
        self.is_code = not self.is_code
        
        if self.is_code:
            # Apply code formatting
            current_text = self.description_field.value
            self.description_field.value = f"```\n{current_text}\n```"
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            # Remove code formatting
            current_text = self.description_field.value
            if current_text.startswith("```\n") and current_text.endswith("\n```"):
                self.description_field.value = current_text[4:-4]
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def toggle_bullet_list(self, e):
        self.is_bullet_list = not self.is_bullet_list
        
        if self.is_bullet_list:
            # Apply bullet list formatting
            current_text = self.description_field.value
            lines = current_text.split('\n')
            self.description_field.value = '\n'.join([f"• {line}" for line in lines])
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            # Remove bullet list formatting
            current_text = self.description_field.value
            lines = current_text.split('\n')
            self.description_field.value = '\n'.join([line[2:] if line.startswith("• ") else line for line in lines])
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def toggle_numbered_list(self, e):
        self.is_numbered_list = not self.is_numbered_list
        
        if self.is_numbered_list:
            # Apply numbered list formatting
            current_text = self.description_field.value
            lines = current_text.split('\n')
            self.description_field.value = '\n'.join([f"{i+1}. {line}" for i, line in enumerate(lines)])
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            # Remove numbered list formatting
            current_text = self.description_field.value
            lines = current_text.split('\n')
            # Remove numbering (assumes format like "1. ", "2. ", etc.)
            self.description_field.value = '\n'.join([line[line.find(". ")+2:] if re.match(r'^\d+\.\s', line) else line for line in lines])
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()

    def toggle_checklist(self, e):
        """
        The function `toggle_checklist` toggles checklist formatting in a text field based on the
        current state.
        
        :param e: The parameter `e` in the `toggle_checklist` method is likely an event object that
        contains information about the event that triggered the method. This object may include details
        such as the type of event, the target element that triggered the event, and any additional data
        related to the event. The method
        """
        self.is_checklist = not self.is_checklist
        
        if self.is_checklist:
            # Apply checklist formatting
            current_text = self.description_field.value
            lines = current_text.split('\n')
            self.description_field.value = '\n'.join([f"- [ ] {line}" for line in lines])
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_300}
            )
        else:
            # Remove checklist formatting
            current_text = self.description_field.value
            lines = current_text.split('\n')
            self.description_field.value = '\n'.join([line[6:] if line.startswith("- [ ] ") else line for line in lines])
            e.control.style = ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.WHITE}
            )
        
        self.description_field.update()
    
    def tool_container(self):
            
        toolbar = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                    [
                        self.style_dropdown,
                        ft.IconButton(
                            icon=ft.Icons.FORMAT_BOLD,
                            tooltip="Bold",
                            on_click=self.toggle_bold
                        ),
                        ft.IconButton(
                            icon=ft.Icons.FORMAT_ITALIC,
                            tooltip="Italic",
                            on_click=self.toggle_italic
                        ),
                        ft.IconButton(
                            icon=ft.Icons.FORMAT_UNDERLINED,
                            tooltip="Underline",
                            on_click=self.toggle_underline
                        )
                    ],  spacing=1),
                    ft.Row(
                    [  
                        ft.IconButton(
                            icon=ft.Icons.STRIKETHROUGH_S,
                            tooltip="Strikethrough",
                            on_click=self.toggle_strikethrough
                        ),
                        ft.IconButton(
                            icon=ft.Icons.FORMAT_QUOTE,
                            tooltip="Quote",
                            on_click=self.toggle_quote
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CODE,
                            tooltip="Code block",
                            on_click=self.toggle_code
                        ),
                        ft.IconButton(
                            icon=ft.Icons.FORMAT_LIST_BULLETED,
                            tooltip="Bulleted list",
                            on_click=self.toggle_bullet_list
                        ),
                        ft.IconButton(
                            icon=ft.Icons.FORMAT_LIST_NUMBERED,
                            tooltip="Numbered list",
                            on_click=self.toggle_numbered_list
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CHECKLIST,
                            tooltip="Checklist",
                            on_click=self.toggle_checklist
                        )
                    ],spacing=1)
                ],
                spacing=10,
            ),
            padding=10,
            border=ft.border.all(1, ft.Colors.OUTLINE),
            border_radius=5
        )
        return toolbar
    
    def edit_title(self, e):
        if self.select_image_index:    
            self.main_instance.steps_data[self.select_image_index]["title"] = e.control.value
               
    def edit_description(self, e):
        if self.select_image_index:
            self.main_instance.steps_data[self.select_image_index]["description"] = e.control.value
               
    def update_details(self, clicked_index, title, description):
        self.title_field.value = title
        self.description_field.value = description
        self.select_image_index = clicked_index
    
    def build(self):
        self.content=ft.Column(
            [
                ft.Row(
                    [ft.Text("Step Details", size=16, weight=ft.FontWeight.BOLD)],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                self.title_field,
                self.tool_container(),
                self.description_field,
            ],
            spacing=20,
        )
        self.width=300
        self.padding=20
        self.bgcolor=ft.Colors.WHITE
        self.border=ft.border.only(left=ft.BorderSide(1, ft.Colors.BLACK12))
        