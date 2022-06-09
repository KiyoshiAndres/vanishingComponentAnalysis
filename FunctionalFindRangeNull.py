import sympy as sym
from SheavesOfFunctions import *

class FindRangeNull():
    def __init__(self, F, C, Sm, e):
        set_of_squigly = self.squigly_functions(C, F, Sm)
        matrix_A = self.matrix_A(set_of_squigly, Sm)
        L, D, U = matrix_A.singular_value_decomposition()
        g_i_functions = self.g_functions(set_of_squigly, U)
        self.output = [self.f_1_set(g_i_functions, D, e, Sm), self.v_1_set(g_i_functions, D, e)]

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
        n = 0
        for function in function_set:
            if n != 0:
                matrix = matrix.col_insert(n, function(points))
                n += 1
            else:
                matrix = function(points)
                n += 1
        return matrix

    def g_functions(self, function_set, matrix):
        """Computes the gi functions"""
        g_i_functions = []
        for i in range(len(function_set)):
            g_i = constant_function(0)
            j = 0
            for function in function_set:
                g_i = SumOfFunctions(g_i, ScalarProduct(matrix.T.row(j)[i], function))
                j += 1
            g_i_functions.append(g_i)
        return g_i_functions

    def f_1_set(self, function_set, diagonal_matrix, e, points):
        set = []
        for i in range(len(function_set)):
            if diagonal_matrix.row(i)[i] > e:
                set.append(ScalarProduct(function_set[i](points).norm(), function_set[i]))
        return set

    def v_1_set(self, function_set, diagonal_matrix, e):
        set = []
        for i in range(len(function_set)):
            if diagonal_matrix.row(i)[i] <= e:
                set.append(function_set[i])
        return set



# Example Data

initial_Sm = [[0,0],[1,1],[-1,1], [2,4], [-2,4]]
initial_F = [constant_function(sym.sqrt(len(initial_Sm)))]
initial_C = [basic_function(n) for n in range(len(initial_Sm[0]))]
initial_e = 0

FindRangeNull(initial_F,initial_C,initial_Sm,initial_e)









