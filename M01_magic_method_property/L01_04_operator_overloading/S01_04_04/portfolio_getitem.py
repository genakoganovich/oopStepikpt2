class Portfolio:
    def __init__(self):
        self._stocks = {}

    # Магия длины
    def __len__(self):
        return len(self._stocks)

    # Магия чтения []
    def __getitem__(self, ticker):
        return self._stocks.get(ticker, 0)

    # Магия записи []
    def __setitem__(self, ticker, amount):
        if amount < 0:
            raise ValueError("Нельзя иметь отрицательное число акций")
        self._stocks[ticker] = amount

    # Вспомогательный метод для добавления (накапливания)
    def add_stock(self, ticker, amount):
        self._stocks[ticker] = self._stocks.get(ticker, 0) + amount

    def __str__(self):
        return str(self._stocks)


# --- Тестируем ---
my_port = Portfolio()

# 1. Используем вспомогательный метод (накапливаем)
my_port.add_stock("AAPL", 10)
my_port.add_stock("AAPL", 5)  # Теперь их 15!

# 2. Используем __setitem__ (устанавливаем напрямую)
my_port["GOOGL"] = 3
my_port["TSLA"] = 50

# 3. Используем __len__
print(f"Всего позиций в портфеле: {len(my_port)}")  # Вывод: 3

# 4. Используем __getitem__
print(f"У нас Apple: {my_port['AAPL']} шт.")  # Вывод: 15
print(f"У нас Google: {my_port['GOOGL']} шт.")  # Вывод: 3