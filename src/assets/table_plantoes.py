import flet as ft
from assets.elementos import ButtonGradient
from assets.ponto import GerenciadorPlantoes
import json


class TablePlantoes:
    def __init__(self, page: ft.Page, nome_usuario: str):
        self.page = page
        self.nome_usuario = nome_usuario
        self.component = self.build()

    def build(self):
        # Dados para a tabela
        print(self.nome_usuario)
        equipes = {
            "Equipe 1": ["Marcos Vinicius", "Filipe", "Carlos", "Rafael"],
            "Equipe 2": ["Valdemir", "Hicaro", "Rodrigo Santana", "Gabriel"],
            "Equipe 3": ["Caio", "Josiel", "Gisnei", "Daniel"],
            "Equipe 4": ["Henrique", "Genisson", "Ayrton", "Romário"],
            "Equipe 5": ["Uelio", "Davi", "Valdenilson", "Rafael"],
            "Equipe 6": ["Wesley", "Moises", "José Leoni", "Gabriel"],
            "Equipe 7": ["Jardel", "Ailton", "José Williams", "Daniel"],
        }

        gerenciador = GerenciadorPlantoes(2024, 2025, equipes)

        # Filtra os plantões do usuário
        plantao_usuario_json = gerenciador.filtrar_por_usuario(self.nome_usuario)

        table_data = [
            {"data": plantao["data"], "descricao": plantao["descricao"]}
            for plantao in json.loads(plantao_usuario_json)
        ]

        def navigate_to_home(e):
            from assets.home import HomePage

            # Limpa os controles e exibe a tela HomePage
            self.page.controls.clear()
            self.page.add(HomePage(self.page).component)
            self.page.update()

        return ft.SafeArea(
            content=ft.Column(
                [
                    ft.Column(
                        [
                            ft.Image(
                                src="Uaubr_logo.png",
                                fit=ft.ImageFit.CONTAIN,
                                width=150,
                                height=50,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "Veja na tabela abaixo quais serão os seus dias de plantão!",
                                        text_align=ft.TextAlign.CENTER,
                                        size=14,
                                        font_family="Poppins",
                                    ),
                                    # Tabela de dados
                                    ft.Column(
                                        [
                                            ft.DataTable(
                                                columns=[
                                                    ft.DataColumn(
                                                        ft.Text(
                                                            "Data",
                                                            font_family="Poppins_Bold",
                                                            size=14,
                                                        )
                                                    ),
                                                    ft.DataColumn(
                                                        ft.Text(
                                                            "Descrição",
                                                            font_family="Poppins_Bold",
                                                            size=14,
                                                        )
                                                    ),
                                                ],
                                                rows=[
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(
                                                                ft.Text(
                                                                    row["data"],
                                                                    font_family="Poppins",
                                                                    expand=True,
                                                                )
                                                            ),
                                                            ft.DataCell(
                                                                ft.Text(
                                                                    row["descricao"],
                                                                    font_family="Poppins",
                                                                    expand=True,
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                    for row in table_data
                                                ],
                                                expand=True,
                                            )
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                    ),
                                    ft.Row(
                                        [
                                            ButtonGradient(
                                                content=ft.Text(
                                                    "Voltar",
                                                    size=16,
                                                    font_family="Poppins",
                                                    color="#f0f0f0",
                                                ),
                                                colors=["#0897D2", "#004E6E"],
                                                on_click=navigate_to_home,  # Evento do botão
                                            ).build()
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                spacing=30,
                            ),
                        ],
                        spacing=30,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Developed by: Carlos S.",
                                size=12,
                                font_family="Poppins_Bold",
                                color="#0CA8E8",
                            ),
                            ft.Text(
                                "Contact: (79) 99685-3126",
                                size=12,
                                font_family="Poppins",
                                color="#0CA8E8",
                            ),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
        )
