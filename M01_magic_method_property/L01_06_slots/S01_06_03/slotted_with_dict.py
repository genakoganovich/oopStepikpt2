class SlottedWithDict:
    __slots__ = ('x', '__dict__')  # Явно разрешаем __dict__

    def __init__(self, x):
        self.x = x


obj = SlottedWithDict(10)
obj.y = 20  # Теперь это работает!
print(obj.__dict__)  # {'y': 20}