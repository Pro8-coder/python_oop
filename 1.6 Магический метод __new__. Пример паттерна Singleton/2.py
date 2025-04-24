"""
Объявите класс SingletonFive, с помощью которого можно было бы создавать
объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве
name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой,
седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего
фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно.
"""


# здесь объявляйте класс SingletonFive
class SingletonFive:
    __instances = []

    def __new__(cls, name, *args, **kwargs):
        if len(cls.__instances) < 5:
            instance = super(SingletonFive, cls).__new__(cls)
            cls.__instances.append(instance)
            instance.name = name
            return instance
        else:
            return cls.__instances[-1]


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

# print([id(obj.name) for obj in objs])
