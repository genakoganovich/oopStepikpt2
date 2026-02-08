class User:
    def __init__(self, username, email):
        self.username = username
        # Теперь мы вызываем нашу "внутреннюю" утилиту
        if User.is_valid_email_format(email):
            self.email = email
        else:
            raise ValueError("Некорректный формат email")

    def __str__(self):
        return f"User({self.username}, {self.email})"

    # --- Вот наша вспомогательная утилита ---
    @staticmethod
    def is_valid_email_format(email_string):
        """
        Проверяет, содержит ли строка символ '@'.
        Это статический метод, он не зависит ни от какого User.
        """
        print(f"(Проверка email: '{email_string}')")
        # Простая проверка для примера
        return isinstance(email_string, str) and "@" in email_string

# 1. Использование внутри класса (как в __init__)
print("--- Создаем пользователя ---")
user1 = User("Alex", "alex@stepik.org")
print(user1)

try:
    print("\n--- Пытаемся создать пользователя с неверным email ---")
    user2 = User("Bob", "bob_at_stepik.org")
except ValueError as e:
    print(f"Поймали ошибку: {e}")

# 2. Использование снаружи класса (как самостоятельной утилиты)
print("\n--- Используем метод как утилиту ---")
is_ok = User.is_valid_email_format("test@test.com")
print(f"test@test.com - это корректный формат? {is_ok}")

is_bad = User.is_valid_email_format("просто_текст")
print(f"просто_текст - это корректный формат? {is_bad}")