"""
В нейронных сетях использую операцию под названием Max Pooling. Суть ее
состоит в сканировании прямоугольной таблицы чисел (матрицы) окном
определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в
пределах этого окна:

 Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):

Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем
MaxPooling, объекты которого создаются командой:

mp = MaxPooling(step=(2, 2), size=(2,2))
где step - шаг смещения окна по горизонтали и вертикали; size - размер окна
по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж
со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)
где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки
таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при
сканировании таблицы часть окна выходит за ее пределы, то эти данные
отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно
не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
# [[6, 8], [9, 7]]

Результатом будет таблица чисел:

6 8
9 7

P.S. В программе достаточно объявить только класс. Выводить на экран ничего
не нужно.
"""


class MaxPooling:
    """
    Класс для выполнения операции Max Pooling на прямоугольной матрице
    чисел.

    :ivar step: Кортеж (шаг по строкам, шаг по столбцам), по умолчанию (2, 2).
    :ivar size: Кортеж (высота окна, ширина окна), по умолчанию (2, 2).
    """

    def __init__(self, step: tuple[int, int] = (2, 2),
                 size: tuple[int, int] = (2, 2)) -> None:
        self.step = step
        self.size = size

    def __call__(self, matrix: list[list[float | int]]
                 ) -> list[list[float | int]]:
        """
        Применяет операцию Max Pooling к матрице.

        :param matrix: Прямоугольная матрица чисел (список списков).
        :return: Результат операции Max Pooling (новая матрица).
        :raises ValueError: Если матрица содержит нечисловые элементы.
        """
        self._validate_matrix(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        result: list[list[int | float]] = []
        for i in range(0, rows - self.size[0] + 1, self.step[0]):
            row_result = []
            for j in range(0, cols - self.size[1] + 1, self.step[1]):
                    window = []
                    for x in range(i, i + self.size[0]):
                        for y in range(j, j + self.size[1]):
                            element = matrix[x][y]
                            if type(element) in (int, float):
                                window.append(element)
                            else:
                                raise ValueError(
                                    "Неверный формат для первого параметра "
                                    "matrix.")
                    row_result.append(max(window))
            if row_result:
                result.append(row_result)
        return result

    def _validate_matrix(self, matrix: list[list[float | int]]) -> None:
        """
        Проверяет, что матрица является прямоугольной и содержит только числа.

        :param matrix: Матрица для проверки.
        :raises ValueError: Если матрица не является прямоугольной или
        списком списков.
        """
        if (not isinstance(matrix, list) or
                not all(isinstance(row, list) for row in matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        rows = len(matrix)
        if rows == 0:
            raise ValueError("Неверный формат для первого параметра matrix.")

        cols = len(matrix[0])
        if not all(len(row) == cols for row in matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")

