"""
Вам необходимо написать программу по работе с массивом однотипных данных
(например, только числа или строки и т.п.). Для этого нужно объявить класс
с именем Array, объекты которого создаются командой:

ar = Array(max_length, cell)
где max_length - максимальное количество элементов в массиве; cell - ссылка на
класс, описывающий отдельный элемент этого массива (см. далее, класс Integer).
Начальные значения в ячейках массива (в объектах класса Integer) должны быть
равны 0.

Для работы с целыми числами объявите в программе еще один класс с именем
Integer, объекты которого создаются командой:

cell = Integer(start_value)
где start_value - начальное значение ячейки (в данном случае - целое число).

В классе Integer должно быть следующее свойство (property):

value - для изменения и считывания значения из ячейки (само значение
хранится в локальной приватной переменной; имя придумайте сами).

При попытке присвоить не целое число должно генерироваться исключение командой:

raise ValueError('должно быть целое число')
Для обращения к отдельным элементам массива в классе Array необходимо
определить набор магических методов для следующих операций:

value = ar[0] # получение значения из первого элемента (ячейки) массива ar
ar[1] = value # запись нового значения во вторую ячейку массива ar
Если индекс не целое число или число меньше нуля или больше либо равно
max_length, то должно генерироваться исключение командой:

raise IndexError('неверный индекс для доступа к элементам массива')
Пример использования классов (эти строчки в программе не писать):

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку
через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.

P.P.S. В качестве дополнительного домашнего задания: объявите еще один
класс Float для работы с вещественными числами и создайте массив, используя
тот же класс Array, с этим новым типом данных.
"""
from typing import Any


class Integer:
    """
    Класс для представления целочисленного элемента массива.

    :ivar start_value: Начальное значение (по умолчанию 0)
    """

    def __init__(self, start_value: int = 0) -> None:
        self.__value = start_value

    @property
    def value(self) -> int:
        """
        Возвращает текущее значение элемента.

        :return: Целое число
        """
        return self.__value

    @value.setter
    def value(self, val: int) -> None:
        """
        Устанавливает новое значение элемента.

        :param val: Новое значение
        :raises ValueError: Если значение не целое число
        """
        if type(val) == int:
            self.__value = val
        else:
            raise ValueError('должно быть целое число')


class Float:
    """
    Класс для представления вещественного элемента массива.

    :ivar start_value: Начальное значение (по умолчанию 0.0)
    """

    def __init__(self, start_value: float = 0.0) -> None:
        self.__value = start_value

    @property
    def value(self) -> float:
        """
        Возвращает текущее значение элемента.

        :return: Вещественное число
        """
        return self.__value

    @value.setter
    def value(self, val: float) -> None:
        """
        Устанавливает новое значение элемента.

        :param val: Новое значение
        :raises ValueError: Если значение не вещественное число
        """
        if type(val) == float:
            self.__value = val
        else:
            raise ValueError('должно быть вещественное число')


class Array:
    """
    Класс для представления массива однотипных элементов.

    :ivar max_length: Максимальное количество элементов
    :ivar cell: Класс элементов массива
    :ivar __array: Внутренний список элементов массива
    """

    def __init__(self, max_length: int, cell: type) -> None:
        self.max_length = max_length
        self.cell = cell
        self.__array: list[Any] = [cell() for _ in range(max_length)]

    def __getitem__(self, item: int) -> Any:
        if type(item) == int and 0 <= item < self.max_length:
            return self.__array[item].value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key: int, value: Any) -> None:
        if type(key) == int and 0 <= key < self.max_length:
            self.__array[key].value = value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __str__(self) -> str:
        """
        Возвращает строковое представление массива.

        :return: Строка значений через пробел
        """
        return ' '.join(str(item.value) for item in self.__array)

