"""
Вам поручают разработать класс для представления маршрутов в навигаторе. Для
этого требуется объявить класс с именем Track, объекты которого могут
создаваться командами:

tr = Track(start_x, start_y)
tr = Track(pt1, pt2, ..., ptN)
где start_x, start_y - начальная координата маршрута (произвольные числа);
pt1, pt2, ..., ptN - набор из произвольного числа точек (координат) маршрута
(объекты класса PointTrack).

При передаче аргументов (start_x, start_y) координата должна представляться
первым объектом класса PointTrack. Наборы всех точек (объектов PointTrack)
должны сохраняться в локальном приватном атрибуте объекта класса Track:

__points - список из точек (координат) маршрута.

Далее, каждая точка (координата) должна определяться классом PointTrack,
объекты которого создаются командой:

pt = PointTrack(x, y)
где x, y - числа (целые или вещественные). Если передается другой тип данных,
то должно генерироваться исключение командой:

raise TypeError('координаты должны быть числами')
В классе PointTrack переопределите магический метод __str__, чтобы информация
об объекте класса возвращалась в виде строки:

"PointTrack: <x>, <y>"

Например:

pt = PointTrack(1, 2)
print(pt) # PointTrack: 1, 2
В самом классе Track должно быть свойство (property) с именем:

points - для получения кортежа из точек маршрута.

Также в классе Track должны быть методы:

def add_back(self, pt) - добавление новой точки в конец маршрута
(pt - объект класса PointTrack);
def add_front(self, pt) - добавление новой точки в начало маршрута
(pt - объект класса PointTrack);
def pop_back(self) - удаление последней точки из маршрута;
def pop_front(self) - удаление первой точки из маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
P.S. В программе требуется объявить только классы. На экран выводить ничего
не нужно.
"""


class PointTrack:
    """
    Класс для представления точки маршрута.

    :ivar x: Координата по оси X
    :ivar y: Координата по оси Y
    :raises TypeError: Если координаты не являются числами
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError('координаты должны быть числами')

        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Возвращает строковое представление точки.

        :return: Строка в формате "PointTrack: x, y"
        """
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    """
    Класс для представления маршрута в навигаторе.

    :ivar __points: Список точек маршрута
    """

    def __init__(self, *args: int | float | PointTrack) -> None:
        """
        Инициализирует маршрут.

        :param args: Два числа (start_x, start_y) или объекты PointTrack
        :raises TypeError: Если переданы некорректные аргументы
        """
        if (len(args) == 2 and type(args[0]) in (int, float) and
                type(args[1]) in (int, float)):
            self.__points = [PointTrack(args[0], args[1])]
        elif args and all(type(arg) is PointTrack for arg in args):
            self.__points = list(args)
        else:
            raise TypeError("Должны быть переданы ровно два числа или "
                            "только объекты PointTrack")

    @property
    def points(self) -> tuple[PointTrack, ...]:
        """
        Возвращает кортеж точек маршрута.

        :return: Неизменяемый кортеж точек
        """
        return tuple(self.__points)

    def add_back(self, pt: PointTrack) -> None:
        """
        Добавляет точку в конец маршрута.

        :param pt: Точка для добавления
        """
        self.__points.append(pt)

    def add_front(self, pt: PointTrack) -> None:
        """
        Добавляет точку в начало маршрута.

        :param pt: Точка для добавления
        """
        self.__points.insert(0, pt)

    def pop_back(self) -> None:
        """Удаляет последнюю точку маршрута."""
        del self.__points[-1]

    def pop_front(self) -> None:
        """Удаляет первую точку маршрута"""
        del self.__points[0]

