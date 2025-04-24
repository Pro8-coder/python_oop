"""
Вы несколько раз уже делали стек-подобную структуру, когда объекты
последовательно связаны между собой:

Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу
(indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. Должно быть
целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать
исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.
"""
from typing import Any, Iterator


class StackObj:
    """
    Класс для представления объектов стека.

    :ivar data: Ссылка на данные объекта
    :ivar next: Ссылка на следующий объект стека (None если отсутствует)
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class Stack:
    """
    Класс для представления стека объектов StackObj.

    :ivar top: Ссылка на первый объект стека (None если стек пуст)
    :ivar _len_stack: Количество объектов в стеке
    """

    def __init__(self) -> None:
        self.top = None
        self._len_stack = 0

    def _check_index(self, index: int) -> None:
        """
        Проверяет корректность индекса.

        :param index: Проверяемый индекс
        :raises IndexError: Если индекс вне допустимого диапазона
        """
        if type(index) != int or not 0 <= index < self._len_stack:
            raise IndexError('неверный индекс')

    def push_back(self, obj: StackObj) -> None:
        """
        Добавляет объект в конец стека.

        :param obj: Объект StackObj для добавления
        """
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next

            current.next = obj

        self._len_stack += 1

    def push_front(self, obj: StackObj) -> None:
        """
        Добавляет объект в начало стека.

        :param obj: Объект StackObj для добавления
        """
        obj.next = self.top
        self.top = obj
        self._len_stack += 1

    def __getitem__(self, item: int) -> Any:
        """
        Возвращает данные объекта по индексу.

        :param item: Индекс объекта
        :return: Данные объекта StackObj
        :raises IndexError: Если индекс некорректен
        """
        self._check_index(item)
        current = self.top
        for _ in range(item):
            current = current.next

        return current.data

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Устанавливает новые данные объекту по индексу.

        :param key: Индекс объекта
        :param value: Новые данные
        :raises IndexError: Если индекс некорректен
        """
        self._check_index(key)
        current = self.top
        for _ in range(key):
            current = current.next

        current.data = value

    def __len__(self) -> int:
        """
        Возвращает количество объектов в стеке.

        :return: Число объектов
        """
        return self._len_stack

    def __iter__(self) -> Iterator[StackObj]:
        """
        Возвращает итератор по объектам стека.

        :return: Итератор объектов StackObj
        :rtype: Iterator[StackObj]
        """
        current = self.top
        while current:
            yield current
            current = current.next

