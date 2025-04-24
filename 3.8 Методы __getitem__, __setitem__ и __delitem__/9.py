"""
Вам необходимо описывать в программе очень большие и разреженные таблицы
данных (с большим числом пропусков). Для этого предлагается объявить класс
SparseTable, объекты которого создаются командой:

st = SparseTable()
В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в
таблицу по индексам row, col (целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами
(row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться
атрибуты rows, cols объекта класса SparseTable. Если происходит попытка
удалить несуществующую ячейку, то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')
Ячейки таблицы представляют собой объекты класса Cell, которые создаются
командой:

data = Cell(value)
где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж)
i, j, а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)
Чтение данных возможно только для существующих ячеек. Если ячейки с указанными
индексами нет, то генерировать исключение командой:

raise ValueError('данные по указанным индексам отсутствуют')
При записи новых значений их следует менять в существующей ячейке или
добавлять новую, если ячейка с индексами (i, j) отсутствует в таблице.
(Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.
"""
from typing import Any


class Cell:
    """
    Класс для представления ячейки таблицы.

    :param value: Значение ячейки (любого типа)
    :ivar value: Хранит значение ячейки
    """

    def __init__(self, value: Any) -> None:
        self.value = value


class SparseTable:
    """
    Класс для работы с разреженной таблицей данных.

    :ivar rows: Текущее количество строк в таблице
    :ivar cols: Текущее количество столбцов в таблице
    :ivar __dt: Приватный словарь для хранения ячеек таблицы
    :vartype __dt: dict[tuple[int, int], Cell]
    """

    def __init__(self) -> None:
        self.rows: int = 0
        self.cols: int = 0
        self.__dt: dict[tuple[int, int], Cell] = {}

    @property
    def dt(self) -> dict[tuple[int, int]: Cell]:
        """
        Доступ к словарю с данными таблицы.

        :return: Словарь с ячейками таблицы
        :rtype: Dict[Tuple[int, int], Cell]
        """
        return self.__dt

    def __check(self, item: tuple[int, int], exc_type: Exception, message: str
                ) -> None:
        """
        Проверяет существование ячейки.

        :param item: Индексы ячейки (строка, столбец)
        :type item: Tuple[int, int]
        :param exc_type: Тип исключения при ошибке
        :type exc_type: Exception
        :param message: Сообщение об ошибке
        :raises: exc_type: Если ячейка не существует
        """
        if item not in self.dt.keys():
            raise exc_type(message)

    def __update_dimensions(self) -> None:
        """Обновляет атрибуты rows и cols на основе текущих данных."""
        # if not self.dt:
        #     self.rows = self.cols = 0
        # else:
        #     self.rows = max(r for r, _ in self.__dt) + 1
        #     self.cols = max(c for _, c in self.__dt) + 1

        rows = cols = 0
        for r, c in self.__dt:
            rows = max(rows, r + 1)
            cols = max(cols, c + 1)
        self.rows, self.cols = rows, cols

    def add_data(self, row: int, col: int, data: Cell) -> None:
        """
        Добавляет данные в таблицу.

        :param row: Индекс строки
        :param col: Индекс столбца
        :param data: Объект ячейки
        """
        self.dt[(row, col)] = data
        self.__update_dimensions()

    def remove_data(self, row: int, col: int) -> None:
        """
        Удаляет ячейку из таблицы.

        :param row: Индекс строки
        :param col: Индекс столбца
        :raises IndexError: Если ячейка не существует
        """
        self.__check((row, col), IndexError,
                     'ячейка с указанными индексами не существует')
        del self.dt[(row, col)]
        self.__update_dimensions()

    def __getitem__(self, item: tuple[int, int]) -> Any:
        """
        Возвращает значение ячейки.

        :param item: Индексы ячейки (строка, столбец)
        :return: Значение ячейки
        :raises ValueError: Если ячейка не существует
        """
        self.__check(item, ValueError,
                     'данные по указанным индексам отсутствуют')
        return self.dt[item].value

    def __setitem__(self, key: tuple[int, int], value: Any) -> None:
        """
        Устанавливает значение ячейки.

        :param key: Индексы ячейки (строка, столбец)
        :param value: Новое значение ячейки
        """
        self.add_data(key[0], key[1], Cell(value))

