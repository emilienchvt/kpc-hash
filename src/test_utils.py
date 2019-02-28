import unittest
from utils import HashCodeProblem

class TestHashCodeProblemMethods(unittest.TestCase):

    def test_parse_input(self):
        problem = HashCodeProblem(instance_folder='test_data', output_folder='test_output')
        example_in = problem.parse_input('a_example.txt')
        expected_in = (3, 5, 1, 6, ['TTTTT', 'TMMMT', 'TTTTT'])
        self.assertEqual(example_in, expected_in)

if __name__ == '__main__':
    unittest.main()
