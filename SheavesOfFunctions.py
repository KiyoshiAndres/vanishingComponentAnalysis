import sympy as sym

def SumOfFunctions(function_1, function_2):
    """Returns the function that is the pointwise sum of two functions"""
    def sum(a):
        return function_1(a) + function_2(a)
    return sum

def SubOfFunctions(function_1, function_2):
    """Returns the function that is the pointwise subtraction of two functions"""
    def sub(a):
        return function_1(a) - function_2(a)
    return sub

def ProductOfFunctions(function_1, function_2):
    """Returns the function that is the pointwise product of two functions"""
    def prod(a):
        return function_1(a) * function_2(a)
    return prod

def ScalarProduct(scalar, function_2):
    def prod(a):
        return scalar * function_2(a)
    return prod

def basic_function(int):
    "Basic building block"
    def function(a):
        return sym.Matrix([point[int - 1] for point in a])
    return function

def constant_function(value):
    def function(a):
        output = []
        for point in a:
            output.append(value)
        return sym.Matrix(output)
    return function