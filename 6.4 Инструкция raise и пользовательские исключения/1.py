"""
Объявите класс-исключение с именем StringException, унаследованным от базового
класса Exception. После этого объявите еще два класса-исключения:

NegativeLengthString - ошибка, если длина отрицательная;
ExceedLengthString - ошибка, если длина превышает заданное значение;

унаследованные от базового класса StringException.

Затем, в блоке try (см. программу) пропишите команду генерации исключения для
перехода в блок обработки исключения ExceedLengthString.
"""


class StringException(Exception):
    pass


class NegativeLengthString(StringException):
    """Ошибка, если длина отрицательная."""


class ExceedLengthString(StringException):
    """Ошибка, если длина превышает заданное значение."""


try:
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
