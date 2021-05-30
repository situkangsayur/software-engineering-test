import unittest
from datetime import datetime
from solution import get_ordered_login_length

class SolutionTest(unittest.TestCase):

    __dateformat__ = '%Y-%m-%d'

    def setUp(self):
        self.sample_answer = [
            ('2021-03-16', '2021-03-18', 3),
            ('2021-03-13', '2021-03-13', 1)] 



    def test_postive_from_readme(self):
        sample = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

        result = get_ordered_login_length(sample)

        self.assertEqual(len(result), len(self.sample_answer))                
        self.assertEqual(result[0], self.sample_answer[0])
        self.assertEqual(result[1], self.sample_answer[1])

    def test_empty_data(self):

        result = get_ordered_login_length([])
        self.assertIsNone(result)


    def test_wrong_dateformat(self):
        sample = ['2021-03-13', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

        self.assertRaises(ValueError, lambda: get_ordered_login_length(sample))

    def test_wrong_list_data_type(self):
        sample = [1,2,34,5]
        self.assertRaises(TypeError, lambda: get_ordered_login_length(sample))

    def test_wrong_list_data_type(self):
        sample = True
        self.assertRaises(Exception, lambda: get_ordered_login_length(sample))



if __name__ == '__main__':
    unittest.main()
