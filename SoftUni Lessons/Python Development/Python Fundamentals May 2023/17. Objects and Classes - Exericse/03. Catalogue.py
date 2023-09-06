class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> list:
        return list(filter(lambda p: p.startswith(first_letter), self.products))
        # return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self) -> str:
        result = f"Items in the {self.name} catalogue:"
        for product in sorted(self.products):
            result += f"\n{product}"
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
