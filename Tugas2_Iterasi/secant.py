import sympy as sym
from pprint import pprint

fun = "10*x**3 + 5*x**2 + 6*x - 3717"
init_x1, init_x2 = 1, 2
n_iter = 17


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
                "error": self.error(x2, next_guess),
            }

            x1 = x2
            x2 = next_guess

        min_error = min(
            self.iterations, key=lambda x_min: self.iterations[x_min]["error"]
        )
        return self.iterations[min_error]["x3"]

    @staticmethod
    def error(x1: float, x2: float) -> float:
        return abs((x1 - x2) / x1) * 100

    def get_iterations(self) -> dict:
        return self.iterations


if __name__ == "__main__":
    secant = Secant(fun, init_x1, init_x2)
    print(f"From {fun} = 0, init_x1 = {init_x1}, init_x2 = {init_x2} \n")

    x = secant.solve(n_iter=n_iter)

    pprint(secant.get_iterations())
    print(f"\nResult X: {x}")
