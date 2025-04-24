"""
Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно
быть три слота для фильтров. Каждый слот строго для своего класса фильтра:

Mechanical - для очистки от крупных механических частиц;
Aragon - для последующей очистки воды;
Calcium - для обработки воды на третьем этапе.



Объекты классов фильтров должны создаваться командами:

filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)
Во всех объектах этих классов должен формироваться локальный атрибут:

date - дата установки фильтров (для простоты - положительное вещественное
число).

Также нужно запретить изменение этого атрибута после создания объектов этих
классов (только чтение). В случае присвоения нового значения, прежнее значение
не менять. Ошибок никаких не генерировать.

Объекты класса GeyserClassic должны создаваться командой:

g = GeyserClassic()
А сам класс иметь атрибут:

MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

add_filter(self, slot_num, filter) - добавление фильтра filter в указанный
слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра).
Также здесь следует проверять, что в первый слот можно установить только
объекты класса Mechanical, во второй - объекты класса Aragon и в третий -
объекты класса Calcium. Иначе слот должен оставаться пустым.

remove_filter(self, slot_num) - извлечение фильтра из указанного слота
(slot_num: 1, 2, и 3);

get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их
установки (по возрастанию номеров слотов);

water_on(self) - включение воды: возвращает True, если вода течет и False - в
противном случае.

Метод water_on() должен возвращать значение True при выполнении следующих
условий:

- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date)
должно быть в пределах [0; MAX_DATE_FILTER])

Пример использования классов  (эти строчки в программе писать не нужно):

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие
объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый
слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также
невозможно
P.S. На экран ничего выводить не нужно.
"""
import time


class Mechanical:
    """
    Класс для представления фильтра Mechanical.

    :ivar date: Дата установки фильтра.
    """

    def __init__(self, date: float) -> None:
        self.date = date

    def __setattr__(self, key: str, value: float) -> None:
        """
        Запрещает изменение атрибута date после его создания.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        """
        if key != "date" or not hasattr(self, "date"):
            super().__setattr__(key, value)


class Aragon:
    """
    Класс для представления фильтра Aragon.

    :ivar date: Дата установки фильтра.
    """

    def __init__(self, date: float) -> None:
        self.date = date

    def __setattr__(self, key: str, value: float) -> None:
        """
        Запрещает изменение атрибута date после его создания.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        """
        if key != "date" or not hasattr(self, "date"):
            super().__setattr__(key, value)


class Calcium:
    """
    Класс для представления фильтра Calcium.

    :ivar date: Дата установки фильтра.
    """
    def __init__(self, date: float) -> None:
        self.date = date

    def __setattr__(self, key: str, value: float) -> None:
        """
        Запрещает изменение атрибута date после его создания.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        """
        if key != "date" or not hasattr(self, "date"):
            super().__setattr__(key, value)


class GeyserClassic:
    """
    Класс для представления фильтра для очистки воды.

    :cvar MAX_DATE_FILTER: Максимальное время работы фильтра.

    :ivar slots: Список слотов для фильтров (по умолчанию все None).
    """

    MAX_DATE_FILTER: int = 100

    def __init__(self) -> None:
        self.slots: list[None | Mechanical, None | Aragon, None | Calcium] = \
            [None, None, None]

    def add_filter(self, slot_num: int,
                   filter: Mechanical | Aragon | Calcium) -> None:
        """
        Добавляет фильтр в указанный слот.

        :param slot_num: Номер слота (1, 2 или 3).
        :param filter: Объект фильтра.
        """
        if self.slots[slot_num - 1] is None:
            if (slot_num == 1 and isinstance(filter, Mechanical)) or \
                    (slot_num == 2 and isinstance(filter, Aragon)) or \
                    (slot_num == 3 and isinstance(filter, Calcium)):
                self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num: int) -> None:
        """
        Удаляет фильтр из указанного слота.

        :param slot_num: Номер слота (1, 2 или 3).
        """
        if 1 <= slot_num <= 3:
            self.slots[slot_num - 1] = None

    def get_filters(self) -> tuple:
        """
        Возвращает кортеж с текущими фильтрами.

        :return: Кортеж с фильтрами.
        """
        return *self.slots,

    def water_on(self) -> bool:
        """
        Проверяет, можно ли включить воду.

        :return: True, если вода может течь, иначе False.
        """
        return all(filter is not None and 0 <= (time.time() - filter.date) \
                   <= self.MAX_DATE_FILTER for filter in self.slots)

