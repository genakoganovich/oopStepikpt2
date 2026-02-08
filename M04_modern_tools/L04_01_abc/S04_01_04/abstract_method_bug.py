from abc import abstractmethod


# ВНИМАНИЕ: Мы забыли (ABC) в скобках!
class FakeAbstractClass:

    @abstractmethod
    def do_something(self):
        pass


print("Пытаемся создать экземпляр...")

# По логике, здесь должна быть ошибка. Но...
obj = FakeAbstractClass()

print(f"Успех! Объект создан: {obj}")
print("Магия защиты не сработала.")