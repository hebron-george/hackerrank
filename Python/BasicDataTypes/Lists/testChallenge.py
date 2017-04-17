import unittest
import challenge
import StringIO
import sys

class TestChallenge(unittest.TestCase):

    def setUp(self):
        self.sample_commands = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']

    def test_read_12_input_commands(self):
        a = challenge.read_input_commands(12)
        e = self.sample_commands
        self.assertEqual(a, e)

    def test_parse_command(self):
        a = challenge.parse_command('insert 0 5')
        e = ['insert', '0', '5']
        self.assertEqual(a, e)

    def test_execute_insert_operation_on_empty_list(self):
        a = challenge.execute_operation([], ['insert', '0', '5'])
        e = [5]
        self.assertEqual(a, e)

    def test_execute_print_operation(self):
        a = StringIO.StringIO()
        sys.stdout = a
        challenge.execute_operation([5], ['print'])
        sys.stdout = sys.__stdout__
        e = '[5]\n'
        self.assertEqual(a.getvalue(), e)

    def test_execute_remove(self):
        e = [8]
        a = challenge.execute_operation([5, 8], ['remove', '5'])
        self.assertEqual(a, e)

    def test_execute_append(self):
        e = [8, 2]
        a = challenge.execute_operation([8], ['append', '2'])
        self.assertEqual(a, e)

    def test_execute_sort(self):
        e = [2, 8]
        a = challenge.execute_operation([8, 2], ['sort'])
        self.assertEqual(a, e)

    def test_execute_pop(self):
        e = [2]
        a = challenge.execute_operation([2, 8], ['pop'])
        self.assertEqual(a, e)

    def test_execute_reverse(self):
        e = [8, 2, 1]
        a = challenge.execute_operation([1, 2, 8], ['reverse'])
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()