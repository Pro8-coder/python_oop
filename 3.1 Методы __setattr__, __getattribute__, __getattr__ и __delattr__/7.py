"""
Объявите в программе класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 1000

Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
и содержать локальные атрибуты:

__a, __b, __c - габаритные размеры (целые или вещественные числа).

Для работы с этими локальными атрибутами в классе Dimensions следует прописать
следующие объекты-свойства:

a, b, c - для изменения и считывания соответствующих локальных атрибутов __a,
__b, __c.

При изменении значений __a, __b, __c следует проверять, что присваиваемое
значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так,
то новое значение не присваивается (игнорируется).

С помощью магических методов данного занятия запретить создание локальных
атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions. При
попытке это сделать генерировать исключение:

raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION
запрещено.")
Пример использования класса  (эти строчки в программе писать не нужно):

d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError
P.S. В программе нужно объявить только класс Dimensions. На экран ничего
выводить не нужно.
"""


class Dimensions:
    """
    Класс для представления габаритных размеров.

    :cvar MIN_DIMENSION: Минимальное допустимое значение для габаритного размера.
    :cvar MAX_DIMENSION: Максимальное допустимое значение для габаритного размера.
    """

    MIN_DIMENSION: int = 10
    MAX_DIMENSION: int = 1000

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        """
        Инициализация экземпляра класса Dimensions.

        :param a: Габаритный размер a.
        :param b: Габаритный размер b.
        :param c: Габаритный размер c.
        """
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key: str, value: int | float) -> None:
        """
        Запрещает изменение атрибутов MIN_DIMENSION и MAX_DIMENSION.

        :param key: Имя атрибута.
        :param value: Значение атрибута.

        :raises AttributeError: Если попытка изменить MIN_DIMENSION или
        MAX_DIMENSION.
        """
        if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

        super().__setattr__(key, value)

    @classmethod
    def __verify(cls, value: int | float) -> bool:
        """
        Проверяет, что значение находится в допустимом диапазоне.

        :param value: Значение для проверки.
        :return: True, если значение в допустимом диапазоне, иначе False.
        """
        return isinstance(value, (int, float)) and \
               cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self) -> int | float:
        """
        Возвращает значение габаритного размера a.

        :return: Значение габаритного размера a.
        """
        return self.__a

    @a.setter
    def a(self, value: int | float) -> None:
        """
        Устанавливает значение габаритного размера a, если оно в допустимом
        диапазоне.

        :param value: Значение для установки.
        """
        if self.__verify(value):
            self.__a = value

    @property
    def b(self) -> int | float:
        """
        Возвращает значение габаритного размера b.

        :return: Значение габаритного размера b.
        """
        return self.__b

    @b.setter
    def b(self, value: int | float) -> None:
        """
        Устанавливает значение габаритного размера b, если оно в допустимом
        диапазоне.

        :param value: Значение для установки.
        """
        if self.__verify(value):
            self.__b = value

    @property
    def c(self) -> int | float:
        """
        Возвращает значение габаритного размера c.

        :return: Значение габаритного размера c.
        """
        return self.__c

    @c.setter
    def c(self, value: int | float) -> None:
        """
        Устанавливает значение габаритного размера c, если оно в допустимом
        диапазоне.

        :param value: Значение для установки.
        """
        if self.__verify(value):
            self.__c = value

