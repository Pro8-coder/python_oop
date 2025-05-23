"""
С помощью декоратора dataclass и функции field:

from dataclasses import dataclass, field
объявите Data Class с именем Velocity и следующим набором полей
(порядок важен):

model (str: с исключением из операций сравнения);
speed (float: с исключением из параметров инициализатора и начальным
значением 0);
weight (float: вес);
dims (tuple: с исключением из операций сравнения и метода __repr__
и начальным значением None).
Создайте два объекта с именами vl1, vl2 класса Velocity с данными:

vl1: model="car"; weight=5.4; dims=(100, 20, 30);
vl2: model="ship"; weight=5.4; dims=(500, 200, 130).
Выполните сравнение на равенство этих двух объектов. Результат
(булево значение) сохраните в переменной res.

P.S. На экран ничего выводить не нужно.
"""
from dataclasses import dataclass, field


@dataclass
class Velocity:
    model: str = field(compare=False)
    speed: float = field(init=False, default=0)
    weight: float
    dims: tuple = field(compare=False, repr=False, default=None)


vl1 = Velocity("car", 5.4, (100, 20, 30))
vl2 = Velocity("ship", 5.4, (500, 200, 130))

res = vl1 == vl2
