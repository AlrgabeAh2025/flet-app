from flet import *


class HomeControl:
    def __init__():
        pass


class Home(View):
    def __init__(self, route):
        super().__init__(route=route)
        self.scroll = ScrollMode.HIDDEN

        self.drawer = NavigationDrawer(
            on_dismiss=self.handle_dismissal,
            on_change=self.handle_change,
            controls=[
                Container(height=12),
                NavigationDrawerDestination(
                    label="الرئيسية",
                    icon_content=Icon(icons.HOME_OUTLINED),
                    selected_icon_content=Icon(icons.HOME),
                ),
                Divider(thickness=2),
                NavigationDrawerDestination(
                    label="الاجهزة المرتبطة",
                    icon_content=Icon(icons.PHONE_ANDROID_OUTLINED),
                    selected_icon_content=Icon(icons.PHONE_ANDROID),
                ),
                NavigationDrawerDestination(
                    label="تسجيل الخروج",
                    icon_content=Icon(icons.LOGOUT_OUTLINED),
                    selected_icon_content=Icon(icons.LOGOUT),
                ),
            ],
        )

        self.appbar = AppBar(
            actions=[
                IconButton(
                    icon=icons.PERSON,
                    icon_color="#ffffff",
                    on_click=lambda x: self.page.go("/Profile"),
                ),
                IconButton(
                    icon=icons.NOTIFICATIONS,
                    icon_color="#ffffff",
                    on_click=lambda x: self.page.go("/notifications"),
                ),
            ],
            leading=IconButton(
                icon=icons.MENU,
                icon_color="#ffffff",
                on_click=lambda e: self.page.open(self.drawer),
            ),
            toolbar_height=100,
            title=Text(
                "وصلة",
                size=30,
                weight=FontWeight.BOLD,
                color="#ffffff",
                font_family="ElMessiri",
            ),
        )

        self.hasChildScreen = ResponsiveRow(
            controls=[
                Dropdown(
                    label="اختر احد الابناء لعرض بياناته",
                    width=100,
                    options=[
                        dropdown.Option(
                            "الطفل 1",
                        ),
                        dropdown.Option(
                            "الطفل 2",
                        ),
                        dropdown.Option(
                            "الطفل 3",
                        ),
                    ],
                    label_style=TextStyle(
                        size=13,
                        weight=FontWeight.NORMAL,
                        font_family="ElMessiri",
                    ),
                ),
                Container(height=10),
                Column(
                    controls=[
                        Container(
                            content=Image(src="/images/BChild.png", width=150),
                            border_radius=border_radius.all(150),
                        ),
                        Container(
                            content=Text(
                                "اسم الطفل",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="#666666",
                                font_family="ElMessiri",
                            ),
                        ),
                        Container(
                            content=Text(
                                "اخر موعد اتصال",
                                size=8,
                                weight=FontWeight.NORMAL,
                                color="#666666",
                                font_family="ElMessiri",
                            ),
                        ),
                        Container(height=20),
                        ResponsiveRow(
                            controls=[
                                Text(
                                    "قائمة الاختصارات",
                                    style=TextStyle(
                                        size=12,
                                        weight=FontWeight.BOLD,
                                        font_family="ElMessiri",
                                    ),
                                    color="#666666",
                                    text_align=TextAlign.START,
                                ),
                            ],
                        ),
                        ResponsiveRow(
                            controls=[
                                Container(
                                    content=Column(
                                        controls=[
                                            Icon(
                                                icons.WIDGETS,
                                                size=50,
                                                color="#110b22",
                                            ),
                                            Text(
                                                "استخدام التطبيقات",
                                                style=TextStyle(
                                                    size=11,
                                                    weight=FontWeight.BOLD,
                                                    font_family="ElMessiri",
                                                    color="#666666",
                                                ),
                                            ),
                                        ],
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        alignment=MainAxisAlignment.SPACE_AROUND,
                                    ),
                                    padding=10,
                                    alignment=alignment.center,
                                    height=120,
                                    border_radius=10,
                                    col={"xs": 6, "sm": 10, "md": 5, "xl": 5},
                                    border=border.all(width=1, color="#110b22"),
                                    on_click=lambda x: self.page.go(
                                        "/MostUsedApplications"
                                    ),
                                ),
                                Container(
                                    content=Column(
                                        controls=[
                                            Icon(
                                                icons.SECURITY,
                                                size=50,
                                                color="#110b22",
                                            ),
                                            Text(
                                                "التنبيهات",
                                                style=TextStyle(
                                                    size=11,
                                                    weight=FontWeight.BOLD,
                                                    font_family="ElMessiri",
                                                    color="#666666",
                                                ),
                                            ),
                                        ],
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        alignment=MainAxisAlignment.SPACE_AROUND,
                                    ),
                                    padding=10,
                                    alignment=alignment.center,
                                    height=120,
                                    border_radius=10,
                                    col={"xs": 6, "sm": 10, "md": 5, "xl": 5},
                                    border=border.all(width=1, color="#110b22"),
                                    on_click=lambda x: self.page.go("/notifications"),
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                            col={"sm": 2, "md": 4, "xl": 2},
                        ),
                        ResponsiveRow(
                            controls=[
                                Text(
                                    "التطبيقات الاكثر استخدام",
                                    style=TextStyle(
                                        size=12,
                                        weight=FontWeight.BOLD,
                                        font_family="ElMessiri",
                                    ),
                                    color="#666666",
                                    text_align=TextAlign.START,
                                ),
                            ],
                        ),
                        Container(
                            content=ResponsiveRow(
                                controls=[
                                    ListTile(
                                        title=Text(
                                            "1h:35m",
                                            style=TextStyle(
                                                size=10,
                                                weight=FontWeight.BOLD,
                                                font_family="ElMessiri",
                                            ),
                                        ),
                                        leading=Text(
                                            "Facebook",
                                            style=TextStyle(
                                                size=15,
                                                weight=FontWeight.BOLD,
                                                font_family="ElMessiri",
                                            ),
                                        ),
                                        trailing=Icon(icons.FACEBOOK),
                                        subtitle=ProgressBar(value=0.8),
                                    ),
                                ],
                            ),
                            bgcolor="#ffffff",
                            border=border.all(0.5, "#110b22"),
                            border_radius=border_radius.all(5),
                            alignment=alignment.center,
                        ),
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            expand=True,
        )

        self.hasNoChild = ResponsiveRow(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                ListTile(
                                    leading=Icon(icons.INFO),
                                    title=Text(
                                        "انت لم تضف جهاز بعد الرجاء اضافة جهاز اولا",
                                        size=13,
                                        weight=FontWeight.NORMAL,
                                        color="#666666",
                                        font_family="ElMessiri",
                                    ),
                                ),
                                Container(
                                    content=Text(
                                        "اولا اضغط على الزر بالاسفل لمسح رمز (QR) على جهاز طفلك ثم يمكنك الحصول على اشعارات فورية بخصوص المحتوى الذي يتابعه طفلك والعديد من المعلومات الاخرى",
                                        size=13,
                                        weight=FontWeight.NORMAL,
                                        color="#666666",
                                        font_family="ElMessiri",
                                    ),
                                    padding=20,
                                ),
                            ]
                        ),
                        bgcolor="#ffffff",
                        border=border.all(color="#110b22", width=1),
                        border_radius=border_radius.all(10),
                    ),
                    Container(height=30),
                    Container(
                        content=Text(
                            "اضغط لاضافة جهاز",
                            size=13,
                            weight=FontWeight.NORMAL,
                            color="#666666",
                            font_family="ElMessiri",
                        ),
                    ),
                    Container(
                        content=Column(
                            controls=[
                                IconButton(icon=icons.QR_CODE, icon_size=120),
                                Container(
                                    content=Text(
                                        "امسح رمز (QR) على جهاز طفلك",
                                        size=14,
                                        weight=FontWeight.NORMAL,
                                        color="#666666",
                                        font_family="ElMessiri",
                                    ),
                                ),
                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        bgcolor="#ffffff",
                        border=border.all(color="#110b22", width=1),
                        border_radius=border_radius.all(10),
                        padding=padding.symmetric(vertical=20),
                    ),
                ],
                expand=True,
            )

        self.controls.append(
            self.hasChildScreen
        )

    def handle_dismissal(self, e):
        self.page.add(Text("Drawer dismissed"))

    def handle_change(self, e):
        routs = {
            "0": "/home",
            "1": "/devices",
            "2": "/home",
        }
        self.page.go(routs[e.data])
        self.page.close(self.drawer)
