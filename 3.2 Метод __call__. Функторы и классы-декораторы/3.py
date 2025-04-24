"""
Предположим, мы разрабатываем класс для обработки формы авторизации на стороне
сервера. Для этого был создан следующий класс с именем LoginForm:

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True
Здесь name - это заголовок формы (строка); validators - список из валидаторов
для проверки корректности поля. В методе post параметр request - это словарь с
ключами 'login' и 'password' и значениями (строками) для логина и пароля
соответственно.

Пример использования класса LoginForm (в программе не писать):

from string import ascii_lowercase, digits

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50),
CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
Вам необходимо в программе объявить классы валидаторов:

LengthValidator - для проверки длины данных в диапазоне [min_length;
max_length];
CharsValidator - для проверки допустимых символов в строке.

Объекты этих классов должны создаваться командами:

lv = LengthValidator(min_length, max_length) # min_length - минимально
допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator(chars) # chars - строка из допустимых символов
Для проверки корректности данных каждый валидатор должен вызываться как
функция:

res = lv(string)
res = cv(string)
и возвращать True, если string удовлетворяет условиям валидатора и False - в
противном случае.

P.S. В программе следует только объявить два класса валидаторов, на экран
выводить ничего не нужно.
"""
from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator


class LengthValidator:
    """
    Валидатор для проверки длины строки.

    :ivar min_length: Минимально допустимая длина строки.
    :ivar max_length: Максимально допустимая длина строки.
    """
    def __init__(self, min_length: int, max_length: int) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, item: str, *args, **kwargs) -> bool:
        """
        Проверяет, что длина строки находится в допустимом диапазоне.

        :param item: Строка для проверки.
        :return: True, если длина строки корректна, иначе False.
        """
        return self.min_length <= len(item) <= self.max_length


class CharsValidator:
    """
    Валидатор для проверки допустимых символов в строке.

    :ivar chars: Строка из допустимых символов.
    """
    def __init__(self, chars: str) -> None:
        self.chars = chars

    def __call__(self, item: str, *args, **kwargs) -> bool:
        """
        Проверяет, что все символы строки допустимы.

        :param item: Строка для проверки.
        :return: True, если все символы допустимы, иначе False.
        """
        return all(char in self.chars for char in item)

