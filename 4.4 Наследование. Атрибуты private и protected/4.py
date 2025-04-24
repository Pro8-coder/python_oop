"""
Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:

air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка); mass - подъемная масса самолета (любое
положительное число); speed - максимальная скорость (любое положительное
число); top - максимальная высота полета (любое положительное число).

В каждом объекте класса Aircraft должны создаваться локальные атрибуты с
именами: _model, _mass, _speed, _top и соответствующими значениями. Если
передаваемые аргументы не соответствуют указанным критериям (строка, любое
положительное число), то генерируется исключение командой:

raise TypeError('неверный тип аргумента')
Далее, в программе объявите следующие дочерние классы:

PassengerAircraft - пассажирский самолет;
WarPlane - военный самолет.

Объекты этих классов создаются командами:

pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число
пассажирских мест (целое положительное число)
wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение
(словарь); ключи - название оружия, значение - количество
В каждом объекте классов PassengerAircraft и WarPlane должны формироваться
локальные атрибуты с именами _chairs и _weapons соответственно. Инициализация
остальных атрибутов должна выполняться через инициализатор базового класса.

В инициализаторах классов PassengerAircraft и WarPlane проверять корректность
передаваемых аргументов chairs и weapons. Если тип данных не совпадает,
то генерировать исключение командой:

raise TypeError('неверный тип аргумента')
Создайте в программе четыре объекта самолетов со следующими данными:

PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}

Все эти объекты представить в виде списка planes.

P.S. В программе нужно объявить только классы и сформировать список На экран
выводить ничего не нужно.
"""


class Aircraft:
    """
    Базовый класс для представления самолета.

    :ivar model: Модель самолета (строка)
    :ivar mass: Подъемная масса самолета (положительное число)
    :ivar speed: Максимальная скорость (положительное число)
    :ivar top: Максимальная высота полета (положительное число)
    :raises TypeError: Если тип аргументов не соответствует требованиям
    """

    def _check_int_float(self, value: int | float):
        """
        Проверяет, что значение является положительным числом.

        :param value: Проверяемое значение
        :raises TypeError: Если значение не является положительным числом
        """
        if type(value) not in (int, float) or value <= 0:
            raise TypeError('неверный тип аргумента')

    def __init__(self, model: str, mass: int | float, speed: int | float,
                 top: int | float) -> None:
        if type(model) != str:
            raise TypeError('неверный тип аргумента')

        self._check_int_float(mass)
        self._check_int_float(speed)
        self._check_int_float(top)

        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    """
    Класс пассажирского самолета.

    :ivar chairs: Количество пассажирских мест (целое положительное число)
    :raises TypeError: Если тип аргументов не соответствует требованиям
    """

    def __init__(self, model: str, mass: int | float, speed: int | float,
                 top: int | float, chairs: int) -> None:
        if type(chairs) != int or chairs <= 0:
            raise TypeError('неверный тип аргумента')

        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    """
    Класс военного самолета.

    :ivar weapons: Вооружение (словарь: название оружия -> количество)
    :raises TypeError: Если тип аргументов не соответствует требованиям
    """

    def __init__(self, model: str, mass: int | float, speed: int | float,
                 top: int | float, weapons: dict[str, int]) -> None:
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')

        super().__init__(model, mass, speed, top)
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
