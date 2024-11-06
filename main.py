import flet as ft

def main(page: ft.Page):
    page.title = 'Autenticator'
    page.window.width = 500
    page.window.height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = False
    page.padding = ft.padding.all(0)
    page.bgcolor = ft.colors.GREY_500

    def logar(e: ft.ControlEvent):
        page.remove(register)
        page.add(login)
    
    def registar(e: ft.ControlEvent):
        page.remove(login)
        page.add(register)

    login = ft.Column(
        controls=[
            ft.Container(
                bgcolor=ft.colors.BLACK45,
                border_radius=10,
                width= 400,
                height= 320,
                padding=ft.padding.all(10),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='G2R Dev',
                            weight='bold',
                            size=25,
                            color=ft.colors.GREEN_400
                        ),
                        ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text='Digite seu email',
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    )
                                ),
                                ft.TextField(
                                    hint_text='Digite a sua senha',
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    password=True,
                                    can_reveal_password=True
                                ),
                                ft.ElevatedButton(
                                    text='Login',
                                    color=ft.colors.BLACK,
                                    bgcolor=ft.colors.BLUE,
                                    width=400,
                                    height=40
                                )
                            ],
                            spacing=15
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton(
                                    text='Recuperar senha'
                                ),
                                ft.TextButton(
                                    text='Criar nova conta',
                                    on_click=lambda e: registar(e)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.EMAIL
                                ),
                                ft.IconButton(
                                    icon=ft.icons.TELEGRAM
                                ),
                                ft.IconButton(
                                    icon=ft.icons.FACEBOOK
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    register = ft.Column(
        controls=[
            ft.Container(
                bgcolor=ft.colors.BLACK12,
                border_radius=10,
                width= 400,
                padding=ft.padding.all(10),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Register',
                            weight='bold',
                            size=20,
                            color=ft.colors.GREEN_400
                        ),
                        ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text='Primeiro nome',
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    )
                                ),
                                ft.TextField(
                                    hint_text='Último nome',
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    )
                                ),
                                ft.TextField(
                                    hint_text='email',
                                    prefix_icon=ft.icons.EMAIL,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    keyboard_type=ft.KeyboardType.EMAIL
                                ),
                                ft.TextField(
                                    hint_text='Digite o seu telefone',
                                    prefix_icon=ft.icons.PHONE,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    keyboard_type=ft.KeyboardType.PHONE
                                ),
                                ft.TextField(
                                    hint_text='Digite a sua senha',
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    password=True,
                                    can_reveal_password=True
                                ),
                                ft.TextField(
                                    hint_text='Digite a senha novamente',
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=12,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    password=True,
                                    can_reveal_password=True
                                ),
                                ft.ElevatedButton(
                                    text='Salvar',
                                    color=ft.colors.BLACK,
                                    bgcolor=ft.colors.BLUE,
                                    width=400,
                                    height=40
                                )
                            ],
                            spacing=15
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton(
                                    text='Já tenho uma conta',
                                    on_click=lambda e: logar(e)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)