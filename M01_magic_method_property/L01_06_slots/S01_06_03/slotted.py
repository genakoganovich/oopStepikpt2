class Slotted:
    __slots__ = ('x',)
    def __init__(self, x):
        self.x = x

obj = Slotted(10)
# obj.y = 20 # AttributeError!