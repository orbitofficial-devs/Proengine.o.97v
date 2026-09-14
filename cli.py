"""
Interactive CLI for the Math Engine.
Run: python cli.py
"""

from engine import MathEngine


BANNER = r"""
=====================================================
  MATH ENGINE  v1.0
  Symbolic • Calculus • Algebra • Linear Algebra
  Number Theory • Statistics
=====================================================
"""

MENU = """
  1. Simplify expression
  2. Expand expression
  3. Factor expression
  4. Derivative
  5. Integral
  6. Limit
  7. Taylor series
  8. Solve equation
  9. Solve system
 10. Solve inequality
 11. Matrix determinant
 12. Matrix inverse
 13. Matrix RREF
 14. Matrix eigenvalues
 15. Matrix rank
 16. Is prime?
 17. Prime factorization
 18. GCD / LCM
 19. Divisors of n
 20. Fibonacci
 21. Mean / Median / Mode
 22. Variance / Std dev
  0. Quit
"""


def show(data):
    print()
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"  {k:14}: {v}")
    else:
        print(f"  {data}")
    print()


def main():
    print(BANNER)
    engine = MathEngine()

    while True:
        print(MENU)
        choice = input("Select (0-22): ").strip()

        try:
            if choice == "0":
                print("Goodbye.")
                break

            elif choice == "1":
                show(engine.simplify(input("Expression: ")))
            elif choice == "2":
                show(engine.expand(input("Expression: ")))
            elif choice == "3":
                show(engine.factor(input("Expression: ")))
            elif choice == "4":
                expr = input("Expression: ")
                order = input("Order [1]: ").strip() or "1"
                show(engine.derivative(expr, int(order)))
            elif choice == "5":
                expr = input("Expression: ")
                lower = input("Lower bound (blank for indefinite): ").strip()
                if lower:
                    upper = input("Upper bound: ").strip()
                    show(engine.integrate(expr, lower, upper))
                else:
                    show(engine.integrate(expr))
            elif choice == "6":
                expr = input("Expression: ")
                pt = input("Limit point: ")
                show(engine.limit(expr, pt))
            elif choice == "7":
                expr = input("Expression: ")
                pt = input("Point [0]: ").strip() or "0"
                order = input("Order [6]: ").strip() or "6"
                show(engine.series(expr, pt, int(order)))
            elif choice == "8":
                eq = input("Equation (e.g. x**2 - 4 = 0): ")
                var = input("Variable [x]: ").strip() or "x"
                show(engine.solve(eq, var))
            elif choice == "9":
                eqs = []
                print("Enter equations one per line, blank to finish:")
                while True:
                    line = input("  > ").strip()
                    if not line:
                        break
                    eqs.append(line)
                vars_str = input("Variables (comma-separated): ")
                variables = [v.strip() for v in vars_str.split(",")]
                show(engine.solve_system(eqs, variables))
            elif choice == "10":
                ineq = input("Inequality (e.g. x**2 - 1 > 0): ")
                var = input("Variable [x]: ").strip() or "x"
                show(engine.solve_inequality(ineq, var))
            elif choice == "11":
                m = read_matrix()
                show(engine.matrix_det(m))
            elif choice == "12":
                m = read_matrix()
                show(engine.matrix_inverse(m))
            elif choice == "13":
                m = read_matrix()
                show(engine.matrix_rref(m))
            elif choice == "14":
                m = read_matrix()
                show(engine.matrix_eigen(m))
            elif choice == "15":
                m = read_matrix()
                show(engine.matrix_rank(m))
            elif choice == "16":
                show(engine.is_prime(int(input("Number: "))))
            elif choice == "17":
                show(engine.factorize(int(input("Number: "))))
            elif choice == "18":
                nums = [int(x) for x in input("Numbers (comma-sep): ").split(",")]
                print("  gcd:", engine.gcd(*nums))
                print("  lcm:", engine.lcm(*nums))
                print()
            elif choice == "19":
                show(engine.divisors(int(input("Number: "))))
            elif choice == "20":
                show(engine.fibonacci(int(input("n: "))))
            elif choice == "21":
                data = input("Numbers (comma-sep): ").split(",")
                print(f"  mean   : {engine.mean(data)}")
                print(f"  median : {engine.median(data)}")
                print(f"  mode   : {engine.mode(data)}")
                print()
            elif choice == "22":
                data = input("Numbers (comma-sep): ").split(",")
                print(f"  variance (pop)   : {engine.variance(data)}")
                print(f"  std dev  (pop)   : {engine.stddev(data)}")
                print(f"  std dev  (sample): {engine.stdev_sample(data)}")
                print()
            else:
                print("Invalid option.\n")

        except Exception as e:
            print(f"\n  ERROR: {e}\n")


def read_matrix():
    print("Enter rows, one per line, values comma-separated. Blank line to finish:")
    rows = []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        rows.append([x.strip() for x in line.split(",")])
    return rows


if __name__ == "__main__":
    main()