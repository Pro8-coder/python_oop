"""
Объявите класс с именем Rect (прямоугольник), объекты которого создаются
командой:

r = Rect(x, y, width, height)
где x, y - координаты верхнего левого угла (любые числа); width, height -
ширина и высота прямоугольника (положительные числа). Ось абсцисс (Ox)
направлена вправо, ось ординат (Oy) направлена вниз.

В каждом объекте класса Rect должны формироваться локальные атрибуты
с именами: _x, _y, _width, _height и соответствующими значениями. Если
переданные аргументы x, y (не числа) и width, height не положительные числа,
то генерировать исключение командой:

raise ValueError('некорректные координаты и параметры прямоугольника')
В классе Rect реализовать метод:

def is_collision(self, rect): ...

который проверяет пересечение текущего прямоугольника с другим
(с объектом rect). Если прямоугольники пересекаются, то должно генерироваться
исключение командой:

raise TypeError('прямоугольники пересекаются')
Сформировать в программе несколько объектов класса Rect со следующими
значениями:

0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1

Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще
один список lst_not_collision, в котором должны быть объекты rect
не пересекающиеся ни с какими другими объектами в списке lst_rect.

P.S. В программе требуется объявить только класс и списки. На экран выводить
ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны
параллельны осям координат (как в этом подвиге) достаточно проверить,
что верхняя грань первого прямоугольника находится ниже нижней грани второго,
или нижняя грань первого прямоугольника выше верхней грани второго.
И то же самое для вертикальных граней.
"""


class Rect:
    def _check_num_value(self, value: int | float) -> None:
        if type(value) not in (int, float):
            raise ValueError(
                'некорректные координаты и параметры прямоугольника')

    def _check_positive_value(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError(
                'некорректные координаты и параметры прямоугольника')

    def __init__(self, x: int | float, y: int | float,
                 width: int | float, height: int | float) -> None:
        for item in [x, y, width, height]:
            self._check_num_value(item)
        for item in [width, height]:
            self._check_positive_value(item)

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect: 'Rect') -> None:
        if not (self._x + self._width <= rect._x or
                rect._x + rect._width <= self._x or
                self._y + self._height <= rect._y or
                rect._y + rect._height <= self._y):
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3),
            Rect(6, 0, 3, 5),
            Rect(3, 2, 4, 4),
            Rect(0, 8, 8, 1)]

lst_not_collision = []
for i, rect in enumerate(lst_rect):
    try:
        for j in range(len(lst_rect)):
            if i != j:
                rect.is_collision(lst_rect[j])
    except TypeError:
        continue
    else:
        lst_not_collision.append(rect)
