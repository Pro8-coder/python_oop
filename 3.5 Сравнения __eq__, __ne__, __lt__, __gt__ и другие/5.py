"""
Перед вами стоит задача выделения файлов с определенными расширениями из
списка файлов, например:

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc",
"my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
Для этого необходимо объявить класс FileAcceptor, объекты которого создаются
командой:

acceptor = FileAcceptor(ext1, ..., extN)
где ext1, ..., extN - строки с допустимыми расширениями файлов, например:
'jpg', 'bmp', 'jpeg'.

После этого предполагается использовать объект acceptor в стандартной функции
filter языка Python следующим образом:

filenames = list(filter(acceptor, filenames))
То есть, объект acceptor должен вызываться как функция:

acceptor(filename)
и возвращать True, если файл с именем filename содержит расширения, указанные
при создании acceptor, и False - в противном случае. Кроме того, с объектами
класса FileAcceptor должен выполняться оператор:

acceptor12 = acceptor1 + acceptor2
Здесь формируется новый объект acceptor12 с уникальными расширениями первого и
второго объектов. Например:

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
Пример использования класса (эти строчки в программе писать не нужно):

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
P.S. На экран в программе ничего выводить не нужно.
"""


class FileAcceptor:
    """
    Класс для фильтрации файлов по их расширениям.

    :ivar args: Расширения файлов, которые будут приняты.
    """

    def __init__(self, *args: str) -> None:
        self.extensions: set[str] = set(ext.lower() for ext in args)

    def __call__(self, filename: str) -> bool:
        """
        Проверяет, соответствует ли файл заданным расширениям.

        :param filename: Имя файла с расширением.
        :return: True, если расширение файла содержится в допустимых,
        иначе False.
        """
        return (filename.split(".")[-1].lower() in self.extensions
                if "." in filename else False)

    def __add__(self, other: 'FileAcceptor') -> 'FileAcceptor':
        """
        Объединяет расширения двух объектов FileAcceptor.

        :param other: Другой объект FileAcceptor.
        :return: Новый объект FileAcceptor с объединёнными расширениями.
        """
        if isinstance(other, FileAcceptor):
            return FileAcceptor(*self.extensions.union(other.extensions))

