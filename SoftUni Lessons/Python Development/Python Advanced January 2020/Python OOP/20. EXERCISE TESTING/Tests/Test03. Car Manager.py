from Project.car_manager import Car
import unittest


class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.car = Car(make="Toyota", model="RAV4", fuel_consumption=7, fuel_capacity=60)

    def test_the_init_if_all_the_attributes_are_taken(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "RAV4")
        self.assertEqual(self.car.fuel_consumption, 7)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_validate_if_make_is_empty_a_error_will_be_given(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_validate_if_model_is_empty_a_error_will_be_given(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_validate_if_new_fuel_consumption_is_bellow_0_a_error_will_be_given(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_validate_if_new_fuel_capacity_is_bellow_0_a_error_will_be_given(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_validate_if_new_fuel_amount_is_bellow_0_a_error_will_be_given(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_when_refuel_is_called_if_new_fuel_amount_is_bellow_0_a_error_will_be_given(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_when_refuel_method_is_called_with_correct_data_if_it_will_work_correctly(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_when_refuel_method_is_called_if_we_give_it_more_liters_than_the_capacity_not_to_overfill(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, 60)

    def test_drive_method_will_raise_error_if_not_enough_fuel_for_the_trip(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(1)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))


if __name__ == '__main__':
    unittest.main()
