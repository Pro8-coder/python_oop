"""
Объявите класс DateString для представления дат, объекты которого создаются
командой:

date = DateString(date_string)
где date_string - строка с датой в формате:

"DD.MM.YYYY"

здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12);
YYYY - год (целое число от 1 до 3000).
Например:

date = DateString("26.05.2022")
или

date = DateString("26.5.2022") # незначащий ноль может отсутствовать
Если указанная дата в строке записана неверно (не по формату), то генерировать
исключение с помощью собственного класса:

DateError - класс-исключения, унаследованный от класса Exception.

В самом классе DateString переопределить магический метод __str__()
для формирования строки даты в формате:

"DD.MM.YYYY"

(здесь должны фигурировать незначащие нули, например, для аргумента
"26.5.2022" должна формироваться строка "26.05.2022").

Далее, в программе выполняется считывание строки из входного потока командой:

date_string = input()
Ваша задача создать объект класса DateString с аргументом date_string
и вывести объект на экран командой:

print(date) # date - объект класса DateString
Если же произошло исключение, то вывести сообщение (без кавычек):

"Неверный формат даты"

Sample Input:

1.2.1812
Sample Output:

01.02.1812
"""


class DateError(Exception):
    """Если указанная дата в строке записана неверно (не по формату)."""


class DateString:
    def _check_date(self, date: str) -> None:
        d = date.split('.')
        if not (d[0].isdigit() and 0 < int(d[0]) < 32 and
                d[1].isdigit() and 0 < int(d[1]) < 32 and
                d[2].isdigit() and 0 < int(d[2]) < 3001):
            raise DateError

    def __init__(self, date_string: str) -> None:
        self._check_date(date_string)
        self.date_string = date_string

    def __str__(self) -> str:
        result = self.date_string.split('.')
        if len(result[0]) == 1:
            result[0] = '0' + result[0]
        if len(result[1]) == 1:
            result[1] = result[1].zfill(2)
        if len(result[2]) != 4:
            result[2] = result[2].rjust(4, "0")

        return ".".join(map(str, result))


date_string = input()

try:
    date = DateString(date_string)
except DateError:
    print("Неверный формат даты")
else:
    print(date)
