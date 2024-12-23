import flet as ft
from assets.elementos import SearchInput, ButtonGradient
from assets.table_plantoes import TablePlantoes  # Importando a tela TablePlantoes

lista_nomes = [
    "Marcos Vinicius",
    "Filipe",
    "Carlos",
    "Rafael",
    "Valdemir",
    "Hicaro",
    "Rodrigo Santana",
    "Gabriel",
    "Caio",
    "Josiel",
    "Gisnei",
    "Daniel",
    "Henrique",
    "Genisson",
    "Ayrton",
    "Romário",
    "Uelio",
    "Davi",
    "Valdenilson",
    "Wesley",
    "Moises",
    "José Leoni",
    "Jardel",
    "Ailton",
    "José Williams",
]


class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.component = self.build()

    def build(self):
        def navigate_to_table(e):
            # Verifica se o campo de entrada não está vazio
            if not self.page.data:  # Se o campo estiver vazio
                # Adiciona uma mensagem de erro ou um aviso
                self.page.add(
                    ft.Text(
                        "Por favor, preencha o campo de nome!", color="red", size=16
                    )
                )
                self.page.update()
                return  # Impede que a navegação continue

            # Limpa a página atual e exibe a TablePlantoes
            self.page.controls.clear()
            self.page.add(TablePlantoes(self.page, self.page.data).build())
            self.page.update()

        def item_selected(item):
            self.page.data = item

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
                                        "Seja bem-vindo ao plantões Uaubr. Aqui você verá com mais facilidade e precisão quais serão os plantões que você irá fazer durante o ano vigente.",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    SearchInput(
                                        "Digite seu nome",
                                        lista_nomes,
                                        on_select_item=item_selected,
                                    ).build(),
                                ],
                                spacing=50,
                            ),
                            ft.Row(
                                [
                                    ButtonGradient(
                                        content=ft.Text(
                                            "Ver meus plantões",
                                            size=16,
                                            font_family="Poppins",
                                            color="#f0f0f0",
                                        ),
                                        colors=["#0897D2", "#004E6E"],
                                        on_click=navigate_to_table,  # Adiciona o evento de clique
                                    ).build()
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
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
