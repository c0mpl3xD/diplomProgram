import flet as ft
from flet_route import Routing, path
from screens.login import Login
from screens.registration import Registration
from screens.main_page import Main_page

def main(page : ft.Page):
    app_routes = [
        path(
            url="/",
            clear=True,
            view=Login().view
        ),
        path(
            url="/registration",
            clear=True,
            view=Registration().view
        ),
        path(
            url="/main_page",
            clear=True,
            view=Main_page().view
        )
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

ft.app(target=main)