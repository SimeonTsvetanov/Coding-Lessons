from project.factory.paint_factory import PaintFactory
import unittest


class TestsPaintFactory(unittest.TestCase):
    def test_init_paint_factory_method_should_return_the_correct_attributes(self):
        paint_factory = PaintFactory("Mask", 10)

        self.assertEqual(paint_factory.name, "Mask")
        self.assertEqual(paint_factory.capacity, 10)
        self.assertEqual(paint_factory.ingredients, {})
        self.assertEqual(paint_factory.products, {})
        self.assertEqual(paint_factory.__class__.__name__, "PaintFactory")
        self.assertEqual(paint_factory.__class__.__base__.__name__, "Factory")

    def test_init_if_name_is_changed_it_will_be_the_new_one(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.name = "masked"
        self.assertEqual(paint_factory.name, "masked")

    def test_init_if_capacity_is_changed_it_will_be_the_new_one(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.capacity = 9
        self.assertEqual(paint_factory.capacity, 9)

    def test_paint_factory_inherits_the_base_class_factory_again(self):
        paint_factory = PaintFactory("Mask", 10)
        self.assertEqual(paint_factory.__class__.__base__.__name__, "Factory")

    def test_products_should_return_ingredients(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.add_ingredient('white', 5)
        self.assertEqual(paint_factory.products, {'white': 5})

    def test_add_ingredient_with_correct_details(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.add_ingredient('white', 1)
        self.assertEqual(paint_factory.ingredients, {'white': 1})

    def test_add_ingredient_with_incorrect_egg_name(self):
        paint_factory = PaintFactory("Mask", 10)
        with self.assertRaises(TypeError) as context:
            paint_factory.add_ingredient('invalid color', 2)
        self.assertEqual(str(context.exception), f"Ingredient of type invalid color not allowed in PaintFactory")

    def test_add_ingredient_with_but_with_bigger_value_then_capacity_should_raise_an_error(self):
        paint_factory = PaintFactory("Mask", 10)
        with self.assertRaises(ValueError) as context:
            paint_factory.add_ingredient('white', 200)
        self.assertEqual(str(context.exception), "Not enough space in factory")

    def test_add_add_ingredient_with_the_same_ingredient_will_just_make_the_count_bigger(self):
        paint_factory = PaintFactory("Mask", 10)

        paint_factory.add_ingredient('white', 1)
        paint_factory.add_ingredient('white', 1)
        self.assertEqual(paint_factory.ingredients, {'white': 2})

    def test_remove_ingredient_with_correct_details_should_add_them_correctly(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.add_ingredient('white', 8)
        paint_factory.remove_ingredient('white', 4)
        self.assertEqual(paint_factory.ingredients, {'white': 4})

    def test_remove_ingredient_with_incorrect_details_name_should_raise_errors(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.add_ingredient('white', 5)
        with self.assertRaises(KeyError):
            paint_factory.remove_ingredient('error_color', 2)

    def test_remove_ingredient_with_incorrect_details_should_raise_errors(self):
        paint_factory = PaintFactory("Mask", 10)
        paint_factory.add_ingredient('white', 5)
        with self.assertRaises(KeyError):
            paint_factory.remove_ingredient('error_color', 2)
        with self.assertRaises(ValueError):
            paint_factory.remove_ingredient('white', 100)


if __name__ == '__main__':
    unittest.main()
