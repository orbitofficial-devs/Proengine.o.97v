"""Algebraic manipulation: simplify, expand, factor, partial fractions."""

import sympy as sp


def simplify(expr):
    return sp.simplify(expr)


def expand(expr):
    return sp.expand(expr)


def factor(expr):
    return sp.factor(expr)


def together(expr):
    return sp.together(expr)


def apart(expr, var):
    return sp.apart(expr, var)
