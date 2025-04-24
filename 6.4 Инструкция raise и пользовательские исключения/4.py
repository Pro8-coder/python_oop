"""
Вам поручается разработать класс TupleData, элементами которого могут являются
только объекты классов: CellInteger, CellFloat и CellString.

Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString,
объекты которых создаются командами:

cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в
ячейке; min_length, max_length - минимальная и максимальная допустимая длина
строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с
именами _min_value, _max_value или _min_length, _max_length и соответствующими
значениями.

Запись и считывание текущего значения в ячейке должно выполняться через
объект-свойство (property) с именем:

value - для записи и считывания значения в ячейке (изначально возвращает
значение None).

Если в момент записи новое значение не соответствует диапазону
[min_value; max_value] или [min_length; max_length], то генерируется
исключения командами:

raise CellIntegerException('значение выходит за допустимый диапазон')
# для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')
# для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')
# для объектов класса CellString
Все три класса исключений должны быть унаследованы от одного общего класса:

CellException

Далее, объявите класс TupleData, объекты которого создаются командой:

ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString
(в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:

value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index
Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом.
Если значение index выходит за диапазон [0; число ячеек-1], то генерировать
исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и
операторы:

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты
ячеек)
    print(d)
Все эти классы в программе можно использовать следующим образом:

ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10),
CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран
отображать ничего не нужно.
"""
from typing import Any, Iterator


class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, '_' + key, value)
        self._value: int | float | str | None = None

    @property
    def value(self) -> int | float | str | None:
        return self._value

    @value.setter
    def value(self, value: int | float | str) -> None:
        self._value = self._check_value(value)

    def _check_value(self, value: Any) -> Any:
        raise NotImplementedError(
            "Метод '_check_value' должен быть переопределен.")


class CellInteger(Cell):
    def __init__(self, min_value: int, max_value: int) -> None:
        super().__init__(min_value=min_value, max_value=max_value)

    def _check_value(self, value: int) -> int:
        if (type(value) != int or
                not self._min_value <= value <= self._max_value):
            raise CellIntegerException(
                'значение выходит за допустимый диапазон')

        return value


class CellFloat(Cell):
    def __init__(self, min_value: int, max_value: int) -> None:
        super().__init__(min_value=min_value, max_value=max_value)

    def _check_value(self, value: float) -> float:
        if (type(value) != float or
                not self._min_value <= value <= self._max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')

        return value


class CellString(Cell):
    def __init__(self, min_length: int, max_length: int) -> None:
        super().__init__(min_length=min_length, max_length=max_length)

    def _check_value(self, value: str) -> str:
        if (type(value) != str or
                not self._min_length <= len(value) <= self._max_length):
            raise CellStringException(
                'длина строки выходит за допустимый диапазон')

        return value


class TupleData:
    @staticmethod
    def __check_type(item: CellInteger | CellFloat | CellString):
        if not isinstance(item, Cell):
            raise TypeError(
                "элементами класса TupleData могут быть только представители "
                "семейства класса Cell")

    def __init__(self, *args: CellInteger | CellFloat | CellString) -> None:
        [self.__check_type(item) for item in args]
        self.cells = args

    def __getitem__(self, index: int) -> int | float | str:
        return self.cells[index].value

    def __setitem__(self, index: int, value: int | float | str) -> None:
        self.cells[index].value = value

    def __len__(self) -> int:
        return len(self.cells)

    def __iter__(self) -> Iterator[int | float | str]:
        for x in self.cells:
            yield x.value
