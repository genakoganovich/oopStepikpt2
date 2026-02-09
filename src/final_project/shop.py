from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    stock: int = 0


class StockError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_product(self, product: Product):
        if product.stock == 0:
            raise StockError(f"Товар '{product.name}' отсутствует на складе.")

        self._items.append(product)

    @property
    def total_price(self) -> float:
        return sum([item.price for item in self._items])

    @classmethod
    def from_products(cls, product_list: list) -> 'ShoppingCart':
        cart = ShoppingCart()
        for product in product_list:
            cart.add_product(product)
        return cart

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"В вашей корзине {len(self)} товаров на сумму {self.total_price} руб."
