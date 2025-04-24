"""
Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные).
В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное
число (целое или вещественное). Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными
числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны
треугольника. То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению
с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона:
s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.
"""


class PositiveNumber:
    """
    Дескриптор для проверки, что значение является положительным числом.

    :ivar name: Имя атрибута, с которым связан дескриптор.
    """

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Устанавливает имя атрибута, с которым связан дескриптор.

        :param owner: Класс, в котором определен дескриптор.
        :param name: Имя атрибута.
        """
        self.name = "_" + name

    def __get__(self, instance: object, owner: type) -> int | float | None:
        """
        Возвращает значение атрибута.

        :param instance: Экземпляр класса, в котором определен дескриптор.
        :param owner: Класс, в котором определен дескриптор.
        """
        return getattr(instance, self.name, None)

    def __set__(self, instance: object, value: int | float) -> None:
        """
        Устанавливает значение атрибута с проверкой на положительность.

        :param instance: Экземпляр класса, в котором определен дескриптор.
        :param value: Значение атрибута.
        :raises ValueError: Если значение не является положительным числом.
        """
        if type(value) not in (int, float) or value <= 0:
            raise ValueError(
                "длины сторон треугольника должны быть положительными числами")

        setattr(instance, self.name, value)


class Triangle:
    """
    Класс для представления треугольника.

    :cvar a: Длина первой стороны треугольника.
    :cvar b: Длина второй стороны треугольника.
    :cvar c: Длина третьей стороны треугольника.
    """

    a: int | float = PositiveNumber()
    b: int | float = PositiveNumber()
    c: int | float = PositiveNumber()

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        """
        Инициализация объекта Triangle.

        :param a: Длина первой стороны треугольника.
        :param b: Длина второй стороны треугольника.
        :param c: Длина третьей стороны треугольника.
        """
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b

        return True

    def __setattr__(self, key: str, value: int | float) -> None:
        """
        Устанавливает значение атрибута, предварительно проверяя, не нарушит
        ли это условие треугольника.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        :raises ValueError: Если новое значение нарушает условие треугольника.
        """
        if ((key == "a" and not self.triangle(value, self.b, self.c)) or
                (key == "b" and not self.triangle(self.a, value, self.c)) or
                (key == "c" and not self.triangle(self.a, self.b, value))):
            raise ValueError(
                "с указанными длинами нельзя образовать треугольник")

        super().__setattr__(key, value)

    def __len__(self) -> int:
        """
        Возвращает периметр треугольника, приведенный к целому значению.

        :return: Периметр треугольника.
        """
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs) -> float:
        """
        Возвращает площадь треугольника, вычисленную по формуле Герона.

        :return: Площадь треугольника.
        """
        p = (self.a + self.b + self.c) * 0.5
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

