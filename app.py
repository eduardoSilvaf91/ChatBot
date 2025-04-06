import flet as ft

from telas.Chat import Chat


def main(page: ft.Page):
    
    page.window.width = 500
    page.window.height = 800
    
    page.title = "JARVIS ASSISTANT"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    chat = ft.Container(
        content = Chat(),
        expand=True,
        padding= 20,
    )

    page.add(chat)
    
        
ft.app(main)