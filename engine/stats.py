"""Basic descriptive statistics."""

import sympy as sp


def _clean(data):
    if not data:
        raise ValueError("Empty dataset.")
    return [sp.Rational(float(x)) if not hasattr(x, "is_rational") else x for x in data]


def mean(data):
    return str(sp.Add(*data) / len(data))


def median(data):
    s = sorted(data, key=float)
    n = len(s)
    if n % 2 == 0:
        return str((s[n // 2 - 1] + s[n // 2]) / 2)
    return str(s[n // 2])


def mode(data):
    from collections import Counter
    counter = Counter([str(x) for x in data])
    max_count = max(counter.values())
    modes = [k for k, v in counter.items() if v == max_count]
    return {"modes": modes, "count": max_count}


def variance(data):
    n = len(data)
    m = sp.Add(*data) / n
    return str(sum((x - m) ** 2 for x in data) / n)


def stddev(data):
    return str(sp.sqrt(sp.sympify(variance(data))))


def stdev_sample(data):
    n = len(data)
    if n < 2:
        raise ValueError("Need at least 2 data points.")
    m = sp.Add(*data) / n
    return str(sp.sqrt(sum((x - m) ** 2 for x in data) / (n - 1)))
