# Вспомогательная функция "болтается" где-то в коде
def is_valid_email_format(email_string):
    return "@" in email_string

class User:
    def __init__(self, username, email):
        self.username = username
        if is_valid_email_format(email):
            self.email = email
        else:
            raise ValueError("Некорректный формат email")

# Использование
# user1 = User("Alex", "alex@stepik.org") # Работает
# user2 = User("Bob", "bob_at_stepik.org")  # ValueError