import flet as ft
from flet import *

def main(page: ft.page):

    page.bgcolor='#0D0618'
    page.title="SemiCon-OIP  v.1.0"
    page.padding=0
    page.window_maximized=True
    page.window_center()
    page.update()

    ##Home Page<begin>
    ##<toolbar>
    c1=ft.Column(expand=0,controls=[
                ft.Container(width=1400,height=40, bgcolor='#0D0618', padding=padding.only(top=15,left=5),content=
                             ft.Row(expand=0, alignment=ft.MainAxisAlignment.START,controls=[
                                ft.Container(expand=0,padding= padding.only(left=15),content=ft.Text("File",size=11),on_click=lambda e: print("File")),
                                ft.Container(expand=0,padding= padding.only(left=15),content=ft.Text("Edit",size=11),on_click=lambda e: print("Edit")),
                                ft.Container(expand=0,padding= padding.only(left=15),content=ft.Text("View",size=11),on_click=lambda e: print("View")),
                                ft.Container(expand=0,padding= padding.only(left=15),content=ft.Text("Settings",size=11),on_click=lambda e: print("Settings")),
                                
                             ])),
    ])
    ##<main_region>
    r1=ft.Row(expand=1, controls=[
            ft.Container(expand=0,width=860,height=1100, padding= padding.only(top=50,left=50),bgcolor='#111122',content=
                    ft.Column(controls=[
                    ft.Text("Get Started,", color='#FFFFFF', size=35,font_family="Roboto", weight=ft.FontWeight.NORMAL, selectable=False),
                    ft.Text("Start with a new project or carry on with your previous.", color='#9B9B9B', size=17,font_family="Roboto", weight=ft.FontWeight.NORMAL, selectable=False),
                    ft.Column(expand=1, alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                        ft.Container(expand=0,width=640,height=85,image_src='C://Users//jacob//Documents//Python//Semicon-OIP//assets//img//Rec1.png',
                        image_fit=ImageFit.CONTAIN,on_click=lambda e: print("Upload")),
                        ft.Container(expand=0,width=640,height=85, image_src='C://Users//jacob//Documents//Python//Semicon-OIP//assets//img//Rec2.png',
                        image_fit=ImageFit.CONTAIN,on_click=lambda e: print("Record")),
         ])         
            ]
            )),
    ##Right Side Image
            ft.Container(expand=1,width=565,height=1100,image_src='C://Users//jacob//Documents//Python//Semicon-OIP//assets//img//home_image.png',
                        image_fit=ImageFit.COVER)
    ])
    page.add(c1,r1)
    ##Home Page<end>

ft.app(target=main)