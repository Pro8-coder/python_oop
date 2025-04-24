"""
В программе вводятся в одну строчку через пробел некоторые данные, например:

"1 -5.6 True abc 0 23.56 hello"
Эти данные разбиваются по пробелу и представляются в виде списка строк:

lst_in = input().split()
Ваша задача сформировать новый список с именем lst_out, в котором строки с
целыми числами будут представлены как целые числа (тип int), строки с
вещественными числами, как вещественные (тип float), а остальные данные -
без изменений.

Например:

lst_out = [1, -5.6, 'True', 'abc', 0, 23.56, 'hello']  # после обработки
введенной строки "1 -5.6 True abc 0 23.56 hello"
Реализовать эту задачу следует с помощью функции map() и объявления
вспомогательной функции с механизмом обработки исключений для
непосредственного преобразования данных в целые или вещественные числа.

P.S. В программе нужно только сформировать список lst_out. На экран ничего
выводить не нужно.

Sample Input:

hello 1 world -2 4.5 True
Sample Output:
"""

lst_in = input().split()

# lst_out = []
# for item in lst_in:
#     try:
#         lst_out.append(int(item))
#     except ValueError:
#         try:
#             lst_out.append(float(item))
#         except ValueError:
#             lst_out.append(item)


def filter_int_float(item):
    try:
        return int(item)
    except ValueError:
        try:
            return float(item)
        except ValueError:
            return item


lst_out = list(map(filter_int_float, lst_in))
