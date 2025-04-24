"""
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты
класса Vector с новыми (вычисленными) координатами. При реализации операторов
+=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при
операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""


class Vector:
    """
    Класс, представляющий многомерный вектор с математическими операциями.

    :ivar coords: Координаты вектора
    """

    def __init__(self, *coords: int | float) -> None:
        self.coords: tuple[int | float, ...] = coords

    def __check_dimensions(self, other: 'Vector') -> None:
        """
        Проверяет совпадение размерностей векторов.

        :param other: Вектор для сравнения размерности
        :raises ArithmeticError: Если размерности не совпадают
        """
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Складывает соответствующие координаты векторов.

        :param other: Вектор для сложения
        :return: Новый вектор-результат
        :raises ArithmeticError: Если размерности не совпадают
        """
        self.__check_dimensions(other)
        return Vector(*(a + b for a, b in zip(self.coords, other.coords)))

    def __iadd__(self, other: 'Vector' | int | float) -> 'Vector':
        """
        Добавляет число или вектор к текущему вектору (+=).

        :param other: Вектор или число для добавления
        :return: Измененный текущий вектор
        :raises ArithmeticError: Если размерности не совпадают (для вектора)
        """
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            self.coords = tuple(a + b for a, b in zip(
                self.coords, other.coords))
        elif type(other) in (int, float):
            self.coords = tuple(a + other for a in self.coords)

        return self

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Вычитает соответствующие координаты векторов.

        :param other: Вектор для вычитания
        :return: Новый вектор-результат
        :raises ArithmeticError: Если размерности не совпадают
        """
        self.__check_dimensions(other)
        return Vector(*(a - b for a, b in zip(self.coords, other.coords)))

    def __isub__(self, other: 'Vector' | int | float) -> 'Vector':
        """
        Вычитает число или вектор из текущего вектора (-=).

        :param other: Вектор или число для вычитания
        :return: Измененный текущий вектор
        :raises ArithmeticError: Если размерности не совпадают (для вектора)
        """
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            self.coords = tuple(a - b for a, b in zip(
                self.coords, other.coords))
        elif type(other) in (int, float):
            self.coords = tuple(a - other for a in self.coords)

        return self

    def __mul__(self, other: 'Vector') -> 'Vector':
        """
        Умножает соответствующие координаты векторов.

        :param other: Вектор для умножения
        :return: Новый вектор-результат
        :raises ArithmeticError: Если размерности не совпадают
        """
        self.__check_dimensions(other)
        return Vector(*(a * b for a, b in zip(self.coords, other.coords)))

    def __eq__(self, other: 'Vector') -> bool:
        """
        Сравнивает векторы на равенство координат.

        :param other: Объект для сравнения
        :return: True если векторы равны, иначе False
        """
        if isinstance(other, Vector):
            return self.coords == other.coords

