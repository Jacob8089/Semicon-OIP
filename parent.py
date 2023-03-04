import flet as ft

def main(page: ft.page):
    page.window_width=500
    page.window_height=350
    page.window_center()
    page.update()

ft.app(target=main)

