"""
Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
В этом классе должны быть реализованы следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает
локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в
программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным
именем. Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не
заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.
"""


class Application:
    """Класс, представляющий приложение в магазине AppStore."""

    def __init__(self, name: str, blocked: bool = False) -> None:
        self.name = name
        self.blocked = blocked


class AppStore:
    """
    Класс, представляющий интернет-магазин приложений для устройств под iOS.
    """

    def __init__(self) -> None:
        """Инициализирует магазин с пустым списком приложений."""
        self.app_lst: list[Application] = []

    def add_application(self, app: Application) -> None:
        """Добавляет приложение в магазин, если его еще нет в списке."""
        if app not in self.app_lst:
            self.app_lst.append(app)

    def remove_application(self, app: Application) -> None:
        """Удаляет приложение из магазина, если оно есть в списке."""
        if app in self.app_lst:
            self.app_lst.remove(app)

    def block_application(self, app: Application) -> None:
        """
        Переключает состояние блокировки приложения, если оно есть в магазине.
        """
        if app in self.app_lst:
            app.blocked = not app.blocked

    def total_apps(self) -> int:
        """Возвращает общее количество приложений в магазине."""
        return len(self.app_lst)

