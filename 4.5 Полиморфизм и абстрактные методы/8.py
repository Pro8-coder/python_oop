"""
Объявите класс с именем Food (еда), объекты которого создаются командой:

food = Food(name, weight, calories)
где name - название продукта (строка); weight - вес продукта (любое
положительное число); calories - калорийная ценность продукта (целое
положительное число).

Объявите следующие дочерние классы с именами:

BreadFood - хлеб;
SoupFood - суп;
FishFood - рыба.

Объекты этих классов должны создаваться командами:

bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба,
False - для остальных
sf = SoupFood(name, weight, calories, dietary) # dietary - True для
диетического супа, False - для других видов
ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь,
сардина и т.д.)
В каждом объекте этих дочерних классов должны формироваться соответствующие
локальные атрибуты с именами:

BreadFood: _name, _weight, _calories, _white
SoupFood: _name, _weight, _calories, _dietary
FishFood: _name, _weight, _calories, _fish

Пример использования классов (эти строчки в программе писать не нужно):

bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
P.S. В программе требуется объявить только классы. На экран выводить ничего
не нужно.
"""


class Food:
    """
    Базовый класс для представления пищевых продуктов.

    :ivar name: Название продукта
    :ivar weight: Вес продукта в граммах
    :ivar calories: Калорийность продукта (ккал)
    """

    def __init__(self, name: str, weight: int | float, calories: int) -> None:
        self.name = name
        self.weight = weight
        self.calories = calories


class BreadFood(Food):
    """
    Класс для представления хлебных изделий.

    :ivar _white: Признак белого хлеба
    """

    def __init__(self, name: str, weight: int | float, calories: int,
                 white: bool) -> None:
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    """
    Класс для представления супов.

    :ivar _dietary: Признак диетического супа
    """

    def __init__(self, name: str, weight: int | float, calories: int,
                 dietary: bool) -> None:
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    """
    Класс для представления рыбных продуктов.

    :ivar _fish: Вид рыбы
    """

    def __init__(self, name: str, weight: int | float, calories: int,
                 fish: str) -> None:
        super().__init__(name, weight, calories)
        self._fish = fish

