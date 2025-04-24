"""
Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается
на следующий и так по цепочке до последнего:

Для этого в программе объявлялись два класса:

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными). При этом
каждый объект класса StackObj должен иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта
принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения
к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов
в стеке, то должно генерироваться исключение командой:

raise IndexError('неверный индекс')
Пример использования классов Stack и StackObj (эти строчки в программе
не писать):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.
"""
from typing import Any, Optional


class StackObj:
    """
    Класс объекта стека

    :ivar __data: строка с данными объекта
    :ivar __next: ссылка на следующий объект
    """

    def __init__(self, data: Any) -> None:
        """
        Инициализация объекта стека.

        :param data: Данные для хранения в объекте.
        """
        self.__data = data
        self.__next: Optional['StackObj'] = None

    @property
    def next(self) -> Optional['StackObj']:
        """
        Получить следующий объект в стеке.

        :return: Следующий объект или None, если его нет.
        """
        return self.__next

    @next.setter
    def next(self, obj: Optional['StackObj']) -> None:
        """
        Установить следующий объект в стеке.

        :param obj: Объект, который будет следующим в стеке.
        """
        self.__next = obj

    @property
    def data(self) -> Any:
        """
        Получить данные объекта.

        :return: Данные, хранящиеся в объекте.
        """
        return self.__data

    @data.setter
    def data(self, data: Any) -> None:
        """
        Установить данные объекта.

        :param data: Новые данные для объекта.
        """
        self.__data = data


class Stack:
    """
    Класс стека, реализующий стекоподобную структуру данных.

    :ivar __top: Вершина стека (первый объект).
    :ivar __len_stack: Количество объектов в стеке.
    """

    def __init__(self) -> None:
        """Инициализация пустого стека."""
        self.__top: StackObj | None = None
        self.__len_stack = 0

    @property
    def top(self) -> StackObj | None:
        """
        Получить вершину стека.

        :return: Объект на вершине стека или None, если стек пуст.
        """
        return self.__top

    @top.setter
    def top(self, obj: StackObj | None) -> None:
        """
        Установить вершину стека.

        :param obj: Объект, который будет установлен на вершину стека.
        """
        self.__top = obj

    def push(self, obj: StackObj) -> None:
        """
        Добавить объект в конец стека.

        :param obj: Объект для добавления в стек.
        """
        if self.top is None:
            self.top = obj
            self.__len_stack += 1
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj
            self.__len_stack += 1

    def pop(self) -> StackObj:
        """
        Извлечь последний объект из стека.

        :return: Извлеченный объект.
        :raises IndexError: Если стек пуст.
        """
        if self.top is None:
            raise IndexError("стек пуст")
        elif self.top.next is None:
            obj = self.top
            self.top = None
            self.__len_stack -= 1
            return obj

        current = self.top
        while current.next.next is not None:
            current = current.next

        obj = current.next
        current.next = None
        self.__len_stack -= 1
        return obj

    def __getitem__(self, item: int) -> StackObj:
        """
        Получить объект стека по индексу.

        :param item: Индекс объекта.
        :return: Объект стека.
        :raises IndexError: Если индекс неверный.
        """
        if type(item) != int or item >= self.__len_stack or item < 0:
            raise IndexError('неверный индекс')

        current = self.__top
        count = 0
        while current is not None:
            if count == item:
                return current
            current = current.next
            count += 1

    def __setitem__(self, key: int, value: StackObj) -> None:
        """
        Заменить объект стека по индексу.

        :param key: Индекс объекта для замены.
        :param value: Новый объект.
        :raises IndexError: Если индекс неверный.
        """
        if type(key) != int or key >= self.__len_stack or key < 0:
            raise IndexError('неверный индекс')

        if key == 0:
            value.next = self.__top.next if self.__top else None
            self.__top = value
            return

        current = self.__top
        count = 0
        while current is not None:
            if count == key - 1:
                value.next = current.next.next
                current.next = value
                return

