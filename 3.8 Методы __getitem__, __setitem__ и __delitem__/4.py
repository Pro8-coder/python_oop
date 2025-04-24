"""
Вам необходимо написать программу для удобного обращения с таблицами
однотипных данных (чисел, строк, булевых значений и т.п.), то есть, все ячейки
таблицы должны представлять какой-то один указанный тип.

Для этого в программе необходимо объявить три класса:

TableValues - для работы с таблицей в целом;
CellInteger - для операций с целыми числами;
IntegerValue - дескриптор данных для работы с целыми числами.

Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных (то есть,
и для записи и считывания значений). Если присваиваемое значение не является
целым числом, должно генерироваться исключение командой:

raise ValueError('возможны только целочисленные значения')
Следующий класс CellInteger описывает одну ячейку таблицы для работы с целыми
числами. В этом классе должен быть публичный атрибут (атрибут класса):

value - объект дескриптора, класса IntegerValue.

А объекты класса CellInteger должны создаваться командой:

cell = CellInteger(start_value)
где start_value - начальное значение ячейки (по умолчанию равно 0 и
сохраняется в ячейке через дескриптор value).

Наконец, объекты последнего класса TableValues создаются командой:

table = TableValues(rows, cols, cell=CellInteger)
где rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс,
описывающий работу с отдельными ячейками таблицы. Если параметр cell
не указан, то генерировать исключение командой:

raise ValueError('параметр cell не указан')
Иначе, в объекте table класса TableValues создается двумерный (вложенный)
кортеж с именем cells размером rows x cols, состоящий из объектов указанного
класса (в данном примере - класса CellInteger).

Также в классе TableValues предусмотреть возможность обращения к отдельной
ячейке по ее индексам, например:

value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
table[0, 0] = value # записывает новое значение в ячейку (0, 0)
Обратите внимание, по индексам сразу должно возвращаться значение ячейки,
а не объект класса CellInteger. И то же самое с присваиванием нового значения.

Пример использования классов (эти строчки в программе не писать):

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
P.S. В программе нужно объявить только классы. Выводить на экран ничего
не нужно.

P.P.S. В качестве домашнего задания создайте класс CellString для работы со
строками и используйте тот же класс TableValues для этого нового типа данных.

Последнее: дескрипторы здесь для повторения. В реальной разработке лучше
использовать в таких задачах объекты-свойства (property).
"""
from typing import Any


class IntegerValue:
    """
    Дескриптор данных для работы с целочисленными значениями.

    Обеспечивает валидацию типа данных при присваивании значений атрибутам.
    Генерирует ValueError при попытке установить нецелочисленное значение.

    :ivar owner: Класс-владелец дескриптора
    :ivar name: Имя управляемого атрибута
    """

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name

    def __get__(self, instance: object, owner: type) -> int:
        """
        Возвращает значение атрибута.

        :param instance: Экземпляр класса-владельца
        :param owner: Класс-владелец
        :return: Текущее значение атрибута
        """
        return instance.__dict__.get(self.name)

    def __set__(self, instance: object, value: int) -> None:
        """
        Устанавливает новое значение с проверкой типа.

        :param instance: Экземпляр класса-владельца
        :param value: Присваиваемое значение
        :raises ValueError: Если значение не является целым числом
        """
        if type(value) == int:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('возможны только целочисленные значения')


class StringValue:
    """
    Дескриптор данных для работы со строковыми значениями.

    Обеспечивает валидацию типа данных при присваивании значений атрибутам.
    Генерирует ValueError при попытке установить не строковое значение.

    :ivar owner: Класс-владелец дескриптора
    :ivar name: Имя управляемого атрибута
    """

    def __set_name__(self, owner: object, name: str) -> None:
        self.name = name

    def __get__(self, instance: object, owner: type) -> str:
        """
        Возвращает значение атрибута.

        :param instance: Экземпляр класса-владельца
        :param owner: Класс-владелец
        :return: Текущее значение атрибута
        """
        return instance.__dict__.get(self.name)

    def __set__(self, instance: object, value: str) -> None:
        """
        Устанавливает новое значение с проверкой типа.

        :param instance: Экземпляр класса-владельца
        :param value: Присваиваемое значение
        :raises ValueError: Если значение не является строкой
        """
        if type(value) == str:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('возможны только строковые значения')


class CellInteger:
    """
    Ячейка таблицы для хранения целочисленных значений.

    Использует IntegerValue в качестве дескриптора данных для поля value.

    :cvar value: Дескриптор для работы со строковыми значениями
    """

    value = IntegerValue()

    def __init__(self, start_value: int = 0) -> None:
        """
        Инициализирует ячейку с начальным значением.

        :param start_value: Начальное значение ячейки
        """
        self.value = start_value


class CellString:
    """
    Ячейка таблицы для хранения строковых значений.

    Использует StringValue в качестве дескриптора данных для поля value.

    :cvar value: Дескриптор для работы со строковыми значениями
    """

    value = StringValue()

    def __init__(self, start_value: str = "_") -> None:
        """
        Инициализирует ячейку с начальным значением.

        :param start_value: Начальное значение ячейки
        """
        self.value = start_value


class TableValues:
    """
    Таблица значений с фиксированным размером и типом ячеек.

    Поддерживает двумерную индексацию и контроль типов данных.
    """

    def __init__(self, rows: int, cols: int, cell: type | None = None) -> None:
        """
        Инициализирует таблицу указанного размера.

        :param rows: Количество строк в таблице
        :param cols: Количество столбцов в таблице
        :param cell: Класс ячеек таблицы
        :raises ValueError: Если не указан класс ячеек
        """
        if not cell:
            raise ValueError('параметр cell не указан')

        self.rows = rows
        self.cols = cols
        self.cells: tuple[tuple[Any, ...], ...] = tuple(tuple(
            cell() for _ in range(cols)
        ) for _ in range(rows))

    def __getitem__(self, item: tuple[int, int]) -> Any:
        """
        Возвращает значение ячейки по индексу.

        :param item: Кортеж с индексами (строка, столбец)
        :return: Значение запрошенной ячейки
        """
        if len(item) == 2:
            row, col = item
            if (type(row) == int and -self.rows <= row < self.rows and
                    type(col) == int and -self.cols <= col < self.cols):
                return self.cells[row][col].value

    def __setitem__(self, key: tuple[int, int], value: Any) -> None:
        """
        Устанавливает новое значение ячейки по индексу.

        :param key: Кортеж с индексами (строка, столбец)
        :param value: Новое значение ячейки
        """
        if len(key) == 2:
            row, col = key
            if (type(row) == int and -self.rows <= row < self.rows and
                    type(col) == int and -self.cols <= col < self.cols):
                self.cells[row][col].value = value

