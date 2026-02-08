from abc import ABC, abstractmethod


# Теперь мы нанимаем "охранника" (ABC)
class RealAbstractClass(ABC):

    @abstractmethod
    def do_something(self):
        pass


# Теперь охранник работает:
try:
    obj = RealAbstractClass()
except TypeError as e:
    print(f"ОШИБКА ПОЙМАНА: {e}")