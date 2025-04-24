"""
Объявите в программе класс MailBox (почтовый ящик), объекты которого
создаются командой:

mail = MailBox()
Каждый объект этого класса должен содержать локальный публичный атрибут:

inbox_list - список из принятых писем.

Также в классе MailBox должен присутствовать метод:

receive(self) - прием новых писем

Этот метод должен читать данные из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
В результате формируется список lst_in из строк. Каждая строка записана
в формате:

"от кого; заголовок; текст письма"

Например:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб.,
чтобы его получить.

Каждая строчка списка lst_in должна быть представлена объектом класса
MailItem, объекты которого создаются командой:

item = MailItem(mail_from, title, content)
где mail_from - email отправителя (строка); title - заголовок письма (строка),
content - содержимое письма (строка). В каждом объекте класса MailItem должны
формироваться соответствующие локальные атрибуты (с именами: mail_from, title,
content). И дополнительно атрибут is_read (прочитано ли) с начальным значением
False.

В классе MailItem должен быть реализован метод:

set_read(self, fl_read) - для отметки, что письмо прочитано (метод должен
устанавливать атрибут is_read = fl_read, если True, то письмо прочитано,
если False, то не прочитано).

С каждым объектом класса MailItem должна работать функция:

bool(item)
которая возвращает True для прочитанного письма и False для непрочитанного.

Вызовите метод:

mail.receive()
Отметьте первое и последнее письмо в списке mail.inbox_list, как прочитанное
(используйте для этого метод set_read). Затем, сформируйте в программе список
(глобальный) с именем inbox_list_filtered из прочитанных писем, используя
стандартную функцию filter() совместно с функцией bool() языка Python.

P.S. На экран ничего выводить не нужно.

Sample Input:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб.,
чтобы его получить.
"""
import sys


class MailItem:
    """
    Класс, представляющий почтовое сообщение.

    :ivar mail_from: Email отправителя
    :ivar title: Заголовок письма
    :ivar content: Содержимое письма
    :ivar is_read: Статус прочтения письма
    """

    def __init__(self, mail_from: str, title: str, content: str) -> None:
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read: bool) -> None:
        """
        Устанавливает статус прочтения письма.

        :param fl_read: Флаг прочтения
        """
        self.is_read = fl_read

    def __bool__(self) -> bool:
        """
        Определяет логическое значение объекта.

        :return: True если письмо прочитано, иначе False
        """
        return self.is_read


class MailBox:
    """
    Класс, представляющий почтовый ящик.

    :ivar inbox_list: Список входящих писем
    """

    def __init__(self) -> None:
        self.inbox_list = []

    def receive(self) -> None:
        """Принимает и обрабатывает входящие письма из stdin."""
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for mail in lst_in:
            self.inbox_list.append(MailItem(*mail.split('; ')))


mail = MailBox()
mail.receive()
if mail:
    mail.inbox_list[0].is_read = True
    mail.inbox_list[-1].is_read = True

inbox_list_filtered = [*filter(bool, mail.inbox_list)]
