"""
Часто множественное наследование используют для наполнения дочернего класса
определенным функционалом. То есть, с указанием каждого нового базового
класса, дочерний класс приобретает все больше и больше возможностей. И,
наоборот, убирая часть базовых классов, дочерний класс теряет соответствующую
часть функционала.

Например, паттерн миксинов активно используют в популярном фреймворке Django.
В частности, когда нужно указать дочернему классу, какие запросы от клиента он
должен обрабатывать (запросы типа GET, POST, PUT, DELETE и т.п.). В качестве
примера реализуем эту идею в очень упрощенном виде, но сохраняя суть паттерна
миксинов.

Предположим, что в программе уже существует следующий набор классов:

class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')
Здесь в каждом классе выполняется имитация обработки запросов. За GET-запрос
отвечает метод get() класса RetriveMixin, за POST-запрос - метод post() класса
CreateMixin, за PUT-запрос - метод put() класса UpdateMixin.

Далее, вам нужно объявить класс с именем GeneralView, в котором следует
указать атрибут (на уровне класса):

allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
для перечня разрешенных запросов. А также объявить метод render_request со
следующей сигнатурой:

def render_request(self, request): ...

Здесь request - это словарь (объект запроса), в котором обязательно должны
быть два ключа:

'url' - адрес для обработки запроса;
'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.

В методе render_request() нужно сначала проверить, является ли указанный
запрос в словаре request разрешенным (присутствует в списке allowed_methods).
И если это не так, то генерировать исключение командой:

raise TypeError(f"Метод {request.get('method')} не разрешен.")
Иначе, вызвать метод по его имени:

method_request = request.get('method').lower()  # имя метода, малыми буквами
Подсказка: чтобы получить ссылку на метод с именем method_request,
воспользуйтесь функцией getattr().

Для использования полученных классов, в программе объявляется следующий
дочерний класс:

class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )
Воспользоваться им можно, например, следующим образом (эти строчки в программе
не писать):

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/',
'method': 'GET'})
print(html)   # GET: https://stepik.org/course/116336/
Если в запросе указать другой метод:

html = view.render_request({'url': 'https://stepik.org/course/116336/',
'method': 'PUT'})
то естественным образом возникнет исключение (реализовывать в программе
не нужно, это уже встроено в сам язык Python):

AttributeError: 'DetailView' object has no attribute 'put'

так как дочерний класс DetailView не имеет метода put. Поправить это можно,
если указать соответствующий базовый класс:

class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )
Теперь, при выполнении команд:

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/',
'method': 'PUT'})
print(html)
будет выведено:

PUT: https://stepik.org/course/116336/

Это и есть принцип работы паттерна миксинов.

P.S. В программе требуется объявить только класс GeneralView. На экран
выводить ничего не нужно.
"""


class RetriveMixin:
    """Миксин для обработки GET-запросов."""

    def get(self, request: dict) -> str:
        """
        Обрабатывает GET-запрос.

        :param request: Словарь запроса с обязательным ключом 'url'
        :return: Строка ответа в формате "GET: <url>"
        """
        return "GET: " + request.get('url')


class CreateMixin:
    """Миксин для обработки POST-запросов."""

    def post(self, request: dict) -> str:
        """
        Обрабатывает POST-запрос.

        :param request: Словарь запроса с обязательным ключом 'url'
        :return: Строка ответа в формате "POST: <url>"
        """
        return "POST: " + request.get('url')


class UpdateMixin:
    """Миксин для обработки PUT-запросов."""

    def put(self, request: dict) -> str:
        """
        Обрабатывает PUT-запрос.

        :param request: Словарь запроса с обязательным ключом 'url'
        :return: Строка ответа в формате "PUT: <url>"
        """
        return "PUT: " + request.get('url')


class GeneralView:
    """
    Базовый класс для обработки HTTP-запросов с проверкой разрешенных методов.

    :cvar allowed_methods: Кортеж разрешенных HTTP-методов по умолчанию
    """

    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: dict) -> str:
        """
        Обрабатывает запрос с проверкой разрешенных методов.

        :param request: Словарь запроса с ключами 'method' и 'url'
        :return: Результат обработки запроса
        :raises TypeError: Если метод запроса не разрешен
        """
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        else:
            return getattr(self, request.get('method').lower())(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    """
    Класс для обработки детализированных запросов (GET и PUT).

    :cvar allowed_methods: Кортеж разрешенных методов для этого представления
    """

    allowed_methods = ('GET', 'PUT', )

