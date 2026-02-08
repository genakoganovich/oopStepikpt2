class Date:
    """
    Класс для представления и работы с датами.
    """

    # --- 1. Основной конструктор ---
    def __init__(self, day, month, year):
        """
        Инициализирует объект Date из трех целых чисел.
        Это основной способ создания.
        """
        print(f"-> Вызван __init__ с ({day}, {month}, {year})")
        self.day = day
        self.month = month
        self.year = year

    # --- Метод для красивого вывода ---
    def __str__(self):
        """Возвращает дату в формате ДД.ММ.ГГГГ."""
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    # --- 2. Альтернативный конструктор (фабричный метод) ---
    @classmethod
    def from_string(cls, date_string):
        """
        Создает и возвращает объект Date из строки формата 'ДД-ММ-ГГГГ'.

        Параметры:
        cls: ссылка на сам класс Date (передается автоматически)
        date_string: строка с датой, например, "28-10-2025"
        """
        print(f"-> Вызван @classmethod from_string с '{date_string}'")

        # Шаг A: Разбираем строку на компоненты
        day_str, month_str, year_str = date_string.split('-')

        # Шаг B: Преобразуем компоненты в числа
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)

        # Шаг C: Используем 'cls' для вызова основного конструктора __init__
        # и создаем новый экземпляр. 'cls' здесь эквивалентно 'Date'.
        # Эта строка эквивалентна: return Date(day, month, year)
        return cls(day, month, year)

print("--- Способ 1: Создание через __init__ ---")
# Мы напрямую вызываем конструктор
new_year_eve = Date(31, 12, 2023)
print(f"Полученный объект: {new_year_eve}\n")


print("--- Способ 2: Создание через @classmethod ---")
# Мы вызываем метод класса
some_day_str = "01-09-2024"
first_day_of_autumn = Date.from_string(some_day_str)
print(f"Полученный объект: {first_day_of_autumn}")