"""
Вы начинаете создавать интернет-магазин. Для этого в программе объявляется
класс SuperShop, объекты которого создаются командой:

myshop = SuperShop(название магазина)
В каждом объекте класса SuperShop должны формироваться следующие локальные
атрибуты:

name - название магазина (строка);
goods - список из товаров.

Также в классе SuperShop должны быть методы:

add_product(product) - добавление товара в магазин (в конец списка goods);
remove_product(product) - удаление товара из магазина (из списка goods).

Здесь product - это объект класса Product, описывающий конкретный товар. В
этом классе следует объявить следующие дескрипторы:

name = StringValue(min_length, max_length)    # min_length - минимально
допустимая длина строки; max_length - максимально допустимая длина строки
price = PriceValue(max_value)    # max_value - максимально допустимое значение

Объекты класса Product будут создаваться командой:

pr = Product(наименование, цена)
Классы StringValue и PriceValue - это дескрипторы данных. Класс StringValue
должен проверять, что присваивается строковый тип с длиной строки в диапазоне
[2; 50], т.е. min_length = 2, max_length = 50. Класс PriceValue должен
проверять, что присваивается вещественное или целочисленное значение в
диапазоне [0; 10000], т.е. max_value = 10000. Если проверки не проходят, то
соответствующие (прежние) значения меняться не должны.

Пример использования класса SuperShop (эти строчки в программе писать не
нужно):

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран
в программе выводить ничего не нужно.
"""


class StringValue:
    """Дескриптор для работы со строками."""

    def __init__(self, min_length: int = 2, max_length: int = 50) -> None:
        """
        Инициализация объекта дескриптора StringValue.

        :param min_length: Минимальная длина строки.
        :param max_length: Максимальная длина строки.
        """
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Устанавливает имя атрибута, к которому привязан дескриптор.

        :param owner: Класс, в котором определён дескриптор.
        :param name: Имя атрибута, к которому привязан дескриптор.
        """
        self._name = "_" + name

    def __get__(self, instance: object, owner: type) -> str:
        """
        Возвращает значение атрибута.

        :param instance: Экземпляр класса, в котором определён дескриптор.
        :param owner: Класс, в котором определён дескриптор.
        :return: Значение атрибута.
        """
        return instance.__dict__.get(self._name)

    def __set__(self, instance: object, value: str) -> None:
        """
        Устанавливает значение атрибута.

        :param instance: Экземпляр класса, в котором определён дескриптор.
        :param value: Значение, которое нужно присвоить атрибуту.
        """
        if isinstance(value, str
                      ) and self.min_length <= len(value) <= self.max_length:
            instance.__dict__[self._name] = value


class PriceValue:
    """Дескриптор для работы с ценами."""

    def __init__(self, max_value: int = 10000) -> None:
        """
        Инициализация объекта дескриптора PriceValue.

        :param max_value: Максимальное допустимое значение.
        """
        self.max_value = max_value

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Устанавливает имя атрибута, к которому привязан дескриптор.

        :param owner: Класс, в котором определён дескриптор.
        :param name: Имя атрибута, к которому привязан дескриптор.
        """
        self._name = "_" + name

    def __get__(self, instance: object, owner: type) -> int | float:
        """
        Возвращает значение атрибута.

        :param instance: Экземпляр класса, в котором определён дескриптор.
        :param owner: Класс, в котором определён дескриптор.
        :return: Значение атрибута.
        """
        return instance.__dict__.get(self._name)

    def __set__(self, instance: object, value: int | float) -> None:
        """
        Устанавливает значение атрибута.

        :param instance: Экземпляр класса, в котором определён дескриптор.
        :param value: Значение, которое нужно присвоить атрибуту.
        """
        if isinstance(value, (int, float)) and 0 <= value <= self.max_value:
            instance.__dict__[self._name] = value


class Product:
    """
    Класс для описания товара.

    :cvar name: Дескриптор для наименования товара.
    :cvar price: Дескриптор для цены товара.
    """

    name = StringValue(min_length=2, max_length=50)
    price = PriceValue(max_value=10000)

    def __init__(self, name: str, price: int | float) -> None:
        """
        Инициализация Product (товара).

        :param name: Наименование товара.
        :param price: Цена товара.
        """
        self.name = name
        self.price = price


class SuperShop:
    """Класс для интернет-магазина."""

    def __init__(self, name: str, goods: list[Product] = None) -> None:
        """
        Инициализация объекта SuperShop (интернет-магазина).

        :param name: Название магазина.
        :param goods: Список товаров (по умолчанию пустой).
        """
        self.name = name
        self.goods = goods if goods is not None else []

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в магазин.

        :param product: Объект класса Product.
        """
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Удаляет товар из магазина.

        :param product: Объект класса Product.
        """
        self.goods.remove(product)

