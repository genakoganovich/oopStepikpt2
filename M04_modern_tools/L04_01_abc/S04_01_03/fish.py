from abc import ABC, abstractmethod

class ISpeakable(ABC):
    @abstractmethod
    def speak(self):
        pass

# --- Правильная реализация ---
class Dog(ISpeakable):
    def speak(self):
        print("Гав!")

# --- НЕПРАВИЛЬНАЯ реализация ---
class Fish(ISpeakable):
    # Мы унаследовали от ISpeakable, "пообещав" реализовать speak(),
    # но не сделали этого.
    def swim(self):
        print("Я плыву.")

# 1. Попытка создать "правильный" класс
try:
    my_dog = Dog()
    print("Объект Dog успешно создан.")
    my_dog.speak()
except Exception as e:
    print(f"Ошибка при создании Dog: {e}")

print("-" * 20)

# 2. Попытка создать "недоделанный" класс
try:
    my_fish = Fish() # Вот здесь и произойдет ошибка!
    print("Объект Fish успешно создан.")
except TypeError as e:
    print(f"Ошибка при создании Fish: {e}")

def make_it_speak(animal: ISpeakable):
    # Мы можем быть УВЕРЕНЫ, что у любого объекта, который сюда попадет,
    # есть метод .speak(), потому что иначе его просто не удалось бы создать.
    animal.speak()

# Этот код выполнится без проблем
make_it_speak(Dog())

# А этот код даже не дойдет до вызова функции, так как объект my_fish
# просто не сможет быть создан. Ошибка будет обнаружена гораздо раньше!
# my_fish = Fish()
# make_it_speak(my_fish)