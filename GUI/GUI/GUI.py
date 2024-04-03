"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.grid(
            rx.foreach(
            rx.Var.range(16),
            lambda i: rx.button(f"{i + 1}", height="8.5vh", color_scheme="gray", on_click=)
            ),
        columns="4",  
        spacing="1",
        width="60%",
    ),

        height="100vh",
    )


app = rx.App()
app.add_page(index)
