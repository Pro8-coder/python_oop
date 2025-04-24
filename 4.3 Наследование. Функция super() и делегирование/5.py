"""
В программе объявлена функция integer_params для класса Vector, которая
применяет к каждому методу класса декоратор integer_params_decorated:

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls

@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


Декоратор integer_params_decorated должен проверять, чтобы все передаваемые
аргументы в методы класса (кроме первого self) были целыми числами (имели тип
int). Если это не так, то должно генерироваться исключение командой:

raise TypeError("аргументы должны быть целыми числами")
Ваша задача объявить эту функцию-декоратор.

Пример использования класса (эти строчки в программе не писать):

vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего
не нужно.
"""
from typing import Callable


def integer_params_decorated(func: Callable) -> Callable:
    """
    Декоратор для проверки целочисленности аргументов методов класса.

    Проверяет, что все аргументы (кроме self) являются целыми числами (int).
    Генерирует TypeError, если найдены аргументы других типов.

    :param func: Метод класса для декорирования
    :return: Обернутый метод с проверкой аргументов
    """
    def wrapper(self, *args, **kwargs):
        """
        Обертка метода, выполняющая проверку типов.

        :param self: Ссылка на экземпляр класса
        :param args: Позиционные аргументы
        :param kwargs: Именованные аргументы
        :raises TypeError: Если аргументы не являются целыми числами
        :return: Результат выполнения оригинального метода
        """
        if any(type(i) != int for i in args):
            raise TypeError("аргументы должны быть целыми числами")
        if any(type(i) != int for i in kwargs):
            raise TypeError("аргументы должны быть целыми числами")

        return func(self, *args, **kwargs)
    return wrapper


def integer_params(cls: type) -> type:
    """
    Классовый декоратор для применения integer_params_decorated ко всем
    методам.

    :param cls: Класс для декорирования
    :return: Класс с модифицированными методами
    """
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    """
    Класс Vector с проверкой целочисленности аргументов методов.

    :ivar __coords: Список координат вектора
    """

    def __init__(self, *args: int) -> None:
        self.__coords = list(args)

    def __getitem__(self, item: int) -> int:
        """
        Получение координаты по индексу.

        :param item: Индекс координаты
        :return: Значение координаты
        """
        return self.__coords[item]

    def __setitem__(self, key: int, value: int) -> None:
        """Установка значения координаты.

        :param key: Индекс координаты
        :param value: Новое значение координаты (должно быть целым числом)
        """
        self.__coords[key] = value

    def set_coords(self, *coords: int, reverse: bool = False) -> None:
        """
        Установка новых координат вектора.

        :param coords: Новые координаты (должны быть целыми числами)
        :param reverse: Флаг обратного порядка (по умолчанию False)
        """
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]

