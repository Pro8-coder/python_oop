"""
Необходимо создать программу для обучающего курса. Для этого объявляются
три класса:

Course - класс, отвечающий за управление курсом в целом;
Module - класс, описывающий один модуль (раздел) курса;
LessonItem - класс одного занятия (урока).

Структура курса на уровне этих классов, приведена на рисунке ниже:



Объекты класса LessonItem должны создаваться командой:

lesson = LessonItem(название урока, число практических занятий, общая
длительность урока)
Соответственно, в каждом объекте класса LessonItem должны создаваться
локальные атрибуты:

title - название урока (строка);
practices - число практических занятий (целое положительное число);
duration - общая длительность урока (целое положительное число).

Необходимо с помощью магических методов реализовать следующую логику
взаимодействия с объектами класса LessonItem:

1. Проверять тип присваиваемых данных локальным атрибутам. Если типы
не соответствуют требованиям, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
2. При обращении к несуществующим атрибутам объектов класса LessonItem
возвращать значение False.
3. Запретить удаление атрибутов title, practices и duration в объектах класса
LessonItem.

Объекты класса Module должны создаваться командой:

module = Module(название модуля)
Каждый объект класса Module должен содержать локальные атрибуты:

name - название модуля;
lessons - список из уроков (объектов класса LessonItem), входящих в модуль
(изначально список пуст).

Также в классе Module должны быть реализованы методы:

add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового
урока (объекта класса LessonItem);
remove_lesson(self, indx) - удаление урока по индексу в списке lessons.

Наконец, объекты класса Course создаются командой:

course = Course(название курса)
И содержат следующие локальные атрибуты:

name - название курса (строка);
modules - список модулей в курсе (изначально список пуст).

Также в классе Course должны присутствовать следующие методы:

add_module(self, module) - добавление нового модуля в конце списка modules;
remove_module(self, indx) - удаление модуля из списка modules по индексу в
этом списке.

Пример использования классов (в программе эти строчки не писать):

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
P.S. На экран ничего выводить не нужно.
"""


class LessonItem:
    """Класс для описания одного занятия (урока)."""

    def __init__(self, title: str, practices: int, duration: int) -> None:
        """
        Инициализация одного занятия (урока).

        :param title: Название урока.
        :param practices: Число практических занятий (целое положительное
        число).
        :param duration: Общая длительность урока (целое положительное число).
        """
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key: str, value: str | int) -> None:
        """
        Устанавливает значение атрибута с проверкой типа.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        :raises TypeError: Если тип значения не соответствует ожидаемому.
        """
        if key == "title" and isinstance(value, str):
            super().__setattr__(key, value)
        elif key in ("practices", "duration") and isinstance(
                value, int) and value >= 0:
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item: str) -> bool:
        """
        Возвращает False при обращении к несуществующим атрибутам.

        :param item: Имя атрибута.
        :return: Всегда возвращает False.
        """
        return False

    def __delattr__(self, item: str) -> None:
        """
        Запрещает удаление атрибутов title, practices и duration.

        :param item: Имя атрибута.
        :raises AttributeError: Если попытка удалить запрещённый атрибут.
        """
        if item in ("title", "practices", "duration"):
            raise AttributeError(f"Удаление атрибута {item} запрещено.")

        super().__delattr__(item)


class Module:
    """Класс для описания одного модуля (раздела) курса."""

    def __init__(self, name: str) -> None:
        """
        Инициализация модуля (раздела курса).

        :param name: Название модуля.
        """
        self.name = name
        self.lessons: list[LessonItem] = []

    def add_lesson(self, lesson: LessonItem) -> None:
        """
        Добавляет урок в модуль.

        :param lesson: Объект класса LessonItem.
        """
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        """
        Удаляет урок из модуля по индексу.

        :param indx: Индекс урока в списке.
        :raises IndexError: Если индекс некорректен.
        """
        if 0 <= indx < len(self.lessons):
            del self.lessons[indx]
        else:
            raise IndexError("Некорректный индекс урока.")


class Course:
    """Класс для управления курсом в целом."""

    def __init__(self, name: str) -> None:
        """
        Инициализация курса.

        :param name: Название курса.
        """
        self.name = name
        self.modules: list[Module] = []

    def add_module(self, module: Module) -> None:
        """
        Добавляет модуль в курс.

        :param module: Объект класса Module.
        """
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        """
        Удаляет модуль из курса по индексу.

        :param indx: Индекс модуля в списке.
        :raises IndexError: Если индекс некорректен.
        """
        if 0 <= indx < len(self.modules):
            del self.modules[indx]
        else:
            raise IndexError("Некорректный индекс курса.")

