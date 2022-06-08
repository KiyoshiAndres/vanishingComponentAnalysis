import sympy as sym
from SheavesOfFunctions import *

# Example Data

initial_Sm = [[0,0],[1,1],[-1,1], [2,4], [-2,4]]
initial_F = [constant_function(sym.sqrt(len(initial_Sm)))]
initial_C = [basic_function(n) for n in range(len(initial_Sm[0]))]
initial_e = 0


class FindRangeNull():
    def __init__(self, F, C, Sm, e):
        set_of_squigly = self.squigly_functions(C, F, Sm)
        matrix_A = self.matrix_A(set_of_squigly, Sm)
        L, D, U = matrix_A.singular_value_decomposition()


    def squigly_functions(self, main_functions, function_set, points):
        """Computes the set of squigly functions"""
        squigly_functions = []
        for function in main_functions:
            squigly_functions.append(self.squigly_function(function_set, function, points))
        return squigly_functions

    def squigly_function(self, function_set, main_func, points):
        """Computes the squigly function"""
        sum = constant_function(0)
        for function in function_set:
            dot_product = function(points).dot(main_func(points))
            scalar_product = ScalarProduct(dot_product, function)
            sum = SumOfFunctions(scalar_product, sum)
        return SubOfFunctions(main_func, sum)

    def matrix_A(self, function_set, points):
        """Computes matrix A"""
        matrix = sym.Matrix()
        n = 0
        for function in function_set:
            if n == 0:
                matrix = function(points)
                n += 1
            else:
                matrix = matrix.col_insert(n, function(points))
                n += 1
        return matrix

FindRangeNull(initial_F,initial_C,initial_Sm,initial_e)












