"""
Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес предметов, который можно положить
в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)
где name - название предмета (строка); weight - вес предмета (вещественное или
целочисленное значение). В объектах класса Thing должны автоматически
формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра
max_weight. Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')
Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке
добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
Если индекс в этих командах указывается неверно, то должно генерироваться
исключение:

raise IndexError('неверный индекс')
Пример использования классов (эти строчки в программе не писать):

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.
"""
from typing import TypeVar

T = TypeVar('T', int, float)


class Thing:
    """
    Класс, представляющий предмет с именем и весом.

    :ivar name: Название предмета.
    :ivar weight: Вес предмета (целое или вещественное число).
    """

    def __init__(self, name: str, weight: T) -> None:
        self.name = name
        self.weight = weight


class Bag:
    """
    Класс, представляющий сумку с ограничением по весу.

    :ivar max_weight: Максимальный допустимый вес предметов в сумке.
    :ivar weight: Текущий суммарный вес предметов в сумке.
    :ivar items: Список предметов, находящихся в сумке.
    """

    def __init__(self, max_weight: T) -> None:
        self.max_weight = max_weight
        self.weight = 0.0
        self.items: list[Thing] = []

    def _check_index(self, index: int) -> None:
        """
        Проверяет, что индекс находится в допустимых границах.

        :raise IndexError: Если индекс неверный.
        """
        if not -len(self.items) <= index < len(self.items):
            raise IndexError('неверный индекс')

    def _check_weight(self, weight: T) -> None:
        """
        Проверяет, что добавление нового предмета не превысит максимальный
        вес сумки.

        :param weight: Вес предмета, который планируется добавить или заменить.
        :raises ValueError: Если превышен максимальный вес.
        """
        if self.weight + weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing: Thing) -> None:
        """
        Добавляет предмет в сумку, если не превышен максимальный вес.

        :param thing: Объект класса Thing для добавления.
        :raises ValueError: Если превышен максимальный вес.
        """
        self._check_weight(thing.weight)
        self.items.append(thing)
        self.weight += thing.weight

    def __getitem__(self, item: int) -> Thing:
        """
        Возвращает предмет по индексу.

        :param index: Индекс предмета.
        :raises IndexError: Если индекс неверный.
        """
        self._check_index(item)
        return self.items[item]

    def __setitem__(self, key: int, value: Thing) -> None:
        """
        Заменяет предмет по индексу на новый.

        :param index: Индекс заменяемого предмета.
        :param thing: Новый предмет.
        :raises IndexError: Если индекс неверный.
        :raises TypeError: Если передан объект не класса Thing.
        :raises ValueError: Если превышен максимальный вес.
        """
        self._check_index(key)
        if type(value) != Thing:
            raise TypeError("объект должен быть класса Thing")

        self._check_weight(value.weight - self.items[key].weight)
        self.weight += value.weight - self.items[key].weight
        self.items[key] = value

    def __delitem__(self, key: int) -> None:
        """
        Удаляет предмет по индексу.

        :param index: Индекс удаляемого предмета.
        :raises IndexError: Если индекс неверный.
        """
        self._check_index(key)
        self.weight -= self.items[key].weight
        del self.items[key]

