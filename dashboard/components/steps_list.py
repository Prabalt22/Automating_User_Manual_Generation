import flet as ft

class StepsList:
    def __init__(self, parent):
        self.parent = parent
    
    def build(self):
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
                            on_click=self.add_step,
                        ),
                        padding=10,
                    ),
                    ft.ListView(
                        controls=[
                            ft.ListTile(
                                leading=ft.Text(f"{i}."),
                                title=ft.Text(self.parent.steps_data[i]["title"]),
                                dense=True,
                                on_click=lambda e, idx=i: self.parent.select_step(idx),
                            ) for i in range(1, self.parent.cnt+1)
                        ],
                        spacing=2,
                    ),
                ],
            ),
            width=200,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(right=ft.BorderSide(1, ft.Colors.BLACK12)),
        )
    
    def add_step(self, e):
        # Placeholder for adding a new step
        pass