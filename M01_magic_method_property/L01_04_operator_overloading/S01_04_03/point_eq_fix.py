class Point:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"Point({self.x!r})"

    # --- Перегрузка оператора РАВЕНСТВА (==) ---
    def __eq__(self, other):
        """Две точки равны, если их координаты x равны."""
        print(f"Вызван __eq__ для {self} и {other}")

        # 1. Проверяем, что сравниваем с объектом того же типа
        if not isinstance(other, Point):
            return NotImplemented

        # 2. Возвращаем результат сравнения атрибутов
        return self.x == other.x

p1 = Point(10)
p2 = Point(10)
p3 = Point(20)

print(p1 == p2) # Выведет: True
print(p1 == p3) # Выведет: False
print(p1 == 10) # Выведет: False (благодаря проверке isinstance)