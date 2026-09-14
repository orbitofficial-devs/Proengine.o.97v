"""
Core MathEngine class.
Wraps all sub-modules into one clean interface.
"""

import sympy as sp

from . import algebra, calculus, solver, linalg, numbertheory, stats


class MathEngine:
    """Unified interface to all math operations."""

    def __init__(self, variable: str = "x"):
        self.x = sp.Symbol(variable, real=True)
        self.var_name = variable

    # ---------- Parsing ----------
    def parse(self, expr: str):
        """Parse a string into a SymPy expression."""
        if not expr or not str(expr).strip():
            raise ValueError("Empty expression.")
        try:
            return sp.sympify(expr, locals={self.var_name: self.x})
        except (sp.SympifyError, SyntaxError, TypeError) as e:
            raise ValueError(f"Invalid expression: {e}")

    def _num_list(self, values):
        out = []
        for v in values:
            try:
                out.append(sp.sympify(v))
            except Exception:
                raise ValueError(f"Invalid number: {v}")
        return out

    # ---------- Algebra ----------
    def simplify(self, expr):      return algebra.simplify(self.parse(expr))
    def expand(self, expr):        return algebra.expand(self.parse(expr))
    def factor(self, expr):        return algebra.factor(self.parse(expr))
    def together(self, expr):      return algebra.together(self.parse(expr))
    def apart(self, expr):         return algebra.apart(self.parse(expr), self.x)

    # ---------- Calculus ----------
    def derivative(self, expr, order=1):
        return calculus.derivative(self.parse(expr), self.x, order)

    def integrate(self, expr, lower=None, upper=None):
        return calculus.integrate(self.parse(expr), self.x, lower, upper)

    def limit(self, expr, point, direction="+"):
        return calculus.limit(self.parse(expr), self.x, point, direction)

    def series(self, expr, point=0, order=6):
        return calculus.series(self.parse(expr), self.x, point, order)

    def sum_series(self, expr, var, start, end):
        v = sp.Symbol(var)
        return calculus.summation(self.parse(expr), v, start, end)

    # ---------- Solver ----------
    def solve(self, equation, variable=None):
        var = sp.Symbol(variable) if variable else self.x
        return solver.solve_equation(equation, var)

    def solve_system(self, equations, variables):
        return solver.solve_system(equations, variables)

    def solve_inequality(self, inequality, variable=None):
        var = sp.Symbol(variable) if variable else self.x
        return solver.solve_inequality(inequality, var)

    # ---------- Linear Algebra ----------
    def matrix_det(self, matrix_data):       return linalg.determinant(matrix_data)
    def matrix_inverse(self, matrix_data):   return linalg.inverse(matrix_data)
    def matrix_rref(self, matrix_data):      return linalg.rref(matrix_data)
    def matrix_eigen(self, matrix_data):     return linalg.eigen(matrix_data)
    def matrix_multiply(self, a, b):         return linalg.multiply(a, b)
    def matrix_transpose(self, matrix_data): return linalg.transpose(matrix_data)
    def matrix_rank(self, matrix_data):      return linalg.rank(matrix_data)

    # ---------- Number Theory ----------
    def is_prime(self, n):          return numbertheory.is_prime(int(n))
    def next_prime(self, n):        return numbertheory.next_prime(int(n))
    def primes_upto(self, n):       return numbertheory.primes_upto(int(n))
    def gcd(self, *nums):           return numbertheory.gcd(*nums)
    def lcm(self, *nums):           return numbertheory.lcm(*nums)
    def factorize(self, n):         return numbertheory.factorize(int(n))
    def divisors(self, n):          return numbertheory.divisors(int(n))
    def modular(self, a, b, m):     return numbertheory.modular(a, b, m)
    def fibonacci(self, n):         return numbertheory.fibonacci(int(n))

    # ---------- Statistics ----------
    def mean(self, data):       return stats.mean(self._num_list(data))
    def median(self, data):     return stats.median(self._num_list(data))
    def mode(self, data):       return stats.mode(self._num_list(data))
    def variance(self, data):   return stats.variance(self._num_list(data))
    def stddev(self, data):     return stats.stddev(self._num_list(data))
    def stdev_sample(self, data): return stats.stdev_sample(self._num_list(data))