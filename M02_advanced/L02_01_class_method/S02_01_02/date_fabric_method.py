class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    # --- Вот наш альтернативный конструктор ---
    @classmethod
    def from_string(cls, date_string):
        """
        Создает объект Date из строки формата 'ДД-ММ-ГГГГ'.
        'cls' здесь - это сам класс Date.
        """
        # 1. Разбираем строку на части
        day, month, year = map(int, date_string.split('-'))

        # 2. Используем 'cls' для создания и возврата нового экземпляра
        return cls(day, month, year)

# 1. Основной способ, через __init__
d1 = Date(25, 12, 2023)
print(f"Создан через __init__: {d1}")

# 2. Альтернативный способ, через наш @classmethod
date_as_string = "28-10-2025"
d2 = Date.from_string(date_as_string)
print(f"Создан из строки:   {d2}")