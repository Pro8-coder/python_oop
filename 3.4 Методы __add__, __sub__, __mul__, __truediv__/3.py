"""
Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами
класса StackObj (когда один объект ссылается на следующий и так далее):

Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)
где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет,
то __next = None).

Объекты класса Stack создаются командой:

st = Stack()
и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет,
то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного
списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии
односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса
StackObj с данными, взятыми из списка (каждый элемент списка для очередного
добавляемого объекта).

P.S. В программе достаточно только объявить классы. На экран ничего выводить
не нужно.
"""


class StackObj:
    """
    Класс StackObj представляет объект односвязного списка.

    :ivar __data: Данные, хранящиеся в объекте.
    :ivar __next: Ссылка на следующий объект в списке.
    """

    def __init__(self, data: str) -> None:
        """
        Инициализация объекта StackObj.

        :param data: Строка с данными, которые будут храниться в объекте.
        """
        self.__data = data
        self.__next: 'StackObj' | None = None

    @property
    def next(self) -> 'StackObj' | None:
        """
        Возвращает ссылку на следующий объект в списке.

        :return: Следующий объект StackObj или None, если его нет.
        """
        return self.__next

    @next.setter
    def next(self, nxt: 'StackObj' | None) -> None:
        """
        Устанавливает ссылку на следующий объект в списке.

        :param nxt: Следующий объект StackObj или None.
        """
        self.__next = nxt

    @property
    def data(self) -> str:
        """
        Возвращает данные, хранящиеся в объекте.

        :return: Строка с данными.
        """
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        """
        Устанавливает данные в объекте.

        :param data: Строка с данными.
        """
        self.__data = data


class Stack:
    """
    Класс Stack представляет односвязный список.

    :ivar top: Ссылка на первый объект в списке.
    """

    def __init__(self) -> None:
        self.top: None | StackObj = None

    def push_back(self, obj: StackObj) -> None:
        """
        Добавляет объект StackObj в конец односвязного списка.

        :param obj: Объект StackObj для добавления.
        """
        if self.top is None:
            self.top = obj
        else:
            current: StackObj = self.top
            while current.next is not None:
                current = current.next

            current.next = obj

    def pop_back(self) -> None:
        """
        Удаляет последний объект из односвязного списка.
        Если список пуст, ничего не делает.
        """
        if self.top is not None:
            if self.top.next is None:
                self.top = None
            else:
                current: StackObj | None = self.top
                while current.next.next is not None:
                    current = current.next

                current.next = None

    def __add__(self, other: StackObj) -> 'Stack':
        """
        Добавляет объект StackObj в конец списка и возвращает self.

        :param other: Объект StackObj для добавления.
        :return: Текущий объект Stack.
        :raises TypeError: Если other не является объектом StackObj.
        """
        if isinstance(other, StackObj):
            self.push_back(other)

        return self

    def __iadd__(self, other: StackObj) -> 'Stack':
        """
        Добавляет объект StackObj в конец списка и возвращает self.

        :param other: Объект StackObj для добавления.
        :return: Текущий объект Stack.
        :raises TypeError: Если other не является объектом StackObj.
        """
        return self.__add__(other)

    def __mul__(self, other: list[str]) -> 'Stack':
        """
        Добавляет несколько объектов StackObj в конец списка и возвращает self.

        :param other: Список строк, из которых создаются объекты StackObj.
        :return: Текущий объект Stack.
        :raises TypeError: Если other не является списком.
        """
        if isinstance(other, list):
            for data in other:
                self.push_back(StackObj(data))

        return self

    def __imul__(self, other: list[str]) -> 'Stack':
        """
        Добавляет несколько объектов StackObj в конец списка и возвращает self.

        :param other: Список строк, из которых создаются объекты StackObj.
        :return: Текущий объект Stack.
        :raises TypeError: Если other не является списком.
        """
        return self.__mul__(other)

