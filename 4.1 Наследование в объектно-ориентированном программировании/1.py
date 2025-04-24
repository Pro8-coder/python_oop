"""
Наследование часто используют, чтобы вынести общий код дочерних классов в
базовый класс. Сделаем такой пример. Объявите в программе базовый класс Animal
(животное), объекты которого можно создать командой:

an = Animal(name, old)
где name - название животного (строка); old - возраст животного (целое число).
Такие же локальные атрибуты (name и old) должны создаваться в объектах класса.

Далее, объявите дочерний класс (от базового Animal) с именем Cat (кошки),
объекты которого создаются командой:

cat = Cat(name, old, color, weight)
где name, old - те же самые параметры, что и в базовом классе; color - цвет
кошки (строка); weight - вес кошки (любое положительное число).

В объектах класса Cat должны автоматически формироваться локальные атрибуты:
name, old, color, weight. Формирование атрибутов name, old должен выполнять
инициализатор базового класса.

По аналогии объявите еще один дочерний класс Dog (собака), объекты которого
создаются командой:

dog = Dog(name, old, breed, size)
здесь name, old - те же самые параметры, что и в базовом классе; breed -
порода собаки (строка); size - кортеж в формате (height, length) высота и
длина - числа.

В объектах класса Dog по аналогии должны формироваться локальные атрибуты:
name, old, breed, size. За формирование атрибутов name, old отвечает
инициализатор базового класса.

Наконец, в классах Cat и Dog объявите метод:

get_info() - для получения информации о животном.

Этот метод должен возвращать строку в формате:

"name: old, <остальные параметры через запятую>"

Например, для следующего объекта класса Cat:

cat = Cat('кот', 4, 'black', 2.25)
метод get_info должен вернуть строку:

"кот: 4, black, 2.25"

P.S. В программе достаточно объявить три класса. Выводить на экран ничего
не нужно.
"""


class Animal:
    """
    Базовый класс для представления животных.

    :ivar name: Название животного
    :ivar old: Возраст животного
    """
    def __init__(self, name: str, old: int) -> None:
        self.name = name
        self.old = old


class Cat(Animal):
    """
    Класс для представления кошек. Наследуется от Animal.

    :ivar color: Цвет кошки
    :ivar weight: Вес кошки
    """

    def __init__(self, name: str, old: int, color: str, weight: int | float
                 ) -> None:
        """
        Инициализирует экземпляр класса Cat.

        :param name: Название кошки
        :param old: Возраст кошки
        :param color: Цвет кошки
        :param weight: Вес кошки
        """
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self) -> str:
        """
        Возвращает информацию о кошке в формате строки.

        :return: Строка с информацией о кошке
        """
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    """
    Класс для представления собак. Наследуется от Animal.

    :ivar breed: Порода собаки
    :ivar size: Размеры собаки (высота, длина)
    :vartype size: tuple[int | float, int | float]
    """

    def __init__(self, name: str, old: int, breed: str,
                 size: tuple[int | float, int | float]) -> None:
        """
        Инициализирует экземпляр класса Dog.

        :param name: Кличка собаки
        :param old: Возраст собаки
        :param breed: Порода собаки
        :param size: Размеры (высота, длина)
        :type size: tuple[int | float, int | float]
        """
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self) -> str:
        """
        Возвращает информацию о собаке в формате строки.

        :return: Строка с информацией о собаке
        """
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"

