"""
Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева
величина (True/False), означающая наличие мины в текущей клетке. При этом, в
каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все
клетки закрыты (False).



С помощью класса GamePole должна быть возможность создавать квадратное игровое
поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка
представляется объектом класса Cell и все объекты хранятся в двумерном списке
N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по
игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если
клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать
метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом
мин M = 12.

P.S. На экран в программе ничего выводить не нужно.
"""

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        m = 0
        while m < self.M:
            n1 = randint(0, self.N - 1)
            n2 = randint(0, self.N - 1)
            if self.pole[n1][n2].mine:
                continue
            self.pole[n1][n2].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (
            1, 1)
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = sum(
                        (self.pole[i + x][j + y].mine for x, y in indx if
                         0 <= i + x < self.N and 0 <= j + y < self.N))

    def show(self):
        for i in self.pole:
            print(*map(
                lambda x: '#' if not x.fl_open else x.around_mines
                if not x.mine else '*', i))


pole_game = GamePole(10, 12)
