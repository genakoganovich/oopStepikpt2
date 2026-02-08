class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Для чисел !r не обязателен, но и не повредит
        return f"Point(x={self.x!r}, y={self.y!r})"


p = Point(10, 20)
print(p)  # __str__ не найден, используется __repr__