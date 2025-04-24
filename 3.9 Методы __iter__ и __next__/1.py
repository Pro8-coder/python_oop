"""
Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка); job - наименование должности (строка); old
- возраст (целое число); salary - зарплата (число: целое или вещественное);
year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные
атрибуты с такими же именами: fio, job, old, salary, year_job и
соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута
(порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения
value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary,
year_job
    print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть
целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
Пример использования класса (эти строчки в программе не писать):

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего
не нужно.
"""


class Person:
    """
    Класс для представления сотрудника с возможностью доступа к атрибутам по
    индексу.

    :ivar fio: ФИО сотрудника
    :ivar job: Должность сотрудника
    :ivar old: Возраст сотрудника
    :ivar salary: Зарплата сотрудника
    :ivar year_job: Стаж работы
    :ivar _attributes: Список имен атрибутов в порядке их индексации
    :ivar _iter_index: Текущий индекс для итерации
    """

    def __init__(self, fio: str, job: str, old: int,
                 salary: int | float, year_job: int) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attributes = ['fio', 'job', 'old', 'salary', 'year_job']
        self._iter_index = 0

    def _check_index(self, index: int) -> None:
        """
        Проверяет корректность индекса атрибута.

        :param index: Проверяемый индекс
        :raises IndexError: Если индекс не целое число или вне диапазона [0; 4]
        """
        if type(index) != int or not 0 <= index <= 4:
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int) -> str | int | float:
        """
        Возвращает значение атрибута по индексу.

        :param item: Индекс атрибута
        :return: Значение соответствующего атрибута
        :raises IndexError: Если индекс некорректен
        """
        self._check_index(item)
        return getattr(self, self._attributes[item])

    def __setitem__(self, key, value):
        """
        Устанавливает новое значение атрибута по индексу.

        :param key: Индекс атрибута
        :param value: Новое значение атрибута
        :raises IndexError: Если индекс некорректен
        """
        self._check_index(key)
        setattr(self, self._attributes[key], value)

    def __iter__(self) -> 'Person':
        """
        Инициализирует итератор по атрибутам.

        :return: Итератор по атрибутам (self)
        :rtype: Person
        """
        self._iter_index = 0
        return self

    def __next__(self) -> str | int | float:
        """
        Возвращает следующее значение атрибута при итерации.

        :return: Значение следующего атрибута
        :raises StopIteration: Когда атрибуты закончились
        """
        if self._iter_index >= len(self._attributes):
            raise StopIteration

        value = getattr(self, self._attributes[self._iter_index])
        self._iter_index += 1
        return value

