"""
Необходимо реализовать связный список (не список языка Python и не хранить
объекты в списке Python), когда объекты класса ObjList связаны с соседними
через приватные свойства __next и __prev:

Для этого объявите класс LinkedList, который будет представлять связный
список в целом и иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец
связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех
объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные
атрибуты:

head - ссылка на первый объект связного списка (если список пустой,
то head = None);
tail - ссылка на последний объект связного списка (если список пустой,
то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных
свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта
нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего
объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:

set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
set_data(self, data) - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:

ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать
в программе не нужно):

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
Объявите в программе классы LinkedList и ObjList в соответствии с заданием.

P.S. На экран ничего выводить не нужно.
"""


class ObjList:
    """Класс, представляющий элемент связного списка."""

    def __init__(self, data: str) -> None:
        """
        Инициализирует элемент списка с данными.

        :param data: Строка с данными.
        """
        self.__data = data
        self.__next: ObjList | None = None
        self.__prev: ObjList | None = None

    def set_next(self, obj: 'ObjList | None') -> None:
        """
        Устанавливает ссылку на следующий элемент.

        :param obj: Следующий элемент списка.
        """
        self.__next = obj

    def set_prev(self, obj: 'ObjList | None') -> None:
        """
        Устанавливает ссылку на предыдущий элемент.

        :param obj: Предыдущий элемент списка.
        """
        self.__prev = obj

    def set_data(self, data: str) -> None:
        """
        Устанавливает данные элемента.

        :param data: Строка с данными.
        """
        self.__data = data

    def get_next(self) -> 'ObjList | None':
        """
        Возвращает ссылку на следующий элемент.

        :return: Следующий элемент списка.
        """
        return self.__next

    def get_prev(self) -> 'ObjList | None':
        """
        Возвращает ссылку на предыдущий элемент.

        :return: Предыдущий элемент списка.
        """
        return self.__prev

    def get_data(self) -> str:
        """
        Возвращает данные элемента.

        :return: Строка с данными.
        """
        return self.__data


class LinkedList:
    """Класс, представляющий связный список."""

    def __init__(self) -> None:
        """Инициализирует пустой связный список."""
        self.head: ObjList | None = None
        self.tail: ObjList | None = None

    def add_obj(self, obj: ObjList) -> None:
        """
        Добавляет новый элемент в конец связного списка.

        :param obj: Элемент для добавления.
        """
        if self.tail is None:
            self.head = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)

        self.tail = obj

    def remove_obj(self) -> None:
        """Удаляет последний элемент из связного списка."""
        if self.tail is None:
            return

        if self.tail.get_prev() is None:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.get_prev()
            new_tail.set_next(None)
            self.tail = new_tail

    def get_data(self) -> list[str]:
        """
        Возвращает список данных всех элементов связного списка.

        :return: Список строк с данными.
        """
        data: list[str] = []
        current: ObjList | None = self.head
        while current is not None:
            data.append(current.get_data())
            current = current.get_next()

        return data

