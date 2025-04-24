"""
Своей работой вы немного впечатлили начальство и оно поручило вам доделать
паттерн слушатель (listener). Идея этого паттерна очень проста и основа
реализуется следующим образом:

class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()
Здесь в объектах класса Subject можно зарегистрировать (добавить) множество
объектов класса Observer (наблюдатель, слушатель). Это делается с помощью
метода add_observer(). Затем, когда данные (self.__data) меняются путем вызова
метода change_data() класса Subject, то у всех слушателей автоматически
вызывается метод update(). В этом методе можно прописать самую разную логику
работы при изменении данных в каждом конкретном слушателе.

В проекте данный паттерн предполагается использовать для отображения
информации о погоде в различных форматах:

- текущая температура;
- текущее атмосферное давление;
- текущая влажность воздуха.

Для этого сами данные определяются классом:

class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность
А вам поручается разработать дочерние классы, унаследованные от класса
Observer, с именами:

TemperatureView - слушатель для отображения информации о температуре;
PressureView - слушатель для отображения информации о давлении;
WetView - слушатель для отображения информации о влажности.

Каждый из этих классов должен переопределять метод update() базового класса
так, чтобы выводилась в консоль информация в формате:

TemperatureView: "Текущая температура <число>"
PressureView: "Текущее давление <число>"
WetView: "Текущая влажность <число>"

Важно: для вывода информации в консоль используйте функцию print() с одним
аргументом в виде F-строки.

Пример использования классов (эти строчки в программе писать не нужно):

subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
# выведет строчки:
# Текущая температура 23
# Текущее давление 150
# Текущая влажность 83
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))
# выведет строчки:
# Текущая температура 24
# Текущее давление 148
P.S. В программе нужно объявить только классы. На экран выводить ничего
не нужно.
"""


class Data:
    """
    Класс для хранения данных о погоде.

    :ivar temp: Температура (число)
    :ivar press: Давление (число)
    :ivar wet: Влажность (число)
    """

    def __init__(self, temp: int | float, press: int | float,
                 wet: int | float) -> None:
        self.temp = temp
        self.press = press
        self.wet = wet


class Observer:
    """Базовый класс наблюдателя (шаблон Observer)."""

    def update(self, data: Data) -> None:
        """
        Метод, вызываемый при изменении данных в Subject.

        :param data: Объект данных (тип Data)
        """
        pass

    def __hash__(self) -> int:
        """
        Генерирует хеш объекта на основе его id (используется для хранения в
        словаре).

        :return: Уникальный хеш объекта
        """
        return hash(id(self))


class Subject:
    """
    Класс субъекта (издателя событий).

    Хранит список наблюдателей и уведомляет их об изменениях данных.

    :ivar __observers: Словарь зарегистрированных наблюдателей
    :ivar __data: Текущие данные о погоде
    """

    def __init__(self) -> None:
        self.__observers: dict[Observer, Observer] = {}
        self.__data: Data | None = None

    def add_observer(self, observer: Observer) -> None:
        """
        Добавляет наблюдателя.

        :param observer: Объект, реализующий Observer
        """
        self.__observers[observer] = observer

    def remove_observer(self, observer: Observer) -> None:
        """
        Удаляет наблюдателя.

        :param observer: Объект, реализующий Observer
        """
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self) -> None:
        """Приватный метод для оповещения всех наблюдателей."""
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data: Data) -> None:
        """
        Изменяет данные и оповещает наблюдателей.

        :param data: Объект данных (тип Data)
        """
        self.__data = data
        self.__notify_observer()


class TemperatureView(Observer):
    """Наблюдатель для отображения температуры."""

    def update(self, data: Data) -> None:
        """
        Выводит текущую температуру.

        :param data: Объект данных (тип Data)
        """
        print(f"Текущая температура {data.temp}")


class PressureView(Observer):
    """Наблюдатель для отображения давления."""

    def update(self, data: Data) -> None:
        """
        Выводит текущее давление.

        :param data: Объект данных (тип Data)
        """
        print(f"Текущее давление {data.press}")


class WetView(Observer):
    """Наблюдатель для отображения влажности."""

    def update(self, data: Data) -> None:
        """
        Выводит текущую влажность.

        :param data: Объект данных (тип Data)
        """
        print(f"Текущая влажность {data.wet}")

