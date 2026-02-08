from dataclasses import dataclass

@dataclass
class Point:
    # Мы просто объявляем, какие поля нам нужны и какого они типа
    x: int
    y: int

# 1. __init__ был сгенерирован автоматически
p1 = Point(1, 2)
print(f"Объект создан: {p1}")

# 2. __repr__ тоже был сгенерирован
# Вывод будет таким же, как мы писали вручную
# Point(x=1, y=2)

# 3. __eq__ тоже работает "из коробки"
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"p1 == p2: {p1 == p2}") # Выведет: True
print(f"p1 == p3: {p1 == p3}") # Выведет: False