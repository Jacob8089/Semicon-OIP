import flet as ft
from flet import *
import time


def main(splash_page: ft.page):

    def toHome(e):
        splash_page.window_destroy()
    
    splash_page.window_width=500
    splash_page.window_height=350
    splash_page.bgcolor='#050518'
    splash_page.title="SemiCon-OIP  v.1.0"
    splash_page.window_center()
    splash_page.padding=0
    splash_page.window_frameless=True
    splash_page.update()


    app_name=ft.Text("Semicon - OIP", color='#FFFFFF', style=ft.TextThemeStyle.DISPLAY_SMALL, weight=ft.FontWeight.BOLD, selectable=False)
    app_desc=ft.Text("Semiconductor Deposition Estimation", color='#FFFFFF', style=ft.TextThemeStyle.BODY_MEDIUM, selectable=False )
    version_no=ft.Text("v.1.0", color='#FFFFFF', style=ft.TextThemeStyle.BODY_SMALL, selectable=False )
    start_bt=ft.ElevatedButton("Get Started",color='#FFFFFF',bgcolor='#871868',icon=ft.icons.NAVIGATE_NEXT_ROUNDED,on_click=toHome)

    #Splash Screen Design<begin>
    c1= ft.Column(expand=0, controls=[
            ft.Container(expand=0, width=500, height=350,
                image_src='C://Users//jacob//Documents//Python//Semicon-OIP//assets//img//image.png',
                image_fit=ImageFit.COVER,
                content=
                    ft.Column(controls=[
                        ft.Container(height=260, width=500,padding=padding.only(top=70,left=25),content=
                            ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER, controls=[app_name,app_desc]),),
                                    ft.Container(height=90, width=500,padding=padding.only(left=25),content=
                                            ft.Column(expand=True, alignment=ft.MainAxisAlignment.START, controls=[start_bt]),)
                        ]))
    ])
    splash_page.add(c1)
    #Splash Screen Design<end>

ft.app(target=main,assets_dir='assets')