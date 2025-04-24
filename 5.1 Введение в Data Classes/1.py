"""
С помощью декоратора dataclass:

from dataclasses import dataclass
объявите класс с именем Person со следующим набором полей (порядок важен):

fio (строка: фамилия, имя, отчество);
old (int: возраст);
salary (int: зарплата, с нулевым начальным значением).
P.S. На экран ничего выводить не нужно.
"""
from dataclasses import dataclass


@dataclass
class Person:
    fio: str
    old: int
    salary: int = 0

