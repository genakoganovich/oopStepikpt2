# --- Родитель 1 ---
class LandAnimal:
    def walk(self):
        print("Я иду по земле.")

    def greet(self):
        print("Я - наземное животное.")


# --- Родитель 2 ---
class WaterAnimal:
    def swim(self):
        print("Я плыву в воде.")

    def greet(self):
        print("Я - водное животное.")


# --- Дочерний класс с двумя родителями ---
class Frog(LandAnimal, WaterAnimal):
    # Тело класса может быть пустым, вся функциональность унаследована
    pass


# --- Тестируем ---
my_frog = Frog()

# Лягушка получила способности от ОБОИХ родителей!
my_frog.walk()  # Унаследовано от LandAnimal
my_frog.swim()  # Унаследовано от WaterAnimal