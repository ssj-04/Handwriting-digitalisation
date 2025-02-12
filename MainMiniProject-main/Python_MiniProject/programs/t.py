import flet as ft

def main(page: ft.Page):
    page.window.width = 400  # Set the window width (e.g., 400 pixels)
    page.window.height = 300  # Set the window height (e.g., 300 pixels)
    page.window.resizable = True # Make the window non-resizable

    # Add your canvas and other controls here...

ft.app(target=main)

# Replace the dimensions as needed
