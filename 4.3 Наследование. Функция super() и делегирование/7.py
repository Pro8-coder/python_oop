"""
Объявите класс StringDigit, который наследуется от стандартного класса str.
Объекты класса StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string
окажется хотя бы один не цифровой символ, то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор +
(конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при
соединении строк появляется не цифровой символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
Пример использования класса (эти строчки в программе не писать):

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError
P.S. В программе нужно объявить только класс. На экран выводить ничего
не нужно.
"""


class StringDigit(str):
    """
    Класс для строк, содержащих только цифры. Наследуется от str.

    Обеспечивает проверку на цифры при создании и операциях сложения.
    При нарушении этого правила вызывает ValueError.

    :ivar _value: Строковое значение (наследуется от str)
    """
    
    @classmethod
    def _check_isdigit(cls, value: str) -> None:
        """
        Проверяет, что значение состоит только из цифр.

        :param value: Проверяемая строка
        :raises ValueError: Если строка содержит нецифровые символы
        """
        if type(value) != str or not value.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __new__(cls, string: str) -> 'StringDigit':
        """
        Создает новый объект StringDigit.

        :param string: Исходная строка из цифр
        :return: Новый объект StringDigit
        :raises ValueError: Если строка содержит нецифровые символы
        """
        cls._check_isdigit(string)
        return super().__new__(cls, string)

    def __add__(self, other: str) -> 'StringDigit':
        """
        Реализует операцию сложения (sd + other).

        :param other: Строка для конкатенации
        :return: Новый объект StringDigit
        :raises ValueError: Если other содержит нецифровые символы
        """
        self._check_isdigit(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other: str) -> 'StringDigit':
        """
        Реализует операцию отраженного сложения (other + sd).

        :param other: Строка для конкатенации
        :return: Новый объект StringDigit
        :raises ValueError: Если other содержит нецифровые символы
        """
        self._check_isdigit(other)
        return StringDigit(other + str(self))

