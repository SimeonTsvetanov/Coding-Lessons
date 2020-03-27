from Project.list import IntegerList
import unittest


class TestsIntegerList(unittest.TestCase):
    def test_init_with_no_arguments_should_create_empty_data(self):
        data = []
        integer_list = IntegerList(*data)

        expected = []
        actual = integer_list.get_data()
        # actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected, msg="I expected to data to be empty but it is not.")

    def test_init_with_integer_args_should_add_args_to_data(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        expected = [1, 2, 3]
        actual = integer_list.get_data()
        self.assertEqual(actual, expected)

    def test_init_with_none_integer_args_should_not_add_elements_to_data(self):
        data = ['peter', 3]
        integer_list = IntegerList(*data)
        expected = [3]
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_get_data_method_should_return_data_attribute(self):
        data = [1, 2]
        integer_list = IntegerList(*data)
        expected = integer_list._IntegerList__data
        actual = integer_list.get_data()
        self.assertEqual(actual, expected)

    def test_add_element_function_should_add_element_and_return_the_list(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        expected = [1, 2, 3, 4]
        actual = integer_list.add(4)
        self.assertEqual(actual, expected)

    # def test_tanya_same_as_above(self):
    #     data = []
    #     integer_list = IntegerList(*data)
    #     integer_list.add(5)
    #     expected = [5]
    #     actual = integer_list.get_data()
    #     self.assertEqual(actual, expected)

    def test_add_element_when_given_string_as_a_value_should_give_value_error(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        with self.assertRaises(ValueError) as context:
            integer_list.add('not a integer')
        self.assertEqual(str(context.exception), "Element is not Integer")

    # def test_tanya_same_as_above_add_method_should_give_error(self):
    #     data = []
    #     integer_list = IntegerList(*data)
    #
    #     with self.assertRaises(ValueError) as context_manager:
    #         integer_list.add(3.5)
    #     self.assertEqual(context_manager.exception.args[0], "Element is not Integer")

    def test_add_method_with_integer_should_return_data(self):
        # Done with Tanya
        data = []
        integer_list = IntegerList(*data)
        expected = [5]
        actual = integer_list.add(5)
        self.assertEqual(actual, expected)

    def test_remove_valid_index_to_remove_element_on_given_index_and_should_return_it(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        expected = 2
        actual = integer_list.remove_index(1)
        self.assertEqual(actual, expected)

    def test_remove_index_when_given_index_out_of_range_should_give_IndexError(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        with self.assertRaises(IndexError) as context:
            integer_list.remove_index(10)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_remove_valid_index_should_delete_element_from_data(self):
        # Done by Tanya in class:
        data = [1]
        integer_list = IntegerList(*data)
        expected = []
        integer_list.remove_index(0)
        actual = integer_list.get_data()
        self.assertEqual(actual, expected)

    def test_get_method_invalid_index_should_give_error(self):
        data = [4, 7, 10]
        integer_list = IntegerList(*data)
        with self.assertRaises(IndexError) as context:
            integer_list.get(3)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_method_valid_index_should_return_element(self):
        data = [4, 7, 10]
        integer_list = IntegerList(*data)
        actual = integer_list.get(1)
        expected = 7
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
