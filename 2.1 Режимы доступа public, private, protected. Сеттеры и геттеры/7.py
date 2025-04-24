"""
Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров
должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату:
xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский
буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False -
в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания,
точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то
возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед
проверкой корректности email. Если параметр email не является строкой,
то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать
не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить
не нужно.
"""
import random
from string import ascii_lowercase, ascii_uppercase, digits


class EmailValidator:
    """Класс для проверки корректности email-адресов."""
    valid: str = ascii_lowercase + ascii_uppercase + digits + "_"

    def __new__(cls, *args, **kwargs) -> None:
        """Запрещает создание объектов класса. Всегда возвращает None."""
        return None

    @staticmethod
    def __is_email_str(email: str) -> bool:
        """
        Проверяет, является ли email строкой.

        :param email: Объект для проверки.
        :return: True, если email — строка, иначе False.
        """
        return isinstance(email, str)

    @classmethod
    def get_random_email(cls) -> str:
        """
        Генерирует случайный email-адрес.

        :return: Случайный email-адрес в формате xxxxxxx...xxx@gmail.com.
        """
        user_length: int = random.randint(1, 100)
        domain: str = "gmail.com"
        user_part: str = ''.join(
            random.choice(cls.valid) for _ in range(user_length))
        return f"{user_part}@{domain}"

    @classmethod
    def check_email(cls, email: str) -> bool:
        """
        Проверяет корректность email-адреса.

        :param email: Email-адрес для проверки.
        :return: True, если email корректен, иначе False.
        """
        if cls.__is_email_str(email) \
                and all(char in cls.valid + '.@' for char in email) \
                and email.count('@') == 1:
            eml = email.split('@')
            if len(eml[0]) < 101 and len(eml[1]) < 51 and '.' in eml[1] \
                    and '..' not in eml[0] + eml[1]:
                return True

        return False

