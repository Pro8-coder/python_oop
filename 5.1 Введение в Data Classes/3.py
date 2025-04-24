"""
С помощью декоратора dataclass и функции field:

from dataclasses import dataclass, field
объявите Data Class с именем Student и следующим набором полей (порядок важен):

fio (строка: фамилия, имя, отчество);
group (строка: группа);
marks (list: оценки студента; начальное значение - пустой список).
Создайте два объекта с именами s1, s2 класса Student и данными:

s1: "Ганди Индира"; group: "МГИМО-11"; marks: [5, 4, 3];
s2: "Манделла Нельсон"; group: "МГИМО-32"; marks: [].
P.S. На экран ничего выводить не нужно.
"""
from dataclasses import dataclass, field


@dataclass
class Student:
    fio: str
    group: str
    marks: list = field(default_factory=list)


s1 = Student("Ганди Индира", "МГИМО-11", [5, 4, 3])
s2 = Student("Манделла Нельсон", "МГИМО-32", [])
