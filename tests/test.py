import unittest
from datetime import datetime
from solution import get_ordered_login_length

class SolutionTest(unittest.TestCase):

    __dateformat__ = '%Y-%m-%d'

    # setup phase add simple data test from readme
    def setUp(self):
        self.sample_answer = [
            ('2021-03-16', '2021-03-18', 3),
            ('2021-03-13', '2021-03-13', 1)] 

    # positive testing with good data
    def test_postive_from_readme(self):
        # create the data sample
        sample = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

        result = get_ordered_login_length(sample)

        # compare the result with the original answer
        self.assertEqual(len(result), len(self.sample_answer))                
        self.assertEqual(result[0], self.sample_answer[0])
        self.assertEqual(result[1], self.sample_answer[1])

    # negative testing with empty list
    def test_empty_data(self):

        result = get_ordered_login_length([])

        # the result should be None 
        self.assertIsNone(result)


    # negative test with wrong datetime format
    def test_wrong_dateformat(self):
        sample = ['2021-03-13', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

        # checking if the exception is raised
        self.assertRaises(ValueError, lambda: get_ordered_login_length(sample))

    # negative testing with wrong item list data type
    def test_wrong_list_data_type(self):

        sample = [1,2,34,5]

        # checking if the exception is raised
        self.assertRaises(TypeError, lambda: get_ordered_login_length(sample))

    # negative testing for wrong data type that passed to the method
    def test_wrong_data_type(self):

        # use boolean data type
        sample = True

        # checking if the exception is raised
        self.assertRaises(Exception, lambda: get_ordered_login_length(sample))


if __name__ == '__main__':
    unittest.main()
