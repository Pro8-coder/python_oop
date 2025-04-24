"""
С помощью декоратора dataclass:

from dataclasses import dataclass
объявите класс с именем House со следующим набором полей (порядок важен):

addr (строка: адрес дома);
size (float: площадь дома);
floors (int: число этажей, начальное значение 1);
rooms (int: число комнат, начальное значение 3).
Объявите в классе House метод __eq__, который бы выполнял сравнение объектов
этого класса по атрибутам floors и rooms (сравнение на равенство).

Создайте два объекта с именами h1, h2 класса House и данными:

h1: "Москва, ул. Тверская, д. 5"; size: 102.5; floors: 3; rooms: 7;
h2: "Москва, ул. Воздвиженка, д. 11"; size: 82.3; floors: 2; rooms: 6.
P.S. На экран ничего выводить не нужно.
"""
from dataclasses import dataclass


@dataclass
class House:
    addr: str
    size: float
    floors: int = 1
    rooms: int = 3

    def __eq__(self, other: 'House') -> bool:
        return (self.floors, self.rooms) == (other.floors, other.rooms)


h1 = House("Москва, ул. Тверская, д. 5", 102.5, 3, 7)
h2 = House("Москва, ул. Воздвиженка, д. 11", 82.3, 2, 6)
