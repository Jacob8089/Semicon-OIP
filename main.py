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
from time import *
import datetime
# import lib

class App(ft.UserControl):
  

    def build(self):
        # self.page.window_frameless=wf
        self.app_name=ft.Text("Semicon - OIP", color='#FFFFFF', style=ft.TextThemeStyle.DISPLAY_SMALL, weight=ft.FontWeight.BOLD, selectable=False)
        self.app_desc=ft.Text("Semiconductor Deposition Estimation", color='#FFFFFF', style=ft.TextThemeStyle.BODY_MEDIUM, selectable=False )
        self.version_no=ft.Text("v.1.0", color='#FFFFFF', style=ft.TextThemeStyle.BODY_SMALL, selectable=False )
        self.start_bt=ft.ElevatedButton("Get Started",color='#FFFFFF',bgcolor='#871868',icon=ft.icons.NAVIGATE_NEXT_ROUNDED,on_click=self.tohome)
        # self.loader=ft.ProgressRing(width=16, height=16, stroke_width = 2)
        self.login_column= ft.Column(expand=True, alignment=ft.MainAxisAlignment.START, controls=[self.start_bt])
        self.splash_design=ft.Column(expand=0, controls=[
            ft.Container(expand=0, width=500, height=350,
                image_src='C://Users//jacob//Documents//Python//Semicon-OIP//assets//img//image.png',
                image_fit=ImageFit.COVER,
                content=
                    ft.Column(controls=[
                        ft.Container(height=260, width=500,padding=padding.only(top=70,left=25),content=
                            ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER, controls=[self.app_name,self.app_desc,self.version_no]),),
                                    ft.Container(height=90, width=500,padding=padding.only(left=25),content=
                                            self.login_column)
                        ]))
    ])
        return self.splash_design
    
    def tohome(self,e):
        self.version_no.value="Loading..."
        sleep(3)
        self.curr = datetime.datetime.now()
        self.page.window_visible=False
        print(f"Navigating to home at {self.curr}")
        self.page.update()
        sleep(3)

class homeScreen(ft.UserControl):
    def __init__(self):
        super().__init__()


def main(page=ft.Page):
    page.bgcolor='#050518'
    page.title="SemiCon-OIP  v.1.0"
    page.window_center()
    page.window_width=500
    page.window_height=350
    page.window_frameless=True
    page.padding=0

    Semicon_start=App(page)
    page.add(Semicon_start)
    page.update()

ft.app(target=main,assets_dir='assets')