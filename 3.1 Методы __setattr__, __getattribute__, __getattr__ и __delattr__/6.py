"""
Объявите класс Circle (окружность), объекты которого должны создаваться
командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности;
radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные
атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить
объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно
проверять, что присваиваемые значения - числа (целые или вещественные).
Дополнительно у радиуса проверять, что число должно быть положительным (строго
больше нуля). Сделать все эти проверки нужно через магические методы. При
некорректных переданных числовых значениях, прежние значения меняться не
должны (исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать
булево значение False.

Пример использования класса (эти строчки в программе писать не нужно):

circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный
радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
P.S. На экран ничего выводить не нужно.
"""


class Circle:
    """
    Класс для представления окружности.

    :ivar x: Координата x центра окружности.
    :ivar y: Координата y центра окружности.
    :ivar radius: Радиус окружности (положительное число).
    """

    def __init__(self, x: int | float, y: int | float,
                 radius: int | float) -> None:
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self) -> int | float:
        """
        Возвращает координату x центра окружности.

        :return: Координата x.
        """
        return self.__x

    @x.setter
    def x(self, new_x: int | float):
        """
        Устанавливает координату x центра окружности.

        :param new_x: Новая координата x.
        """
        self.__x = new_x

    @property
    def y(self) -> int | float:
        """
        Возвращает новую координату y центра окружности.

        :return: Координата y.
        """
        return self.__y

    @y.setter
    def y(self, new_y: int | float):
        """
        Устанавливает новую координату y центра окружности.

        :param new_y: Новая координата y.
        """
        self.__y = new_y

    @property
    def radius(self) -> int | float:
        """
        Возвращает радиус окружности.

        :return: Радиус окружности.
        """
        return self.__radius

    @radius.setter
    def radius(self, new_radius: int | float):
        """
        Устанавливает новый радиус окружности (больше 0).

        :param new_radius: Новый радиус окружности.
        """
        if new_radius > 0:
            self.__radius = new_radius

    def __setattr__(self, key: str, value: int | float) -> None:
        """
        Устанавливает значение атрибута с проверкой типа.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        :raises TypeError: Если значение не является числом.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")

        super().__setattr__(key, value)

    def __getattr__(self, item) -> bool:
        """
        Возвращает False при обращении к несуществующему атрибуту.

        :param item: Имя атрибута.
        :return: Всегда возвращает False.
        """
        return False

