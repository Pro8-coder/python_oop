"""
Представьте, что вы получили задание от заказчика. Вас просят реализовать
простую имитацию локальной сети, состоящую из набора серверов, соединенных
между собой через роутер.

Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у
каждого есть свой уникальный IP-адрес. Для простоты - это просто целое
(натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм
следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации
серверу с IP = 3. Для этого, он сначала отправляет пакет роутеру, а уже тот,
смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

Для реализации этой схемы программе предлагается объявить три класса:

Server - для описания работы серверов в сети;
Router - для описания работы роутеров в сети (в данной задаче полагается один
роутер);
Data - для описания пакета информации.

Серверы будут создаваться командой:

sv = Server()
При этом, уникальный IP-адрес каждого сервера должен формироваться
автоматически при создании нового экземпляра класса Server.

Далее, роутер должен создаваться аналогичной командой:

router = Router()
А, пакеты данных, командой:

data = Data(строка с данными, IP-адрес назначения)
Для формирования и функционирования локальной сети, в классе Router должны
быть реализованы следующие методы:

link(server) - для присоединения сервера server (объекта класса Server) к
роутеру (для простоты, каждый сервер соединен только с одним роутером);
unlink(server) - для отсоединения сервера server (объекта класса Server) от
роутера;
send_data() - для отправки всех пакетов (объектов класса Data) из буфера
роутера соответствующим серверам (после отправки буфер должен очищаться).

И одно обязательное локальное свойство (могут быть и другие свойства):

buffer - список для хранения принятых от серверов пакетов (объектов класса
Data).

Класс Server должен содержать свой набор методов:

send_data(data) - для отправки информационного пакета data (объекта класса
Data) с указанным IP-адресом получателя (пакет отправляется роутеру и
сохраняется в его буфере - локальном свойстве buffer);
get_data() - возвращает список принятых пакетов (если ничего принято не было,
то возвращается пустой список) и очищает входной буфер;
get_ip() - возвращает свой IP-адрес.

Соответственно в объектах класса Server должны быть локальные свойства:

buffer - список принятых пакетов (объекты класса Data, изначально пустой);
ip - IP-адрес текущего сервера.

Наконец, объекты класса Data должны содержать два следующих локальных свойства:

data - передаваемые данные (строка);
ip - IP-адрес назначения.

Пример использования этих классов (эти строчки в программе писать не нужно):

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
Ваша задача реализовать классы Router, Server и Data в соответствии с
приведенным техническим заданием (ТЗ). Что-либо выводить на экран не нужно.
"""


class Data:
    """Класс, представляет пакет данных в сети."""

    def __init__(self, data: str, ip: int) -> None:
        """
        Инициализирует пакет данных.

        :param data (str): Передаваемые данные.
        :param ip (int): IP-адрес назначения.
        """
        self.data = data
        self.ip = ip


class Server:
    """Класс, представляющий сервер в локальной сети."""
    __server_ip: int = 0
    __free_server_ip: list[int] = []

    def __init__(self) -> None:
        """Инициализирует сервер с пустым буфером и уникальным IP-адресом."""
        self.buffer: list[Data] = []
        self.router: Router | None = None

        if self.__free_server_ip:
            self.ip = min(self.__free_server_ip)
            self.__free_server_ip.remove(self.ip)
        else:
            Server.__server_ip += 1
            self.ip = Server.__server_ip

    def __del__(self) -> None:
        """
        Освобождает IP-адрес сервера при удалении объекта.
        Добавляет IP-адрес в список свободных для повторного использования.
        """
        if self.ip not in Server.__free_server_ip:
            Server.__free_server_ip.append(self.ip)

    def send_data(self, data: Data) -> None:
        """
        Отправляет пакет данных через подключенный роутер.

        :param data: Пакет данных для отправки.
        """
        if self.router:
            self.router.buffer.append(data)

    def get_data(self) -> list[Data]:
        """
        Возвращает и очищает буфер принятых пакетов.

        :return: Список принятых пакетов.
        """
        packets = self.buffer.copy()
        self.buffer.clear()
        return packets

    def get_ip(self) -> int:
        """
        Возвращает IP-адрес сервера.

        :return: IP-адрес сервера.
        """
        return self.ip


class Router:
    """Класс, представляющий роутер в локальной сети."""
    __router_ip: int = 0
    __free_router_ip: list[int] = []

    def __init__(self) -> None:
        """Инициализирует роутер с пустыми буфером и списком серверов."""
        self.buffer: list[Data] = []
        self.connected_servers: list[Server] = []

        if self.__free_router_ip:
            self.ip = min(self.__free_router_ip)
            self.__free_router_ip.remove(self.ip)
        else:
            Router.__router_ip += 1
            self.ip = self.__router_ip

    def __del__(self) -> None:
        """
        Освобождает IP-адрес роутера при удалении объекта.
        Добавляет IP-адрес в список свободных для повторного использования.
        """
        if self.ip not in self.__free_router_ip:
            self.__free_router_ip.append(self.ip)

    def link(self, server) -> None:
        """
        Подключает сервер к роутеру.

        :param server: Сервер для подключения.
        """
        self.connected_servers.append(server)
        server.router = self

    def unlink(self, server) -> None:
        """
        Отключает сервер от роутера.

        :param server: Сервер для отключения.
        """
        if server in self.connected_servers:
            self.connected_servers.remove(server)
            server.router = None

    def send_data(self) -> None:
        """
        Отправляет все пакеты из буфера серверу-адресату, если он подключен.
        Очищаем буфер.
        """
        for data in self.buffer:
            for server in self.connected_servers:
                if data.ip == server.ip:
                    server.buffer.append(data)

        self.buffer.clear()

