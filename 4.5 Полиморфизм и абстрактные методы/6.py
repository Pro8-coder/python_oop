"""
С помощью модуля abc можно определять не только абстрактные методы, но и
абстрактные объекты-свойства (property). Делается это следующим образом:

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        '''Метод для перемещения транспортного средства'''

    @property
    @abstractmethod
    def speed(self):
        '''Абстрактный объект-свойство'''
Используя эту информацию и информацию о модуле abc из подвига 6, объявите
базовый класс с именем CountryInterface со следующими абстрактными методами и
свойствами:

name - абстрактное свойство (property), название страны (строка);
population - абстрактное свойство (property), численность населения
(целое положительное число);
square - абстрактное свойство (property), площадь страны (положительное число);

get_info() - абстрактный метод для получения сводной информации о стране.

На основе класса CountryInterface объявите дочерний класс Country, объекты
которого создаются командой:

country = Country(name, population, square)
В самом классе Country должны быть переопределены следующие свойства и методы
базового класса:

name - свойство (property) для считывания названия страны (строка);
population - свойство (property) для записи и считывания численности населения
(целое положительное число);
square - свойство (property) для записи и считывания площади страны
(положительное число);

get_info() - метод для получения сводной информации о стране в виде строки:

"<название>: <площадь>, <численность населения>"

Пример использования классов (эти строчки в программе писать не нужно):

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
P.S. В программе требуется объявить только классы. На экран выводить ничего
не нужно.
"""
from abc import ABC, abstractmethod


class CountryInterface(ABC):
    """
    Абстрактный базовый класс для представления страны.

    Определяет интерфейс обязательных свойств и методов для всех стран.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Абстрактное свойство: название страны.

        :getter: Возвращает название страны
        :setter: Устанавливает название страны
        :raises NotImplementedError: Если не переопределен в дочернем классе
        """
        raise NotImplementedError("Метод name должен быть переопределен")

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None:
        raise NotImplementedError("Метод name должен быть переопределен")

    @property
    @abstractmethod
    def population(self) -> int:
        """
        Абстрактное свойство: численность населения.

        :getter: Возвращает численность населения
        :setter: Устанавливает численность населения
        :raises NotImplementedError: Если не переопределен в дочернем классе
        """
        raise NotImplementedError("Метод population должен быть переопределен")

    @population.setter
    @abstractmethod
    def population(self, value: int) -> None:
        raise NotImplementedError("Метод population должен быть переопределен")

    @property
    @abstractmethod
    def square(self) -> int | float:
        """
        Абстрактное свойство: площадь страны.

        :getter: Возвращает площадь страны
        :setter: Устанавливает площадь страны
        :raises NotImplementedError: Если не переопределен в дочернем классе
        """
        raise NotImplementedError("Метод square должен быть переопределен")

    @square.setter
    @abstractmethod
    def square(self, value: int | float) -> None:
        raise NotImplementedError("Метод square должен быть переопределен")

    def get_info(self) -> str:
        """
        Абстрактный метод для получения сводной информации о стране.

        :raises NotImplementedError: Если не переопределен в дочернем классе
        """
        raise NotImplementedError("Метод get_info должен быть переопределен")


class Country(CountryInterface):
    """
    Класс, представляющий конкретную страну.

    :ivar _name: Название страны
    :ivar _population: Численность населения
    :ivar _square: Площадь территории
    """

    def __init__(self, name: str, population: int, square: int | float
                 ) -> None:
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self) -> str:
        """
        Возвращает название страны.

        :return: Название страны
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название страны.

        :param value: Новое название страны
        """
        self._name = value

    @property
    def population(self) -> int:
        """
        Возвращает численность населения.

        :return: Численность населения
        """
        return self._population

    @population.setter
    def population(self, value: int) -> None:
        """
        Устанавливает численность населения.

        :param value: Новая численность населения
        """
        self._population = value

    @property
    def square(self) -> int | float:
        """
        Возвращает площадь страны.

        :return: Площадь территории
        """
        return self._square

    @square.setter
    def square(self, value: int | float) -> None:
        """
        Устанавливает площадь страны.

        :param value: Новая площадь территории
        """
        self._square = value

    def get_info(self) -> str:
        """
        Возвращает сводную информацию о стране в формате:
        'название: площадь, население'.

        :return: Строка с информацией о стране
        """
        return f"{self.name}: {self.square}, {self.population}"

