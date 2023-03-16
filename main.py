## An application focusing on calculating the total deposition 
##        of dopants on a semiconductor material
## By uploading the microscopinc images and specifying the 
##        incubation cycle, the application calculates the necessary
##        parameter and the user is able to fuse the parameters to 
##        inbuilt fuctions.
## The next version development focuses on live feeding of from
##        microscopic video files in claculating the parameters.

import flet as ft
from flet import *
import time
from lib import *

class Main(UserControl):
    def __init__(self):
        pass
    def run(self):
        pass


class Functionalities(Main):
    def __init__(self):
        super().__init__()
        pass
    def build(self):
        pass

class Animation(Main):
    def __init__(self):
        pass
    def build(self):
        pass

class App():
    def __init__(self):
        super().__init__()


def main(page: ft.page):
    
    page.window_width=500
    page.window_height=350
    page.bgcolor='#050518'
    page.title="SemiCon-OIP  v.1.0"
    page.window_center()
    page.padding=0
    page.window_frameless=True
    page.update()


    app_name=ft.Text("Semicon - OIP", color='#FFFFFF', style=ft.TextThemeStyle.DISPLAY_SMALL, weight=ft.FontWeight.BOLD, selectable=False)
    app_desc=ft.Text("Semiconductor Deposition Estimation", color='#FFFFFF', style=ft.TextThemeStyle.BODY_MEDIUM, selectable=False )
    version_no=ft.Text("v.1.0", color='#FFFFFF', style=ft.TextThemeStyle.BODY_SMALL, selectable=False )

    #Splash Screen Design<begin>
    c1= ft.Column(expand=0, controls=[
            ft.Container(expand=0, width=500, height=350,
                image_src='C://Users//jacob//Documents//Python//Semicon-OIP//assets//img//image.png',
                image_fit=ImageFit.COVER,
                content=
                    ft.Column(controls=[
                        ft.Container(height=260, width=500,padding=padding.only(top=70,left=25),content=
                            ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER, controls=[app_name,app_desc]),),
                                    ft.Container(height=90, width=500,padding=padding.only(top=40,left=25),content=
                                            ft.Column(expand=True, alignment=ft.MainAxisAlignment.START, controls=[version_no]),)
                        ]))
    ])
    page.add(c1)
    #Splash Screen Design<end>

ft.app(target=main,assets_dir='assets')