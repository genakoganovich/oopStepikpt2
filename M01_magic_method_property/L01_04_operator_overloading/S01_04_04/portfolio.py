class Portfolio:
    def __init__(self):
        # Храним данные в словаре: Тикер -> Количество
        self._stocks = {}

    def add_stock(self, ticker, amount):
        # Если акция уже есть, увеличиваем количество. Если нет — создаем.
        # Метод .get(key, 0) вернет текущее значение или 0, если ключа нет.
        self._stocks[ticker] = self._stocks.get(ticker, 0) + amount

    def __repr__(self):
        return f"Portfolio({self._stocks})"

    # Добавляем внутрь класса Portfolio
    def __len__(self):
        """Возвращает количество уникальных позиций (тикеров) в портфеле."""
        return len(self._stocks)

# Добавляем внутрь класса Portfolio
    def __getitem__(self, ticker):
        """Позволяет получать количество акций через obj['TICKER']"""
        # Если акции нет, пусть возвращает 0 (удобно для аналитики),
        # или можно позволить словарю выбросить KeyError
        return self._stocks.get(ticker, 0)

    # Добавляем внутрь класса Portfolio
    def __setitem__(self, ticker, amount):
        """Позволяет писать obj['TICKER'] = amount"""
        # Здесь можно добавить валидацию!
        if amount < 0:
            raise ValueError("Количество не может быть отрицательным")

        # Перезаписываем или добавляем (тут логика зависит от вашей задачи)
        # В данном случае реализуем прямую установку значения
        self._stocks[ticker] = amount

p = Portfolio()
p.add_stock("AAPL", 10)
p.add_stock("TSLA", 5)
print(p["AAPL"])  # Вывод: 10
print(p["IBM"])   # Вывод: 0 (так как мы использовали .get в реализации)

print(len(p))  # Вывод: 2 (две уникальные бумаги)