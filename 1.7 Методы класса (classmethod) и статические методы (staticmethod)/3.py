"""
 Объявите класс CardCheck для проверки корректности информации на пластиковых
 картах. Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает
булево значение True, если номер в верном формате и False - в противном
случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра
(от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты.
Возвращает булево значение True, если имя записано верно и False - в
противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными
латинскими символами и цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в
программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name
(декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        # Проверка, что number является строкой
        if not isinstance(number, str):
            return False

        parts = number.split('-')

        # Проверяем, что получилось 4 части, каждая из которых состоит из 4 цифр
        if len(parts) != 4 or not all(
                len(part) == 4 and part.isdigit() for part in parts):
            return False

        return True

    @staticmethod
    def check_name(name):
        # Проверка, что name является строкой
        if not isinstance(name, str):
            return False

        # Проверка формата имени: два слова, состоящих из допустимых символов
        if len(name.split()) != 2:
            return False
        return all(
            char in CardCheck.CHARS_FOR_NAME for char in name.replace(" ", ""))

