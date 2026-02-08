class Point:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"Point({self.x})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x

    # --- Перегрузка оператора "МЕНЬШЕ ЧЕМ" (<) ---
    def __lt__(self, other):
        """Одна точка "меньше" другой, если ее координата x меньше."""
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x

# Создаем список из объектов Point в произвольном порядке
points_list = [Point(100), Point(20), Point(50), Point(-10)]
print(f"Исходный список: {points_list}")

# А теперь магия! Python будет многократно вызывать __lt__ и __eq__
# для сравнения элементов и их расстановки.
sorted_points = sorted(points_list)

print(f"Отсортированный список: {sorted_points}")