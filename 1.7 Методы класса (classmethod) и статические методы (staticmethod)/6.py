"""
Объявите класс для мессенджера с именем Viber. В этом классе должны быть
следующие методы:

add_message(msg) - добавление нового сообщения в список сообщений;
remove_message(msg) - удаление сообщения из списка;
set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить
атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть,
то убирается);
show_last_message(число) - отображение последних сообщений;
total_messages() - возвращает общее число сообщений.

Эти методы предполагается использовать следующим образом (эти строчки в
программе не писать):

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Класс Message (необходимо также объявить) позволяет создавать
объекты-сообщения со следующим набором локальных свойств:

text - текст сообщения (строка);
fl_like - поставлен или не поставлен лайк у сообщения (булево значение True -
если лайк есть и False - в противном случае, изначально False);

P.S. Как хранить список сообщений, решите самостоятельно.
"""


class Message:
    """Класс, представляющий сообщение в мессенджере."""

    def __init__(self, text: str, fl_like: bool = False) -> None:
        """
        Инициализирует объект сообщения.

        :param text: Текст сообщения.
        :param fl_like: Статус лайка (по умолчанию False).
        """
        self.text = text
        self.fl_like = fl_like


class Viber:
    """Класс, представляющий мессенджер Viber."""

    __msg_lst: list[Message] = []

    @classmethod
    def add_message(cls, msg: Message) -> None:
        """
        Добавляет сообщение в список сообщений.

        :param msg: Объект сообщения для добавления.
        """
        if isinstance(msg, Message):
            cls.__msg_lst.append(msg)

    @classmethod
    def remove_message(cls, msg: Message) -> None:
        """
        Удаляет сообщение из списка сообщений.

        :param msg: Объект сообщения для удаления.
        """
        if msg in cls.__msg_lst:
            cls.__msg_lst.remove(msg)

    @classmethod
    def set_like(cls, msg: Message) -> None:
        """
        Переключает лайк для сообщения.

        :param msg: Объект сообщения, для которого нужно переключить лайк.
        """
        if msg in cls.__msg_lst:
            msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num: int) -> None:
        """
        Отображает последние сообщения.

        :param num: Количество сообщений для отображения.
        """
        if num > len(cls.__msg_lst):
            num = len(cls.__msg_lst)
        last_messages = cls.__msg_lst[-num:]
        for ms in last_messages:
            print(f"Сообщение: {ms.text}, Лайк: {ms.fl_like}")

    @classmethod
    def total_messages(cls) -> int:
        """
        Возвращает общее количество сообщений.

        :return: Количество сообщений в списке.
        """
        return len(cls.__msg_lst)

