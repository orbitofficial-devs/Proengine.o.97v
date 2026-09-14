"""Matrix operations: determinant, inverse, RREF, eigenvalues, rank."""

import sympy as sp


def _to_matrix(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Matrix must be a non-empty list of rows.")
    rows = []
    for row in data:
        if not isinstance(row, list):
            raise ValueError("Each row must be a list.")
        rows.append([sp.sympify(v) for v in row])
    return sp.Matrix(rows)


def determinant(data):
    m = _to_matrix(data)
    if m.rows != m.cols:
        raise ValueError("Determinant requires a square matrix.")
    return {"matrix": str(m.tolist()), "determinant": str(m.det())}


def inverse(data):
    m = _to_matrix(data)
    if m.rows != m.cols:
        raise ValueError("Inverse requires a square matrix.")
    if m.det() == 0:
        raise ValueError("Matrix is singular (determinant is 0).")
    return {"matrix": str(m.tolist()), "inverse": str(m.inv().tolist())}


def rref(data):
    m = _to_matrix(data)
    r, pivots = m.rref()
    return {
        "matrix": str(m.tolist()),
        "rref": str(r.tolist()),
        "pivots": list(pivots),
    }


def eigen(data):
    m = _to_matrix(data)
    if m.rows != m.cols:
        raise ValueError("Eigenvalues require a square matrix.")
    eigenvals = m.eigenvals()
    eigenvects = m.eigenvects()
    return {
        "matrix": str(m.tolist()),
        "eigenvalues": {str(k): int(v) for k, v in eigenvals.items()},
        "eigenvectors": [
            {
                "eigenvalue": str(ev),
                "multiplicity": int(mult),
                "vectors": [str(vec) for vec in vecs],
            }
            for ev, mult, vecs in eigenvects
        ],
    }


def multiply(a, b):
    ma = _to_matrix(a)
    mb = _to_matrix(b)
    if ma.cols != mb.rows:
        raise ValueError(
            f"Cannot multiply {ma.rows}×{ma.cols} by {mb.rows}×{mb.cols}."
        )
    return {"product": str((ma * mb).tolist())}


def transpose(data):
    m = _to_matrix(data)
    return {"transpose": str(m.T.tolist())}


def rank(data):
    m = _to_matrix(data)
    return {"matrix": str(m.tolist()), "rank": int(m.rank())}
