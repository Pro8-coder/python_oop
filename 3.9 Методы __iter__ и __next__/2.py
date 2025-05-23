"""
Вам дают задание разработать итератор для последовательного перебора элементов
вложенных (двумерных) списков следующей структуры:

lst = [[x00],
       [x10, x11],
       [x20, x21, x22],
       [x30, x31, x32, x33],
       ...
      ]
Для этого необходимо в программе объявить класс с именем TriangleListIterator,
объекты которого создаются командой:

it = TriangleListIterator(lst)
где lst - ссылка на перебираемый список.

Затем, с объектами класса TriangleListIterator должны быть доступны следующие
операции:

for x in it:  # последовательный перебор всех элементов списка: x00, x10,
x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
Итератор должен перебирать элементы списка по указанной треугольной форме.
Даже если итератору на вход будет передан прямоугольная таблица (вложенный
список), то ее перебор все равно должен осуществляться по треугольнику.
Если же это невозможно (из-за структуры списка), то естественным образом
должна возникать ошибка IndexError: index out of range (выход индекса за
допустимый диапазон).

P.S. В программе нужно объявить только класс. Выводить на экран ничего
не нужно.
"""
from typing import Any


class TriangleListIterator:
    """
    Итератор для последовательного перебора элементов вложенных списков в
    треугольной форме.

    :ivar lst: Ссылка на перебираемый список
    :ivar row: Текущий индекс строки (начинается с 0)
    :ivar col: Текущий индекс столбца (начинается с 0)
    """

    def __init__(self, lst: list[list]) -> None:
        self.lst = lst
        self.row = self.col = 0

    def __iter__(self) -> 'TriangleListIterator':
        """
        Возвращает итератор для использования в циклах.

        :return: Сам объект итератора
        """
        self.row = self.col = 0
        return self

    def __next__(self) -> Any:
        """
        Возвращает следующий элемент при итерации.

        :return: Очередной элемент списка
        :raises IndexError: При выходе за пределы треугольной структуры
        :raises StopIteration: При завершении итерации
        """
        if self.row >= len(self.lst):
            raise StopIteration

        if self.col > self.row:
            self.row += 1
            self.col = 0
            return self.__next__()

        item = self.lst[self.row][self.col]
        self.col += 1
        return item

