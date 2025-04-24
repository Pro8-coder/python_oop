"""
Объявите класс ValidateString для проверки корректности переданной строки.
Объекты этого класса создаются командой:

validate = ValidateString(min_length=3, max_length=100)
где min_length - минимальное число символов в строке; max_length -
максимальное число символов в строке.
В классе ValidateString должен быть реализован метод:

validate(self, string) - возвращает True, если string является строкой
(тип str) и длина строки в пределах [min_length; max_length]. Иначе
возвращается False.

Объявите дескриптор данных StringValue для работы со строками, объекты
которого создаются командой:

st = StringValue(validator=ValidateString(min_length, max_length))
При каждом присвоении значения объекту st должен вызываться валидатор (объект
класса ValidateString) и с помощью метода validate() проверяться корректность
присваиваемых данных. Если данные некорректны, то присвоение не выполняется
(игнорируется).

Объявите класс RegisterForm с тремя объектами дескриптора StringValue:

login = StringValue(...) - для ввода логина;
password = StringValue(...)  - для ввода пароля;
email = StringValue(...)  - для ввода Email.

Объекты класса RegisterForm создаются командой:

form = RegisterForm(логин, пароль, email)
где логин, пароль, email - начальные значения логина, пароля и Email.
В классе RegisterForm также должны быть объявлены методы:

get_fields() - возвращает список из значений полей в порядке [login, password,
email];
show() - выводит в консоль многострочную строку в формате:

<form>
Логин: <login>
Пароль: <password>
Email: <email>
</form>

P.S. В программе требуется объявить классы с описанным функционалом. На экран
в программе выводить ничего не нужно.
"""


class ValidateString:
    """Класс для проверки корректности строки."""

    def __init__(self, min_length: int = 3, max_length: int = 100) -> None:
        """
        Инициализирует объект ValidateString.

        :param min_length: Минимальная длина строки.
        :param max_length: Максимальная длина строки.
        """
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string: str) -> bool:
        """
        Проверяет, является ли строка корректной.

        :param string: Строка для проверки.
        :return: True, если строка корректна, иначе False.
        """
        return isinstance(string, str) and self.min_length <= len(
            string) <= self.max_length


class StringValue:
    """Дескриптор для работы со строками."""

    def __init__(self, validator: ValidateString) -> None:
        """
        Инициализация объекта дескриптора.

        :param validator: Объект класса ValidateString для проверки значений.
        """
        self.validator = validator

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Устанавливает имя атрибута, к которому привязан дескриптор.

        :param owner: Класс, в котором определён дескриптор.
        :param name: Имя атрибута, к которому привязан дескриптор.
        """
        self.name = name

    def __get__(self, instance: object, owner: type) -> str:
        """
        Возвращает значение атрибута.

        :param instance: Экземпляр класса, в котором определён дескриптор.
        :param owner: Класс, в котором определён дескриптор.
        :return: Значение атрибута.
        """
        return instance.__dict__.get(self.name)

    def __set__(self, instance: object, value: str) -> None:
        """
        Устанавливает значение атрибута.

        :param instance: Экземпляр класса, в котором определён дескриптор.
        :param value: Значение, которое нужно присвоить атрибуту.
        """
        if self.validator.validate(value):
            instance.__dict__[self.name] = value


class RegisterForm:
    """
    Класс для регистрационной формы.

    :cvar login: Дескриптор для логина.
    :cvar password: Дескриптор для пароля.
    :cvar email: Дескриптор для Email.
    """

    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login: str, password: str, email: str) -> None:
        """
        Инициализация объекта формы.

        :param login: Начальное значение логина.
        :param password: Начальное значение пароля.
        :param email: Начальное значение Email.
        """
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self) -> list[str]:
        """
        Возвращает список значений полей.

        :return: Список значений в порядке [login, password, email].
        """
        return [self.login, self.password, self.email]

    def show(self) -> None:
        """
        Выводит в консоль многострочную строку с текущими значениями полей.
        """
        print(f'<form>\nЛогин: {self.login}\n'
              f'Пароль: {self.password}\nEmail: {self.email}\n</form>')

