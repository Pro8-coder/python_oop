"""
Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса
должны создаваться командой:

dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего
времени. Эти объекты должны создаваться командой:

clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные
числа).

В классе Clock также должен быть (по крайней мере) один метод
(возможны и другие):

get_time() - возвращает текущее время в секундах (то есть,
значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в
формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате:
часы: минуты: секунды
Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
Обратите внимание, добавляется незначащий ноль, если число меньше 10.

P.S. На экран ничего выводить не нужно, только объявить классы.
"""


class Clock:
    """
    Класс для хранения текущего времени.

    :ivar hours: Часы (целое неотрицательное число).
    :ivar minutes: Минуты (целое неотрицательное число).
    :ivar seconds: Секунды (целое неотрицательное число).
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        """
        Возвращает текущее время в секундах.

        :return: Время в секундах.
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    """
    Класс для вычисления разницы между двумя временными метками.

    :ivar clock1: Первый объект времени (класс Clock).
    :ivar clock2: Второй объект времени (класс Clock).
    """

    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        """
        Возвращает строку разницы времен в формате "часы: минуты: секунды".

        Если разница отрицательная, возвращается 0 в формате "00: 00: 00".

        :return: Строка разницы времен.
        """
        diff: int = self.clock1.get_time() - self.clock2.get_time()
        if diff < 0:
            diff = 0

        h: int = diff // 3600
        m: int = (diff % 3600) // 60
        s: int = diff % 60
        return f"{h:02}: {m:02}: {s:02}"

    def __len__(self) -> int:
        """
        Возвращает разницу времен в секундах.

        Если разница отрицательная, возвращается 0.

        :return: Разница времен в секундах.
        """
        return max(0, self.clock1.get_time() - self.clock2.get_time())

