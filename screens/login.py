from flet import *
from flet_route import Basket, Params
from API.Models.user import User
from API.Services.userService import UserService

class Login:
    def __init__(self):
        pass

    def view(self, page : Page, params: Params, basket : Basket):
        
        def login(e: ControlEvent):
            user = User()
            user.email = user_email.value
            user.password = user_password.value
            service = UserService()
            res = service.login(user)
            #page.go("/main_page")
            if res:
                page.go("/main_page")
            else:
                page.dialog = dlg
                dlg.open = True
                page.update()

        def validate_login(e: ControlEvent):
            if all([user_email.value, user_password.value]):
                button_login.disabled=False
            else:
                button_login.disabled=True
            page.update()

        dlg = AlertDialog(title=Text("Помилка"))
        user_email = TextField(label="Введіть почту", width=200, height=40, text_align=TextAlign.LEFT, on_change=validate_login)
        user_password = TextField(label="Пароль", width=200, height=40, text_align=TextAlign.LEFT, password=True, on_change=validate_login)
        button_login = FilledButton(text="Авторизуватися", width=200, disabled=True, on_click=login)
        button_route_registration = TextButton(text="Реєстрація", width=200, on_click=lambda _:page.go("/registration"))

        return View(
            "/",
            controls=[
                user_email,
                user_password,
                button_login,
                button_route_registration
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )