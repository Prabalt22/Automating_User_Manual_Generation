import flet as ft
# from assets import sof

class CapturingPage(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.steps = 1
    
  
    def step_details(self):
        return ft.Container(
            content=ft.Column([
                ft.Text(f"Number of steps: {self.steps}"),
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Text("Latest step details", weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.WHITE,
                            padding=10,
                            border_radius=5
                        ),
                        ft.Container(
                            content=ft.Image(
                                src=f"assets/software-update-1.png",
                                width=200,
                                height=150,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            padding=10
                        ),
                        ft.Text("Click \"Desktop\"", size=16),
                        ft.Container(
                            content=ft.TextField(
                                label="Step Description",
                                multiline=True,
                                min_lines=2
                            ),
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
            ft.OutlinedButton(
                "Pause",
                icon=ft.Icons.PAUSE,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=20
                )
            ),
            ft.ElevatedButton(
                "Finish",
                icon=ft.Icons.CHECK,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    bgcolor=ft.Colors.GREEN,
                    color=ft.Colors.WHITE,
                    padding=20
                ),
                # on_click=self.main_instance_function_back
            )
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
        
    
    
def main(page: ft.Page):
    page.title = "Screen Capture"
    page.theme_mode = "light"
    page.window.width = 410
    page.window.height = 600
    
    capture_page = CapturingPage(page)
    page.add(capture_page)


ft.app(target=main)