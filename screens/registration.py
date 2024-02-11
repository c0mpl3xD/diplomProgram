from flet import *
from flet_route import Basket, Params
from API.Models.user import User
from API.Services.userService import UserService

class Registration:
    def __init__(self):
        pass

    def view(self, page : Page, params: Params, basket : Basket):

        def registration(e):
            user = User()
            user.id = 0
            user.email = user_email.value
            user.login = user_login.value
            user.password = user_password.value
            service = UserService()
            res = service.register(user)

        def validate_registration(e: ControlEvent):
            if all([user_email.value, user_login.value, user_password.value]):
                button_registration.disabled=False
            else:
                button_registration.disabled=True
            page.update()
        
        user_email = TextField(label="Введіть почту", width=200, height=40, text_align=TextAlign.LEFT, on_change=validate_registration)
        user_login = TextField(label="Логін", width=200, height=40, text_align=TextAlign.LEFT, on_change=validate_registration)
        user_password = TextField(label="Пароль", width=200, height=40, text_align=TextAlign.LEFT, password=True, on_change=validate_registration)
        button_registration = FilledButton(text="Зареєструватися", width=200, disabled=True, on_click=registration)
        button_route_login = TextButton(text="Повернутися до авторизації", width=200, on_click=lambda _: page.go("/"))

        return View(
            "/registration",
            controls=[
                user_email,
                user_login,
                user_password,
                button_registration,
                button_route_login
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
