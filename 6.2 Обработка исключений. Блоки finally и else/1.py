"""
В программе вводятся два значения в одну строчку через пробел. Значениями
могут быть числа, слова, булевы величины (True/False). Необходимо прочитать
эти значения из входного потока. Если оба значения являются числами,
то вычислить их сумму, иначе соединить их в одну строку с помощью оператора +
(конкатенации строк). Результат вывести на экран (в блоке finally).

P.S. Реализовать программу с использованием блоков try/except/finally.

Sample Input:

8 11
Sample Output:

19
"""
a, b = input().split()

# try:
#     result = (int(a) + int(b) if a.isdigit() and b.isdigit() else
#               float(a) + float(b))
# except ValueError:
#     result = a + b
# finally:
#     print(result)

try:
    result = int(a) + int(b)
except ValueError:
    try:
        result = float(a) + float(b)
    except ValueError:
        result = a + b
finally:
    print(result)
