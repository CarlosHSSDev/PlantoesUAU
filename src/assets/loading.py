import flet as ft


class Loading:
    def __init__(self, page: ft.Page):
        self.page = page
        self.component = self.build()

    def build(self):
        return ft.SafeArea(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Image(src="Uaubr_logo.png", width=300, fit=ft.ImageFit.FIT_WIDTH),
                            ft.Text(
                                "Plantões",
                                color="#f0f0f0",
                                font_family="Poppins_Bold",
                                size=32,
                            ),
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
        )


