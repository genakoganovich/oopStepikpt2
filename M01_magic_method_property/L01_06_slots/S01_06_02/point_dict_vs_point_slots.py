# Класс 1: Обычный, с __dict__
class PointWithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс 2: Оптимизированный, со __slots__
class PointWithSlots:
    # Объявляем фиксированный набор атрибутов
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- Тестируем обычный класс ---
print("--- PointWithDict ---")
p_dict = PointWithDict(10, 20)
print(f"Атрибуты: x={p_dict.x}, y={p_dict.y}")

# У него есть __dict__
print(f"__dict__: {p_dict.__dict__}")

# Мы можем добавлять новые атрибуты на лету
p_dict.z = 30
print(f"Новый атрибут z: {p_dict.z}")
print(f"__dict__ после добавления: {p_dict.__dict__}")


# --- Тестируем класс со слотами ---
print("\n--- PointWithSlots ---")
p_slots = PointWithSlots(10, 20)
print(f"Атрибуты: x={p_slots.x}, y={p_slots.y}")

# Попытка получить доступ к __dict__
try:
    print(p_slots.__dict__)
except AttributeError as e:
    print(f"Попытка доступа к __dict__: Ошибка! {e}")

# Попытка добавить новый атрибут
try:
    p_slots.z = 30
except AttributeError as e:
    print(f"Попытка добавить новый атрибут: Ошибка! {e}")