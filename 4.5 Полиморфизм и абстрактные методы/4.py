"""
В языке Python есть еще один распространенный способ объявления абстрактных
методов класса через декоратор abstractmethod модуля abc:

from abc import ABC, abstractmethod
Чтобы корректно работал декоратор abstractmethod сам класс должен
наследоваться от базового класса ABC. Например, так:

class Transport(ABC):
    @abstractmethod
    def go(self):
        '''Метод для перемещения транспортного средства'''

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        '''Абстрактный метод класса'''
Мы здесь имеем два абстрактных метода внутри класса Transport, причем,
первый метод go() - это обычный метод, а второй abstract_class_method() - это
абстрактный метод уровня класса. Обратите внимание на порядок использования
декораторов classmethod и abstractmethod. Они должны быть записаны именно в
такой последовательности.

Теперь, если объявить какой-либо дочерний класс, например:

class Bus(Transport):
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def go(self):
        print("bus go")

    @classmethod
    def abstract_class_method(cls):
        pass
То в нем обязательно нужно переопределить абстрактные методы go и
abstract_class_method класса Transport. Иначе, объект класса Bus не будет
создан (возникнет исключение TypeError).

Используя эту информацию, объявите базовый класс Model (модель), в котором
нужно объявить один абстрактный метод с сигнатурой:

def get_pk(self): ...

и один обычный метод:

def get_info(self): ...

который бы возвращал строку "Базовый класс Model".

На основе класса Model объявите дочерний класс ModelForm, объекты которого
создаются командой:

form = ModelForm(login, password)
где login - заголовок перед полем ввода логина (строка); password - заголовок
перед полем ввода пароля (строка). В каждом объекте класса ModelForm должны
формироваться локальные атрибуты с именами _login и _password, а также
автоматически появляться локальный атрибут _id с уникальным целочисленным
значением для каждого объекта класса ModelForm.

В классе ModelForm переопределите метод:

def get_pk(self): ...

который должен возвращать значение атрибута _id.

Пример использования классов (эти строчки в программе писать не нужно):

form = ModelForm("Логин", "Пароль")
print(form.get_pk())
P.S. В программе требуется объявить только классы. На экран выводить ничего
не нужно.
"""
from typing import Any
from abc import ABC, abstractmethod


class Model(ABC):
    """
    Абстрактный базовый класс модели.

    Определяет интерфейс для работы с моделями данных.
    """

    @abstractmethod
    def get_pk(self) -> Any:
        """
        Абстрактный метод для получения первичного ключа.

        :raises NotImplementedError: Если метод не реализован в дочернем классе
        """
        raise NotImplementedError('Метод get_pk должен быть переопределен')

    def get_info(self) -> str:
        """
        Возвращает информацию о базовом классе.

        :return: Информационная строка
        """
        return "Базовый класс Model"


class ModelForm(Model):
    """
    Класс формы модели, наследующий от Model.

    :cvar __id_counter: Счетчик для генерации уникальных ID
    :ivar _login: Заголовок поля логина
    :ivar _password: Заголовок поля пароля
    :ivar _id: Уникальный идентификатор формы
    """

    __id_counter = 0

    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        ModelForm.__id_counter += 1
        self._id = self.__id_counter

    def get_pk(self) -> int:
        """
        Возвращает первичный ключ формы (уникальный ID).

        Реализация абстрактного метода из класса Model.

        :return: Уникальный идентификатор формы
        """
        return self._id

