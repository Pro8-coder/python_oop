"""
Вам необходимо написать программу описания музеев. Для этого нужно объявить
класс Museum, объекты которого формируются командой:

mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:

name - название музея (строка);
exhibits - список экспонатов (изначально пустой список).

Сам класс Museum должен иметь методы:

add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка
exhibits);
remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по
ссылке obj - на экспонат)
get_info_exhibit(self, indx) - получение информации об экспонате (строка) по
индексу списка (нумерация с нуля).

Экспонаты представляются объектами своих классов. Для примера объявите в
программе следующие классы экспонатов:

Picture - для картин;
Mummies - для мумий;
Papyri - для папирусов.

Объекты этих классов должны создаваться следующим образом (с соответствующим
набором локальных атрибутов):

p = Picture(название, художник, описание)            # локальные атрибуты:
name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты:
name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты:
name - название папируса; date - датировка (строка); descr - описание
Метод get_info_exhibit() класса Museum должен возвращать значение атрибута
descr указанного экспоната в формате:

"Описание экспоната {name}: {descr}"

Например:

"Описание экспоната Девятый вал: Айвазовский написал супер картину."

Пример использования классов (в программе эти строчки писать не нужно - только
для примера):

mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному
султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая
картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века,
удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее
найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
P.S. На экран ничего выводить не нужно.
"""


class Picture:
    """Класс для описания картины как экспоната музея."""

    def __init__(self, name: str, author: str, descr: str) -> None:
        """
        Инициализация экспоната Picture.

        :param name: Название картины.
        :param author: Художник.
        :param descr: Описание картины.
        """
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    """Класс для описания мумии как экспоната музея."""

    def __init__(self, name: str, location: str, descr: str) -> None:
        """
        Инициализация экспоната Mummies.

        :param name: Имя мумии.
        :param location: Место находки.
        :param descr: Описание мумии.
        """
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    """Класс для описания папируса как экспоната музея."""

    def __init__(self, name: str, date: str, descr: str) -> None:
        """
        Инициализация экспоната Papyri.

        :param name: Название папируса.
        :param date: Датировка папируса.
        :param descr: Описание папируса.
        """
        self.name = name
        self.date = date
        self.descr = descr


class Museum:
    """Класс для описания музея и управления его экспонатами."""

    def __init__(self, name: str) -> None:
        """
        Инициализация Museum.

        :param name: Название музея.
        """
        self.name = name
        self.exhibits: list[Picture | Mummies | Papyri] = []

    def add_exhibit(self, obj: Picture | Mummies | Papyri) -> None:
        """
        Добавляет новый экспонат в музей.

        :param obj: Объект экспоната (Picture, Mummies или Papyri).
        """
        self.exhibits.append(obj)

    def remove_exhibit(self, obj: Picture | Mummies | Papyri) -> None:
        """
        Удаляет экспонат из музея.

        :param obj: Объект экспоната (Picture, Mummies или Papyri).
        """
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx: int) -> str:
        """
        Возвращает описание экспоната по индексу.

        :param indx: Индекс экспоната в списке.
        :return: Строка с описанием экспоната.
        :raises IndexError: Если индекс некорректен.
        """
        if 0 <= indx < len(self.exhibits):
            return f"Описание экспоната {self.exhibits[indx].name}: " \
                   f"{self.exhibits[indx].descr}"
        else:
            raise IndexError("Некорректный индекс экспоната.")

