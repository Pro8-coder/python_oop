"""
Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Необходимо каждую из этих строк представить объектом класса BookStudy,
которые создаются командой:

bs = BookStudy(name, author, year)
где name - название пособия (строка); author - автор пособия (строка);
year - год издания (целое число). Такие же публичные локальные атрибуты должны
быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам:
name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных
строк (списка lst_in). После этого определить число книг с уникальными хэшами.
Это число сохранить через переменную unique_books (целое число).

P.S. На экран ничего выводить не нужно.

Sample Input:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021
Sample Output:
"""
import sys


class BookStudy:
    """
    Класс для представления учебного пособия.

    :ivar name: Название пособия.
    :ivar author: Автор пособия.
    :ivar year: Год издания.
    """

    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self) -> int:
        """
        Вычисляет хэш объекта на основе названия и автора (без учета регистра).

        :return: Целочисленный хэш.
        """
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other: 'BookStudy') -> bool:
        """
        Сравнивает объекты BookStudy по их хэшам.

        :param other: Другой объект BookStudy.
        :return: True, если хэши равны, иначе False.
        """
        return hash(self) == hash(other)


lst_in: list[str] = list(map(str.strip, sys.stdin.readlines()))
lst_bs: list[BookStudy] = [BookStudy(*line.split("; ")) for line in lst_in]
unique_books: int = len(set(lst_bs))
