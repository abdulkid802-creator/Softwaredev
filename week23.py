import unittest

# class TestStringMethod(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('hello'.upper(), 'HELLO')
# if __name__ == '__main__':
#     unittest.main()

# def add(a, b):
#     return a + b
# class TestAdd(unittest.TestCase):
#     def test_add_numbers(self):
#         self.assertEqual(5, add(2, 3))
# if __name__ == "__main__":
#     unittest.main()

def categorise_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age: {age}"

# class TestCategorizeByAge(unittest.TestCase):
#     def test_child(self):
#         self.assertEqual("Child",categorise_by_age(5))
#     def test_adolescent(self):
#         self.assertEqual("Adolescent",categorise_by_age(15))
#     def test_adult(self):
#         self.assertEqual("Adult",categorise_by_age(30))
#     def test_golden_age(self):
#         self.assertEqual("Golden age",categorise_by_age(70))
#     def test_negative_age(self):
#         self.assertEqual("Invalid age: -1",categorise_by_age(-1))
#     def test_too_old(self):
#         self.assertEqual("Invalid age: 151",categorise_by_age(151))
# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from Calculation import Calculation
# class TestCalculations(unittest.TestCase):
#     def setUp(self):
#         self.calculation = Calculation(8, 2)
#     def test_sum(self):
#         self.assertEqual(10, self.calculation.get_sum(), 'The sum is wrong.')
#     def test_diff(self):
#         self.assertEqual(6, self.calculation.get_difference(), 'The difference is wrong.')
#     def test_product(self):
#         self.assertEqual(16, self.calculation.get_product(), 'The product is wrong.')
#     def test_quotient(self):
#         self.assertEqual(4, self.calculation.get_quotient(), 'The quotient is wrong.')
# if __name__ == '__main__':
#     unittest.main()

from calc_bill import calculate_total

class TestCalculateTotal(unittest.TestCase):
    def test_gold_under_25(self):
        total, msg = calculate_total(10, True)
        expected = round((57.23 * 10) * 0.965, 2)
        self.assertEqual(expected,total)
        self.assertIn("No quantity discount", msg)
    def test_gold_25_to_99(self):
        total, msg = calculate_total(50, True)
        expected = round((57.23 * 50) * 0.915, 2)
        self.assertEqual(expected,total)
        self.assertIn("quantity discount of 5%", msg)
    
    def test_gold_100_or_more(self):
        total, msg = calculate_total(150, True)
        expected = round((57.23 * 150) * 0.865, 2)
        self.assertEqual(expected ,total)
        self.assertIn("quantity discount of 10%", msg)
    def test_non_gold(self):
        total, msg = calculate_total(20, False)
        expected = round(57.23 * 20, 2)
        self.assertEqual(expected,total)
        self.assertIn("No quantity discount", msg)
    def test_zero_quantity(self):
        total, msg = calculate_total(0, True)
        self.assertEqual(0,total)
        self.assertIn("No quantity discount", msg)

    def test_negative_quantity(self):
        total, msg = calculate_total(-5, True)
        expected = round((57.23 * 5) * 0.965, 2)
        self.assertEqual(expected,total)
        self.assertIn("No quantity discount", msg)
if __name__ == '__main__':
    unittest.main()