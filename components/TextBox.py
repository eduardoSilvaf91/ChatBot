import flet as ft

class TextBox(ft.Column):
    
    def __init__(self, txt = ''):
        super().__init__()
      
        
        self.__text = ft.Text(
            color=ft.ThemeMode.SYSTEM,
            value = txt,
            weight = ft.FontWeight.W_500,
            text_align = ft.TextAlign.JUSTIFY,
            selectable = True
            
        )
        
        self.color_border = ft.Colors.GREY_200
        
        self.controls= [
            ft.Container(
                content = ft.Column(
                        controls = [self.__text],
                    ),
                bgcolor = self.color_border,

                border = ft.Border(
                        top=ft.BorderSide(width=10,color=self.color_border),
                        bottom=ft.BorderSide(width=10,color=self.color_border),
                        left=ft.BorderSide(width=10,color=self.color_border),
                        right=ft.BorderSide(width=10,color=self.color_border),  
                    ),
                border_radius= ft.BorderRadius(top_left=10,
                                               top_right=10,
                                               bottom_left=10,
                                               bottom_right=10,
                                               ),
                
                width = 800,
                padding = 10,
                expand= False,
                )   
        ]
    
    def change_text(self, new_text):
        self.__text.value = new_text
        #self.update()
        