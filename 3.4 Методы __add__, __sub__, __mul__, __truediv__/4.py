"""
Вам поручается создать программу по учету книг (библиотеку). Для этого
необходимо в программе объявить два класса:

Lib - для представления библиотеки в целом;
Book - для описания отдельной книги.

Объекты класса Book должны создаваться командой:

book = Book(title, author, year)
где title - заголовок книги (строка); author - автор книги (строка);
year - год издания (целое число).

Объекты класса Lib создаются командой:

lib = Lib()
Каждый объект должен содержать локальный публичный атрибут:

book_list - ссылка на список из книг (объектов класса Book). Изначально список
пустой.

Также объекты класса Lib должны работать со следующими операторами:

lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит
по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет
начинается с нуля)
lib -= indx
При реализации бинарных операторов + и - создавать копии библиотек (объекты
класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:

n = len(lib) # n - число книг
которая возвращает число книг в библиотеке.

P.S. В программе достаточно только объявить классы. На экран ничего выводить
не нужно.
"""


class Book:
    """
    Класс Book представляет книгу.

    :ivar title: Заголовок книги.
    :ivar author: Автор книги.
    :ivar year: Год издания книги.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


class Lib:
    """
    Класс Lib представляет библиотеку.

    :ivar book_list: Список книг в библиотеке (изначально пустой).
    """

    def __init__(self) -> None:
        self.book_list: list[Book] = []

    def __add__(self, other: Book) -> 'Lib':
        """
        Добавляет книгу в библиотеку.

        :param other: Книга для добавления.
        :return: Текущий объект Lib.
        :raises TypeError: Если other не является объектом Book.
        """
        if isinstance(other, Book):
            self.book_list.append(other)

        return self

    def __iadd__(self, other: Book) -> 'Lib':
        """
        Добавляет книгу в библиотеку.

        :param other: Книга для добавления.
        :return: Текущий объект Lib.
        :raises TypeError: Если other не является объектом Book.
        """
        return self.__add__(other)

    def __sub__(self, other: Book | int) -> 'Lib':
        """
        Удаляет книгу из библиотеки.

        :param other: Книга или индекс книги для удаления.
        :return: Текущий объект Lib.
        :raises TypeError: Если other не является объектом Book
        или целым числом.
        :raises ValueError: Если книга не найдена в библиотеке.
        :raises IndexError: Если индекс выходит за пределы списка книг.
        """
        if isinstance(other, Book) and other in self.book_list:
            self.book_list.remove(other)
        elif (type(other) == int and
                -len(self.book_list) <= other < len(self.book_list)):
            del self.book_list[other]

        return self

    def __isub__(self, other: Book | int) -> 'Lib':
        """
        Удаляет книгу из библиотеки.

        :param other: Книга или индекс книги для удаления.
        :return: Текущий объект Lib.
        :raises TypeError: Если other не является объектом Book
        или целым числом.
        :raises ValueError: Если книга не найдена в библиотеке.
        :raises IndexError: Если индекс выходит за пределы списка книг.
        """
        return self.__sub__(other)

    def __len__(self) -> int:
        """
        Возвращает количество книг в библиотеке.

        :return: Число книг.
        """
        return len(self.book_list)

