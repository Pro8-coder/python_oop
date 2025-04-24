"""
Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики".
Для этого требуется объявить класс TicTacToe (крестики-нолики), объекты
которого создаются командой:

game = TicTacToe()
Каждый объект game должен иметь публичный атрибут:

pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

Каждая клетка игрового поля представляется объектом класса Cell и создается
командой:

cell = Cell()
Объекты класса Cell должны иметь следующие публичные локальные атрибуты:

is_free - True, если клетка свободна; False в противном случае;
value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

Также с каждым объектом класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка свободна (cell.is_free=True) и False
в противном случае.

Класс TicTacToe должен иметь следующий метод:

clear() - очистка игрового поля (все клетки заполняются нулями и переводятся
в закрытое состояние);

А объекты этого класса должны иметь следующую функциональность (обращение
по индексам):

game[0, 0] = 1 # установка нового значения, если поле закрыто
res = game[1, 1] # получение значения центральной ячейки поля (возвращается
число)
Если указываются некорректные индексы, то должно генерироваться исключение
командой:

raise IndexError('неверный индекс клетки')
Если идет попытка присвоить новое значение в открытую клетку поля,
то генерировать исключение:

raise ValueError('клетка уже занята')
Также должны быть реализованы следующие полные срезы при обращении к клеткам
игрового поля:

slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом
indx
slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом
indx
Пример использования классов (эти строчки в программе не писать):

game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.

P.P.S. При передаче среза в магических методах __setitem__() и __getitem__()
параметр индекса становится объектом класса slice. Его можно указывать
непосредственно в квадратных скобках упорядоченных коллекций (списков,
кортежей и т.п.).
"""
from typing import TypeVar

T = TypeVar('T', int, slice)


class Cell:
    """
    Класс клетки игрового поля для игры в крестики-нолики.

    :ivar is_free: Флаг, указывающий свободна ли клетка
    :ivar value: Значение клетки (0 - пусто, 1 - крестик, 2 - нолик)
    """

    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self) -> bool:
        """
        Возвращает статус клетки.

        :return: True если клетка свободна, False если занята
        """
        return self.is_free


class TicTacToe:
    """
    Класс игрового поля для игры в крестики-нолики размером 3x3.

    :ivar pole: Игровое поле (кортеж 3x3 из объектов Cell)
    :vartype pole: tuple[tuple[Cell, ...], ...]
    """

    def __init__(self) -> None:
        self.pole: tuple[tuple[Cell, ...], ...] = tuple(tuple(
            Cell() for _ in range(3)) for _ in range(3))

    def _check_index(self, index: T) -> None:
        """
        Проверяет корректность индекса.

        :param index: Проверяемый индекс
        :raises IndexError: Если индекс выходит за границы поля
        """
        if type(index) == int and not 0 <= index < 3:
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item: tuple[T, T]) -> int | tuple[int, ...]:
        """
        Возвращает значение клетки или среза клеток.

        :param item: Индекс или срез для доступа к клеткам
        :type item: tuple[int | slice, int | slice]
        :return: Значение клетки или кортеж значений для среза
        :rtype: int | tuple[int, ...]
        :raises IndexError: При некорректных индексах
        """
        row, col = item
        self._check_index(row)
        self._check_index(col)

        if isinstance(row, slice):
            return tuple(self.pole[i][col].value for i in range(3))
        if isinstance(col, slice):
            return tuple(self.pole[row][i].value for i in range(3))

        return self.pole[row][col].value

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        """
        Устанавливает значение в указанную клетку.

        :param key: Координаты клетки (row, col)
        :param value: Значение для установки (1 - крестик, 2 - нолик)
        :raises IndexError: При некорректных индексах
        :raises ValueError: При попытке изменить занятую клетку или
        недопустимом значении
        """
        row, col = key
        self._check_index(row)
        self._check_index(col)

        cell = self.pole[row][col]

        if not cell.is_free:
            raise ValueError('клетка уже занята')
        elif value not in (1, 2):
            raise ValueError('допустимые значения: 1 (крестик) или 2 (нолик)')

        cell.value = value
        cell.is_free = False

    def clear(self) -> None:
        """Сбрасывает игровое поле в начальное состояние (как при __init__)."""
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

