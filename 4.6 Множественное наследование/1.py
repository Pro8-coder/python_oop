"""
С помощью множественного наследования удобно описывать принадлежность объектов
к нескольким разным группам. Выполним такой пример.

Определите в программе классы в соответствии с их иерархией, представленной
на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку
на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive
с произвольными допустимыми для них значениями. Сохраните все эти объекты
в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки
из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран
выводить ничего не нужно.
"""


class Digit:
    """
    Базовый класс для числовых значений.

    :ivar value: Числовое значение
    :raises TypeError: Если значение не является числом
    """

    def __init__(self, value: int | float) -> None:
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')

        self.value = value


class Integer(Digit):
    """
    Класс для целочисленных значений.

    :ivar value: Целое число
    :raises TypeError: Если значение не целое число
    """

    def __init__(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(value)


class Float(Digit):
    """
    Класс для вещественных значений.

    :param value: Вещественное число
    :raises TypeError: Если значение не вещественное число
    """

    def __init__(self, value: float) -> None:
        if type(value) is not float:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(value)


class Positive(Digit):
    """
    Класс для положительных значений.

    :param value: Положительное число
    :raises TypeError: Если значение не положительное число
    """

    def __init__(self, value: int) -> None:
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(value)


class Negative(Digit):
    """
    Класс для отрицательных значений.

    :param value: Отрицательное число
    :raises TypeError: Если значение не отрицательное число
    """

    def __init__(self, value: int) -> None:
        if 0 <= value:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(value)


class PrimeNumber(Integer, Positive):
    """Класс для простых чисел."""
    pass


class FloatPositive(Float, Positive):
    """Класс для положительных вещественных чисел."""
    pass


digits = [PrimeNumber(1), PrimeNumber(3), PrimeNumber(7), FloatPositive(1.2),
          FloatPositive(7.3), FloatPositive(3.1), FloatPositive(1.7),
          FloatPositive(11.4)]

lst_positive = list(filter(lambda x: isinstance(x, Integer), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
