"""
Объявите в программе класс Player (игрок), объекты которого создаются командой:

player = Player(name, old, score)
где name - имя игрока (строка); old - возраст игрока (целое число);
score - набранные очки в игре (целое число). В каждом объекте класса Player
должны создаваться аналогичные локальные атрибуты: name, old, score.

С объектами класса Player должна работать функция:

bool(player)
которая возвращает True, если число очков больше нуля, и False - в противном
случае.

С помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
считываются строки из входного потока в список строк lst_in. Каждая строка
записана в формате:

"имя; возраст; очки"

Например:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0

Каждую строку списка lst_in необходимо представить в виде объекта
класса Player с соответствующими данными. И из этих объектов сформировать
список players.

Отфильтруйте этот список (создайте новый: players_filtered), оставив всех
игроков с числом очков больше нуля. Используйте для этого стандартную
функцию filter() совместно с функцией bool() языка Python.

P.S. На экран ничего выводить не нужно.

Sample Input:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0
"""
import sys


class Player:
    """Класс, представляющий игрока.

    :ivar name: Имя игрока
    :ivar old: Возраст игрока
    :ivar score: Количество набранных очков
    """

    def __init__(self, name: str, old: int, score: int) -> None:
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self) -> bool:
        """Определяет логическое значение объекта.

        :return: True если очков больше 0, иначе False
        """
        return self.score != 0

    def __str__(self) -> str:
        """Строковое представление игрока.

        :return: Строка с информацией об игроке
        """
        return f"name: {self.name}, old: {self.old}, score: {self.score}"

    def __repr__(self) -> str:
        """Формальное строковое представление.

        :return: Строка для отладки
        """
        return self.__str__()


lst_in = list(map(str.strip, sys.stdin.readlines()))

# players = [Player(
#     line.split("; ")[0], int(line.split("; ")[1]), int(line.split("; ")[2])
# ) for line in lst_in]

# players = [Player(*map(
#     lambda j: int(j) if j.isdigit() else j, line.split("; ")
# )) for line in lst_in]

players = []
for line in lst_in:
    parts = line.split("; ")
    players.append(Player(parts[0], int(parts[1]), int(parts[2])))

players_filtered = [*filter(bool, players)]
