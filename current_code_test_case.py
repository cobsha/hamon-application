import unittest
import current_code

class stringCount(unittest.TestCase):
    def test_check_normal_string(self):
        test_string = "shafi"
        desired_result = {'s': 1, 'h': 1, 'a': 1, 'f': 1, 'i': 1}
        self.assertEqual(current_code.f(test_string), desired_result)

    def test_special_characters_check(self):
        test_string = "@##&*%"
        desired_result = {'@': 1, '#': 2, '&': 1, '*': 1, '%': 1}
        self.assertEqual(current_code.f(test_string), desired_result)
    def test_list_check(self):
        test_string = ["India", "US", "UK", "US", "UAE", "Germany", "India"]
        desired_result = {'India': 2, 'US': 2, 'UK': 1, 'UAE': 1, 'Germany': 1}
        self.assertEqual(current_code.f(test_string), desired_result)

if __name__ == '__main__':
    unittest.main()
