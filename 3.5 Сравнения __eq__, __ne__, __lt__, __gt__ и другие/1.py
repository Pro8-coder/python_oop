"""
Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные
числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты
которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные
числа); max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены
следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции
сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2
И функция:

n = len(track) # возвращает целочисленную длину маршрута (привести к типу int)
для объекта track
Создайте два маршрута track1 и track2 с координатами:

1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

Сравните их между собой на равенство. Результат сравнения сохраните в
переменной res_eq.

P.S. На экран в программе ничего выводить не нужно.
"""


class TrackLine:
    """
    Класс, представляющий линейный сегмент маршрута.

    :ivar to_x: Координата x следующей точки маршрута.
    :ivar to_y: Координата y следующей точки маршрута.
    :ivar max_speed: Максимальная скорость на данном участке.
    """

    def __init__(self, to_x: int | float, to_y: int | float, max_speed: int
                 ) -> None:
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    """
    Класс, представляющий маршрут.

    :ivar start_x: Координата x начальной точки маршрута.
    :ivar start_y: Координата y начальной точки маршрута.
    :ivar track_list: Список точек на маршруте (TrackLine).
    """

    def __init__(self, start_x: int | float, start_y: int | float) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.track_list: list[TrackLine] = []

    def get_tracks(self) -> tuple[TrackLine, ...]:
        """
        Возвращает кортеж из объектов класса TrackLine.

        :return: Кортеж сегментов маршрута.
        """
        return tuple(self.track_list)

    def add_track(self, tr: TrackLine):
        """
        Добавляет линейный сегмент маршрута.

        :param tr: Объект класса TrackLine, представляющий сегмент маршрута.
        """
        self.track_list.append(tr)

    def __len__(self) -> int:
        """
        Возвращает целочисленную длину маршрута.

        :return: Длина маршрута.
        """
        total_length = 0
        if self.track_list:
            prev_x, prev_y = self.start_x, self.start_y
            for track in self.track_list:
                total_length += ((track.to_x - prev_x) ** 2 + (
                        track.to_y - prev_y) ** 2) ** 0.5
                prev_x, prev_y = track.to_x, track.to_y

        return int(total_length)

    def __eq__(self, other: 'Track') -> bool:
        """
        Сравнивает два маршрута на равенство по длине.

        :param other: Другой объект класса Track.
        :return: True, если длины маршрутов равны, иначе False.
        """
        return len(self) == len(other)

    def __lt__(self, other: 'Track') -> bool:
        """
        Сравнивает два маршрута по длине.

        :param other: Другой объект класса Track.
        :return: True, если длина текущего маршрута меньше длины другого,
        иначе False.
        """
        return len(self) < len(other)


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
