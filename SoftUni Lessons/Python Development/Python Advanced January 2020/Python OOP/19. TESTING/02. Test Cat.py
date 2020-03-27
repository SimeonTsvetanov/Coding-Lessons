import unittest


# For testing remove or comment the class CAT:
class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat(name="Tom")

    def test_if_cat_size_is_increased_after_eating(self):
        """Cat's size is increased after eating"""
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_if_car_is_fed_after_eating(self):
        """Cat is fed after eating"""
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_when_already_fed_should_raise_error(self):
        """Cat cannot eat if already fed, raises an error"""

        with self.assertRaises(Exception) as context:
            self.cat.eat()
            self.cat.eat()

        self.assertEqual('Already fed.', str(context.exception))

    def test_cannot_fall_asleep_if_not_fed_raises_an_error(self):
        """Cat cannot fall asleep if not fed, raises an error"""

        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_if_not_sleepy_after_sleeping(self):
        """Cat is not sleepy after sleeping"""
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
