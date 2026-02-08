class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """Реализуем repr для наглядного вывода."""
        return f"Vector({self.x}, {self.y})"

    # --- Перегрузка оператора СЛОЖЕНИЯ (+) ---
    def __add__(self, other):
        """Этот метод вызывается для выражения `self + other`."""

        # Хорошей практикой является проверка типа второго операнда
        if not isinstance(other, Vector):
            # NotImplemented - это специальный синглтон, который говорит Python,
            # что наш метод не знает, как выполнить операцию с этим типом.
            return NotImplemented

        # Создаем и возвращаем НОВЫЙ объект Vector
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # --- Перегрузка оператора ВЫЧИТАНИЯ (-) ---
    def __sub__(self, other):
        """Этот метод вызывается для выражения `self - other`."""

        if not isinstance(other, Vector):
            return NotImplemented

        # Создаем и возвращаем НОВЫЙ объект Vector
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

# Создаем два вектора
v1 = Vector(10, 20)
v2 = Vector(3, 7)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# 1. Тестируем сложение
# За кулисами Python вызывает v1.__add__(v2)
sum_vector = v1 + v2
print(f"v1 + v2 = {sum_vector}") # Ожидаем Vector(13, 27)

# 2. Тестируем вычитание
# За кулисами Python вызывает v1.__sub__(v2)
diff_vector = v1 - v2
print(f"v1 - v2 = {diff_vector}") # Ожидаем Vector(7, 13)

# 3. Что будет при операции с другим типом?
try:
    result = v1 + 5
except TypeError as e:
    print(f"\nv1 + 5 -> Ошибка: {e}")