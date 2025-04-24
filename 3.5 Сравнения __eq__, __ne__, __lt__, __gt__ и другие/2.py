"""
Объявите класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 10000
Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
Значения a, b, c должны сохраняться в локальных приватных атрибутах
__a, __b, __c объектах этого класса.

Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть
объявлены объекты-свойства (property) с именами: a, b, c. Причем, в момент
присваивания нового значения должна выполняться проверка попадания числа в
диапазон [MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, то оно
игнорируется и существующее значение не меняется.

С объектами класса Dimensions должны выполняться следующие операторы сравнения:

dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
dim1 > dim2    # True, если объем dim1 больше объема dim2
dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
dim1 < dim2    # True, если объем dim1 меньше объема dim2
Объявите в программе еще один класс с именем ShopItem (товар), объекты
которого создаются командой:

item = ShopItem(name, price, dim)
где name - название товара (строка); price - цена товара (целое или
вещественное число); dim - габариты товара (объект класса Dimensions).

В каждом объекте класса ShopItem должны создаваться локальные атрибуты:

name - название товара;
price - цена товара;
dim - габариты товара (объект класса Dimensions).

Создайте список с именем lst_shop из четырех товаров со следующими данными:

- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)

Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию
объема (габаритов) товаров списка lst_shop, используя стандартную функцию
sorted() языка Python и ее параметр key для настройки сортировки. Прежний
список lst_shop должен оставаться без изменений.

P.S. На экран в программе ничего выводить не нужно.
"""


class Dimensions:
    """
    Класс для представления габаритов товара.

    :cvar MIN_DIMENSION: Минимальное допустимое значение габарита.
    :cvar MAX_DIMENSION: Максимальное допустимое значение габарита.
    :ivar a: Габаритный размер a.
    :ivar b: Габаритный размер b.
    :ivar c: Габаритный размер c.
    """

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self) -> int | float:
        """
        Возвращает значение габарита a.

        :return: Значение габарита a.
        """
        return self.__a

    @a.setter
    def a(self, item: int | float) -> None:
        """
        Устанавливает значение габарита a.

        :param item: Новое значение габарита a.
        """
        if (type(item) in (int, float) and
                self.MIN_DIMENSION <= item <= self.MAX_DIMENSION):
            self.__a = item

    @property
    def b(self) -> int | float:
        """
        Возвращает значение габарита b.

        :return: Значение габарита b.
        """
        return self.__b

    @b.setter
    def b(self, item: int | float) -> None:
        """
        Устанавливает значение габарита b.

        :param item: Новое значение габарита b.
        """
        if (type(item) in (int, float) and
                self.MIN_DIMENSION <= item <= self.MAX_DIMENSION):
            self.__b = item

    @property
    def c(self) -> int | float:
        """
        Возвращает значение габарита c.

        :return: Значение габарита c.
        """
        return self.__c

    @c.setter
    def c(self, item: int | float) -> None:
        """
        Устанавливает значение габарита c.

        :param item: Новое значение габарита c.
        """
        if (type(item) in (int, float) and
                self.MIN_DIMENSION <= item <= self.MAX_DIMENSION):
            self.__c = item

    def __lt__(self, other: 'Dimensions') -> bool:
        """
        Сравнивает объемы двух объектов Dimensions.

        :param other: Другой объект Dimensions.
        :return: True, если объем текущего объекта меньше объема другого.
        """
        return (self.__a * self.__b * self.__c) < (
                other.__a * other.__b * other.__c)

    def __le__(self, other: 'Dimensions') -> bool:
        """
        Сравнивает объемы двух объектов Dimensions.

        :param other: Другой объект Dimensions.
        :return: True, если объем текущего объекта меньше или равен объему
        другого.
        """
        return (self.__a * self.__b * self.__c) <= (
                other.__a * other.__b * other.__c)


class ShopItem:
    """
    Класс для представления товара.

    :ivar name: Название товара.
    :ivar price: Цена товара.
    :ivar dim: Габариты товара (объект класса Dimensions).
    """

    def __init__(self, name: str, price: int | float, dim: Dimensions) -> None:
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [
    ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
    ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
    ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
    ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))
]
lst_shop_sorted = sorted(
    lst_shop, key=lambda item: item.dim.a * item.dim.b * item.dim.c)
