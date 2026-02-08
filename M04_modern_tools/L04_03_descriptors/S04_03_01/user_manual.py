class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # 1. Определяем обычный метод-геттер
    def get_full_name(self):
        print("-> (Вызывается геттер full_name)")
        return f"{self.first_name} {self.last_name}"

    # 2. Создаем дескриптор property вручную и присваиваем его атрибуту класса
    full_name = property(fget=get_full_name)
