import flet as ft
from config import ALERT_DIALOG_IMAGE

class CheckSetting(ft.Column): 
    def __init__(self,page):
        super().__init__()
        self.page = page
        # self.dialog.open = True
        # self.page.update()
        
        self.dialog = ft.AlertDialog(
            
            # title
            title=ft.Row(controls=[
                ft.Text("New Version Available!",size=30)
                ],alignment="center"),
            
            # content
            content=ft.Column(
                [
                    ft.Image(
                        src=f"{ALERT_DIALOG_IMAGE}\\software-update-1.png",
                        width=300,height=150,
                        fit=ft.ImageFit.CONTAIN ),
                    ft.Text(
                        "PLS Check Setting Panel to Update the Image Download Folder",
                            width=300,
                            text_align=ft.TextAlign.CENTER 
                )],
                width=400,
                height=250,
                spacing=30,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER ),
            
            # action
            actions=[
                ft.ElevatedButton("I'II DO it Later",
                                  icon=ft.Icons.ARROW_BACK,
                                  on_click=lambda _:self.handle_close()),
                ft.ElevatedButton("PLS CHECK YOUR SETTING",
                                  icon=ft.Icons.FILE_UPLOAD_SHARP,
                                  bgcolor = "#cf5cb2",
                                  color = "black",
                                  on_click=lambda _:self.handle_close()),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
        
        
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()    
    
      
    def handle_close(self):
        self.dialog.open = False
        self.page.update()
        