import unittest
from math_quiz import get_random_integer, get_random_operator, calculate_answer

class TestMathQuizGame(unittest.TestCase):

    def test_get_random_integer(self):
        #Test if random numbers generated are within the specified range.
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        #Test if random operators generated are one of the expected values.
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = get_random_operator()
            self.assertIn(operator, valid_operators)

    def test_calculate_answer(self):
        #Test if calculate_answer generates the correct problem statement and answer.
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 3, '+', '10 + 3', 13),
            (10, 3, '-', '10 - 3', 7),
            (10, 3, '*', '10 * 3', 30),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()