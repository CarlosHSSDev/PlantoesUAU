import flet as ft
import asyncio
import requests
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


async def periodic_requests():
    """
    Função que realiza requisições periódicas ao servidor Flask.
    """
    while True:
        try:
            # Faz uma requisição GET para o servidor Flask
            response = requests.get("http://127.0.0.1:5000/")
            print(f"Flask response: {response.json()}")
        except Exception as e:
            print(f"Error in periodic request: {str(e)}")

        # Aguarda 30 segundos antes de repetir
        await asyncio.sleep(30)


def main(page: ft.Page):
    page.fonts = {"Poppins": "Poppins-Regular.ttf", "Poppins_Bold": "Poppins-Bold.ttf"}
    page.theme = ft.Theme(font_family="Poppins")
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#101010"

    async def run_tasks():
        await asyncio.gather(
            transition_to_home(page),
            periodic_requests()
        )

    asyncio.run(run_tasks())


ft.app(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
