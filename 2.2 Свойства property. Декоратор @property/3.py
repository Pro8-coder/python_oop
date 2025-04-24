"""
Реализуйте односвязный список (не список Python, не использовать список Python
для хранения объектов), когда один объект ссылается на следующий и так по
цепочке до последнего:

Для этого объявите в программе два класса:

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса
StackObj должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта
принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства
__next;
data - для записи и считывания информации из локального приватного свойства
__data.

При записи необходимо реализовать проверку, что __next будет ссылаться на
объект класса StackObj или значение None. Если проверка не проходит,
то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список
пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного
списка;
pop(self) - извлечение последнего объекта с его удалением из односвязного
списка;
get_data(self) - получение списка из объектов односвязного списка (список из
строк локального атрибута __data каждого объекта в порядке их добавления, или
пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать
не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
P.S. В программе требуется объявить только классы. На экран ничего выводить
не нужно.
"""
from typing import Union


class StackObj:
    """Класс, представляющий объект односвязного списка."""

    def __init__(self, data: str) -> None:
        """
        Инициализирует объект StackObj.

        :param data: Строка с данными.
        """
        self.__data = data
        self.__next: None | StackObj = None

    @property
    def next(self) -> Union['StackObj', None]:
        """
        Возвращает ссылку на следующий объект.

        :return: Следующий объект или None.
        """
        return self.__next

    @next.setter
    def next(self, nxt: Union['StackObj', None]) -> None:
        """
        Устанавливает ссылку на следующий объект.

        :param nxt: Следующий объект или None.
        """
        if nxt is None or isinstance(nxt, StackObj):
            self.__next = nxt

    @property
    def data(self) -> str:
        """
        Возвращает данные объекта.

        :return: Строка с данными.
        """
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        """
        Устанавливает данные объекта.

        :param data: Строка с данными.
        """
        self.__data = data


class Stack:
    """Класс для управления односвязным списком."""

    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self.top: StackObj | None = None

    def push(self, obj: StackObj) -> None:
        """
        Добавляет объект в конец стека.

        :param obj: Объект StackObj для добавления.
        """
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop(self) -> StackObj | None:
        """
        Извлекает и удаляет последний объект из стека.

        :return: Последний объект или None, если стек пуст.
        """
        if self.top is None:
            return None
        elif self.top.next is None:
            current = self.top
            self.top = None
            return current
        else:
            penultimate = self.top
            while penultimate.next.next is not None:
                penultimate = penultimate.next

            current = penultimate.next
            penultimate.next = None
            return current

    def get_data(self) -> list[str]:
        """
        Возвращает список данных всех объектов стека.

        :return: Список строк с данными.
        """
        data: list[str] = []
        current = self.top
        while current is not None:
            data.append(current.data)
            current = current.next

        return data

