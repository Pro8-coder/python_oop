"""
Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый
класс с именем StackInterface со следующими абстрактными методами:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

На основе этого класса объявите дочерний класс с именем Stack. Объекты этого
класса должны создаваться командой:

st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:

_top - ссылка на первый объект стека (для пустого стека _top = None).

В самом классе Stack переопределить абстрактные методы базового класса:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

Сами объекты стека должны определяться классом StackObj и создаваться командой:

obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом объекте класса
StackObj должны автоматически формироваться атрибуты:

_data - информация, хранящаяся в объекте (строка);
_next - ссылка на следующий объект стека (если следующий отсутствует,
то _next = None).

Пример использования классов (эти строчки в программе писать не нужно):

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов
не было, то del_obj = None)
P.S. В программе требуется объявить только классы. На экран выводить ничего
не нужно.
"""
from abc import ABC, abstractmethod


class StackObj:
    """
    Объект стека, хранящий данные и ссылку на следующий элемент.

    :ivar _data: Данные, хранящиеся в объекте
    :ivar _next: Ссылка на следующий объект стека
    """

    def __init__(self, data: str) -> None:
        self._data = data
        self._next: 'StackObj' | None = None


class StackInterface(ABC):
    """Абстрактный интерфейс стека."""

    @abstractmethod
    def push_back(self, obj: StackObj) -> None:
        """
        Добавляет объект в конец стека.

        :param obj: Объект StackObj для добавления
        :raises NotImplementedError: Если метод не переопределен
        """
        raise NotImplementedError("Метод push_back должен быть переопределен")

    @abstractmethod
    def pop_back(self) -> StackObj:
        """
        Удаляет и возвращает последний объект стека.

        :return: Удаленный объект или None если стек пуст
        :raises NotImplementedError: Если метод не переопределен
        """
        raise NotImplementedError("Метод pop_back должен быть переопределен")


class Stack(StackInterface):
    """
    Реализация стека на основе связанного списка.

    :ivar _top: Ссылка на вершину стека
    """

    def __init__(self) -> None:
        self._top: StackObj | None = None

    def push_back(self, obj: StackObj) -> None:
        """
        Добавляет объект в конец стека.

        :param obj: Объект StackObj для добавления
        """
        if self._top is None:
            self._top = obj
        else:
            current = self._top
            while current._next:
                current = current._next

            current._next = obj

    def pop_back(self) -> StackObj | None:
        """
        Удаляет и возвращает последний объект стека.

        :return: Удаленный объект или None если стек пуст
        """
        if self._top is None:
            return None

        if self._top._next is None:
            popped = self._top
            self._top = None
            return popped

        current = self._top
        while current._next._next:
            current = current._next

        poped = current._next
        current._next = None
        return poped

