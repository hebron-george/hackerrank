import unittest, challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_list_for_base_1112(self):
        a = challenge.get_list(1,1,1,2)
        e = [[0,0,0], [0,0,1], [0,1,0], [1,0,0], [1,1,1]]
        self.assertEqual(a,e)

    def test_get_list_for_base_2223(self):
        a = challenge.get_list(2, 2, 2, 3)
        e = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 2], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
        self.assertEqual(a,e)

if __name__ == "__main__":
    unittest.main()
