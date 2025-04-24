"""
Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса
должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое
начальное значение элементов матрицы (должно быть число: целое или
вещественное). Если в качестве аргументов передаются не числа, то генерировать
исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное
число')
Также объекты можно создавать командой:

m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или
вещественных). Если список list2D не прямоугольный, или хотя бы один из его
элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')
Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2)
присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то
генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')
Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0
и до размеров матрицы), то генерировать исключение:

raise IndexError('недопустимые значения индексов')
Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
Во всех этих операция должна формироваться новая матрица с соответствующими
значениями. Если размеры матриц не совпадают (разные хотя бы по одной оси),
то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')
Пример для понимания использования индексов (эти строчки в программе писать
не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
P.S. В программе нужно объявить только класс. Выводить на экран ничего
не нужно.
"""
from typing import Union


class Matrix:
    """
    Класс для работы с двумерными матрицами.

    Поддерживает основные операции: сложение, вычитание, индексацию.
    Матрица может быть создана либо по размерам с заполняющим значением,
    либо из готового двумерного списка.

    :ivar rows: Количество строк в матрице
    :vartype rows: int
    :ivar cols: Количество столбцов в матрице
    :vartype cols: int
    :ivar matrix: Двумерный список, содержащий элементы матрицы
    :vartype matrix: List[List[Union[int, float]]]
    """

    def __init__(self, *args) -> None:
        """
        Инициализация матрицы.

        Возможные варианты создания:
        1. Matrix(rows, cols, fill_value)
        2. Matrix(list2D)

        :param args: либо (rows, cols, fill_value), либо (list2D,)
        :raises TypeError: если аргументы не соответствуют требованиям
        :raises ValueError: если список не прямоугольный
        """
        if len(args) == 3:
            rows, cols, fill_value = args
            if type(rows) != int or type(cols) != int or type(
                    fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; '
                                'fill_value - произвольное число')

            self.rows = rows
            self.cols = cols
            self.matrix: list[list[int | float]] = [
                [fill_value for _ in range(cols)] for _ in range(rows)]
        elif len(args) == 1:
            list2D = args[0]
            if type(list2D) != list:
                raise TypeError(
                    'список должен быть прямоугольным, состоящим из чисел')

            if len(list2D) == 0:
                self.rows = 0
                self.cols = 0
                self.matrix = []
                return

            first_row_len = len(list2D[0])
            for row in list2D:
                if len(row) != first_row_len:
                    raise TypeError(
                        'список должен быть прямоугольным, состоящим из чисел')
                if not all(type(x) in (int, float) for x in row):
                    raise TypeError(
                        'список должен быть прямоугольным, состоящим из чисел')

            self.rows = len(list2D)
            self.cols = first_row_len
            self.matrix = [row.copy() for row in list2D]

    def _check_index(self, index: tuple[int, int]) -> None:
        """
        Проверка корректности индексов.

        :param index: кортеж (row, col)
        :raises IndexError: если индексы выходят за границы
        """
        if type(index) == tuple and len(index) == 2:
            row, col = index
            if type(row) != int or not 0 <= row < self.rows:
                raise IndexError('недопустимые значения индексов')
            if type(col) != int or not 0 <= col < self.cols:
                raise IndexError('недопустимые значения индексов')
        else:
            raise IndexError('недопустимые значения индексов')

    def _check_value(self, value: int | float) -> None:
        """
        Проверка типа значения.

        :param value: значение для проверки
        :raises TypeError: если значение не числовое
        """
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, index: tuple[int, int]) -> int | float:
        """
        Получение элемента по индексу.

        :param index: кортеж (row, col)
        :return: значение элемента
        :raises IndexError: при недопустимых индексах
        """
        self._check_index(index)
        return self.matrix[index[0]][index[1]]

    def __setitem__(self, index: tuple[int, int], value: int | float) -> None:
        """
        Установка значения элемента по индексу.

        :param index: кортеж (row, col)
        :param value: новое значение
        :raises IndexError: при недопустимых индексах
        :raises TypeError: при нечисловом значении
        """
        self._check_index(index)
        self._check_value(value)
        self.matrix[index[0]][index[1]] = value

    def __add__(self, other: Union['Matrix', int, float]) -> 'Matrix':
        """
        Сложение матриц или матрицы с числом.

        :param other: матрица или число
        :return: новая матрица-результат
        :raises ValueError: при несовпадении размеров матриц
        :raises TypeError: при недопустимом типе операнда
        """
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError(
                    'операции возможны только с матрицами равных размеров')

            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other[i, j]

            return result
        elif type(other) in (int, float):
            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other

            return result

    def __sub__(self, other: Union['Matrix', int, float]) -> 'Matrix':
        """
        Вычитание матриц или числа из матрицы.

        :param other: матрица или число
        :return: новая матрица-результат
        :raises ValueError: при несовпадении размеров матриц
        :raises TypeError: при недопустимом типе операнда
        """
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError(
                    'операции возможны только с матрицами равных размеров')

            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other[i, j]

            return result
        elif type(other) in (int, float):
            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other

            return result

