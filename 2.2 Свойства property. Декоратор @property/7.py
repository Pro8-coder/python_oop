"""
Вы создаете телефонную записную книжку. Она определяется классом PhoneBook.
Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты
этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр,
X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии
с заданием.

Пример использования классов (эти строчки в программе писать не нужно):

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
P.S. В программе требуется объявить только классы. На экран ничего выводить
не нужно.
"""


class PhoneNumber:
    """Класс для представления телефонного номера."""

    def __init__(self, number: int, fio: str) -> None:
        """
        Инициализация объекта PhoneNumber.

        :param number: Номер телефона (11 цифр).
        :param fio: ФИО владельца номера.
        """
        if not isinstance(number, int) or len(str(number)) != 11:
            raise ValueError("Номер телефона должен быть 11-значным числом.")
        if not isinstance(fio, str):
            raise ValueError("ФИО должно быть строкой.")

        self.number = number
        self.fio = fio


class PhoneBook:
    """Класс для управления телефонной книгой."""

    def __init__(self) -> None:
        """Инициализация объекта PhoneNumber."""
        self.phone_list: list[PhoneNumber] = []

    def add_phone(self, phone: PhoneNumber) -> None:
        """
        Добавляет новый номер телефона в книгу.

        :param phone: Объект класса PhoneNumber.
        """
        self.phone_list.append(phone)

    def remove_phone(self, indx: int) -> None:
        """
        Удаляет номер телефона по индексу.

        :param indx: Индекс номера в списке.
        """
        del self.phone_list[indx]

    def get_phone_list(self) -> list[PhoneNumber]:
        """
        Возвращает список всех номеров телефонов.

        :return: Список объектов PhoneNumber.
        """
        return self.phone_list

