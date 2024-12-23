import flet as ft


class SearchInput(ft.TextField):
    def __init__(
        self, placeholder: str, suggestions: list, on_select_item=None, **kwargs
    ):
        super().__init__(**kwargs)
        self.placeholder = placeholder
        self.suggestions = suggestions
        self.on_select_item = on_select_item
        self.bgcolor = "#202020"
        self.border_color = "#202020"
        self.border_radius = 10
        self.text_style = ft.TextStyle(size=14, weight=ft.FontWeight.W_300)
        self.height = 40
        self.content_padding = ft.padding.symmetric(vertical=0, horizontal=10)
        self.suffix_icon = ft.Icons.SEARCH
        self.value = placeholder

        # Sugestões
        self.suggestion_list = ft.ListView(expand=True, spacing=0)

        # Adicionando eventos
        self.on_change = self.filter_items
        self.on_focus = self.limpar
        self.on_blur = self.blur

    def filter_items(self, e):
        search_text = e.control.value.lower()
        self.suggestion_list.controls.clear()
        for item_text in self.suggestions:
            if search_text in item_text.lower():
                self.suggestion_list.controls.append(
                    ft.ListTile(
                        title=ft.Text(item_text),
                        bgcolor="#151515",
                        data=item_text,
                        on_click=lambda x, item=item_text: self.select_item(item, e),
                    )
                )
        e.control.border_radius = ft.border_radius.only(
            bottom_left=0, bottom_right=0, top_left=10, top_right=10
        )
        e.control.update()
        self.suggestion_list.update()

    def select_item(self, item, e):
        self.value = item
        self.suggestion_list.controls.clear()
        e.control.border_radius = ft.border_radius.all(10)
        e.control.update()
        self.page.update()

        if self.on_select_item:
            self.on_select_item(item)

    def limpar(self, e):
        e.control.value = ""
        e.control.update()

    def blur(self, e):
        if e.control.value.strip() == "":
            e.control.value = self.placeholder
            self.suggestion_list.controls.clear()
            self.suggestion_list.update()
            e.control.border_radius=ft.border_radius.all(10)
            e.control.update()

    def build(self):
        return ft.Column([self, self.suggestion_list], spacing=0)


class ButtonGradient():
    def __init__(self, content, colors, expand=True, on_click=None):
        self.on_click = on_click
        self.content = content
        self.colors = colors
        self.container = None
        self.expand = expand

    def on_hover(self, e):
        if e.data == "true":  # Mouse entrou no componente
            self.container.opacity = 0.8
        else:  # Mouse saiu do componente
            self.container.opacity = 1.0
        e.control.update()

    def build(self):
        self.container = ft.Container(
            content=self.content,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.top_right,
                colors=self.colors,
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.all(10),
            border_radius=ft.border_radius.all(10),
            on_hover=self.on_hover,
            on_click=self.on_click,
            expand=self.expand
        )
        return self.container
    
