import sympy as sym
from pprint import pprint

fun = "x**3 + x**2 - 3*x - 3"


class Secant:
    def __init__(self, _fun: str, _x0: float, _x1: float) -> None:
        self.function = sym.sympify(_fun)
        self.x0 = _x0
        self.x1 = _x1
        self.x = sym.Symbol("x")
        self.iterations = {}

    def solve(self, n_iter: int) -> float:
        x1 = self.x0
        x2 = self.x1

        for i in range(n_iter):
            function_value_x1 = self.function.subs(self.x, x1)
            function_value_x2 = self.function.subs(self.x, x2)

            try:
                next_guess = x2 - (function_value_x2 * (x2 - x1)) / (
                    function_value_x2 - function_value_x1
                )
            except ZeroDivisionError:
                print(
                    "Error: Division by zero. The derivative of the function is zero."
                )
                return

            next_guess = float(next_guess.evalf())

            self.iterations[i + 1] = {
                "x1": x1,
                "x2": x2,
                "x3": next_guess,
                "f(x1)": function_value_x1,
                "f(x2)": function_value_x2,
                "f(x3)": self.function.subs(self.x, next_guess),
                "error": self.calculate_error(x2, next_guess),
            }

            x1 = x2
            x2 = next_guess

        min_error = min(self.iterations, key=lambda x: self.iterations[x]["error"])
        return self.iterations[min_error]["x3"]

    @staticmethod
    def calculate_error(x1: float, x2: float) -> float:
        return abs((x1 - x2) / x1) * 100

    def get_iterations(self) -> dict:
        return self.iterations


if __name__ == "__main__":
    init_x1 = 1
    init_x2 = 2

    secant = Secant(fun, init_x1, init_x2)
    print(f"From {fun} = 0, init_x1 = {init_x1}, init_x2 = {init_x2} \n")

    x = secant.solve(n_iter=9)

    pprint(secant.get_iterations())
    print(f"\nResult X: {x}")

# Output:
# From x**3 + x**2 - 3*x - 3 = 0, init_x1 = 1, init_x2 = 2
#
# {1: {'f(x1)': -4, 'f(x2)': 3, 'f(x3)': -1.3646, 'x1': 1, 'x2': 2, 'x3': 1.5714},
#  2: {'f(x1)': 3,
#      'f(x2)': -1.3646,
#      'f(x3)': -0.2478,
#      'x1': 2,
#      'x2': 1.5714,
#      'x3': 1.7054},
#  3: {'f(x1)': -1.3646,
#      'f(x2)': -0.2478,
#      'f(x3)': 0.0289,
#      'x1': 1.5714,
#      'x2': 1.7054,
#      'x3': 1.7351},
#  4: {'f(x1)': -0.2478,
#      'f(x2)': 0.0289,
#      'f(x3)': -0.0024,
#      'x1': 1.7054,
#      'x2': 1.7351,
#      'x3': 1.7318},
#  5: {'f(x1)': 0.0289,
#      'f(x2)': -0.0024,
#      'f(x3)': -0.0024,
#      'x1': 1.7351,
#      'x2': 1.7318,
#      'x3': 1.7318}}
#
# Result: 1.7318
