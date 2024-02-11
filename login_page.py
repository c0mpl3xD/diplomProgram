import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet import AppBar, RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment, View
from flet_core.control_event import ControlEvent
from API.Models.user import User
from API.Services.userService import UserService


def start_window(page : ft.Page):
    page.window_resizable = True
    #login
    user_email = ft.TextField(label="Введіть почту", width=200, height=40, text_align=ft.TextAlign.LEFT)
    user_login = ft.TextField(label="Логін", width=200, height=40, text_align=ft.TextAlign.LEFT, visible=False)
    user_password = ft.TextField(label="Пароль", width=200, height=40, text_align=ft.TextAlign.LEFT, password=True)
    button_login = ft.FilledButton(text="Авторизуватися", width=200, disabled=True)
    button_route_registration = ft.TextButton(text="Реєстрація", width=200)

    def validate_login(e: ControlEvent):
        if all([user_email.value, user_password.value]):
            button_login.disabled=False
        else:
            button_login.disabled=True
        page.update()

    def validate_registration(e: ControlEvent):
        if all([user_email.value, user_login.value, user_password.value]):
            button_login.disabled=False
        else:
            button_login.disabled=True
        page.update()

    def login(e: ControlEvent):
        user = User()
        user.email = user_email.value
        user.password = user_password.value
        service = UserService()
        res = service.login(user)
        
        #Open main window route='/main'

    def registration(e):
        user = User()
        user.id = 0
        user.email = user_email.value
        user.login = user_login.value
        user.password = user_password.value
        service = UserService()
        res = service.register(user)

    def route_change(e: RouteChangeEvent):
        page.views.clear()
        page.title = "Login"
        user_email.on_change=validate_login
        user_email.value=""
        user_login.on_change=validate_login
        user_login.value=""
        user_login.visible=False
        user_password.on_change=validate_login
        user_password.value=""
        button_login.disabled=True
        button_login.text="Авторизуватися"
        button_login.on_click=login
        button_route_registration.text="Зареєструватися"
        button_route_registration.on_click=lambda _: page.go('/registration')

        page.views.append(
            View(
                route='/login',
                controls=[
                Column(
                    [
                        user_email,
                        user_login,
                        user_password,
                        button_login,
                        button_route_registration
                    ]
                )
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            ) 
        )

        if page.route == '/registration':
            page.title = "Registration"
            user_email.value=""
            user_email.on_change=validate_registration
            user_login.on_change=validate_registration
            user_login.value=""
            user_login.visible=True
            user_password.on_change=validate_registration
            user_password.value=""
            button_login.disabled=True
            button_login.text="Зареєструватися"
            button_login.on_click=registration
            button_route_registration.text="Повернутися до авторизації"
            button_route_registration.on_click=lambda _: page.go('/login')

            page.views.append(
            View(
                route='/registration',
                controls=[
                Column(
                    [
                        user_email,
                        user_login,
                        user_password,
                        button_login,
                        button_route_registration
                    ]
                )
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ) 
        )
        
        page.update()
    
    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
    
    #login
    user_email.on_change=validate_login
    user_password.on_change=validate_login
    button_login.on_click=login
    #route
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    button_route_registration.on_click=lambda _: page.go('/registration')
    page.go(page.route)


ft.app(target=start_window)