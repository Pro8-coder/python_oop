"""
Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title
объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author
объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price
объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title
объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author
объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price
объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)
При этом, в каждом объекте должны создаваться приватные локальные свойства:

__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.

P.S. В программе требуется объявить только класс. Ничего на экран выводить не
нужно.
"""


class Book:
    """Класс, представляющий книгу с автором, названием и ценой."""

    def __init__(self, author: str, title: str, price: int) -> None:
        """
        Инициализирует объект книги.

        :param author: Имя автора книги.
        :param title: Название книги.
        :param price: Цена книги.
        """
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title: str) -> None:
        """
        Устанавливает новое название книги.

        :param title: Новое название книги.
        """
        self.__title = title

    def set_author(self, author: str) -> None:
        """
        Устанавливает нового автора книги.

        :param author: Новое имя автора книги.
        """
        self.__author = author

    def set_price(self, price: int) -> None:
        """
        Устанавливает новую цену книги.

        :param price: Новая цена книги.
        """
        self.__price = price

    def get_title(self) -> str:
        """
        Возвращает название книги.

        :return: Название книги.
        """
        return self.__title

    def get_author(self) -> str:
        """
        Возвращает имя автора книги.

        :return: Имя автора книги.
        """
        return self.__author

    def get_price(self) -> int:
        """
        Возвращает цену книги.

        :return: Цена книги.
        """
        return self.__price

