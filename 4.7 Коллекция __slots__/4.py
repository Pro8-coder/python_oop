"""
Объявите класс Note (нота), объекты которого создаются командой:

note = Note(name, ton)
где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си);
ton - тональность ноты (целое число). Тональность (ton) принимает следующие
целые значения:

-1 - бемоль (flat);
0 - обычная нота (normal);
1 - диез (sharp).

Если в названии (name) или тональности (ton) передаются недопустимые значения,
то генерируется исключение командой:

raise ValueError('недопустимое значение аргумента')
В каждом объекте класса Note должны формироваться локальные атрибуты с именами
_name и _ton с соответствующими значениями.

Объявите класс с именем Notes, в объектах которого разрешены только локальные
атрибуты с именами (ограничение задается через коллекцию __slots__):

_do - ссылка на ноту до (объект класса Note);
_re - ссылка на ноту ре (объект класса Note);
_mi - ссылка на ноту ми (объект класса Note);
_fa - ссылка на ноту фа (объект класса Note);
_solt - ссылка на ноту соль (объект класса Note);
_la - ссылка на ноту ля (объект класса Note);
_si - ссылка на ноту си (объект класса Note).

Объект класса Notes должен создаваться командой:

notes = Notes()
и быть только один (одновременно в программе два и более объектов класса Notes
недопустимо). Используйте для этого паттерн Singleton.

В момент создания объекта Notes должны автоматически создаваться перечисленные
локальные атрибуты и ссылаться на соответствующие объекты класса Note
(тональность (ton) у всех нот изначально равна 0).

Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ;
6 - си. Например:

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
Если указывается недопустимый индекс (не целое число, или число, выходящее за
интервал [0; 6]), то генерируется исключение командой:

raise IndexError('недопустимый индекс')
Создайте в программе объект notes класса Notes.

P.S. В программе следует объявить только классы и создать объект notes. На
экран выводить ничего не нужно.
"""


class Note:
    """
    Класс для представления музыкальной ноты.

    :cvar __valid_names: Кортеж допустимых названий нот
    :cvar __valid_tons: Кортеж допустимых значений тональности
    :ivar _name: Название ноты
    :ivar _ton: Тональность ноты (-1 - бемоль, 0 - обычная, 1 - диез)
    :raises ValueError: Если имя или тональность недопустимы
    """

    __valid_names = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    __valid_tons = (-1, 0, 1)

    def __init__(self, name: str, ton: int = 0) -> None:
        if name not in self.__valid_names or ton not in self.__valid_tons:
            raise ValueError('недопустимое значение аргумента')

        self._name = name
        self._ton = ton

    def __setattr__(self, key: str, value: str | int) -> None:
        """
        Устанавливает атрибут с проверкой допустимости значений.

        :param key: Имя атрибута
        :param value: Значение атрибута
        :raises ValueError: Если имя или тональность недопустимы
        """
        if (key == '_name' and value not in self.__valid_names) or (
                key == '_ton' and value not in self.__valid_tons):
            raise ValueError('недопустимое значение аргумента')

        super().__setattr__(key, value)


class Notes:
    """
    Класс-контейнер для нот (реализация Singleton).

    :ivar _do: Нота до
    :ivar _re: Нота ре
    :ivar _mi: Нота ми
    :ivar _fa: Нота фа
    :ivar _solt: Нота соль
    :ivar _la: Нота ля
    :ivar _si: Нота си
    """

    __instance = None
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')

    def __new__(cls) -> 'Notes':
        """
        Реализация паттерна Singleton.

        :return: Единственный экземпляр класса Notes
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._do = Note('до', 0)
            cls.__instance._re = Note('ре', 0)
            cls.__instance._mi = Note('ми', 0)
            cls.__instance._fa = Note('фа', 0)
            cls.__instance._solt = Note('соль', 0)
            cls.__instance._la = Note('ля', 0)
            cls.__instance._si = Note('си', 0)

        return cls.__instance

    def __del__(self) -> None:
        """Сбрасывает ссылку на экземпляр при удалении объекта."""
        Notes.__instance = None

    def __getitem__(self, index: int) -> Note:
        """
        Возвращает ноту по индексу.

        :param index: Индекс ноты
        :return: Объект ноты
        """
        if type(index) != int or not -1 < index < 7:
            raise IndexError('недопустимый индекс')

        return getattr(self, self.__slots__[index])

