import flet as ft
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import View, Page, AppBar, ElevatedButton, Text

def main(page: Page):
    page.title="log"

    def route_change(e: RouteChangeEvent):
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home', bgcolor='blue')),
                    Text(value='Home', size=30),
                    ElevatedButton(text='Go to reg', on_click=lambda _: page.go('/reg'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        if page.route == '/reg':
            page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('reg', bgcolor='blue')),
                    Text(value='reg', size=30),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
        
        page.update()
    
    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)