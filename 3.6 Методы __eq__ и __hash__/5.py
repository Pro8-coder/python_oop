"""
Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие
габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты
a, b, c (с соответствующими числовыми значениями). Также для каждого объекта
должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку,
записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю,
то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса
Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию)
хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.

Sample Input:

1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
Sample Output:
"""


class Dimensions:
    """
    Класс для представления габаритов тела.

    :ivar a: Высота тела.
    :ivar b: Ширина тела.
    :ivar c: Глубина тела.
    """

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        """
        Инициализация объекта Dimensions.

        :raises ValueError: Если значение атрибута не является положительным
        числом.
        """
        if a <= 0 or a <= 0 or a <= 0:
            raise ValueError(
                "габаритные размеры должны быть положительными числами")

        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> int:
        """
        Вычисляет хэш объекта на основе всех трех габаритов.

        :return: Целочисленный хэш.
        """
        return hash((self.a, self.b, self.c))

    def __eq__(self, other: 'Dimensions') -> bool:
        """
        Сравнивает объекты Dimensions по их хэшам.

        :param other: Другой объект Dimensions.
        :return: True, если хэши равны, иначе False.
        """
        return hash(self) == hash(other)

    def __lt__(self, other: 'Dimensions') -> bool:
        """
        Сравнивает объекты Dimensions по их хэшам для сортировки.

        :param other: Другой объект Dimensions.
        :return: True, если хэш текущего объекта меньше хэша другого объекта,
        иначе False.
        """
        return hash(self) < hash(other)

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dimensions.

        :return: Строка в формате "Dimensions: a, b, c; hash: хэш".
        """
        return (f"Dimensions: {self.a}, {self.b}, {self.c}; "
                f"hash: {self.__hash__()}")

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Dimensions для отладки.

        :return: Строка в формате "Dimensions: a, b, c; hash: хэш".
        """
        return self.__str__()


s_inp = input()

lst_dims: list[Dimensions] = [Dimensions(*map(
    lambda j: float(j) if "." in j else int(j), i.split()
)) for i in s_inp.split("; ")]

lst_dims = sorted(lst_dims)
