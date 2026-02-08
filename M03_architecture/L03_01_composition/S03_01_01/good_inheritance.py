class Vehicle:
    def move(self):
        print("Транспортное средство движется.")

class Car(Vehicle): # Car IS-A Vehicle
    def honk(self):
        print("Би-бип!")

my_car = Car()
my_car.move() # Унаследованный метод