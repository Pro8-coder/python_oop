"""
Объявите класс с именем ValidatorString, объекты которого создаются командой:

vs = ValidatorString(min_length, max_length, chars)
где min_length, max_length - минимально и максимально допустимая длина строки
(целые числа, формируемые диапазон [min_length; max_length]); chars - строка
из набора символов (хотя бы один из них должен присутствовать в проверяемой
строке). Если chars - пустая строка, то проверку на вхождение символов
не делать.

В самом классе ValidatorString объявите метод:

def is_valid(self, string): ...

который проверяет строку string на соответствие критериям: string должна быть
строкой, с длиной в диапазоне [min_length; max_length] и в string присутствует
хотя бы один символ из chars. Если хотя бы один из этих критериев
не выполняется, то генерируется исключение командой:

raise ValueError('недопустимая строка')
Затем, объявите класс с именем LoginForm, объекты которого создаются командой:

lg = LoginForm(login_validator, password_validator)
где login_validator - валидатор для логина (объект класса ValidatorString);
password_validator - валидатор для пароля (объект класса ValidatorString).

В самом классе LoginForm объявите следующий метод:

def form(self, request): ...

где request - объект запроса (словарь). В словаре request должен быть ключ
'login' со значением введенного логина (строки) и ключ 'password' со значением
введенного пароля (строка). Если хотя бы одного ключа нет, то генерировать
исключение командой:

raise TypeError('в запросе отсутствует логин или пароль')
В противном случае (если проверка для request прошла), проверять корректность
полученного формой логина и пароля с помощью валидаторов, указанных в
параметрах login_validator и password_validator, при создании объекта формы.

Если логин/пароль введены верно, то в объекте класса LoginForm локальным
атрибутам _login и _password присвоить соответствующие значения.

Пример использования классов (эти строчки должны быть в программе):

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
Sample Input:

sergey balakirev!
Sample Output:

sergey
"""


class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str) -> None:
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string: str) -> None:
        if (type(string) != str or
                not self.min_length <= len(string) <= self.max_length):
            raise ValueError('недопустимая строка')
        if self.chars:
            if not any(s in string for s in self.chars):
                raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator: ValidatorString,
                 password_validator: ValidatorString) -> None:
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request: dict[str, str]) -> None:
        if 'login' in request and 'password' in request:
            self.login_validator.is_valid(request['login'])
            self.password_validator.is_valid(request['password'])
            self._login = request['login']
            self._password = request['password']
        else:
            raise TypeError('в запросе отсутствует логин или пароль')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
