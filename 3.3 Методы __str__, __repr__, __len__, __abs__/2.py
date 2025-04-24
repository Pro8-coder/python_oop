"""
Объявите класс с именем Model, объекты которого создаются командой:

model = Model()
Объявите в этом классе метод query() для формирования записи базы данных.
Использоваться этот метод должен следующим образом:

model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

Например:

model.query(id=1, fio='Sergey', old=33)
Все эти переданные данные должны сохраняться внутри объекта model класса
Model. Затем, при выполнении команды:

print(model)
В консоль должна выводиться информация об объекте в формате:

"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

Например:

"Model: id = 1, fio = Sergey, old = 33"

Если метод query() не вызывался, то в консоль выводится строка:

"Model"

P.S. В программе нужно только объявить класс, выводить в консоль ничего
не нужно.
"""


class Model:
    """
    Класс для представления модели данных.

    Объекты этого класса сохраняют данные, переданные через метод `query`,
    и выводят их в строковом представлении при вызове `print`.
    """

    def __init__(self) -> None:
        """
        Инициализация экземпляра класса Model.

        Создаёт пустой словарь `data` для хранения данных.
        """
        self.data: dict = {}

    def __str__(self) -> str:
        """
        Возвращает строковое представление модели.

        :return: Строка в формате "Model: field_1 = value_1, field_2 =
        value_2, ...". Если данные отсутствуют, возвращает "Model".
        """
        if not self.data:
            return "Model"
        else:
            details: str = ", ".join(
                f"{key} = {value}" for key, value in self.data.items()
            )
            return f"Model: {details}"

    def query(self, **kwargs) -> None:
        """
        Сохраняет переданные данные в модели.

        :param kwargs: Пары ключ-значение для сохранения в модели.
        """
        self.data.update(kwargs)

