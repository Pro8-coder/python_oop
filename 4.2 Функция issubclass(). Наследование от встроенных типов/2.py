"""
Разрабатывается интернет-магазин. Каждый товар предполагается представлять
классом Thing, объекты которого создаются командой:

thing = Thing(name, price, weight)
где name - наименование товара (строка); price - цена (вещественное число);
weight - вес товара (вещественное число). В каждом объекте этого класса
создаются аналогичные атрибуты: name, price, weight.

Класс Thing необходимо определить так, чтобы его объекты можно было
использовать в качестве ключей словаря, например:

d = {}
d[thing] = thing
И для каждого уникального набора данных name, price, weight должны
формироваться свои уникальные ключи.

Затем, вам необходимо объявить класс словаря DictShop, унаследованный от
базового класса dict. В этом новом словаре ключами могут выступать только
объекты класса Thing. При попытке указать любой другой тип, генерировать
исключение командой:

raise TypeError('ключами могут быть только объекты класса Thing')
Объекты класса DictShop должны создаваться командами:

dict_things = DictShop() # пустой словарь
dict_things = DictShop(things) # словарь с набором словаря things
где things - некоторый словарь. В инициализаторе следует проверять, чтобы
аргумент thing был словарем, если не так, то выбрасывать исключение:

raise TypeError('аргумент должен быть словарем')
И проверять, чтобы все ключи являлись объектами класса Thing. Если это не так,
то генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Дополнительно в классе DictShop переопределить метод:

__setitem__()

с проверкой, что создаваемый ключ является объектом класса Thing. Иначе,
генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Пример использования классов (эти строчки в программе не писать):

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

dict_things[1] = th_1 # исключение TypeError
P.S. В программе нужно объявить только классы. На экран выводить ничего
не нужно.
"""
from typing import Any


class Thing:
    """
    Класс для представления товара, который может быть ключом словаря.

    :ivar name: Наименование товара
    :ivar price: Цена товара
    :ivar weight: Вес товара
    """

    def __init__(self, name: str, price: float, weight: float) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self) -> int:
        """
        Возвращает хеш-значение объекта на основе его атрибутов.

        :return: Хеш-значение
        """
        return hash((self.name, self.price, self.weight))

    def __eq__(self, other: 'Thing') -> bool:
        """
        Сравнивает объекты по атрибутам name, price и weight.

        :param other: Другой объект Thing для сравнения
        :return: Результат сравнения
        """
        if isinstance(other, Thing):
            return (self.name, self.price, self.weight) == (
                other.name, other.price, other.weight)


class DictShop(dict):
    """
    Словарь, где ключами могут быть только объекты класса Thing.

    Наследуется от встроенного класса dict.
    """

    def __init__(self, things: dict[Thing, Any] | None = None) -> None:
        """
        Инициализирует словарь с проверкой типа ключей.

        :param things: Исходный словарь (ключи должны быть Thing)
        :raises TypeError: Если аргумент не словарь или ключи не Thing
        """
        if things is not None:
            if type(things) != dict:
                raise TypeError('аргумент должен быть словарем')
            if any(type(key) != Thing for key in things):
                raise TypeError(
                    'ключами могут быть только объекты класса Thing')

        super().__init__(things or {})

    def __setitem__(self, key: Thing, value: Any) -> None:
        """
        Устанавливает значение по ключу с проверкой типа ключа.

        :param key: Ключ (должен быть объектом Thing)
        :param value: Значение для сохранения
        :raises TypeError: Если ключ не является объектом Thing
        """
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')

        super().__setitem__(key, value)

