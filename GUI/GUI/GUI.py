"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    
class ExampleState(rx.State):
    # A base var for the list of colors to cycle through.
    colors: list[str] = [
        "black",
        "red",
        "green",
        "blue",
        "purple",
    ]

    # A base var for the index of the current color.
    index: int = 0

    def next_color(self):
        """An event handler to go to the next color."""
        # Event handlers can modify the base vars.
        # Here we reference the base vars `colors` and `index`.
        self.index = (self.index + 1) % len(self.colors)

    @rx.var
    def color(self) -> str:
        """A computed var that returns the current color."""
        # Computed vars update automatically when the state changes.
        return self.colors[self.index]


def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.grid(
            rx.foreach(
            rx.Var.range(25),
            lambda i: rx.button(height="18vh", width = "18vh" )
            ),
        
        columns="5",  
        spacing="1",
        width="50%",
    ),

        height="100vh",
        width = "185vh"
    )


app = rx.App()
app.add_page(index)
