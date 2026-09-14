"""Equation, system, and inequality solving."""

import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application,
)


TRANSFORMS = standard_transformations + (implicit_multiplication_application,)


def _to_eq(equation_str, var):
    """Turn 'x**2 = 4' or 'x**2 - 4' into a SymPy Eq."""
    s = str(equation_str).strip()
    if "=" in s:
        left, right = s.split("=", 1)
        left_expr = parse_expr(left, transformations=TRANSFORMS, local_dict={str(var): var})
        right_expr = parse_expr(right, transformations=TRANSFORMS, local_dict={str(var): var})
        return sp.Eq(left_expr, right_expr)
    else:
        expr = parse_expr(s, transformations=TRANSFORMS, local_dict={str(var): var})
        return sp.Eq(expr, 0)


def solve_equation(equation_str, var):
    eq = _to_eq(equation_str, var)
    solutions = sp.solve(eq, var, dict=False)
    return {
        "equation": str(eq),
        "variable": str(var),
        "solutions": [str(s) for s in solutions] if isinstance(solutions, list) else [str(solutions)],
        "count": len(solutions) if isinstance(solutions, list) else 1,
    }


def solve_system(equations, variables):
    symbols = [sp.Symbol(v) for v in variables]
    eqs = []
    for eq_str in equations:
        s = str(eq_str).strip()
        if "=" in s:
            left, right = s.split("=", 1)
            eqs.append(sp.Eq(
                parse_expr(left, transformations=TRANSFORMS, local_dict=dict(zip(variables, symbols))),
                parse_expr(right, transformations=TRANSFORMS, local_dict=dict(zip(variables, symbols))),
            ))
        else:
            eqs.append(sp.Eq(
                parse_expr(s, transformations=TRANSFORMS, local_dict=dict(zip(variables, symbols))),
                0,
            ))

    solutions = sp.solve(eqs, symbols, dict=True)
    formatted = []
    for sol in solutions:
        formatted.append({str(k): str(v) for k, v in sol.items()})
    return {
        "equations": [str(e) for e in eqs],
        "variables": variables,
        "solutions": formatted,
        "count": len(formatted),
    }


def solve_inequality(inequality_str, var):
    s = str(inequality_str).strip()

    # Detect the operator
    for op in [">=", "<=", ">", "<"]:
        if op in s:
            left, right = s.split(op, 1)
            left_expr = sp.sympify(left)
            right_expr = sp.sympify(right)
            if op == ">=":
                ineq = left_expr >= right_expr
            elif op == "<=":
                ineq = left_expr <= right_expr
            elif op == ">":
                ineq = left_expr > right_expr
            else:
                ineq = left_expr < right_expr
            break
    else:
        raise ValueError("No inequality operator found. Use <, >, <=, or >=.")

    solution = sp.solve_univariate_inequality(ineq, var, relational=False)
    return {
        "inequality": str(ineq),
        "variable": str(var),
        "solution": str(solution),
    }
