from project.product import Product
from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            return [p for p in self.products if p.name == product_name][0]
        except Exception:
            pass

    def remove(self, product_name: str):
        try:
            self.products.remove([p for p in self.products if p.name == product_name][0])
        except Exception:
            pass

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])

