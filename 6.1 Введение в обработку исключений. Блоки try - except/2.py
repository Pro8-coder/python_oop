"""
В программе вводятся в одну строчку через пробел некоторые данные, например:

"1 -5.6 2 abc 0 False 22.5 hello world"
Эти данные разбиваются по пробелу и представляются в виде списка строк:

lst_in = input().split()
Ваша задача посчитать сумму всех целочисленных значений, присутствующих в
списке lst_in. Результат (сумму) вывести на экран.

Подсказка: отбор только целочисленных значений можно выполнить с помощь
функции filter() с последующим их преобразованием в целые числа с помощью
функции map() и, затем, вычислением их суммы с помощью функции sum(). Для
отбора целочисленных значений рекомендуется объявить вспомогательную функцию,
которая бы возвращала True для строк, в которых присутствует целое число и
False - для всех остальных строк.

Sample Input:

8 11 abcd -7.5 2.0 -5
Sample Output:

14
"""
from typing import Any

lst_in = input().split()

# print(sum(map(int, filter(lambda x: x.lstrip('-').isdigit(), lst_in))))


# def try_int(item: Any) -> bool:
#     try:
#         int(item)
#         return True
#     except ValueError:
#         return False
#
#
# print(sum(list(map(int, (filter(try_int, lst_in))))))


result = 0
for item in lst_in:
    try:
        result += int(item)
    except ValueError:
        continue


print(result)
