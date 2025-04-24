"""
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или
вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector)
с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector)
с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает
кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с
целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise
ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна
координата является вещественной. Иначе, v должен быть объектом класса
VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.
"""


class Vector:
    """
    Класс для работы с векторами произвольной размерности.

    Поддерживает операции сложения и вычитания векторов одинаковой размерности.
    Координаты могут быть целыми или вещественными числами.

    :ivar coords: Координаты вектора (целые или вещественные числа)
    """

    def __init__(self, *coords: int | float) -> None:
        self.coords = coords

    def get_coords(self) -> tuple[int | float, ...]:
        """
        Возвращает координаты вектора.

        :return: Кортеж координат вектора
        """
        return self.coords

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Операция сложения векторов.

        :param other: Вектор для сложения
        :return: Новый вектор - сумма
        :raises TypeError: Если размерности векторов не совпадают
        """
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

        return Vector(*(a + b for a, b in zip(self.coords, other.coords)))

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Операция вычитания векторов.

        :param other: Вектор для вычитания
        :return: Новый вектор - разность
        :raises TypeError: Если размерности векторов не совпадают
        """
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

        return Vector(*(a - b for a, b in zip(self.coords, other.coords)))


class VectorInt(Vector):
    """
    Класс для работы с векторами с целочисленными координатами.

    Наследует функциональность класса Vector, добавляя проверку
    целочисленности координат.
    """

    def __init__(self, *coords: int) -> None:
        if any(type(x) != int for x in coords):
            raise ValueError('координаты должны быть целыми числами')

        super().__init__(*coords)

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Операция сложения векторов с проверкой типа результата.

        :param other: Вектор для сложения
        :return: VectorInt если все координаты целые, иначе Vector
        :raises TypeError: Если размерности векторов не совпадают
        """
        result = super().__add__(other)
        # try:
        #     return VectorInt(*result.coords)
        # except ValueError:
        #     return result
        if any(type(x) != int for x in other.coords):
            return result

        return VectorInt(*result.coords)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Операция вычитания векторов с проверкой типа результата.

        :param other: Вектор для вычитания
        :return: VectorInt если все координаты целые, иначе Vector
        :raises TypeError: Если размерности векторов не совпадают
        """
        result = super().__sub__(other)
        # try:
        #     return VectorInt(*result.coords)
        # except ValueError:
        #     return result
        if any(type(x) != int for x in other.coords):
            return result

        return VectorInt(*result.coords)

