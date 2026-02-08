class MyClass:
    # Мы явно объявляем, что у экземпляров этого класса
    # будут только атрибуты 'attr1' и 'attr2'.
    __slots__ = ('attr1', 'attr2')

    def __init__(self, val1, val2):
        self.attr1 = val1
        self.attr2 = val2