"""
Объявите класс с именем Money (деньги), объекты которого создаются командой:

money = Money(value)
где value - любое число (целое или вещественное). Если указывается не числовое
значение, то генерируется исключение командой:

raise TypeError('сумма должна быть числом')
В каждом объекте этого класса должен формироваться локальный атрибут _money с
соответствующим значением. Также в классе Money должно быть объект-свойство
(property):

money - для записи и считывания значения из атрибута _money.

В связке с классом Money работает еще один класс:

class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)
Он определяет работу арифметических операторов. В данном примере описан
алгоритм сложения двух объектов класса Money (или объектов его дочерних
классов).

Обратите внимание, как реализован метод __add__() в этом классе. Он
универсален при работе с любыми объектами класса Money или его дочерних
классов. Здесь атрибут __class__ - это ссылка на класс объекта self.
С помощью __class__ можно создавать объекты того же класса, что и self.

Вам необходимо добавить в класс MoneyOperators аналогичную реализацию
оператора вычитания.

На основе двух классов (Money и MoneyOperators) предполагается создавать
классы кошельков разных валют. Например, так:

class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
И, затем применять их следующим образом (эти строчки в программе писать
не нужно):

m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError
P.S. В программе требуется объявить только классы. На экран выводить ничего
не нужно.
"""


class Money:
    """
    Базовый класс для представления денежных сумм.

    :ivar _money: Защищенный атрибут для хранения суммы
    :raises TypeError: Если передано не числовое значение
    """

    def __init__(self, value: int | float) -> None:
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')

        self._money = value

    @property
    def money(self) -> int | float:
        """
        Возвращает текущее значение суммы.

        :return: Текущая сумма
        """
        return self._money

    @money.setter
    def money(self, value: int | float) -> None:
        """
        Устанавливает новое значение суммы с проверкой типа.

        :param value: Новое значение суммы
        :raises TypeError: Если значение не является числом
        """
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = value


class MoneyOperators:
    """Класс-миксин для арифметических операций с денежными суммами."""

    def __add__(self, other: int | float | 'MoneyOperators'
                ) -> 'MoneyOperators':
        """
        Реализует операцию сложения денежных сумм.

        :param other: Число или объект Money для сложения
        :return: Новый объект того же класса
        :raises TypeError: При несовместимых типах операндов
        """
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other: int | float | 'MoneyOperators'
                ) -> 'MoneyOperators':
        """
        Реализует операцию вычитания денежных сумм.

        :param other: Число или объект Money для вычитания
        :return: Новый объект того же класса
        :raises TypeError: При несовместимых типах операндов
        """
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class MoneyR(Money, MoneyOperators):
    """Класс для представления денег в рублях."""

    def __str__(self) -> str:
        """
        Возвращает строковое представление суммы в рублях.

        :return: Строка вида 'MoneyR: <сумма>'
        """
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    """Класс для представления денег в долларах."""

    def __str__(self) -> str:
        """
        Возвращает строковое представление суммы в долларах.

        :return: Строка вида 'MoneyD: <сумма>'
        """
        return f"MoneyD: {self.money}"

