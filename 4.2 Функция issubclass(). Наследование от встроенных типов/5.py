"""
Необходимо в программе объявить класс VideoItem для представления одного видео
(например, в youtube). Объекты этого класса должны создаваться командой:

video = VideoItem(title, descr, path)
где title - заголовок видео (строка); descr - описание видео (строка);
path - путь к видеофайлу. В каждом объекте класса VideoItem должны создаваться
соответствующие атрибуты: title, descr, path.

Затем, нужно создать класс для формирования оценки видео в баллах от 0 до 5.
Для этого нужно объявить еще один класс с именем VideoRating, объекты которого
создаются командой:

rating = VideoRating()
В каждом объекте класса VideoRating должен быть локальный приватный атрибут с
именем __rating, содержащий целое число от 0 до 5 (по умолчанию 0). А для
записи и считывания значения из этого приватного атрибута должно быть
объект-свойство (property) с именем rating.

Так как атрибут __rating - это целое число в диапазоне [0; 5], то в момент
присвоения ему какого-либо значения необходимо проверять, что присваиваемое
значение - целое число в диапазоне [0; 5]. Если это не так, то генерировать
исключение командой:

raise ValueError('неверное присваиваемое значение')
Далее, в каждом объекте класса VideoItem должен быть локальный атрибут
rating - объект класса VideoRating.

Пример использования классов (эти строчки в программе не писать):

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР',
'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError
P.S. В программе нужно объявить только класс. На экран выводить ничего
не нужно.
"""


class VideoItem:
    """
    Класс для представления видео с возможностью оценки.

    :param title: Заголовок видео
    :param descr: Описание видео
    :param path: Путь к видеофайлу
    """

    def __init__(self, title: str, descr: str, path: str) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    """
    Класс для оценки видео в диапазоне от 0 до 5 баллов.

    Содержит приватный атрибут __rating и property для безопасного доступа
    к нему.
    """

    def __init__(self) -> None:
        self.__rating = 0

    @property
    def rating(self) -> int:
        """
        Возвращает текущий рейтинг видео.

        :return: Текущая оценка от 0 до 5
        """
        return self.__rating

    @rating.setter
    def rating(self, value: int) -> None:
        """
        Устанавливает новое значение рейтинга.

        :param value: Новая оценка (должна быть целым числом от 0 до 5)
        :raises ValueError: Если значение вне допустимого диапазона
        """
        if type(value) == int and -1 < value < 6:
            self.__rating = value
        else:
            raise ValueError('неверное присваиваемое значение')

