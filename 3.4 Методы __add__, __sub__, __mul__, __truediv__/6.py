"""
Объявите класс Box3D для представления прямоугольного параллелепипеда
(бруска), объекты которого создаются командой:

box = Box3D(width, height, depth)
где width, height, depth - ширина, высота и глубина соответственно (числа:
целые или вещественные)

В каждом объекте класса Box3D должны создаваться публичные атрибуты:

width, height, depth - ширина, высота и глубина соответственно.

С объектами класса Box3D должны выполняться следующие операторы:

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие
размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность
умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие
размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие
размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
При каждой арифметической операции следует создавать новый объект класса
Box3D с соответствующими значениями локальных атрибутов.

P.S. В программе достаточно только объявить класс Box3D. На экран ничего
выводить не нужно.
"""


class Box3D:
    """
    Класс Box3D представляет прямоугольный параллелепипед (брусок).

    :ivar width: Ширина параллелепипеда.
    :ivar height: Высота параллелепипеда.
    :ivar depth: Глубина параллелепипеда.
    """

    def __init__(self, width: int | float, height: int | float,
                 depth: int | float) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other: 'Box3D') -> 'Box3D':
        """
        Сложение двух объектов Box3D.

        :param other: Другой объект Box3D.
        :return: Новый объект Box3D с суммой размерностей.
        :raises TypeError: Если other не является объектом Box3D.
        """
        if isinstance(other, Box3D):
            return Box3D(self.width + other.width,
                         self.height + other.height,
                         self.depth + other.depth)

    def __mul__(self, other: int | float) -> 'Box3D':
        """
        Умножение размерностей объекта Box3D на число.

        :param other: Число для умножения.
        :return: Новый объект Box3D с умноженными размерностями.
        :raises TypeError: Если other не является числом.
        """
        if type(other) in (int, float):
            return Box3D(self.width * other,
                         self.height * other,
                         self.depth * other)

    def __rmul__(self, other: int | float) -> 'Box3D':
        """
        Умножение числа на объект Box3D.

        :param other: Число для умножения.
        :return: Новый объект Box3D с умноженными размерностями.
        """
        return self.__mul__(other)

    def __sub__(self, other: 'Box3D') -> 'Box3D':
        """
        Вычитание одного объекта Box3D из другого.

        :param other: Другой объект Box3D.
        :return: Новый объект Box3D с разностью размерностей.
        :raises TypeError: Если other не является объектом Box3D.
        """
        if isinstance(other, Box3D):
            return Box3D(self.width - other.width,
                         self.height - other.height,
                         self.depth - other.depth)

    def __floordiv__(self, other: int | float) -> 'Box3D':
        """
        Целочисленное деление размерностей объекта Box3D на число.

        :param other: Число для деления.
        :return: Новый объект Box3D с целочисленно разделенными размерностями.
        :raises TypeError: Если other не является числом.
        :raises ZeroDivisionError: Если other равен нулю.
        """
        if type(other) in (int, float):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль недопустимо")
            else:
                return Box3D(self.width // other,
                             self.height // other,
                             self.depth // other)

    def __mod__(self, other: int | float) -> 'Box3D':
        """
        Остаток от деления размерностей объекта Box3D на число.

        :param other: Число для деления.
        :return: Новый объект Box3D с остатками от деления размерностей.
        :raises TypeError: Если other не является числом.
        :raises ZeroDivisionError: Если other равен нулю.
        """
        if type(other) in (int, float):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль недопустимо")
            else:
                return Box3D(self.width % other,
                             self.height % other,
                             self.depth % other)

