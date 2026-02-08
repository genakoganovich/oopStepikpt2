class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # 1. Сначала пишем __repr__ для разработчиков.
    def __repr__(self):
        return f"Car(model={self.model!r}, color={self.color!r})"

    # 2. Затем добавляем __str__ для красивого вывода.
    def __str__(self):
        return f"Красный автомобиль модели Tesla"  # В нашем случае это будет негибко, лучше так:
        # return f"{self.color.capitalize()} автомобиль модели {self.model}"


my_car = Car("Tesla", "red")

# Теперь у нас есть оба варианта:
print(my_car)  # Вызовет __str__:  Красный автомобиль модели Tesla
print(repr(my_car))  # Вызовет __repr__: Car(model='Tesla', color='red')
print([my_car])  # Вызовет __repr__: [Car(model='Tesla', color='red')]