import flet as ft

class Input(ft.Row):
    
    def __init__(self, function, theme_mode = ft.ThemeMode.LIGHT):
        super().__init__(alignment=ft.MainAxisAlignment.CENTER, width= 800)
        
        self.theme_mode = theme_mode
        self.placeholder = "Pergunte alguma coisa..."

        self.color = ft.Colors.GREY_300 if self.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.GREY_800
        
        self.__inText = ft.TextField(
            autocorrect=True,
            
            hint_text = self.placeholder,
            
            on_submit= function,
            
            show_cursor = True,
            # border= ft.InputBorder.OUTLINE,
            border_color= ft.Colors.GREY_300 if self.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.GREY_800,
            border_radius= ft.BorderRadius(bottom_left=50,
                                           bottom_right= 50,
                                           top_left=50,
                                           top_right=50,
                                           ),
            cursor_color = ft.Colors.BLACK,
            autofocus = True,
            #color= ft.Colors.BLACK,
            bgcolor = ft.Colors.GREY_300 if self.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.GREY_800,
            #text_style = ft.TextStyle(color=ft.Colors.WHITE),
            disabled= False,
            expand=True,
            )
        
        
        self.__button = ft.IconButton(icon = ft.Icons.SEND,
                                      icon_color= ft.Colors.WHITE,
                                      on_click= function,
                                      bgcolor= ft.Colors.BLACK87,
                                      mouse_cursor=ft.MouseCursor.CLICK
                                      )
        
        
        self.controls = [
            self.__inText,
            self.__button
            ]
        
    
            
    def clear_input(self):
        
        self.__inText.value = ''
        self.update()
    
    def get_value(self):
        return self.__inText.value 
