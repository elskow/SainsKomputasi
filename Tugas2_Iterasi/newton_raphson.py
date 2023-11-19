import sympy as sym
from pprint import pprint

fun = "x**3 + x**2 - 3*x - 3"


class NewtonRaphson:
    def __init__(self, _fun: str, _x1: float) -> None:
        self.function = sym.sympify(_fun)
        self.initial_guess = _x1
        self.x = sym.Symbol("x")
        self.derivative = sym.diff(self.function, self.x)
        self.iterations = {}

    def solve(self, n_iter: int) -> float:
        current_guess = self.initial_guess

        for i in range(n_iter):
            function_value = self.function.subs(self.x, current_guess)
            derivative_value = self.derivative.subs(self.x, current_guess)

            try:
                next_guess = current_guess - (function_value / derivative_value)
            except ZeroDivisionError:
                print(
                    "Error: Division by zero. The derivative of the function is zero."
                )
                return

            next_guess = float(next_guess.evalf())

            self.iterations[i + 1] = {
                "iteration": i + 1,
                "current_guess": current_guess,
                "next_guess": next_guess,
                "function_value": function_value,
                "derivative_value": derivative_value,
                "error": self.calculate_error(current_guess, next_guess),
            }

            current_guess = next_guess

        return current_guess

    @staticmethod
    def calculate_error(x1: float, x2: float) -> float:
        return abs((x1 - x2) / x1) * 100

    def get_iterations(self) -> dict:
        return self.iterations


if __name__ == "__main__":
    init_x = 1

    newton = NewtonRaphson(fun, init_x)
    print(f"From {fun} = 0, init_x = {init_x} \n")

    x = newton.solve(n_iter=10)

    pprint(newton.get_iterations())
    print(f"\nRoot: {x}")
