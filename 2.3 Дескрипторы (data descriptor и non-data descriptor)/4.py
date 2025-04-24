"""
Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться
командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак
(целое число).

В каждом объекте этого класса должен создаваться локальный приватный атрибут:

__things - список вещей в рюкзаке (изначально список пуст).

Сам же класс Bag должен иметь объект-свойство:

things - для доступа к локальному приватному атрибуту __things (только для
считывания, не записи).

Также в классе Bag должны быть реализованы следующие методы:

add_thing(self, thing) - добавление нового предмета в рюкзак (добавление
возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление
не происходит);
remove_thing(self, indx) - удаление предмета по индексу списка __things;
get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса Thing и создается командой:

t = Thing(название, вес)
где название - наименование предмета (строка); вес - вес предмета (целое или
вещественное число).

В каждом объекте класса Thing должны формироваться локальные атрибуты:

name - наименование предмета;
weight - вес предмета.

Пример использования классов (эти строчки в программе писать не нужно):

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран
в программе выводить ничего не нужно.
"""


class Thing:
    """Класс для описания предмета."""

    def __init__(self, name: str, weight: int | float) -> None:
        """
        Инициализация объекта Thing (предмета).

        :param name: Наименование предмета.
        :param weight: Вес предмета.
        """

        self.name = name
        self.weight = weight


class Bag:
    """Класс для описания рюкзака."""

    def __init__(self, max_weight: int) -> None:
        """
        Инициализация объекта Bag (описания рюкзака).

        :param max_weight: Максимальный суммарный вес рюкзака.
        """

        self.max_weight = max_weight
        self.__things: list[Thing] = []

    @property
    def things(self) -> list[Thing]:
        """
        Возвращает список вещей в рюкзаке.

        :return: Список объектов класса Thing.
        """
        return self.__things

    def add_thing(self, thing: Thing) -> None:
        """
        Добавляет новый предмет в рюкзак.

        :param thing: Объект класса Thing.
        """
        if isinstance(thing, Thing) and \
                self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx: int) -> None:
        """
        Удаляет предмет по индексу.

        :param indx: Индекс предмета в списке.
        """
        if 0 <= indx < len(self.__things):
            del self.__things[indx]

    def get_total_weight(self) -> int | float:
        """
        Возвращает суммарный вес предметов в рюкзаке.

        :return: Суммарный вес.
        """
        return sum(thing.weight for thing in self.__things)

