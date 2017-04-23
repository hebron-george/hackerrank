import unittest
import challenge


class TestClass(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_student_average(self):
        a = challenge.get_student_average("Hebron", {"Hebron": [52, 56, 60]})
        e = 56.00
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
