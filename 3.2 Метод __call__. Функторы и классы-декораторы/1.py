"""
Объявите класс RandomPassword для генерации случайных паролей. Объекты этого
класса должны создаваться командой:

rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length,
max_length - минимальная и максимальная длина генерируемых паролей.

Непосредственная генерация одного пароля должна выполняться командой:

psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из
случайно выбранных символов строки psw_chars.

С помощью генератора списка (list comprehension) создайте список lst_pass из
трех сгенерированных паролей объектом rnd класса RandomPassword, созданного с
параметрами:

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
P.S. Выводить на экран ничего не нужно, только создать список из паролей.

P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же
функционал с использованием замыканий функций.
"""
import random


class RandomPassword:
    """
    Класс для генерации случайных паролей.

    :ivar psw_chars: Строка из разрешенных символов для пароля.
    :ivar min_length: Минимальная длина пароля.
    :ivar max_length: Максимальная длина пароля.
    """

    def __init__(self, psw_chars: str, min_length: int, max_length: int
                 ) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs) -> str:
        """
        Генерация случайного пароля.

        :return: Случайно сгенерированный пароль.
        """
        password: str = ""
        for _ in range(random.randint(self.min_length, self.max_length)):
            password += random.choice(self.psw_chars)

        return password


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*",
                     min_length=5, max_length=20)

lst_pass = [rnd() for _ in range(3)]
