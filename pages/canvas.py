import flet as ft
from flet import *
import time

def main(page: ft.page):
     
    page.bgcolor='#070011'
    page.title="SemiCon-OIP  v.1.0"
    page.padding=0
    page.window_maximized=True
    page.window_frameless=False
    page.window_min_width= 700
    page.window_center()
    page.update()

    ##Image Option<begin>
    ##<toolbar>
    page.appbar = ft.AppBar(
        center_title=False,
        bgcolor='#111122',
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="New/Open", on_click=lambda e: print("Record")),
                    ft.PopupMenuItem(text="Save/Save as", on_click=lambda e: print("Record")),
                    ft.PopupMenuItem(text="Export", on_click=lambda e: print("Record")),
                    ft.PopupMenuItem(text="Print", on_click=lambda e: print("Record")),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Exit now",on_click= lambda e: page.window_destroy()),
                ]
            ),
        ],
    )

    nav= ft.NavigationRail(
        expand=False,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.7,
        bgcolor='#1C1C33',
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.SWITCH_ACCESS_SHORTCUT, 
                selected_icon=ft.icons.SWITCH_ACCESS_SHORTCUT_ADD_OUTLINED, 
                label="Filter"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.APP_SHORTCUT_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.APP_SHORTCUT_ROUNDED),
                label="Adjust",
                padding=5,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOK_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.BOOK),
                label="Docs")
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    path='C:\\Users\\jacob\\Documents\\Python\\Semicon-OIP\\assets\\img\\sample.png'
    w=512 
    h=653

    t=t = ft.Tabs(
        selected_index=0,
        animation_duration=500,
        tabs=[
            
            ft.Tab(
                text="Files",
                content=
                ft.Container(
                    padding=padding.only(top=20,left=15),
                    content=ft.Column(expand=0, controls=[
                            ft.Text("The uploaded files are,"),
                            ft.Divider(height=0.25, color="#8E8E8E"),
                            ft.ListView(expand=1, padding=padding.only(left=5,right=5,top=10),first_item_prototype=True,
                                        divider_thickness=0.5,spacing=10, auto_scroll=True,controls=[
                                    ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.icons.ALBUM),ft.Text("Sample_5%_incubation.png")])
                                        ,)
                            ])
        
                    ])
                ),
            ),
            ft.Tab(
                text="Process",
                content=ft.Container(
                    padding=padding.only(top=20,left=15),
                    content=ft.Column(expand=0, visible=True,controls=[
                            ft.Text("The image processing techniques in order to calculate the total surface coverage area of the dopants present over the semiconducter wafer material undergoing incubation."),
                            ft.Divider(height=0.25, color="#8E8E8E"),
                            ft.Text("Threashold"),
                            ft.Slider(min=0, max=3, divisions=10),
                            ft.Text("Median Filter"),
                            ft.Slider(min=0, max=100,),
                            ft.Text("Default Slider:"),
                            ft.Slider(min=0, max=100,),
                            ft.Switch(label="Optimization Plot",)
                    ])
                ),
            ),
            ft.Tab(
                text="Maths",
                content=
                ft.Container(
                    padding=padding.only(top=20,left=15,right=15),
                    content=ft.Column(controls=[ft.Text("Here you can mathematically analyze on your methodolgy you chose for the optimization."),
                                                ft.Divider(height=0.25, color="#8E8E8E"),
                                                ft.TextField(label="Functional Analysis", autofocus=True,value="import lib",
                                                             color='#FFDE88',border_color='Blue',multiline=True,max_length=500),
                                                ft.FilledButton("Save method", icon=icons.DOWNLOADING)
                    ])
                ),
            ),
            ft.Tab(
                text="Analysis",
                content=
                ft.Container(
                    padding=padding.only(top=20,bottom=15,left=15),
                    content=ft.Column(controls=[ft.Text("Select or add methods you can choose to optimize on the result that obtained from the processing part."),
                                                ft.FilledButton("Add method", icon="add"), 
                                                ft.Divider(height=0.25, color="#8E8E8E"),
                              ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Avrami Equation",size=15),
                            subtitle=ft.Text("To determine the crystallization kinetics of polymers, where the Avrami exponent (na) provides information for the nucleation and growth mechanisms.",
                                             size=10,text_align= ft.TextAlign.JUSTIFY),
                            trailing=ft.PopupMenuButton(
                                icon=ft.icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(text="Activate"),
                                ],
                            ),
                        ),
                        # ft.ListTile(
                        #     leading=ft.Icon(ft.icons.ALBUM),
                        #     title=ft.Text(" "),
                        #     trailing=ft.PopupMenuButton(
                        #         icon=ft.icons.MORE_VERT,
                        #         items=[
                        #             ft.PopupMenuItem(text="Item 1"),
                        #             ft.PopupMenuItem(text="Item 2"),
                        #         ],
                        #     ),
                        # ),
                        # ft.ListTile(
                        #     leading=ft.Icon(ft.icons.ALBUM),
                        #     title=ft.Text(" "),
                        #     trailing=ft.PopupMenuButton(
                        #         icon=ft.icons.MORE_VERT,
                        #         items=[
                        #             ft.PopupMenuItem(text="Item 1"),
                        #             ft.PopupMenuItem(text="Item 2"),
                        #         ],
                        #     ),
                        # ),                     
                        ])         
                ),
            ),
        ],
        expand=1,
    )
       

    r2=ft.Row(expand=True, controls=[
        nav,
        ft.Container(expand=0, height=1200,width=900,content=
                     ft.Row(expand=0,alignment=ft.MainAxisAlignment.CENTER,auto_scroll=True,controls=[
                        ft.Container(margin=margin.only(top=50,bottom=50),expand=0,border=border.all(1, 'Blue'),
                                     width=640, height=850,image_src=path, image_fit=ImageFit.CONTAIN,alignment=ft.alignment.center,
                                     content=ft.Text("No file loaded.")),
                     ])),
        ft.Container(expand=1, padding=padding.only(top=10),width=290, bgcolor='#1C1C33', content=t)
    ])
    page.add(r2)

    ##Image Option<end>

ft.app(target=main)