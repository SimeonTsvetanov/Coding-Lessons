"""
Objects and Classes - Exericse
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1734#2

SUPyF2 Objects/Classes-Exericse - 03. Catalogue

Problem:
Create a class Catalogue. The __init__ method should accept the name of the catalogue.
Each catalogue should also have an attribute called products and it should be a list.
The class should also have three more methods:
•	add_product(product) - add the product to the product list
•	get_by_letter(first_letter) - returns a list containing only the products that start with the given letter
•	__repr__ - returns the catalogue info in the following format:
"Items in the {name} catalogue:
{item1}
{item2}"
The items should be sorted alphabetically (default sorting)

Examples:
Test Code:
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))

Output:
['Chair', 'Carpet']
Items in the Furniture catalogue:
Carpet
Chair
Desk
Mirror
Sofa
"""


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        f_l_list = [pr for pr in self.products if pr[0] == first_letter]
        return f_l_list

    def __str__(self):
        result = ''
        result_list = [x for x in sorted(self.products)]
        result += f"Items in the {self.name} catalogue:\n"
        result += f"\n".join(result_list)
        return result

    
class Catalogue_take_two:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
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

