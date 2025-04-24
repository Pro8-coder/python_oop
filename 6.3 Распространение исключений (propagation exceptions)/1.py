"""
Объявите функцию с сигнатурой:

def input_int_numbers(): ...

которая бы считывала строку из введенных целых чисел, записанных через пробел,
и возвращала кортеж из введенных чисел (в виде целых чисел, а не строк).

Если хотя бы одно значение не является целым числом, то генерировать
исключение, командой:

raise TypeError('все числа должны быть целыми')
Вызовите эту функцию в цикле до тех пор, пока пользователь не введет в строке
все целочисленные значения (то есть, цикл завершается, когда функция
отработает штатно, без генерации исключения).

Выведите на экран прочитанные значения, записанные в виде строки через пробел.

Sample Input:

1 abc 3 5
2.4 -5 4 3 2
0 -5 8 11
1 2 3 4
Sample Output:

0 -5 8 11
"""


def input_int_numbers():
    lst_inp = input().split()
    result = []
    for num in lst_inp:
        if num.replace("-", "").isdigit():
            result.append(int(num))
        else:
            raise TypeError('все числа должны быть целыми')

    return tuple(result)


while True:
    try:
        result = input_int_numbers()
    except TypeError:
        continue
    else:
        print(*[f"{i}" for i in result])
        break
