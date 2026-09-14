"""Primality, factorization, GCD/LCM, modular arithmetic, Fibonacci."""

import sympy as sp


def is_prime(n):
    return {"number": n, "is_prime": bool(sp.isprime(n))}


def next_prime(n):
    return {"number": n, "next_prime": int(sp.nextprime(n))}


def primes_upto(n):
    return {"limit": n, "primes": [int(p) for p in sp.primerange(2, n + 1)]}


def gcd(*nums):
    if len(nums) < 2:
        raise ValueError("Provide at least two numbers.")
    return {"numbers": list(nums), "gcd": int(sp.gcd(*nums))}


def lcm(*nums):
    if len(nums) < 2:
        raise ValueError("Provide at least two numbers.")
    return {"numbers": list(nums), "lcm": int(sp.lcm(*nums))}


def factorize(n):
    if n < 2:
        return {"number": n, "factors": {}}
    factors = sp.factorint(n)
    return {
        "number": n,
        "factors": {int(k): int(v) for k, v in factors.items()},
        "display": " × ".join(
            f"{k}^{v}" if v > 1 else str(k) for k, v in factors.items()
        ),
    }


def divisors(n):
    return {"number": n, "divisors": sorted(int(d) for d in sp.divisors(n))}


def modular(a, b, m):
    if m == 0:
        raise ValueError("Modulus cannot be 0.")
    return {
        "a": a, "b": b, "modulus": m,
        "a+b mod m": (a + b) % m,
        "a*b mod m": (a * b) % m,
        "a^b mod m": pow(a, b, m),
    }


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0.")
    return {"n": n, "fibonacci": int(sp.fibonacci(n))}
