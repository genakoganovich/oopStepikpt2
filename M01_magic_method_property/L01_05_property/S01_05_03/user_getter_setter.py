class User:
    def __init__(self, name, age):
        self.name = name
        self._age = 0      # Инициализируем нулем
        self.age = age     # Тут сработает наш сеттер!

    # 1. ГЕТТЕР (Чтение)
    @property
    def age(self):
        return self._age

    # 2. СЕТТЕР (Запись)
    @age.setter
    def age(self, value):
        print(f">> Проверяем число {value}...")
        if 0 <= value <= 120:
            self._age = value  # Всё ок, кладем в сейф
            print(">> Успешно сохранено!")
        else:
            print(">> Ошибка! Недопустимый возраст.")

# Проверяем
u = User("Маша", 25)
# Вывод: >> Проверяем число 25... >> Успешно сохранено!

u.age = -5
# Вывод: >> Проверяем число -5... >> Ошибка! Недопустимый возраст.

print(u.age) # 25 (осталось старое значение)