"""
Объявите класс PrimaryKey, который должен работать совместно с менеджером
контекста следующим образом:

with PrimaryKey() as pk:
    raise ValueError
где pk - ссылка на объект класса PrimaryKey. Класс PrimaryKey должен в момент
входа в менеджер контекста выводить на экран сообщение "вход", а при
завершении работы менеджера контекста выводить тип возникшего исключения.

Класс PrimaryKey следует реализовать так, чтобы менеджер контекста сам
обрабатывал возникшее исключение.
"""
from types import TracebackType
from typing import Type, Optional


class PrimaryKey:
    def __enter__(self) -> 'PrimaryKey':
        print("вход")
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool:
        if exc_type:
            print(exc_type.__name__)

        return True


with PrimaryKey() as pk:
    raise ValueError
