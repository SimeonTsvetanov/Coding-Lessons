import unittest


# Remove or comment the Worker class for testing in Judge:
class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


class WorkerTests(unittest.TestCase):
    def setUp(self):
        """This function is created to keep the code DRI It will be executed on each test."""
        self.worker = Worker(name="Simeon", salary=1000, energy=10)

    def test_if_init_name_salary_energy_are_the_correct_attributes(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        self.assertEqual(self.worker.name, "Simeon")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 10)

    def test_if_energy_is_incremented_when_rest_is_called(self):
        """Test if the worker's energy is incremented after the rest method is called. """
        self.worker.rest()
        # After resting the energy should be 11
        self.assertEqual(self.worker.energy, 11)

    def test_work_when_energy_is_0_should_raise_error(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        with self.assertRaises(Exception) as context:
            # Forcing the worker to work 11 times, but he has just 10 energy:
            [self.worker.work() for each_time in range(11)]
        self.assertEqual('Not enough energy.', str(context.exception))

    def test_if_money_is_increased_after_work_method_is_called(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)

    def test_if_worker_energy_is_decreased_after_work_method_is_called(self):
        """Test if the worker's energy is decreased after the work method is called"""
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_if_get_info_method_gives_the_correct_string(self):
        """Test if the get_info method returns the proper string with correct values"""
        self.assertEqual(self.worker.get_info(), "Simeon has saved 0 money.", msg="test has gone good!")


if __name__ == "__main__":
    unittest.main()
