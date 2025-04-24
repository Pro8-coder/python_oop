"""
Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и
решило дать вам испытание для подтверждения уровня полученных навыков. Вам
выпала великая честь создать полноценную программу игры в "Крестики-нолики".
И вот перед вами текст с заданием самого испытания.

Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления
игровым процессом. Объекты этого класса будут создаваться командой:

game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 -
стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False -
в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон
[0; 2]), то следует генерировать исключение командой:

raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 -
крестики и 2 - нолики, в классе TicTacToe должны быть три публичных атрибута
(атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо
действия);
show() - отображение текущего состояния игрового поля (как именно - на свое
усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и
ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик
в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть
свободные клетки) и False - в противном случае.

Все эти функции и свойства предполагается использовать следующим образом
(эти строчки в программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
Вам в программе необходимо объявить только два класса: TicTacToe и Cell так,
чтобы с их помощью можно было бы сыграть в "Крестики-нолики" между человеком и
компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить
классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера
хотя бы один раз.
"""
from random import choice


class Cell:
    """
    Класс клетки игрового поля.

    :ivar value: Текущее значение клетки (0 - свободна, 1 - крестик, 2 - нолик)
    """

    def __init__(self) -> None:
        self.value = 0

    def __bool__(self) -> bool:
        """
        Возвращает True, если клетка свободна.

        :return: Состояние клетки
        """
        return self.value == 0


class TicTacToe:
    """
    Класс игры в крестики-нолики.

    :cvar FREE_CELL: Значение свободной клетки
    :cvar HUMAN_X: Значение клетки с крестиком (игрок)
    :cvar COMPUTER_O: Значение клетки с ноликом (компьютер)
    :ivar _size_pole: Размер игрового поля
    :ivar _win: Текущий статус игры (0 - игра продолжается, 1 - победа игрока,
    2 - победа компьютера, 3 - ничья)
    :ivar pole: Игровое поле (кортеж кортежей клеток)
    """

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self) -> None:
        self._size_pole = 3
        self._win = 0
        self.pole: tuple[tuple[Cell, ...], ...] = tuple(tuple(
            Cell() for _ in range(self._size_pole)
        ) for _ in range(self._size_pole))

    def __check_index(self, index: tuple[int, int]) -> None:
        """
        Проверяет корректность индексов.

        :param index: Кортеж с индексами (строка, столбец)
        :raises IndexError: Если индексы некорректны
        """
        if type(index) == tuple and len(index) == 2:
            row, col = index
            if type(row) != int or not 0 <= row < self._size_pole:
                raise IndexError('некорректно указанные индексы')
            if type(col) != int or not 0 <= col < self._size_pole:
                raise IndexError('некорректно указанные индексы')
        else:
            raise IndexError('некорректно указанные индексы')

    def __check_cell(self, index: tuple[int, int]) -> None:
        """
        Проверяет, свободна ли клетка.

        :param index: Кортеж с индексами (строка, столбец)
        :raises ValueError: Если клетка уже занята
        """
        if self.pole[index[0]][index[1]].value != 0:
            raise ValueError("клетка уже занята")

    def __check_win(self, gamer: int) -> None:
        """
        Проверяет условия победы.

        :param gamer: Игрок для проверки (HUMAN_X или COMPUTER_O)
        """
        for i in range(self._size_pole):
            if all(self.pole[i][j].value == gamer for j in range(
                    self._size_pole)):
                self._win = gamer
                return
            if all(self.pole[j][i].value == gamer for j in range(
                    self._size_pole)):
                self._win = gamer
                return

        if all(self.pole[i][i].value == gamer for i in range(self._size_pole)):
            self._win = gamer
            return

        if all(self.pole[i][-1-i].value == gamer for i in range(
                self._size_pole)):
            self._win = gamer
            return

        if all(cell.value != self.FREE_CELL for row in self.pole
               for cell in row):
            self._win = 3

    def __getitem__(self, index: tuple[int, int]) -> int:
        """
        Возвращает значение клетки по индексу.

        :param index: Кортеж с индексами (строка, столбец)
        :return: Значение клетки
        """
        self.__check_index(index)
        return self.pole[index[0]][index[1]].value

    def __setitem__(self, index: tuple[int, int], value: int) -> None:
        """
        Устанавливает значение клетки по индексу.

        :param index: Кортеж с индексами (строка, столбец)
        :param value: Значение для установки
        """
        self.__check_index(index)
        self.__check_cell(index)
        self.pole[index[0]][index[1]].value = value
        self.__check_win(value)

    def __bool__(self) -> bool:
        """
        Проверяет, продолжается ли игра.

        :return: True если игра продолжается
        """
        return self._win == 0

    def init(self) -> None:
        """Сбрасывает игру в начальное состояние."""
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

        self._win = 0

    def show(self) -> None:
        """Выводит текущее состояние поля в консоль."""
        for row in self.pole:
            print("|", end="")
            for cell in row:
                if cell.value == self.HUMAN_X:
                    print("x|", end="")
                elif cell.value == self.COMPUTER_O:
                    print("O|", end="")
                else:
                    print(" |", end="")
            print()
        print()

    def human_go(self) -> None:
        """Обрабатывает ход человека."""
        while True:
            try:
                index = tuple(map(int, input(
                    "Введите координаты клетки (строка столбец): ").split()))
                self[index] = self.HUMAN_X
                break
            except (IndexError, ValueError) as e:
                print(f"Ошибка: '{e}'. Попробуйте еще раз.")

    def computer_go(self) -> None:
        """Обрабатывает ход компьютера."""
        free_cells = [(i, j) for i in range(self._size_pole) for j in range(
            self._size_pole) if self.pole[i][j].value == 0]
        if free_cells:
            index = choice(free_cells)
            self[index] = self.COMPUTER_O

    @property
    def is_human_win(self) -> bool:
        """
        Проверяет победу человека.

        :return: True если игрок победил
        """
        return self._win == 1

    @property
    def is_computer_win(self) -> bool:
        """
        Проверяет победу компьютера.

        :return: True если компьютер победил
        """
        return self._win == 2

    @property
    def is_draw(self) -> bool:
        """
        Проверяет ничью.

        :return: True если ничья
        """
        return self._win == 3


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
