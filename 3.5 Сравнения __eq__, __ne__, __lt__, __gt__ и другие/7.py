"""
Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или
целочисленное); volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""


class Body:
    """
    Класс для представления физического тела.

    :ivar name: Название тела.
    :ivar ro: Плотность тела (вещественное или целое число).
    :ivar volume: Объем тела (вещественное или целое число).
    """

    def __init__(self, name: str, ro: int | float, volume: int | float
                 ) -> None:
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other: int | float | 'Body') -> bool:
        """
        Сравнивает массу тела с другим телом или числом.

        :param other: Другое тело или число.
        :return: True, если массы равны, иначе False.
        """
        if isinstance(other, Body):
            return self.ro * self.volume == other.ro * other.volume
        elif type(other) in (int, float):
            return self.ro * self.volume == other

    def __lt__(self, other: int | float | 'Body') -> bool:
        """
        Сравнивает массу тела с другим телом или числом.

        :param other: Другое тело или число.
        :return: True, если масса текущего тела меньше, иначе False.
        """
        if isinstance(other, Body):
            return self.ro * self.volume < other.ro * other.volume
        elif type(other) in (int, float):
            return self.ro * self.volume < other

