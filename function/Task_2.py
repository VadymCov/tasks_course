# 🧮 Mathematical Functions Program
# This program takes an integer and a function name as input on separate lines,
# applies the specified function to the number, and outputs the result.
# Supported functions: square (x**2), cube (x**3), sqrt (math.sqrt(x)),
# abs (abs(x)), sin (math.sin(x) in radians).
# Solved without conditional statements using a dictionary of functions.

from math import *


def square(n):
    return n**2


def cube(n):
    return n**3


def root(n):
    return n**0.5


def module(n):
    return abs(n)


def sine(n):
    return sin(n)


n, name = [input() for _ in range(2)]
math_functions = {"квадрат": square, "куб": cube, "корень": root, "модуль": module, "синус": sine}
print(math_functions[name](int(n)))
