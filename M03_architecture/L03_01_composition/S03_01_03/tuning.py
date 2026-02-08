class Engine:
    def start(self): print("Двигатель (150 л.с.) запущен.")

class SportEngine(Engine): # SportEngine IS-A Engine
    def start(self): print("Спортивный двигатель (500 л.с.) взревел!")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine # Мы получаем двигатель извне!

    def start_car(self):
        self.engine.start()

# --- Демонстрация гибкости ---
standard_engine = Engine()
my_car = Car("Ford", standard_engine)
my_car.start_car() # Вывод: Двигатель (150 л.с.) запущен.

# А теперь "тюнингуем" машину, просто заменив один атрибут!
print("\n--- Производим тюнинг ---")
sport_engine = SportEngine()
my_car.engine = sport_engine
my_car.start_car() # Вывод: Спортивный двигатель (500 л.с.) взревел!