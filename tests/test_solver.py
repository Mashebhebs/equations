from solver import *
import unittest

class SolverTestCase(unittest.TestCase):

    def test_solver_multiple_equations(self):

        
        # Test if a response is given
        self.assertIsNotNone(solve_equation(4,-2), "Should show solution")

        # Test if a problem is solved
        self.assertEqual("The value of x = 4.0",solve_equation(2,-8))



if __name__ == "__main__":
    unittest.main()