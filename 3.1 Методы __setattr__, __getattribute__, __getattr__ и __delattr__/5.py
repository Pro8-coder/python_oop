"""
Объявите класс SmartPhone, объекты которого предполагается создавать командой:

sm = SmartPhone(марка смартфона)
Каждый объект должен содержать локальные атрибуты:

model - марка смартфона (строка);
apps - список из установленных приложений (изначально пустой).

Также в классе SmartPhone должны быть объявлены следующие методы:

add_app(self, app) - добавление нового приложения на смартфон (в конец списка
apps);
remove_app(self, app) - удаление приложения по ссылке на объект app.

При добавлении нового приложения проверять, что оно отсутствует в списке apps
(отсутствует объект соответствующего класса).

Каждое приложение должно определяться своим классом. Для примера объявите
следующие классы:

AppVK - класс приложения ВКонтаке;
AppYouTube - класс приложения YouTube;
AppPhone - класс приложения телефона.

Объекты этих классов должны создаваться следующим образом (с соответствующим
набором локальных атрибутов):

app_1 = AppVK() # name = "ВКонтакте"
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365,
"Работа": 112}) # name = "Phone", phone_list = словарь с контактами
Пример использования классов (в программе эти строчки не писать):

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
P.S. На экран ничего выводить не нужно.
"""


class AppVK:
    """
    Класс для представления приложения ВКонтакте.

    :ivar name: Название приложения (по умолчанию "ВКонтакте").
    """

    def __init__(self) -> None:
        self.name: str = "ВКонтакте"


class AppYouTube:
    """
    Класс для представления приложения YouTube.

    :ivar name: Название приложения (по умолчанию "YouTube").
    :ivar memory_max: Максимальный объем памяти, занимаемый приложением.
    """

    def __init__(self, memory_max: int) -> None:
        self.name: str = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    """
    Класс для представления приложения телефона.

    :ivar name: Название приложения (по умолчанию "Phone").
    :ivar phone_list: Словарь с контактами.
    """

    def __init__(self, phone_list: dict) -> None:
        self.name: str = "Phone"
        self.phone_list = phone_list


class SmartPhone:
    """
    Класс для представления смартфона.

    :ivar model: Модель смартфона.
    :ivar apps: Список установленных приложений.
    """

    def __init__(self, model: str) -> None:
        self.model = model
        self.apps: list[AppVK | AppYouTube | AppPhone] = []

    def add_app(self, app: AppVK | AppYouTube | AppPhone) -> None:
        """
        Добавляет новое приложение на смартфон.

        :param app: Объект приложения (AppVK, AppYouTube или AppPhone).
        """
        if not any(isinstance(i, type(app)) for i in self.apps):
            self.apps.append(app)

    def remove_app(self, app: AppVK | AppYouTube | AppPhone) -> None:
        """
        Удаляет приложение с смартфона.

        :param app: Объект приложения (AppVK, AppYouTube или AppPhone).
        """
        if app in self.apps:
            self.apps.remove(app)

