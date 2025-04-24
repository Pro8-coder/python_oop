"""
Объявите в программе класс с именем Box (ящик), объекты которого должны
создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing)
в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого
класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или
вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета
регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта
класса Thing одного ящика и можно найти ровно один равный объект из второго
ящика).

Пример использования классов:

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
P.S. В программе только объявить классы, выводить на экран ничего не нужно.
"""
from collections import Counter


class Thing:
    """
    Класс для представления предмета.

    :ivar name: Название предмета.
    :ivar mass: Масса предмета (целое или вещественное число).
    """

    def __init__(self, name: str, mass: int | float) -> None:
        self.name = name
        self.mass = mass

    def __eq__(self, other: 'Thing') -> bool:
        """
        Сравнивает два предмета.

        :param other: Другой предмет.
        :return: True, если предметы равны, иначе False.
        """
        return (self.name.lower() == other.name.lower() and
                self.mass == other.mass)

    def __hash__(self) -> int:
        """
        Возвращает хэш объекта.

        :return: Хэш объекта.
        """
        return hash((self.name.lower(), self.mass))


class Box:
    """
    Класс для представления ящика с предметами.

    :ivar lst: Список предметов в ящике.
    """

    def __init__(self) -> None:
        self.lst: list[Thing] = []

    def add_thing(self, obj: Thing) -> None:
        """
        Добавляет предмет в ящик.

        :param obj: Предмет для добавления.
        """
        if isinstance(obj, Thing):
            self.lst.append(obj)

    def get_things(self) -> list['Thing']:
        """
        Возвращает список предметов в ящике.

        :return: Список предметов.
        """
        return self.lst

    def __eq__(self, other: 'Box') -> bool:
        """
        Сравнивает два ящика.

        :param other: Другой ящик.
        :return: True, если ящики равны, иначе False.
        """
        if isinstance(other, Box):
            return Counter(self.lst) == Counter(other.lst)

