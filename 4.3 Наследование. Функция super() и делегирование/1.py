"""
Ранее вы уже использовали делегирование методов, когда вызывали инициализатор
базового класса через функцию super(). Чаще всего делегирование в Python
связано с вызовом магических методов базовых классов (так как их имена нельзя
менять). Выполним такой пример.

Объявите в программе базовый класс с именем Book, объекты которого создаются
командой:

book = Book(title, author, pages, year)
где title - заголовок книги (строка); author - автор книги (строка); pages -
число страниц (целое число); year - год издания (целое число). В каждом
объекте класса Book должны формироваться соответствующие локальные атрибуты:
title, author, pages, year.

Объявите дочерний класс DigitBook от класса Book, объекты которого создаются
командой:

db = DigitBook(title, author, pages, year, size, frm)
где дополнительные параметры size - размер книги в байтах (целое число); frm -
формат книги (строка: 'pdf', 'doc', 'fb2', 'txt'). В каждом объекте
класса DigitBook должны формироваться соответствующие локальные атрибуты:
title, author, pages, year, size, frm.

Инициализация локальных атрибутов title, author, pages, year должна
выполняться в базовом классе Book, а параметры size, frm инициализируются в
дочернем классе DigitBook.

P.S. В программе нужно объявить только классы. На экран выводить ничего
не нужно.
"""


class Book:
    """
    Базовый класс для представления книги.

    :ivar title: Название книги
    :ivar author: Автор книги
    :ivar pages: Количество страниц
    :ivar year: Год издания
    """

    def __init__(self, title: str, author: str, pages: int, year: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    """
    Класс для представления цифровой книги (наследуется от Book).

    :ivar size: Размер файла в байтах
    :ivar frm: Формат файла ('pdf', 'doc', 'fb2', 'txt')
    """

    def __init__(self, title: str, author: str, pages: int, year: int,
                 size: int, frm: str) -> None:
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm

