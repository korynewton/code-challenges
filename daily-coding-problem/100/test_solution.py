import unittest
from solution import num_steps

class TestNumSteps(unittest.TestCase):
    def test_movement(self):
        tests = [[[(0,0),(1,1),(1,2)],2], [[(1,5),(0,0),(-5,3)],10], [[(-100,-50),(-73,0),(-24,32),(24,24)],147]]
        for test_case in tests:
           moves = test_case[0]
           answer = test_case[1]
        self.assertEqual(num_steps(moves),answer)



if __name__ == "__main__":
    unittest.main()
