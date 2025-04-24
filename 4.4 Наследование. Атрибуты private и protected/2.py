"""
Объявите класс Furniture (мебель), объекты которого создаются командой:

f = Furniture(name, weight)
где name - название предмета (строка); weight - вес предмета (целое или
вещественное число).

В каждом объекте класса Furniture должны создаваться защищенные локальные
атрибуты с именами _name и _weight. В самом классе Furniture нужно объявить
приватные методы:

__verify_name() - для проверки корректности имени;
__verify_weight() - для проверки корректности веса.

Метод __verify_name() проверяет, что имя должно быть строкой, если это не так,
то генерируется исключение командой:

raise TypeError('название должно быть строкой')
Метод __verify_weight() проверяет, что вес должен быть положительным числом
(строго больше нуля), если это не так, то генерируется исключение командой:

raise TypeError('вес должен быть положительным числом')
Данные методы следует вызывать всякий раз при записи новых значений в атрибуты
_name и _weight (а также при их создании).

На основе базового класса Furniture объявить следующие дочерние классы:

Closet - для представления шкафов;
Chair - для представления стульев;
Table - для представления столов.

Объекты этих классов должны создаваться командами:

obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе;
False - обычный шкаф; doors - число дверей (целое число)
obj = Chair(name, weight, height)       # height - высота стула
(любое положительное число)
obj = Table(name, weight, height, square) # height - высота стола;
square - площадь поверхности (любые положительные числа)
В каждом объекте этих классов должны создаваться соответствующие защищенные
атрибуты:

- в объектах класса Closet: _name, _weight, _tp, _doors
- в объектах класса Chair: _name, _weight, _height
- в объектах класса Table: _name, _weight, _height, _square

В каждом классе (Closet, Chair, Table) объявить метод:

get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов
этих классов.

Пример использования классов (эти строчки в программе писать не нужно):

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
P.S. В программе нужно объявить только классы. На экран выводить ничего
не нужно.
"""


class Furniture:
    """
    Базовый класс для представления мебели.

    Содержит основные атрибуты и методы проверки для всех видов мебели.

    :ivar name: Название предмета мебели
    :ivar weight: Вес предмета (положительное число)
    :raises TypeError: Если название не строка или вес не положительное число
    """

    def __init__(self, name: str, weight: int | float) -> None:
        self._name = name
        self._weight = weight
        self.__verify_name()
        self.__verify_weight()

    def __verify_name(self) -> None:
        """
        Проверяет, что название является строкой.

        :raises TypeError: Если название не является строкой
        """
        if type(self._name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self) -> None:
        """
        Проверяет, что вес является положительным числом.

        :raises TypeError: Если вес не число или не положительный
        """
        if type(self._weight) not in (int, float) or self._weight <= 0:
            raise TypeError('вес должен быть положительным числом')


class Closet(Furniture):
    """
    Класс для представления шкафов.

    :ivar tp: Тип шкафа (True - шкаф-купе, False - обычный)
    :ivar doors: Количество дверей
    """

    def __init__(self, name: str, weight: int | float, tp: bool, doors: int
                 ) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self) -> tuple[str | int | float | bool, ...]:
        """
        Возвращает кортеж атрибутов шкафа.

        :return: Кортеж (name, weight, tp, doors)
        """
        return self._name, self._weight, self._tp, self._doors


class Chair(Furniture):
    """
    Класс для представления стульев.

    :ivar height: Высота стула (положительное число)
    """

    def __init__(self, name: str, weight: int | float, height: int | float
                 ) -> None:
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self) -> tuple[str | int | float, ...]:
        """
        Возвращает кортеж атрибутов стула.

        :return: Кортеж (name, weight, height)
        """
        return self._name, self._weight, self._height


class Table(Furniture):
    """
    Класс для представления столов.

    :ivar height: Высота стола (положительное число)
    :ivar square: Площадь поверхности (положительное число)
    """

    def __init__(self, name: str, weight: int | float, height: int | float,
                 square: int | float) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self) -> tuple[str | int | float, ...]:
        """
        Возвращает кортеж атрибутов стола.

        :return: Кортеж (name, weight, height, square)
        """
        return self._name, self._weight, self._height, self._square

