"""
Известно, что с объектами класса tuple можно складывать только такие же
объекты (кортежи). Например:

t1 = (1, 2, 3)
t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
Если же мы попытаемся прибавить любой другой итерируемый объект, например,
список:

t2 = t1 + [4, 5]
то возникнет ошибка. Предлагается поправить этот функционал и создать свой
собственный класс Tuple, унаследованный от базового класса tuple и
поддерживающий оператор:

t1 = Tuple(iter_obj)
t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым
(соединенным) набором данных
где iter_obj - любой итерируемый объект (список, словарь, строка, множество,
кортеж и т.п.)

Пример использования класса (эти строчки в программе не писать):

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
P.S. В программе нужно объявить только класс. На экран выводить ничего
не нужно.
"""
from typing import Iterable


class Tuple(tuple):
    """
    Создает новый кортеж из итерируемого объекта.

    :param iterable: Итерируемый объект для преобразования (по умолчанию None)
    :return: Новый экземпляр Tuple

    Особенности:
    - Для словарей использует пары (key, value)
    - Для None создает пустой кортеж
    - Для не итерируемых объектов TypeError (кроме None)
    """

    def __new__(cls, iterable: Iterable | None = None) -> 'Tuple':
        """
        Создает новый кортеж из итерируемого объекта.

        :param iterable: Итерируемый объект для преобразования (по умолчанию
        None)
        :return: Новый экземпляр Tuple
        :raises TypeError: Если передан не итерируемый объект (кроме None)
        """
        if iterable is None:
            return super().__new__(cls, ())

        if not hasattr(iterable, '__iter__'):
            raise TypeError(
                f"Ожидается итерируемый объект, получен {type(iterable)}")

        if type(iterable) == dict:
            return super().__new__(cls, iterable.items())

        return super().__new__(cls, iterable or ())

    def __add__(self, other: Iterable) -> 'Tuple':
        """
        Сложение с итерируемым объектом.

        :param other: Итерируемый объект для сложения
        :return: Новый кортеж с объединенными элементами
        :raises TypeError: Если other не является итерируемым
        """
        if not hasattr(other, '__iter__'):
            raise TypeError(
                f"Ожидается итерируемый объект, получен {type(other)}")

        if type(other) == dict:
            return Tuple(tuple(self) + tuple(other.items()))
        else:
            return Tuple(tuple(self) + tuple(other))

