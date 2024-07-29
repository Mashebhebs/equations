from solve_quadratic_equations import *

import unittest

class SolveQuadraticEquationTestCase(unittest.TestCase):

    def test_solve_quadratic_equation_no_real_solution_above_x_axis(self):

        # Test when 𝑥 is above the 𝑥-axis
        a,b,c = 1,2,3
        self.assertEqual("no solution", solution_exists(a,b,c)[1])
        self.assertEqual("There are no real roots for this equation.", solve(a,b,c))

        # Test when 𝑥 is above the 𝑥-axis

    def test_solve_quadratic_equation_no_real_solution_below_x_axis(self):
        a,b,c = -4,3,-7
        self.assertEqual("no solution", solution_exists(a,b,c)[1])
        self.assertEqual("There are no real roots for this equation.", solve(a,b,c))

    def test_solve_quadratic_equation_no_solution_b_equal_0(self):
       
        # Test when there is no real solution and b is equal to 0
        a,b,c = 4,0,1
        self.assertEqual("no solution", solution_exists(a,b,c)[1])
        self.assertEqual("There are no real roots for this equation.", solve(a,b,c))

    def test_solve_quadratic_equation_real_unequal_roots(self):

        # Test when real roots exist and are unequal

        a,b,c = 6,2,-8

        self.assertEqual("unequal",solution_exists(a,b,c)[1])
        self.assertEqual("The values of 𝑥: 𝑥 = -1.33 or 𝑥 = 1.0.", solve(a,b,c))

    def test_solve_quadratic_equation_real_unequal_roots_c_equal_0(self):

        # Test when there are unequal roots but c is equal to 0

        a,b,c = 2,6,0

        self.assertEqual("unequal",solution_exists(a,b,c)[1])
        self.assertEqual("The values of 𝑥: 𝑥 = -3.0 or 𝑥 = 0.0.", solve(a,b,c))

    def test_solve_quadratic_equation_real_unequal_roots_b_equal_0(self):

        # Test when there are unequal roots but b is equal to 0

        a,b,c = 2,0,-8

        self.assertEqual("unequal",solution_exists(a,b,c)[1])
        self.assertEqual("The values of 𝑥: 𝑥 = -2.0 or 𝑥 = 2.0.", solve(a,b,c))

    def test_solve_quadratic_equation_real_equal_roots(self):

        # Test when there are equal roots

        a,b,c = 1,2,1

        self.assertEqual("equal",solution_exists(a,b,c)[1])
        self.assertEqual("The value of 𝑥: 𝑥 = -1.0", solve(a,b,c))



