"""
Теперь, вам необходимо разработать итератор, который бы перебирал указанные
столбцы двумерного списка. Список представляет собой двумерную таблицу из
данных:

lst = [[x11, x12, ..., x1N],
       [x21, x22, ..., x2N],
       ...
       [xM1, xM2, ..., xMN]
      ]
Для этого в программе необходимо объявить класс с именем IterColumn, объекты
которого создаются командой:

it = IterColumn(lst, column)
где lst - ссылка на двумерный список; column - индекс перебираемого столбца
(отсчитывается от 0).

Затем, с объектами класса IterColumn должны быть доступны следующие операции:

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка:
x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
P.S. В программе нужно объявить только класс итератора. Выводить на экран
ничего не нужно.
"""
from typing import Any


class IterColumn:
    """
    Итератор для последовательного перебора элементов указанного столбца
    двумерного списка.

    :ivar lst: Ссылка на перебираемый двумерный список
    :type lst: List[List[Any]]
    :ivar column: Индекс целевого столбца
    :ivar row: Текущий индекс строки (начинается с 0)
    """

    def __init__(self, lst: list[list[Any]], column: int) -> None:
        self.lst = lst
        self.column = column
        self.row = 0

    def __iter__(self) -> 'ImportError':
        """
        Возвращает итератор для использования в циклах.

        :return: Сам объект итератора
        """
        self.row = 0
        return self

    def __next__(self) -> Any:
        """
        Возвращает следующий элемент столбца.

        :return: Элемент из текущей строки и заданного столбца
        :raises StopIteration: При достижении конца списка
        """
        if self.row >= len(self.lst):
            raise StopIteration

        self.row += 1
        return self.lst[self.row - 1][self.column]

