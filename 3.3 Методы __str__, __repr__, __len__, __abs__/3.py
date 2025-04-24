"""
Объявите класс WordString, объекты которого создаются командами:

w1 = WordString()
w2 = WordString(string)
где string - передаваемая строка. Например:

words = WordString("Курс по Python ООП")
Реализовать следующий функционал для объектов этого класса:

len(words) - должно возвращаться число слов в переданной строке (слова
разделяются одним или несколькими пробелами);
words(indx) - должно возвращаться слово по его индексу (indx - порядковый
номер слова в строке, начиная с 0).

Также в классе WordString реализовать объект-свойство (property):

string - для передачи и считывания строки.

Пример пользования классом WordString (эти строчки в программе писать
не нужно):

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
P.S. В программе нужно только объявить класс, выводить в консоль ничего
не нужно.
"""


class WordString:
    """
    Класс для работы со строками, где слова разделены пробелами.

    :ivar string: Строка для инициализации объекта (по умолчанию пустая).
    """

    def __init__(self, string: str = "") -> None:
        self.string = string

    @property
    def string(self) -> str:
        """
        Возвращает текущую строку.

        :return: Текущая строка.
        """
        return self.__string

    @string.setter
    def string(self, value: str) -> None:
        """
        Устанавливает новую строку.

        :param value: Новая строка.
        """
        self.__string = value

    def __len__(self) -> int:
        """
        Возвращает количество слов в строке.

        :return: Количество слов.
        """
        return len(self.__string.split())

    def __call__(self, indx: int, *args, **kwargs) -> str:
        """
        Возвращает слово по его индексу.

        :param indx: Индекс слова (начиная с 0).
        :return: Слово по указанному индексу.
        """
        words: list[str] = self.__string.split()

        if 0 <= indx < len(words):
            return words[indx]
        else:
            return ""

