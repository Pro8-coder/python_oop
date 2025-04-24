"""
Объявите класс LinkedList (связный список) для работы со следующей структурой
данных:

Здесь создается список из связанных между собой объектов класса ObjList.
Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj
класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет,
то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет,
то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст,
то head = None);
tail - ссылка на последний объект связного списка (если список пуст,
то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного
списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его
порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса
ObjList, расположенного под индексом indx (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.
"""


class ObjList:
    """
    Класс для представления элемента двусвязного списка.

    :ivar data: Строка с данными, хранящимися в элементе.
    """
    def __init__(self, data: str) -> None:
        """
        Инициализация экземпляра класса ObjList.
        Создаёт пустые связи `__prev = None` и `__next = None`.

        :param data: Строка с данными.
        """
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self) -> str:
        """
        Возвращает данные, хранящиеся в элементе.

        :return: Строка с данными.
        """
        return self.__data

    @property
    def prev(self) -> "ObjList" | None:
        """
        Возвращает ссылку на предыдущий элемент списка.

        :return: Предыдущий элемент списка или None.
        """
        return self.__prev

    @prev.setter
    def prev(self, value: "ObjList") -> None:
        """
        Устанавливает ссылку на предыдущий элемент списка.

        :param value: Предыдущий элемент списка.
        """
        self.__prev = value

    @property
    def next(self) -> "ObjList" | None:
        """
        Возвращает ссылку на следующий элемент списка.

        :return: Следующий элемент списка или None.
        """
        return self.__next

    @next.setter
    def next(self, value: "ObjList") -> None:
        """
        Устанавливает ссылку на следующий элемент списка.

        :param value: Следующий элемент списка.
        """
        self.__next = value


class LinkedList:
    """
    Класс для представления двусвязного списка.

    Содержит ссылки на первый (`head`) и последний (`tail`) элементы списка.
    """

    def __init__(self) -> None:
        """
        Инициализация экземпляра класса LinkedList.

        Создаёт пустой список с `head = None` и `tail = None`.
        """
        self.head: None | ObjList = None
        self.tail: None | ObjList = None

    def add_obj(self, obj: ObjList) -> None:
        """
        Добавляет новый элемент в конец списка.

        :param obj: Элемент списка (объект класса ObjList).
        """
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def remove_obj(self, indx: int) -> None:
        """
        Удаляет элемент списка по указанному индексу.

        :param indx: Индекс элемента для удаления (начиная с 0).
        :raises IndexError: Если индекс выходит за пределы списка.
        """
        current: None | ObjList = self.head
        for i in range(indx):
            if current is not None:
                current = current.next
            else:
                raise IndexError("Индекс вне диапазона0.")

        if current is None:
            raise IndexError("Индекс вне диапазона1.")

        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def __len__(self) -> int:
        """
        Возвращает количество элементов в списке.

        :return: Количество элементов.
        """
        count: int = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __call__(self, indx: int) -> str:
        """
        Возвращает данные элемента списка по указанному индексу.

        :param indx: Индекс элемента (начиная с 0).
        :return: Данные элемента (строка).
        :raises IndexError: Если индекс выходит за пределы списка.
        """
        current: None | ObjList = self.head
        for i in range(indx):
            if current is not None:
                current = current.next
            else:
                raise IndexError("Индекс вне диапазона.")

        if current is None:
            raise IndexError("Индекс вне диапазона.")

        return current.data

