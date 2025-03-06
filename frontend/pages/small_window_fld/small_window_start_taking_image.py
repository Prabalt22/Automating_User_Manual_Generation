import flet as ft
from frontend.pages.dashboard_fld.dashboard import StepGuideCreator

class CapturingPage(ft.Column):
    def __init__(self, page, curr_guide_name, mouse_listener):
        super().__init__()
        self.page = page
        self.curr_guide_name = curr_guide_name
        self.page.title = "Screenshot App"
        self.page.window.width = 410
        self.page.window.height = 650
        self.steps = 0
        
        # Initialize the constructor 
        self.mouse_listener = mouse_listener 
        
        # data to step
        self.steps_data = {} 
        
        self.steps_text = ft.TextField(f"Number of steps: {self.steps}")
        self.title = ft.TextField(label = "Click \"Desktop\"", on_change=self.title_edit)
        self.description = ft.TextField(
                                label="Step Description",
                                multiline=True,
                                min_lines=2,
                                on_change=self.description_edit
                            )
        self.taken_screenshot = ft.Image(
                                src=f"assets/software-update-1.png",
                                width=200,
                                height=150,
                                fit=ft.ImageFit.CONTAIN,
                            )
        
        
        # buttons
        self.pause_btn = ft.OutlinedButton(
                "Pause",
                icon=ft.Icons.PAUSE,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=20
                ),
                data = "start button",
                on_click = self.toggle_action
            )
        self.finish_btn = ft.ElevatedButton(
                "Finish",
                icon=ft.Icons.CHECK,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    bgcolor=ft.Colors.GREEN,
                    color=ft.Colors.WHITE,
                    padding=20
                ),
                on_click=self.finish_screenshot_bottom
        )
    
    
    def toggle_action(self, e):
        if e.control.data == "Pause":
            e.control.text = "Pause"
            e.control.icon=ft.Icons.PAUSE
            e.control.style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=20
            )
            e.control.data = "start button"
            self.mouse_listener.begin1()
            print("Resume mouse listener")
            
        else:
            e.control.text="Start button"
            e.control.style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
                padding=20
            )
            e.control.data = "Pause"
            self.mouse_listener.end()
            print("Pause mouse listener")
       
        e.control.update()
            
    def finish_screenshot_bottom(self, e):
        self.stop_mouse_listener(e)
        self.page.clean()
        self.page.add(StepGuideCreator(self.page, self.curr_guide_name,  self.steps_data))
        self.page.update()
        
    def stop_mouse_listener(self, e):
        self.mouse_listener.end()
        print("c1hi")
    
    def title_edit(self, e):
        self.steps_data[self.steps]["title"] = e.control.value
        
    def description_edit(self, e):
        self.steps_data[self.steps]["description"] = e.control.value
    
    def update_counter(self, screenshot_path):
        self.steps += 1
        self.steps_text.value = f"Number of steps: {self.steps}"
        self.taken_screenshot.src = screenshot_path
        
        self.steps_data[self.steps] = {
            "title":"", 
            "description":"",
            "screenshot_path":screenshot_path
        }
        
        # reset the field
        self.title.value = ""
        self.description.value = ""
        
        # update ui
        self.steps_text.update()
        self.title.update()
        self.description.update()
        self.taken_screenshot.update()
        
    
    def step_details(self):
        return ft.Container(
            content=ft.Column([
                self.steps_text,
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Text("Latest step details", weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.WHITE,
                            padding=10,
                            border_radius=5
                        ),
                        ft.Container(
                            content=self.taken_screenshot,
                            padding=10
                        ),
                        self.title,
                        ft.Container(
                            content=self.description,
                            padding=10
                        )
                    ]),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(1, "black"),
                    padding=20
                )
            ])
        )

    def action_buttons(self):
        return ft.Row([
            self.pause_btn,
            self.finish_btn,
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def build(self):
        self.controls = [
            ft.Container(
                content=self.step_details(),
                padding=20,
                alignment=ft.alignment.center
            ),
            self.action_buttons()
        ]
        self.spacing = 20
        self.expand = True
        
                  