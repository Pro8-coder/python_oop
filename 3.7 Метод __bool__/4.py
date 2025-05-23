"""
Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)
где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты
(числа) нижнего правого угла. Первая команда создает объект класса Ellipse
без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с
локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал
True, если все локальные атрибуты x1, y1, x2, y2 существуют и
False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2),
то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')
Сформируйте в программе список с именем lst_geom, содержащий четыре объекта
класса Ellipse. Два объекта должны быть созданы командой

Ellipse()
и еще два - командой:

Ellipse(x1, y1, x2, y2)
Переберите список в цикле и вызовите метод get_coords() только для объектов,
имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен
магический метод __bool__()).

P.S. На экран ничего выводить не нужно.
"""
from typing import TypeVar

T = TypeVar('T', int, float)


class Ellipse:
    """Класс для представления эллипса через координаты ограничивающего
    прямоугольника.

    Эллипс может быть создан:
    - без координат: Ellipse()
    - с координатами: Ellipse(x1, y1, x2, y2)
    где (x1, y1) - левый верхний угол, (x2, y2) - правый нижний угол.
    """

    def __init__(self, *args: T) -> None:
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self) -> bool:
        """Определяет логическое значение эллипса.

        :return: True если все координаты существуют, иначе False
        """
        return hasattr(self, 'x1')

    def get_coords(self) -> tuple[T, T, T, T]:
        """Возвращает координаты эллипса.

        :return: Кортеж координат (x1, y1, x2, y2)
        :raises AttributeError: Если координаты отсутствуют
        """
        if not self:
            raise AttributeError('нет координат для извлечения')

        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(4, 3, 2, 1)]

for el in lst_geom:
    if el:
        el.get_coords()
