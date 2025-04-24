"""
С помощью функции make_dataclass создайте аналог следующего класса:

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = 'gray'

    def draw(self):
        return f"window: {(self.width, self.height)}; color: {self.color}"
На созданный объект класса должна вести переменная Window. Используя
переменную Window создайте объект wnd класса с параметрами:

width=100, height=20

P.S. На экран ничего выводить не нужно.
"""
from dataclasses import make_dataclass, field

Window = make_dataclass('Window', ['width', 'height',
                                   ('color', str, field(default='gray'))],
                        namespace={'draw': lambda self:
                                   f"window: {(self.width, self.height)}; "
                                   f"color: {self.color}"})


wnd = Window(100, 20)
