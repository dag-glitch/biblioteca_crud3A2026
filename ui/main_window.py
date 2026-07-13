import flet as ft

def main_window(page: ft.page):
    page.title = "Sistema de Biblioteca Universitaria"
    page.window_width = 1100
    page.window_height = 700
    page.paddig = 0 
    page.bgcolor = ft.Colors.BLUE_GREY_50

    #ejemplo de widget: Text
    titulo = ft.text("Sistema de biblioteca universitaria",
                     size=24,
                     weight= ft.FontWeight.BOLD
                     )
    
    subtitulo = ft.Text(
        "Seeleccione una opcion del menu",
        size=16,
        color = ft.Colors.BLUE_GREY_600
    )
    #Widget container
    contenido = ft.Container(
        content = ft.Column(
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10,
        ),
        padding = 30,
        expand = True
    )

    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content=ft.Column(
            controls =[
                ft.Text (
                    "Biblioteca",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestion",
                    size=12,
                    color=ft.Colors.BLUE_GREY_100
                ),
                ft.Divider(color=ft.Colors.BLUE_GREY_700),
                ft.ElevatedButton(
                    "Libros",
                    icon = ft.icons.BOOK,
                    width=100,
                ),
                ft.ElevatedButton(
                    "Usuarios",
                    icon=ft.Icons.PERSON,
                    width=180,
                ),
                ft.ElevatedButton(
                    "Prestamos",
                    icon=ft.Icons.PERSON,
                    width=180,
                ),
                ft.ElevatedButton(
                    "Devoluciones",
                    icon=ft.Icons.PERSON,
                    width=180,
                ),
            ],
            spacing=16
        )
    )

    layout = ft.Row(
        controls=[
            menu_lateral,
            contenido
        ],
        expand = True
    )
    page.add(layout)

    
    