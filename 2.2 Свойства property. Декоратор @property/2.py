"""
Объявите в программе класс WindowDlg, объекты которого предполагается
создавать командой:

wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться приватные локальные
атрибуты:

__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).

В классе WindowDlg необходимо реализовать метод:

show() - для отображения окна на экране (выводит в консоль строку в формате:
"<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:

width - для изменения и считывания ширины окна;
height - для изменения и считывания высоты окна.

При изменении размеров окна необходимо выполнять проверку:

- переданное значение является целым числом в диапазоне [0; 10000].

Если хотя бы один размер изменился (высота или ширина), то следует выполнить
автоматическую перерисовку окна (вызвать метод show()). При начальной
инициализации размеров width, height вызывать метод show() не нужно.

P.S. В программе нужно объявить только класс с требуемой функциональностью.
"""


class WindowDlg:
    """
    Класс, представляющий диалоговое окно с заголовком, шириной и высотой.
    """

    def __init__(self, title: str, width: int, height: int) -> None:
        """
        Инициализирует объект WindowDlg.

        :param title: Заголовок окна.
        :param width: Ширина окна.
        :param height: Высота окна.
        """
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self) -> None:
        """Отображает окно на экране, выводя информацию в консоль."""
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self) -> int:
        """
        Возвращает текущую ширину окна.

        :return: Ширина окна.
        """
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        """
        Устанавливает новую ширину окна, если она корректна.

        :param width: Новая ширина окна.
        """
        if isinstance(width, int) and -1 < width < 10001:
            self.__width = width
            self.show()

    @width.deleter
    def width(self) -> None:
        """Удаляет текущую ширину окна."""
        del self.__width

    @property
    def height(self) -> int:
        """
        Возвращает текущую высоту окна.

        :return: Высота окна.
        """
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        """
        Устанавливает новую высоту окна, если она корректна.

        :param height: Новая высота окна.
        """
        if isinstance(height, int) and -1 < height < 10001:
            self.__height = height
            self.show()

    @height.deleter
    def height(self) -> None:
        """Удаляет текущую высоту окна."""
        del self.__height

