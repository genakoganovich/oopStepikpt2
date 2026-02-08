class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Создаем экземпляр класса
user_alex = User("Alex", "alex@example.com")

# Пытаемся его "напечатать"
print(user_alex)