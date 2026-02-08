class Engine:
    def start(self):
        print("Двигатель запущен.")

    def stop(self):
        print("Двигатель остановлен.")

# ЭТО НЕПРАВИЛЬНЫЙ, НЕЛОГИЧНЫЙ ДИЗАЙН!
class Car(Engine): # Машина ЯВЛЯЕТСЯ Двигателем? НЕТ!
    def drive(self):
        print("Машина едет.")

my_bad_car = Car()
my_bad_car.start() # Технически это сработает...
my_bad_car.drive()