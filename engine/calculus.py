"""Derivatives, integrals, limits, series, summations."""

import sympy as sp


def derivative(expr, var, order=1):
    if order < 1:
        raise ValueError("Derivative order must be >= 1.")
    result = sp.diff(expr, var, order)
    return {
        "input": str(expr),
        "operation": f"d^{order}/d{var}^{order}",
        "result": str(result),
        "simplified": str(sp.simplify(result)),
    }


def integrate(expr, var, lower=None, upper=None):
    if lower is not None and upper is not None:
        a = sp.sympify(lower)
        b = sp.sympify(upper)
        result = sp.integrate(expr, (var, a, b))
        return {
            "input": str(expr),
            "operation": f"∫[{a}, {b}]",
            "result": str(result),
            "simplified": str(sp.simplify(result)),
            "numeric": float(result.evalf()) if result.is_number else None,
        }
    result = sp.integrate(expr, var)
    return {
        "input": str(expr),
        "operation": "∫ (indefinite)",
        "result": str(result),
        "simplified": str(sp.simplify(result)),
    }


def limit(expr, var, point, direction="+"):
    p = sp.sympify(point)
    result = sp.limit(expr, var, p, dir=direction)
    return {
        "input": str(expr),
        "operation": f"lim {var}→{p}",
        "result": str(result),
    }


def series(expr, var, point=0, order=6):
    p = sp.sympify(point)
    result = sp.series(expr, var, p, order).removeO()
    return {
        "input": str(expr),
        "operation": f"Taylor series around {p} (order {order})",
        "result": str(result),
    }


def summation(expr, var, start, end):
    a = sp.sympify(start)
    b = sp.sympify(end)
    result = sp.summation(expr, (var, a, b))
    return {
        "input": str(expr),
        "operation": f"Σ from {a} to {b}",
        "result": str(result),
        "simplified": str(sp.simplify(result)),
    }