"""
Необходимо объявить функцию-декоратор class_log для класса, которая бы
создавала логирование вызовов методов класса. Например следующие строчки
программы:

vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
декорируют класс Vector и в список vector_log добавляются имена методов,
которые были вызваны при использовании этого класса. В частности, после
выполнения команд:

v = Vector(1, 2, 3)
v[0] = 10
в списке vector_log должны быть два метода:

['__init__', '__setitem__']

Ваша задача реализовать декоратор с именем class_log.

Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим
образом:

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls
Используйте этот принцип для успешного прохождения подвига.

P.S. В программе нужно объявить только класс и необходимые функции. На экран
выводить ничего не нужно.
"""
from typing import Any, Callable

vector_log = []


def class_log(log_list: list) -> Callable:
    """
    Декоратор класса для логирования вызовов методов.

    Записывает имена вызываемых методов в переданный список.

    :param log_list: Список для записи имен вызванных методов
    :return: Декоратор класса
    """
    def decorate(cls: type) -> type:
        for name, method in cls.__dict__.items():
            if callable(method):
                def make_logger(m: Callable) -> Callable:
                    def logger(*args, **kwargs) -> Any:
                        log_list.append(m.__name__)
                        return m(*args, **kwargs)
                    return logger
                setattr(cls, name, make_logger(method))
        return cls
    return decorate


@class_log(vector_log)
class Vector:
    """
    Класс вектора с координатами.

    :ivar args: Координаты вектора
    """

    def __init__(self, *args: int | float) -> None:
        self.__coords = list(args)

    def __getitem__(self, item: int) -> Any:
        """
        Получение координаты по индексу.

        :param item: Индекс координаты
        :return: Значение координаты
        """
        return self.__coords[item]

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Установка значения координаты по индексу.

        :param key: Индекс координаты
        :param value: Новое значение координаты
        """
        self.__coords[key] = value

