"""
Вы создаете интернет-магазин. Для этого нужно объявить два класса:

Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара.

Объекты класса Shop следует создавать командой:

shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:

goods - список товаров (изначально список пустой).

А также в классе объявить методы:

add_product(self, product) - добавление нового товара в магазин (в конец
списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка
goods);

Объекты класса Product следует создавать командой:

p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:

id - уникальный идентификационный номер товара (генерируется автоматически как
целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).

В классе Product через магические методы (подумайте какие) осуществить
проверку на тип присваиваемых данных локальным атрибутам объектов класса
(например, id - целое число, name - строка и т.п.). Если проверка не проходит,
то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление
локального атрибута id. При попытке это сделать генерировать исключение:

raise AttributeError("Атрибут id удалять запрещено.")
Пример использования классов (в программе эти строчки не писать):

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
P.S. На экран ничего выводить не нужно.
"""


class Product:
    """Класс для представления отдельного товара."""

    __id_counter = 0

    def __new__(cls, *args, **kwargs) -> "Product":
        """
        Создает объект товара и присваивает уникальный id.

        :return: Экземпляр класса Product.
        """
        instance = super(Product, cls).__new__(cls)
        cls.__id_counter += 1
        instance.id = cls.__id_counter
        return instance

    def __init__(self, name: str, weight: int | float,
                 price: int | float) -> None:
        """
        Инициализация товара.

        :param name: Название товара.
        :param weight: Вес товара.
        :param price: Цена товара.
        """
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key: str, value: str | int | float) -> None:
        """
        Устанавливает значение атрибута с проверкой типа.

        :param key: Имя атрибута.
        :param value: Значение атрибута.
        :raises TypeError: Если тип значения не соответствует ожидаемому.
        """
        if key == "id" and isinstance(value, int):
            super().__setattr__(key, value)
        elif key == "name" and isinstance(value, str):
            super().__setattr__(key, value)
        elif key in ("weight", "price") and isinstance(value, (
                int, float)) and value >= 0:
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item) -> None:
        """
        Запрещает удаление атрибута id.

        :param item: Имя атрибута.
        :raises AttributeError: Если попытка удалить атрибут id.
        """
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")

        super().__delattr__(item)


class Shop:
    """Класс для управления магазином."""

    def __init__(self, shop_name: str) -> None:
        """
        Инициализация магазина.

        :param shop_name: Название магазина.
        """
        self.shop_name = shop_name
        self.goods: list[Product] = []

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

