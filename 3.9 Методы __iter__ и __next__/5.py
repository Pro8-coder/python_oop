"""
В программе необходимо реализовать таблицу TableValues по следующей схеме:

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого
класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться
локальный приватный атрибут __data с соответствующим значением. Для работы
с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются
командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки
(int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках
таблицы равны 0 (целое число).

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col
(индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При попытке записать по индексам table[row, col] данные другого типа
(не совпадающего с атрибутом type_data объекта класса TableValues), должно
генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность. Если
индексы не целое число или они выходят за диапазон размера таблицы, то
генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.
"""
from typing import Any, Iterator


class Cell:
    """
    Класс для представления ячейки таблицы.

    :ivar __data: Приватный атрибут для хранения данных ячейки
    """

    def __init__(self, data: Any) -> None:
        self.__data = data

    @property
    def data(self) -> Any:
        """
        Возвращает значение ячейки.

        :return: Текущее значение ячейки
        """
        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        """
        Устанавливает новое значение ячейки.

        :param value: Новое значение для установки
        """
        self.__data = value


class TableValues:
    """
    Класс для представления таблицы значений.

    :ivar rows: Количество строк в таблице
    :ivar cols: Количество столбцов в таблице
    :ivar type_data: Тип данных для ячеек таблицы
    :ivar table_lst: Двумерный список объектов Cell (в Cell по умолчанию 0)
    """

    def __init__(self, rows: int, cols: int, type_data: type = int) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table_lst: list[list[Cell]] = [[Cell(0) for _ in range(self.cols)
                                             ] for _ in range(self.rows)]

    def _check_index(self, index: tuple[int, int]) -> None:
        """
        Проверяет корректность индексов.

        :param index: Кортеж с индексами (строка, столбец)
        :raises IndexError: Если индексы некорректны
        """
        if type(index) == tuple and len(index) == 2:
            row_index, col_index = index
            if type(row_index) != int or not (
                    -self.rows <= row_index < self.rows):
                raise IndexError('неверный индекс')
            if type(col_index) != int or not (
                    -self.cols <= col_index < self.cols):
                raise IndexError('неверный индекс')
        else:
            raise IndexError('неверный индекс')

    def _check_type_data(self, value: Any) -> None:
        """
        Проверяет соответствие типа данных.

        :param value: Проверяемое значение
        :raises TypeError: Если тип не соответствует ожидаемому
        """
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, index: tuple[int, int]) -> Any:
        """
        Возвращает значение ячейки по индексу.

        :param index: Кортеж с индексами (строка, столбец)
        :return: Значение ячейки
        :raises IndexError: Если индексы некорректны
        """
        self._check_index(index)
        return self.table_lst[index[0]][index[1]].data

    def __setitem__(self, index: tuple[int, int], value: Any) -> None:
        """
        Устанавливает значение ячейки по индексу.

        :param index: Кортеж с индексами (строка, столбец)
        :param value: Новое значение ячейки
        :raises IndexError: Если индексы некорректны
        :raises TypeError: Если тип данных не соответствует
        """
        self._check_index(index)
        self._check_type_data(value)
        self.table_lst[index[0]][index[1]].data = value

    def __iter__(self) -> Iterator[list[Any]]:
        """
        Итератор по строкам таблицы.

        :return: Итератор списков значений ячеек
        """
        for row in self.table_lst:
            yield [cell.data for cell in row]

