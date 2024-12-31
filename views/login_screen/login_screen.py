from flet import *
import request

class LoginControl:
    def __init__(self):
        self.baseUrl = 'http://127.0.0.1:8000/'
    
    def sendData(data , method):
        pass

    def loginRequest(self , userName , password):
        pass

class Login(View):
    def __init__(self, route):
        super().__init__(route=route)  
        self.scroll = ScrollMode.AUTO
        self.controls.append( 
            ResponsiveRow(
                controls=[
                     Row(
                        controls=[
                            IconButton(
                                icon=icons.ARROW_BACK,
                                on_click=lambda x:self.page.go("/")
                            )
                        ],
                        expand=False,
                        alignment=MainAxisAlignment.START
                    ),
                     Column(
                        controls=[
                            ResponsiveRow(
                                controls=[
                                    Image(
                                        src="images/logo.png",
                                        fit=ImageFit.COVER,
                                        border_radius=border_radius.all(20.0),
                                         col={"xs":10 , "sm":10, "md":7 , "lg":5 , "xl":5},
                                        ),
                                ],
                                expand=False,
                                alignment=MainAxisAlignment.CENTER
                            ),
                            Text(
                                "وصلة",
                                size=30,
                                weight=FontWeight.BOLD,
                                font_family="ElMessiri"
                            ),
                            Container(height=10),
                            TextField(
                                label="اســـم المــستخدم", 
                                border_radius=border_radius.all(22),
                                border_color="#171335",
                                text_style=TextStyle(
                                            size=15,
                                            font_family="ElMessiri"
                                        ),
                                label_style=TextStyle(
                                            size=18,
                                            font_family="ElMessiri"
                                        ),
                                ),
                            Container(height=10),
                            TextField(
                                label="كــلمة المــرور", 
                                password=True, 
                                can_reveal_password=True,
                                border_radius=border_radius.all(22),
                                border_color="#171335",
                                text_style=TextStyle(
                                            size=15,
                                            font_family="ElMessiri"
                                        ),
                                label_style=TextStyle(
                                            size=18,
                                            font_family="ElMessiri"
                                        ),
                                ),
                            Container(height=20),
                            ResponsiveRow(
                                controls=[
                                    ElevatedButton(
                                        "تسجيل الدخول",
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(radius=22),
                                            bgcolor="#171335",
                                            color="#ffffff",
                                            text_style=TextStyle(
                                                size=15,
                                                weight=FontWeight.BOLD,
                                                font_family="ElMessiri"
                                            ),
                                            padding=5
                                        )
                                    ),
                                ]
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True
            )
        )
