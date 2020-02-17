import unittest
from solution import return_primes_summed_to_n

class TestSolution(unittest.TestCase):
    def test_solution(self):
        tests = [[4,[2,2]], [74, [3,71]],[1024,[3,1021]], [66,[5,61]]]
        for test in tests:
            x,y = test
            self.assertEqual(return_primes_summed_to_n(x),y)

if __name__ == "__main__":
    unittest.main()
        
