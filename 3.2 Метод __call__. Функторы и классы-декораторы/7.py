"""
Необходимо объявить класс-декоратор с именем Handler, который можно было бы
применять к функциям следующим образом:

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
Здесь аргумент methods декоратора Handler содержит список разрешенных запросов
для обработки. Сама декорированная функция вызывается по аналогии с предыдущим
подвигом:

res = contact({"method": "POST", "url": "contact.html"})
В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию
подразумевается GET-запрос. Если ключ method принимает значение отсутствующее
в списке methods декоратора Handler, например, "PUT", то декорированная
функция contact должна возвращать значение None.

Для имитации GET и POST-запросов в классе Handler необходимо объявить два
вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки
GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки
POST-запроса

В зависимости от типа запроса должен вызываться соответствующий метод (его
выбор в классе можно реализовать методом __getattribute__()). На выходе эти
методы должны формировать строки в заданном формате.

P.S. В программе достаточно объявить только класс. Ничего на экран выводить
не нужно.

Небольшая справка
Для реализации декоратора с параметрами на уровне класса в инициализаторе
__init__(self, methods) прописываем параметр для декоратора, а магический
метод __call__() объявляем как полноценный декоратор на уровне функции,
например:

class Handler:
    def __init__(self, methods):
        # здесь нужные строчки

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            # здесь нужные строчки
        return wrapper

"""


class Handler:
    """
    Класс-декоратор для обработки HTTP-запросов (GET и POST).

    :ivar methods: Кортеж с разрешёнными методами запросов (по умолчанию
    ('GET',)).
    """

    def __init__(self, methods: tuple = ('GET',)) -> None:
        self.methods = methods

    def __call__(self, func: callable, *args, **kwargs) -> callable:
        """
        Декорирует функцию, добавляя обработку запросов.

        :param func: Декорируемая функция.
        :return: Декорированная функция.
        """
        def wrapper(request: dict, *args, **kwargs) -> None | str:
            """
            Обрабатывает запрос и вызывает соответствующую функцию.

            :param request: Словарь с данными запроса (должен содержать ключ "method").
            :return: Строка в формате "<метод>: <данные из функции>" или None.
            """
            method = request.get("method", "GET")
            if method in self.methods:
                return self.__getattribute__(method.lower())(
                    func, request, *args, **kwargs)

            return None

        return wrapper

    def get(self, func: callable, request: dict, *args, **kwargs) -> str:
        """
        Обрабатывает GET-запрос.

        :param func: Декорируемая функция.
        :param request: Словарь с данными запроса.
        :return: Строка в формате "GET: <данные из функции>".
        """
        return f"GET: {func(request, *args, **kwargs)}"

    def post(self, func: callable, request: dict, *args, **kwargs) -> str:
        """
        Обрабатывает POST-запрос.

        :param func: Декорируемая функция.
        :param request: Словарь с данными запроса.
        :return: Строка в формате "POST: <данные из функции>".
        """
        return f"POST: {func(request, *args, **kwargs)}"

