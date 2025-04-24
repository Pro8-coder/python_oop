"""
Известно, что в Python мы можем соединять два списка между собой с помощью
оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка соответствующие
значения вычитаемого списка, как это показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования
оставшихся элементов списка должен сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить
класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами
класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]
P.S. В программе требуется только объявить класс. На экран ничего выводить
не нужно.
"""
from collections import defaultdict


class NewList:
    def __init__(self, lst: None | list = None) -> None:
        """
        Инициализация объекта NewList.

        :param lst: Список начальных значений. Если не передан, то пустой
        список.
        """
        self._lst = lst.copy() if lst and isinstance(lst, list) else []

    def get_list(self) -> list:
        """
        Возвращает результирующий список объекта класса NewList.

        :return: Список значений.
        """
        return self._lst

    def __sub__(self, other: list | 'NewList') -> 'NewList':
        """
        Реализация оператора вычитания для объектов класса NewList.

        :param other: Список или объект NewList, который вычитается из
        текущего списка.
        :return: Новый объект NewList с результатом
        вычитания.
        :raises ArithmeticError: Если правый операнд не является
        списком или объектом NewList.
        """
        if isinstance(other, list):
            other_lst = other
        elif isinstance(other, NewList):
            other_lst = other.get_list()
        else:
            raise ArithmeticError(
                "Правый операнд должен иметь тип list или NewList"
            )

        counter: dict = defaultdict(int)
        for item in other_lst:
            key = (item, type(item))
            counter[key] += 1

        result: list = []
        for item in self._lst:
            key = (item, type(item))
            if counter.get(key, 0) > 0:
                counter[key] -= 1
            else:
                result.append(item)

        return NewList(result)

    def __rsub__(self, other: list) -> 'NewList':
        """
        Реализация оператора вычитания, когда объект NewList находится
        справа от оператора.

        :param other: Список, из которого вычитается текущий объект NewList.
        :return: Новый объект NewList с результатом вычитания.
        """
        if not isinstance(other, list):
            raise ArithmeticError("Левый операнд должен иметь тип list")

        return NewList(other) - self

    def __isub__(self, other: list | 'NewList') -> 'NewList':
        """
        Реализация оператора -= для объектов класса NewList.

        :param other: Список или объект NewList, который вычитается из
        текущего списка.
        :return: Измененный объект NewList.
        """
        self._lst = (self - other).get_list()
        return self

