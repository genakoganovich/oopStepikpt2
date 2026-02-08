class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Прячем данные в "сейф"

    # @property превращает метод в атрибут (только для чтения)
    @property
    def age(self):
        print(">> Открываем сейф и показываем возраст")
        return self._age

user = User("Иван", 30)

# Мы пишем user.age (без скобок!), а Python незаметно вызывает метод
print(user.age)
# Вывод:
# >> Открываем сейф и показываем возраст
# 30

# user.age = 40  <-- ОШИБКА! Сейф закрыт, менять нельзя.