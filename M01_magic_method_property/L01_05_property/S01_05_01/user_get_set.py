class User:
    def __init__(self, name, age):
        self.name = name
        self._age = 0  # Начальное безопасное значение
        self.set_age(age) # Используем сеттер для установки

    def get_age(self):
        """Это наш геттер."""
        return self._age

    def set_age(self, new_age):
        """Это наш сеттер с валидацией."""
        if isinstance(new_age, int) and 0 <= new_age <= 120:
            self._age = new_age
        else:
            print("Ошибка: возраст должен быть числом от 0 до 120.")

user = User("Иван", 30)

# Чтобы ПРОЧИТАТЬ возраст, мы вызываем метод
current_age = user.get_age()
print(f"Текущий возраст: {current_age}")

# Чтобы ИЗМЕНИТЬ возраст, мы тоже вызываем метод
user.set_age(35)
print(f"Новый возраст: {user.get_age()}")