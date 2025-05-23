"""
Объявите в программе класс Car, в котором реализуйте объект-свойство с именем
model для записи и считывания информации о модели автомобиля из локальной
приватной переменной __model.

Объект-свойство объявите с помощью декоратора @property. Также в
объекте-свойстве model должны быть реализованы проверки:

- модель автомобиля - это строка;
- длина строки модели должна быть в диапазоне [2; 100].

Если проверка не проходит, то локальное свойство __model остается без
изменений.

Объекты класса Car предполагается создавать командой:

car = Car()
и далее работа с объектом-свойством, например:

car.model = "Toyota"
P.S. В программе объявить только класс. На экран ничего выводить не нужно.
"""


class Car:
    """Класс, представляющий автомобиль с моделью."""

    def __init__(self) -> None:
        """Инициализирует объект автомобиля с пустой моделью."""
        self.__model: str = ""

    @property
    def model(self) -> str:
        """
        Возвращает текущую модель автомобиля.

        :return: Модель автомобиля.
        """
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        """
        Устанавливает новую модель автомобиля, если она корректна.

        :param model: Новая модель автомобиля.
        """
        if isinstance(model, str) and 1 < len(model) < 101:
            self.__model = model

    @model.deleter
    def model(self) -> None:
        """Удаляет текущую модель автомобиля."""
        del self.__model

