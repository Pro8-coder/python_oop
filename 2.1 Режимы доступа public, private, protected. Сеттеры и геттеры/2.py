"""
Объявите класс с именем Money и определите в нем следующие переменные и методы:

- приватная локальная переменная money (целочисленная) для хранения
количества денег (своя для каждого объекта класса Money);
- публичный метод set_money(money) для передачи нового значения приватной
локальной переменной money (изменение выполняется только если метод
check_money(money) возвращает значение True);
- публичный метод get_money() для получения текущего объема средств (денег);
- публичный метод add_money(mn) для прибавления средств из объекта mn класса
Money к средствам текущего объекта;
- приватный метод класса check_money(money) для проверки корректности объема
средств в параметре money (возвращает True, если значение корректно и
False - в противном случае).

Проверка корректности выполняется по критерию: параметр money должен быть
целым числом, больше или равным нулю.

Пример использования класса Money (эти строчки в программе не писать):

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
"""


class Money:
    """Класс, представляющий денежные суммы."""

    def __init__(self, money: int) -> None:
        """
        Инициализирует объект Money с заданной суммой.

        :param money: Начальная сумма денег. Должна быть целым числом >= 0.
        """
        self.__money: int = 0
        if self.__check_money(money):
            self.__money = money

    @classmethod
    def __check_money(cls, money: int) -> bool:
        """
        Проверяет корректность суммы денег.

        :param money: Сумма для проверки.
        :return: True, если сумма корректна, иначе False.
        """
        return isinstance(money, int) and not isinstance(money, bool) \
               and money >= 0

    def set_money(self, money: int) -> None:
        """
        Устанавливает новую сумму денег, если она корректна.

        :param money: Новая сумма денег.
        """
        if self.__check_money(money):
            self.__money = money

    def get_money(self) -> int:
        """
        Возвращает текущую сумму денег.

        :return: Текущая сумма денег.
        """
        return self.__money

    def add_money(self, mn: 'Money') -> None:
        """
        Добавляет средства из объекта mn к текущему объекту.

        :param mn: Объект класса Money, из которого добавляются средства.
        """
        if isinstance(mn, Money):
            self.__money += mn.get_money()

