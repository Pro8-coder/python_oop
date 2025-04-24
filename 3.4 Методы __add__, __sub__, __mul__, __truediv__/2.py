"""
Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать
только целые и вещественные числа, остальные игнорировать (если указываются
в списке). Например:

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта создается
свой список).

Также с объектами класса ListMath должны работать следующие операторы:

lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число
(в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число
(в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число
(в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые
объекты класса ListMath с новыми списками, прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри
списка текущего объекта (новый объект не создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить
не нужно.
"""


class ListMath:
    def __init__(self, lst: None | list = None) -> None:
        """
        Инициализация объекта ListMath.

        :param lst: Список начальных значений. Если не передан, создается
        пустой список.
        """
        self.lst_math = [x for x in lst if type(x) in (int, float)] \
            if lst and isinstance(lst, list) else []

    def __add__(self, other: int | float) -> 'ListMath':
        """
        Сложение каждого элемента списка с числом.

        :param other: Число для сложения.
        :return: Новый объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        """
        if isinstance(other, (int, float)):
            return ListMath([x + other for x in self.lst_math])
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

    def __radd__(self, other: int | float) -> 'ListMath':
        """
        Сложение числа с каждым элементом списка (случай, когда число слева).

        :param other: Число для сложения.
        :return: Новый объект ListMath.
        """
        return self.__add__(other)

    def __iadd__(self, other: int | float) -> 'ListMath':
        """
        Сложение каждого элемента списка с числом (оператор +=).

        :param other: Число для сложения.
        :return: Текущий объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        """
        if isinstance(other, (int, float)):
            self.lst_math = [x + other for x in self.lst_math]
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

        return self

    def __sub__(self, other: int | float) -> 'ListMath':
        """
        Вычитание числа из каждого элемента списка.

        :param other: Число для вычитания.
        :return: Новый объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        """
        if isinstance(other, (int, float)):
            return ListMath([x - other for x in self.lst_math])
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

    def __rsub__(self, other: int | float) -> 'ListMath':
        """
        Вычитание каждого элемента списка из числа (случай, когда число слева).

        :param other: Число для вычитания.
        :return: Новый объект ListMath.
        """
        if isinstance(other, (int, float)):
            return ListMath([other - x for x in self.lst_math])
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

    def __isub__(self, other: int | float) -> 'ListMath':
        """
        Вычитание числа из каждого элемента списка (оператор -=).

        :param other: Число для вычитания.
        :return: Текущий объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        """
        if isinstance(other, (int, float)):
            self.lst_math = [x - other for x in self.lst_math]
        else:
            raise TypeError("Операнд должен быть числом (int или float)")
        return self

    def __mul__(self, other: int | float) -> 'ListMath':
        """
        Умножение каждого элемента списка на число.

        :param other: Число для умножения.
        :return: Новый объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        """
        if isinstance(other, (int, float)):
            return ListMath([x * other for x in self.lst_math])
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

    def __rmul__(self, other: int | float) -> 'ListMath':
        """
        Умножение числа на каждый элемент списка (случай, когда число слева).

        :param other: Число для умножения.
        :return: Новый объект ListMath.
        """
        return self.__mul__(other)

    def __imul__(self, other: int | float) -> 'ListMath':
        """
        Умножение каждого элемента списка на число (оператор *=).

        :param other: Число для умножения.
        :return: Текущий объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        """
        if isinstance(other, (int, float)):
            self.lst_math = [x * other for x in self.lst_math]
        else:
            raise TypeError("Операнд должен быть числом (int или float)")
        return self

    def __truediv__(self, other: int | float) -> 'ListMath':
        """
        Деление каждого элемента списка на число.

        :param other: Число для деления.
        :return: Новый объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        :raises ZeroDivisionError: Если other равно 0.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль запрещено")
            return ListMath([x / other for x in self.lst_math])
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

    def __rtruediv__(self, other: int | float) -> 'ListMath':
        """
        Деление числа на каждый элемент списка (случай, когда число слева).

        :param other: Число для деления.
        :return: Новый объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        :raises ZeroDivisionError: Если какой-либо элемент списка равен 0.
        """
        if isinstance(other, (int, float)):
            if any(x == 0 for x in self.lst_math):
                raise ZeroDivisionError("Деление на ноль запрещено")
            return ListMath([other / x for x in self.lst_math])
        else:
            raise TypeError("Операнд должен быть числом (int или float)")

    def __itruediv__(self, other: int | float) -> 'ListMath':
        """
        Деление каждого элемента списка на число (оператор /=).

        :param other: Число для деления.
        :return: Текущий объект ListMath.
        :raises TypeError: Если other не является числом (int или float).
        :raises ZeroDivisionError: Если other равно 0.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль запрещено")
            self.lst_math = [x / other for x in self.lst_math]
        else:
            raise TypeError("Операнд должен быть числом (int или float)")
        return self

