"""
Объявите в программе класс Point, объекты которого должны создаваться
командами:

pt = Point()
pt = Point(x, y)
где x, y - произвольные числа (координаты точки).

В каждом объекте класса Point должны формироваться локальные атрибуты _x, _y с
соответствующими значениями. Если аргументы не указываются (первая команда),
то _x = 0, _y = 0.

Далее, в программе вводятся два значения в одну строчку через пробел.
Значениями могут быть числа, слова, булевы величины (True/False). Необходимо
прочитать эти значения из входного потока. Если оба значения являются числами,
то формировать объект pt командой:

pt = Point(x, y)
Если хотя бы одно из значений не числовое, то формировать объект pt командой:

pt = Point()
Реализовать этот функционал с помощью блоков try/except. А в блоке finally
вывести на экран сообщение в формате (без кавычек):

"Point: x = <значение x>, y = <значение y>"

Sample Input:

10 20
Sample Output:

Point: x = 10, y = 20
"""


class Point:
    def __init__(self, x: int | float = 0, y: int | float = 0) -> None:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError("Принимает только 'x' и 'y' в виде чисел")

        self._x = x
        self._y = y

    @property
    def x(self) -> int | float:
        return self._x

    @property
    def y(self) -> int | float:
        return self._y


a, b = input().split()
try:
    pt = Point(*(int(a), int(b)) if a.isdigit() and b.isdigit() else (
        float(a), float(b)))
except ValueError:
    pt = Point()
finally:
    print(f"Point: x = {pt.x}, y = {pt.y}")
