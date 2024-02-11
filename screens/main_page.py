from flet import *
from flet_route import Basket, Params

class Main_page:
    def __init__(self):
        pass

    def view(self, page : Page, params: Params, basket : Basket):

        cameraDD = Dropdown(width=200, label="Камери", hint_text="Оберіть камеру", options=[
            dropdown.Option("Camera1"),
            dropdown.Option("Camera2")
        ])

        return View(
            "/main_page",
            controls=[
                cameraDD
            ]
        )