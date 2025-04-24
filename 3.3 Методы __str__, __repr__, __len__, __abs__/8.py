"""
Объявите класс Recipe для представления рецептов. Отдельные ингредиенты
рецепта должны определяться классом Ingredient. Объекты этих классов должны
создаваться командами:

ing = Ingredient(name, volume, measure)
recipe = Recipe()
recipe = Recipe(ing_1, ing_2,..., ing_N)
где ing_1, ing_2,..., ing_N - объекты класса Ingredient.

В каждом объекте класса Ingredient должны создаваться локальные атрибуты:

name - название ингредиента (строка);
volume - объем ингредиента в рецепте (вещественное число);
measure - единица измерения объема ингредиента (строка), например, литр,
чайная ложка, грамм, штук и т.д.;

С объектами класса Ingredient должна работать функция:

str(ing)  # название: объем, ед. изм.
и возвращать строковое представление объекта в формате:

"название: объем, ед. изм."

Например:

ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing) # Соль: 1, столовая ложка
Класс Recipe должен иметь следующие методы:

add_ingredient(ing) - добавление нового ингредиента ing (объект класса
Ingredient) в рецепт (в конец);
remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса
Ingredient) из рецепта;
get_ingredients() - получение кортежа из объектов класса Ingredient текущего
рецепта.

Также с объектами класса Recipe должна поддерживаться функция:

len(recipe) - возвращает число ингредиентов в рецепте.

Пример использования классов (эти строчки в программе писать не нужно):

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
P.S. На экран ничего выводить не нужно, только объявить классы.
"""


class Ingredient:
    """
    Класс для представления ингредиента рецепта.

    :ivar name: Название ингредиента.
    :ivar volume: Объем ингредиента.
    :ivar measure: Единица измерения объема.
    """

    def __init__(self, name: str, volume: float, measure: str) -> None:
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self) -> str:
        """
        Возвращает строковое представление ингредиента.

        :return: Строка в формате "название: объем, ед. изм.".
        """
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    """
    Класс для представления рецепта.

    :ivar ing_list: Список ингредиентов рецепта.
    """

    def __init__(self, *args: Ingredient) -> None:
        self.ing_list: list[Ingredient] = list(args)

    def get_ingredients(self) -> tuple[Ingredient, ...]:
        """
        Возвращает кортеж из ингредиентов рецепта.

        :return: Кортеж ингредиентов.
        """
        return tuple(self.ing_list)

    def add_ingredient(self, ing: Ingredient) -> None:
        """
        Добавляет новый ингредиент в рецепт.

        :param ing: Ингредиент для добавления.
        """
        self.ing_list.append(ing)

    def remove_ingredient(self, ing: Ingredient) -> None:
        """
        Удаляет ингредиент из рецепта.

        :param ing: Ингредиент для удаления.
        """
        if ing in self.ing_list:
            self.ing_list.remove(ing)

    def __len__(self) -> int:
        """
        Возвращает количество ингредиентов в рецепте.

        :return: Количество ингредиентов.
        """
        return len(self.ing_list)

