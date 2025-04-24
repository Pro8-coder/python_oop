"""
В программе необходимо объявить классы для работы с кошельками в разных
валютах:

MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков

Объекты этих классов могут создаваться командами:

rub = MoneyR()   # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро
В каждом объекте этих классов должны формироваться локальные атрибуты:

__cb - ссылка на класс CentralBank (центральный банк, изначально None);
__volume - объем денежных средств в кошельке (если не указано, то 0).

Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства
(property) для работы с локальными атрибутами:

cb - для изменения и считывания данных из переменной __cb;
volume - для изменения и считывания данных из переменной __volume.

Объекты классов должны поддерживать следующие операторы сравнения:

rub < dl
dl >= euro
rub == euro  # значения сравниваются по текущему курсу центрального банка с
погрешностью 0.1 (плюс-минус)
euro > rub
При реализации операторов сравнения считываются соответствующие значения
__volume из сравниваемых объектов и приводятся к рублевому эквиваленту в
соответствии с курсом валют центрального банка.

Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки,
необходимо в программе объявить еще один класс CentralBank. Объекты класса
CentralBank создаваться не должны (запретить), при выполнении команды:

cb = CentralBank()

должно просто возвращаться значение None. А в самом классе должен
присутствовать атрибут:

rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
Здесь числа (в значениях словаря) - курс валюты по отношению к доллару.

Также в CentralBank должен быть метод уровня класса:

register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и
MoneyE.

При регистрации значение __cb объекта money должно ссылаться на класс
CentralBank. Через эту переменную объект имеет возможность обращаться к
атрибуту rates класса CentralBank и брать нужные котировки.

Если кошелек не зарегистрирован, то при операциях сравнения должно
генерироваться исключение:

raise ValueError("Неизвестен курс валют.")
Пример использования классов (эти строчки в программе писать не нужно):

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
P.S. В программе на экран ничего выводить не нужно, только объявить классы.
"""


class Money:
    """
    Базовый класс для представления кошелька с денежными средствами.

    :ivar __volume: Объем денежных средств (по умолчанию 0).
    :ivar __cb: Ссылка на ЦБ (по умолчанию None).
    """

    def __init__(self, volume: int | float = 0) -> None:
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self) -> int | float:
        """
        Возвращает объем денежных средств.

        :return: Объем денежных средств.
        """
        return self.__volume

    @volume.setter
    def volume(self, value: int | float) -> None:
        """
        Устанавливает объем денежных средств.

        :param value: Новый объем денежных средств.
        """
        self.__volume = value

    @property
    def cb(self) -> 'CentralBank':
        """
        Возвращает ссылку на CentralBank.

        :return: Ссылка на CentralBank.
        """
        return self.__cb

    @cb.setter
    def cb(self, value: 'CentralBank') -> None:
        """
        Устанавливает ссылку на CentralBank.

        :param value: Ссылка на CentralBank.
        """
        self.__cb = value

    def _convert_to_rub(self) -> float:
        """
        Конвертирует объем денежных средств в рубли.

        :return: Объем денежных средств в рублях.
        :raises ValueError: Если курс валют неизвестен.
        """
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        if type(self) == MoneyR:
            return self.volume
        elif type(self) == MoneyD:
            return self.volume * self.cb.rates['rub']
        elif type(self) == MoneyE:
            return self.volume * self.cb.rates['rub'] / self.cb.rates['euro']
        else:
            raise ValueError("Неизвестный тип кошелька.")

    def __eq__(self, other: 'Money') -> bool:
        """
        Сравнивает два кошелька по объему денежных средств в рублях.

        :param other: Другой кошелек.
        :return: True, если объемы равны с погрешностью 0.1, иначе False.
        """
        return abs(self._convert_to_rub() - other._convert_to_rub()) < 0.1

    def __lt__(self, other: 'Money') -> bool:
        """
        Сравнивает два кошелька по объему денежных средств в рублях.

        :param other: Другой кошелек.
        :return: True, если текущий кошелек меньше другого, иначе False.
        """
        return self._convert_to_rub() < other._convert_to_rub()

    def __le__(self, other: 'Money') -> bool:
        """
        Сравнивает два кошелька по объему денежных средств в рублях.

        :param other: Другой кошелек.
        :return: True, если текущий кошелек меньше или равен другому,
        иначе False.
        """
        return self._convert_to_rub() <= other._convert_to_rub()


class MoneyR(Money):
    """Класс для рублевых кошельков."""


class MoneyD(Money):
    """Класс для долларовых кошельков."""


class MoneyE(Money):
    """Класс для евро-кошельков."""


class CentralBank:
    """
    Класс для управления курсами валют и регистрации кошельков.

    :cvar rates: Курсы валют.
    """

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs) -> None:
        """
        Запрещает создание объектов класса CentralBank.

        :return: None.
        """
        return None

    @classmethod
    def register(cls, money: Money):
        """
        Регистрирует кошелек, устанавливая ссылку на CentralBank.

        :param money: Кошелек для регистрации.
        """
        money.cb = cls

