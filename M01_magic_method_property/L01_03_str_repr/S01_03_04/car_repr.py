class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # Реализуем ТОЛЬКО repr. Этого уже достаточно для комфортной работы.
    def __repr__(self):
        return f"Car(model={self.model!r}, color={self.color!r})"


my_car = Car("Tesla", "Red")
print(my_car)  # Выведет: Car(model='Tesla', color='Red')