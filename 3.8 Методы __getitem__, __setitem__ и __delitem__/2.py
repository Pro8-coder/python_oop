"""
Вам необходимо для навигатора реализовать определение маршрутов. Для этого в
программе нужно объявить класс Track, объекты которого создаются командой:

tr = Track(start_x, start_y)
где start_x, start_y - координата начала пути.

В этом классе должен быть реализован следующий метод:

add_point(x, y, speed) - добавление новой точки маршрута (линейный сегмент),
который можно пройти со средней скоростью speed.

Также с объектами класса Track должны выполняться команды:

coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и
скорости (число) для линейного сегмента маршрута с индексом indx
tr[indx] = speed # изменение средней скорости линейного участка маршрута
по индексу indx
Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1,
где N - число линейных сегментов в маршруте), то генерируется исключение
командой:

raise IndexError('некорректный индекс')
Пример использования класса (эти строчки в программе не писать):

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего
не нужно.
"""
from typing import TypeVar

T = TypeVar('T', int, float)


class Track:
    """
    Класс для представления маршрута с точками и скоростями перемещения.

    :ivar start_x: Начальная координата X
    :ivar start_y: Начальная координата Y
    :ivar track_point: Словарь точек маршрута с координатами и скоростями
    :vartype track_point: dict[tuple[T, T], T]
    """

    def __init__(self, start_x: T, start_y: T) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.track_point: dict[tuple[T, T], T] = {}

    def add_point(self, x: T, y: T, speed: T) -> None:
        """
        Добавляет новую точку в маршрут.

        :param x: Координата X точки
        :param y: Координата Y точки
        :param speed: Скорость перемещения до этой точки
        """
        self.track_point[(x, y)] = speed

    def __getitem__(self, item: int) -> tuple[tuple[T, T], T]:
        """
        Возвращает координаты и скорость по индексу точки.

        :param item: Индекс точки в маршруте
        :return: Кортеж ((координата X, координата Y), скорость)
        :rtype: Tuple[Tuple[T, T], T]
        :raises IndexError: Если индекс некорректен
        """
        if type(item) == int and 0 <= item < len(self.track_point):
            return list(self.track_point.items())[item]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key: int, value: T) -> None:
        """
        Устанавливает новую скорость для точки по индексу.

        :param key: Индекс точки в маршруте
        :param value: Новая скорость
        :raises IndexError: Если индекс некорректен
        """
        if type(key) == int and 0 <= key < len(self.track_point):
            self.track_point[list(self.track_point.keys())[key]] = value
        else:
            raise IndexError('некорректный индекс')

