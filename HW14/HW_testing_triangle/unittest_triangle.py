from HW14.HW_testing_triangle.triangle import get_triangle_side
import unittest

class UnitTest(unittest.TestCase):

    def test_convert_string_to_float(self):
        self.assertRaises(ValueError, get_triangle_side, 'asd')

    def test_work_with_float(self):
        self.assertEqual(get_triangle_side('2.25'), 2.25)

    def test_work_with_integer(self):
        self.assertEqual(get_triangle_side('2'), 2.0)

    def test_negative_value_exception(self):
        self.assertRaises(ValueError, get_triangle_side, '0')


if __name__ == '__main__':
    unittest.main(verbosity=2)
