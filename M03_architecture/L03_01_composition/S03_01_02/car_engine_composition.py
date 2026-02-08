class Engine:
    """Компонент: Двигатель"""
    def start(self):
        print("Двигатель запущен.")

    def stop(self):
        print("Двигатель остановлен.")

class Wheel:
    """Компонент: Колесо"""
    def rotate(self):
        print("Колесо вращается.")


class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

    def start_car(self):
        """Машина делегирует запуск своему двигателю."""
        print(f"Запускаем машину {self.model}...")
        self.engine.start()

    def stop_car(self):
        """Машина делегирует остановку своему двигателю."""
        self.engine.stop()

    def drive(self):
        """Машина делегирует вращение своим колесам."""
        print("Машина едет...")
        for wheel in self.wheels:
            wheel.rotate()


# --- Тестируем ---
my_car = Car("Tesla")
my_car.start_car()
my_car.drive()