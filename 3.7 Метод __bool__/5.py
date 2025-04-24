"""
Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь
представлять и управлять игровым полем. Будем полагать, что оно имеет размеры
N x M клеток. Каждая клетка будет представлена объектом класса Cell и
содержать либо число мин вокруг этой клетки, либо саму мину.

Для начала в программе объявите класс GamePole, который будет создавать и
управлять игровым полем. Объект этого класса должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного
объекта класса GamePole (используйте паттерн Singleton, о котором мы с вами
говорили, когда рассматривали магический метод __new__()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов
(N строк и M столбцов), состоящий из объектов класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство
(property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля
(расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов
начинается с нуля; метод меняет значение атрибута __is_open объекта Cell
в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше
усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого
удобно воспользоваться функцией randint модуля random). После расстановки всех
total_mines мин, вычислите их количество вокруг остальных клеток
(где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j).
Если индексы указаны некорректно, то генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля.
Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина,
False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта;
False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие
объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных
значений (либо булево значение True/False, либо целое число от 0 до 8).
Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.

Пример использования классов (эти строчки в программе писать не нужно):

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим
числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
P.S. В программе на экран выводить ничего не нужно, только объявить классы.
"""
from random import randint


class Cell:
    """
    Класс, представляющий клетку игрового поля в игре 'Сапер'.

    :ivar __is_mine: Наличие мины в клетке (True - есть мина, False - нет)
    :ivar __number: Количество мин в соседних клетках (от 0 до 8)
    :ivar __is_open: Состояние клетки (True - открыта, False - закрыта)
    """

    def __init__(self) -> None:
        self.__is_mine: bool = False
        self.__number: int = 0
        self.__is_open: bool = False

    @property
    def is_mine(self) -> bool:
        """
        Возвращает информацию о наличии мины в клетке.

        :return: True, если в клетке есть мина, иначе False
        """
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        """
        Устанавливает наличие мины в клетке.

        :param value: True - есть мина, False - нет
        :raises ValueError: Если передано не булево значение
        """
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_mine = value

    @property
    def number(self) -> int:
        """
        Возвращает количество мин в соседних клетках.

        :return: Число мин (от 0 до 8)
        """
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        """
        Устанавливает количество мин в соседних клетках.

        :param value: Число мин (от 0 до 8)
        :raises ValueError: Если значение не в диапазоне 0-8
        """
        if type(value) != int or value not in range(9):
            raise ValueError("недопустимое значение атрибута")

        self.__number = value

    @property
    def is_open(self) -> bool:
        """
        Возвращает состояние клетки (открыта/закрыта).

        :return: True, если клетка открыта, иначе False
        """
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool) -> None:
        """
        Устанавливает состояние клетки (открыта/закрыта).

        :param value: True - открыть клетку, False - закрыть
        :raises ValueError: Если передано не булево значение
        """
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_open = value

    def __bool__(self) -> bool:
        """
        Определяет поведение объекта в булевом контексте.

        :return: True, если клетка закрыта, иначе False
        """
        return not self.__is_open


class GamePole:
    """
    Класс, управляющий игровым полем в игре 'Сапер' (реализует Singleton).

    :cvar __instance: Единственный экземпляр класса (Singleton)
    :ivar N: Количество строк игрового поля
    :ivar M: Количество столбцов игрового поля
    :ivar total_mines: Общее количество мин на поле
    :ivar __pole_cells: Двумерный кортеж объектов Cell
    :vartype __pole_cells: Tuple[Tuple[Cell, ...], ...]
    """

    __instance: 'GamePole' | None = None

    def __new__(cls, *args, **kwargs) -> 'GamePole':
        """
        Контролирует создание только одного экземпляра класса (Singleton).

        :return: Единственный экземпляр класса
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, N: int, M: int, total_mines: int) -> None:
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells: tuple[tuple[Cell, ...], ...] = None

    @property
    def pole(self) -> tuple[tuple[Cell, ...], ...]:
        """
        Возвращает игровое поле (только для чтения).

        :return: Двумерный кортеж клеток
        """
        return self.__pole_cells

    def init_pole(self) -> None:
        """
        Инициализирует игровое поле: расставляет мины и вычисляет числа
        вокруг них.
        """
        self.__pole_cells = tuple(tuple(
            Cell() for _ in range(self.M)) for _ in range(self.N))

        mines_placed = 0
        while mines_placed < self.total_mines:
            i, j = randint(0, self.N-1), randint(0, self.M-1)
            if not self.__pole_cells[i][j].is_mine:
                self.__pole_cells[i][j].is_mine = True
                mines_placed += 1

        for i in range(self.N):
            for j in range(self.M):
                if not self.__pole_cells[i][j].is_mine:
                    count = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.N and 0 <= nj < self.M:
                                if self.__pole_cells[ni][nj].is_mine:
                                    count += 1

                    self.__pole_cells[i][j].number = count

    def open_cell(self, i: int, j: int) -> None:
        """
        Открывает указанную клетку игрового поля.

        :param i: Индекс строки
        :param j: Индекс столбца
        :raises IndexError: Если индексы выходят за границы поля
        """
        if not (0 <= i < self.N and 0 <= j < self.M):
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        self.__pole_cells[i][j].__is_open = True

    def show_pole(self) -> None:
        """Отображает игровое поле в консоли (для отладки)."""
        for row in self.__pole_cells:
            print(" ".join('M' if cell.is_mine else str(
                cell.number) if cell.is_open else '#' for cell in row))

