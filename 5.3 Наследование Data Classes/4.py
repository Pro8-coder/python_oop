"""
В программе ниже объявлен класс GlobalGraphData следующим образом:

class GlobalGraphData:
    colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'gray']

    @staticmethod
    def get_color():
        return GlobalGraphData.colors[random.randint(0,
        len(GlobalGraphData.colors)-1)]
Необходимо продолжить эту программу и объявить дата-класс Graph, используя
декоратор dataclass, со следующим набором полей (порядок важен):

width (float: с исключением из параметров инициализатора и операций сравнения;
начальное значение 0.5);
color (Any: начальное значение генерируется методом get_color класса
GlobalGraphData; с исключением из параметров инициализатора и операций
сравнения).
Следом объявите еще один дата-класс Rect на базе класса Graph, используя
декоратор dataclass, со следующим набором полей (порядок важен):

sp (tuple: координата верхнего левого угла прямоугольника);
ep (tuple: координата нижнего правого угла прямоугольника).
В классе Rect объявите метод draw, который должен возвращать строку формата
(без кавычек):

"Rect: (x0, y0); (x1, y1)"

где (x0, y0) - координаты верхнего левого угла прямоугольника (значения
берутся из поля sp); (x1, y1) - координаты нижнего правого угла прямоугольника
(значения берутся из поля ep).

Создайте объект rect класса Rect с координатами:

sp: (1, 2);
ep: (10, 20).
P.S. На экран ничего выводить не нужно.
"""
import random
from dataclasses import dataclass, field
from typing import Any


class GlobalGraphData:
    colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'gray']

    @staticmethod
    def get_color():
        return GlobalGraphData.colors[random.randint(
            0, len(GlobalGraphData.colors)-1)]


@dataclass
class Graph:
    width: float = field(init=False, compare=False, default=0.5)
    color: Any = field(init=False, compare=False,
                       default_factory=GlobalGraphData.get_color)


@dataclass
class Rect(Graph):
    sp: tuple
    ep: tuple

    def draw(self) -> str:
        return f"Rect: {self.sp}; {self.ep}"


rect = Rect((1, 2), (10, 20))
