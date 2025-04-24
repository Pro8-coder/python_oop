"""
Создается программа по учету склада. Каждый предмет на складе должен
описываться базовым классом Thing. Объекты этого класса создаются командой:

th1 = Thing(name, weight)
где name - наименование предмета (строка); weight - вес предмета (вещественное
число).

Для описания каждого конкретного вида предметов, создаются дочерние классы
(на основе базового Thing):

ArtObject - для представления арт-объектов;
Computer - для системных блоков компьютеров;
Auto - для автомобилей.

Объекты этих классов создаются командами:

obj = ArtObject(name, weight, author, date)  # author - автор (строка); date -
дата создания (строка)
obj = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое
число); cpu - тип процессора (строка)
obj = Auto(name, weight, dims)               # dims - габариты, кортеж
(width, length, height) - вещественные или целые числа
На основе класса Auto создаются дочерние классы Mercedes и Toyota, объекты
которых определяются командами:

auto = Mercedes(name, weight, dims, model, old) # model - модель (строка);
old - время использования, в годах (целое число)
auto = Toyota(name, weight, dims, model, wheel) # model - модель (строка);
wheel - тип руля: True - леворульный, False - праворульный
Во всех объектах классов должны создаваться соответствующие локальные
атрибуты: name, weight и т.д.

Инициализация атрибутов должна выполняться в соответствующих классах
(не должно быть дублирования кода).

P.S. В программе нужно объявить только классы. На экран выводить ничего
не нужно.
"""


class Thing:
    """
    Базовый класс для предметов на складе.

    :ivar name: Наименование предмета
    :ivar weight: Вес предмета
    """

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    """
    Класс для арт-объектов.

    :ivar author: Автор произведения
    :ivar date: Дата создания
    """

    def __init__(self, name: str, weight: float, author: str, date: str
                 ) -> None:
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    """
    Класс для системных блоков компьютеров.

    :ivar memory: Объем памяти (ГБ)
    :ivar cpu: Модель процессора
    """

    def __init__(self, name: str, weight: float, memory: int, cpu: str
                 ) -> None:
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    """
    Базовый класс для автомобилей.

    :ivar dims: Габариты (ширина, длина, высота)
    """

    def __init__(self, name: str, weight: float,
                 dims: tuple[int | float, int | float, int | float]) -> None:
        super().__init__(name, weight)
        self.weight = weight
        self.dims = dims


class Mercedes(Auto):
    """
    Класс для автомобилей Mercedes.

    :ivar model: Модель автомобиля
    :ivar old: Срок эксплуатации (в годах)
    """

    def __init__(self, name: str, weight: float,
                 dims: tuple[int | float, int | float, int | float],
                 model: str, old: int) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    """
    Класс для автомобилей Toyota.

    :ivar model: Модель автомобиля
    :ivar wheel: Тип руля (True - леворульный, False - праворульный)
    """

    def __init__(self, name: str, weight: float,
                 dims: tuple[int | float, int | float, int | float],
                 model: str, wheel: bool) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

