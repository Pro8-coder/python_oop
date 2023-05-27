"""
Объявите класс TriangleChecker, объекты которого можно было бы создавать
командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы
возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно
число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных
пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные
значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите
результат на экран (код, который она вернет).
"""


# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        count = 0
        for i in (type(self.a), type(self.b), type(self.c)):
            if i is (int, float):
                return 1
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        for i in (self.a, self.b, self.c):
            if i < (self.a + self.b + self.c - i):
                count += 1
            if count == 3:
                return count
        return 2


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и
# вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
