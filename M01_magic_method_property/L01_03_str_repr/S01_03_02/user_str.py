class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # --- Вот и наша "магия" ---
    def __str__(self):
        # Мы сами решаем, как будет выглядеть наш объект в виде строки.
        # Этот метод должен ВЕРНУТЬ строку, а не напечатать ее!
        return f"Пользователь {self.username} (email: {self.email})"


# Создаем экземпляр класса
user_alex = User("Alex", "alex@example.com")
user_maria = User("Maria", "maria@stepik.org")

# Теперь `print()` будет работать так, как мы хотим!
print(user_alex)
print(user_maria)

# Функция str() тоже будет использовать наш метод
user_string = str(user_alex)
print(f"\nРезультат вызова str(): {user_string}")