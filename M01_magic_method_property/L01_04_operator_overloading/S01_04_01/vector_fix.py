class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Добавим repr для красивого вывода
        return f"Vector({self.x}, {self.y})"

    # --- Вот наша перегрузка оператора `+` ---
    def __add__(self, other):
        """Этот метод вызывается, когда Vector стоит СЛЕВА от знака `+`."""
        # 'self' - это первый вектор (v1)
        # 'other' - это второй вектор (v2)

        # Создаем НОВЫЙ вектор, являющийся суммой двух других
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)


# Теперь магия работает!
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# За кулисами Python выполняет: v1.__add__(v2)
result = v1 + v2

print(v1)
print(v2)
print(result)  # Выведет: Vector(6, 8)