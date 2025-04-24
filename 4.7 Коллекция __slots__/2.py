"""
Объявите класс Planet (планета), объекты которого создаются командой:

p = Planet(name, diametr, period_solar, period)
где name - наименование планеты; diametr - диаметр планеты (любое
положительное число); period_solar - период (время) обращения планеты вокруг
Солнца (любое положительное число); period - период обращения планеты вокруг
своей оси (любое положительное число).

В каждом объекте класса Planet должны формироваться локальные атрибуты с
именами: _name, _diametr, _period_solar, _period и соответствующими значениями.

Затем, объявите класс с именем SolarSystem (солнечная система). В объектах
этого класса должны быть допустимы, следующие локальные атрибуты (ограничение
задается через коллекцию __slots__):

_mercury - ссылка на планету Меркурий (объект класса Planet);
_venus - ссылка на планету Венера (объект класса Planet);
_earth - ссылка на планету Земля (объект класса Planet);
_mars - ссылка на планету Марс (объект класса Planet);
_jupiter - ссылка на планету Юпитер (объект класса Planet);
_saturn - ссылка на планету Сатурн (объект класса Planet);
_uranus - ссылка на планету Уран (объект класса Planet);
_neptune - ссылка на планету Нептун (объект класса Planet).

Объект класса SolarSystem должен создаваться командой:

s_system = SolarSystem()
и быть только один (одновременно в программе два и более объектов класса
SolarSystem недопустимо). Используйте для этого паттерн Singleton.

В момент создания объекта SolarSystem должны автоматически создаваться
перечисленные локальные атрибуты и ссылаться на соответствующие объекты класса
Planet со следующими данными по планетам:

Создайте в программе объект s_system класса SolarSystem.

P.S. В программе следует объявить только классы и создать объект s_system.
На экран выводить ничего не нужно.
"""


class Planet:
    """
    Класс для представления планеты.

    :ivar name: Название планеты
    :ivar diametr: Диаметр планеты (положительное число)
    :ivar period_solar: Период обращения вокруг Солнца (положительное число)
    :ivar period: Период вращения вокруг оси (положительное число)
    """

    def __init__(self, name: str, diametr: int | float,
                 period_solar: int | float, period: int | float) -> None:
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    """
    Класс-одиночка (Singleton), представляющий Солнечную систему.

    Обеспечивает единственный экземпляр, содержащий планеты солнечной системы
    в виде атрибутов. Доступные планеты:

    :ivar _mercury: Планета Меркурий
    :ivar _venus: Планета Венера
    :ivar _earth: Планета Земля
    :ivar _mars: Планета Марс
    :ivar _jupiter: Планета Юпитер
    :ivar _saturn: Планета Сатурн
    :ivar _uranus: Планета Уран
    :ivar _neptune: Планета Нептун
    """

    __instance = None
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter',
                 '_saturn', '_uranus', '_neptune')

    def __new__(cls) -> 'SolarSystem':
        """Реализация паттерна Singleton для создания единственного экземпляра.

        При первом вызове создает экземпляр класса и инициализирует все
        планеты. При последующих вызовах возвращает существующий экземпляр.

        :return: Единственный экземпляр SolarSystem
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
            cls.__instance._venus = Planet('Венера', 12104, 224.7, 5832.45)
            cls.__instance._earth = Planet('Земля', 12756, 365.3, 23.93)
            cls.__instance._mars = Planet('Марс', 6794, 687, 24.62)
            cls.__instance._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
            cls.__instance._saturn = Planet('Сатурн', 120660, 10753, 10.63)
            cls.__instance._uranus = Planet('Уран', 51118, 30665, 17.2)
            cls.__instance._neptune = Planet('Нептун', 49528, 60150, 16.1)

        return cls.__instance

    def __del__(self) -> None:
        """Сбрасываем Singleton при удалении объекта."""
        SolarSystem.__instance = None


s_system = SolarSystem()
