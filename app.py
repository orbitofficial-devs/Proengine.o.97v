"""Flask web API for the Math Engine."""

from flask import Flask, render_template, request, jsonify
from engine import MathEngine

app = Flask(__name__)
engine = MathEngine()


def handle(fn):
    """Wrap an operation, catching exceptions."""
    try:
        data = request.get_json() or {}
        result = fn(data)
        return jsonify({"ok": True, "data": result})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400


@app.route("/")
def home():
    return render_template("index.html")


# ---- Algebra ----
@app.route("/api/simplify", methods=["POST"])
def api_simplify():
    return handle(lambda d: {"result": engine.simplify(d["expression"])})


@app.route("/api/expand", methods=["POST"])
def api_expand():
    return handle(lambda d: {"result": engine.expand(d["expression"])})


@app.route("/api/factor", methods=["POST"])
def api_factor():
    return handle(lambda d: {"result": engine.factor(d["expression"])})


# ---- Calculus ----
@app.route("/api/derivative", methods=["POST"])
def api_derivative():
    return handle(lambda d: engine.derivative(d["expression"], int(d.get("order", 1))))


@app.route("/api/integrate", methods=["POST"])
def api_integrate():
    return handle(lambda d: engine.integrate(
        d["expression"], d.get("lower") or None, d.get("upper") or None
    ))


@app.route("/api/limit", methods=["POST"])
def api_limit():
    return handle(lambda d: engine.limit(d["expression"], d.get("point", "0")))


@app.route("/api/series", methods=["POST"])
def api_series():
    return handle(lambda d: engine.series(
        d["expression"], d.get("point", 0), int(d.get("order", 6))
    ))


# ---- Solver ----
@app.route("/api/solve", methods=["POST"])
def api_solve():
    return handle(lambda d: engine.solve(d["equation"], d.get("variable", "x")))


@app.route("/api/solve_system", methods=["POST"])
def api_solve_system():
    return handle(lambda d: engine.solve_system(d["equations"], d["variables"]))


@app.route("/api/inequality", methods=["POST"])
def api_inequality():
    return handle(lambda d: engine.solve_inequality(
        d["inequality"], d.get("variable", "x")
    ))


# ---- Linear Algebra ----
@app.route("/api/det", methods=["POST"])
def api_det():
    return handle(lambda d: engine.matrix_det(d["matrix"]))


@app.route("/api/inverse", methods=["POST"])
def api_inverse():
    return handle(lambda d: engine.matrix_inverse(d["matrix"]))


@app.route("/api/rref", methods=["POST"])
def api_rref():
    return handle(lambda d: engine.matrix_rref(d["matrix"]))


@app.route("/api/eigen", methods=["POST"])
def api_eigen():
    return handle(lambda d: engine.matrix_eigen(d["matrix"]))


@app.route("/api/rank", methods=["POST"])
def api_rank():
    return handle(lambda d: engine.matrix_rank(d["matrix"]))


# ---- Number Theory ----
@app.route("/api/is_prime", methods=["POST"])
def api_is_prime():
    return handle(lambda d: engine.is_prime(d["n"]))


@app.route("/api/factorize", methods=["POST"])
def api_factorize():
    return handle(lambda d: engine.factorize(d["n"]))


@app.route("/api/gcd", methods=["POST"])
def api_gcd():
    return handle(lambda d: {
        "gcd": engine.gcd(*d["numbers"]),
        "lcm": engine.lcm(*d["numbers"]),
    })


@app.route("/api/divisors", methods=["POST"])
def api_divisors():
    return handle(lambda d: engine.divisors(d["n"]))


@app.route("/api/fibonacci", methods=["POST"])
def api_fibonacci():
    return handle(lambda d: engine.fibonacci(d["n"]))


# ---- Stats ----
@app.route("/api/stats", methods=["POST"])
def api_stats():
    def go(d):
        data = d["data"]
        return {
            "mean": engine.mean(data),
            "median": engine.median(data),
            "mode": engine.mode(data),
            "variance": engine.variance(data),
            "stddev": engine.stddev(data),
        }
    return handle(go)


if __name__ == "__main__":
    app.run(debug=True)