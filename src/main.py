import flet as ft
import asyncio
from assets.home import HomePage
from assets.loading import Loading


async def transition_to_home(page: ft.Page):
    # Mostra a tela de loading inicialmente
    loading_screen = Loading(page).build()
    page.add(loading_screen)
    page.update()

    # Aguarda 3 segundos
    await asyncio.sleep(3)

    # Remove a tela de loading e adiciona a HomePage
    page.controls.clear()
    home_screen = HomePage(page).build()
    page.add(home_screen)
    page.update()


def main(page: ft.Page):
    page.fonts = {"Poppins": "Poppins-Regular.ttf", "Poppins_Bold": "Poppins-Bold.ttf"}
    page.theme = ft.Theme(font_family="Poppins")
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#101010"
    page.window_width = 390
    page.window_height = 844

    # Executa a transição entre telas
    asyncio.run(transition_to_home(page))


ft.app(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
