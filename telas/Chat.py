import flet as ft
from components.TextBox import TextBox
from components.Input import Input
from components.llm import chain

class Chat(ft.Column):
    
    def __init__(self):
        super().__init__(expand=True, width= 800)
        
        self.__input = Input(function = lambda e : self.send_Input(e))
        
        self.__user_text = ''
        self.__ai = chain
        
        self.controls = [
            ft.Column(controls=[
                # add chat
                
            ],expand=True, scroll= ft.ScrollMode.AUTO, auto_scroll= True),
            
            self.__input,
            
        ]
        
    
    def add_user_text_box(self, e):
        
        self.controls[0].controls.append(
            ft.Row(controls=[
                ft.Icon(
                name= ft.Icons.PERSON,
                color = ft.Colors.GREEN,
                size = 30,
                ),
                ft.Text(
                    value="User",
                    weight=ft.FontWeight.BOLD,
                    selectable=True
                    
                )
            ],expand=True))
            
        self.controls[0].controls.append(
            TextBox(self.__user_text)
            )
        
    def add_IA_text_box(self, e):
        loading = ft.ProgressBar(width=30)
        
        self.controls[0].controls.append(
            ft.Row(controls=[
                ft.Icon(
                name= ft.Icons.MEMORY,
                color = ft.Colors.BLUE,
                size = 30,
                ),
                ft.Text(
                    value="JARVIS ASSISTANT",
                    weight=ft.FontWeight.BOLD,
                    selectable=True
                    
                ),
                loading
            ],expand=True))
        self.update()
        ia_box = TextBox()
        
        self.controls[0].controls.append(
            ia_box
            )
        
        txt = ""
        c = self.__ai.stream({f"texto": {self.__user_text}})
        
        for t in c:
            txt += t
            ia_box.change_text(txt)
            self.update()
        loading.visible = False
        self.update()

    
    def send_Input(self, e):
        
        if len(self.__input.get_value()) != 0:
            self.__user_text = self.__input.get_value()
            
            self.__input.clear_input()
            
            self.add_user_text_box(e)
            self.update()
            
            # ###  AI ###
            self.add_IA_text_box(e)
            
            
            
            