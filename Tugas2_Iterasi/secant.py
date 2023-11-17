import sympy as sym
from pprint import pprint

fun = "x**3 + x**2 - 3*x - 3"


class Secant:
    def __init__(self, _fun: str, _x0: float, _x1: float) -> None:
        self.fn = _fun
        self.x0 = _x0
        self.x1 = _x1

        self.__f = sym.sympify(self.fn)
        self.__x = sym.Symbol("x")

        self.__log_iter = {}

    def solve(self, n_iter: int, precision: int = 4) -> float:
        x1 = self.x0
        x2 = self.x1

        x_res = 0

        for i in range(n_iter):
            upperbounds = self.__f.subs(self.__x, x2) * (x2 - x1)
            lowerbounds = self.__f.subs(self.__x, x2) - self.__f.subs(self.__x, x1)

            # Set the precision for function result
            upperbounds = round(upperbounds, precision)
            lowerbounds = round(lowerbounds, precision)

            x_res = x2 - (upperbounds / lowerbounds)

            # Make the result decimal number
            # 1/4 -> 0.25
            x_res = float(x_res.evalf())
            x_res = round(x_res, precision)

            self.__log_iter[i + 1] = {
                "x1": x1,
                "x2": x2,
                "x3": x_res,
                "f(x1)": round(self.__f.subs(self.__x, x1), precision),
                "f(x2)": round(self.__f.subs(self.__x, x2), precision),
                "f(x3)": round(self.__f.subs(self.__x, x_res), precision),
            }

            x1 = x2
            x2 = x_res

        return x_res

    def get_log(self) -> dict:
        return self.__log_iter


if __name__ == "__main__":
    init_x1 = 1
    init_x2 = 2

    secant = Secant(fun, init_x1, init_x2)
    print(f"From {fun} = 0, init_x1 = {init_x1}, init_x2 = {init_x2} \n")

    x = secant.solve(n_iter=5, precision=4)
    pprint(secant.get_log())
    print(f"\nResult: {x}")

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
