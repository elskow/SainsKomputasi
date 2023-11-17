import sympy as sym
from pprint import pprint

fun = "x**3 + x**2 - 3*x - 3"


class NewtonRaphson:
    def __init__(self, _fun: str, _x1: float) -> None:
        self.fn = _fun
        self.x1 = _x1

        self.__f = sym.sympify(self.fn)
        self.__x = sym.Symbol("x")

        self.__f1 = sym.diff(self.__f, self.__x)

        self.__log_iter = {}

    def solve(self, n_iter: int, precision: int = 4) -> float:
        x_prev = self.x1

        for i in range(n_iter):
            f_res = self.__f.subs(self.__x, x_prev)
            f1_res = self.__f1.subs(self.__x, x_prev)

            # Set the precision for function result
            f_res = round(f_res, precision)
            f1_res = round(f1_res, precision)

            x_curr = x_prev - (f_res / f1_res)

            # Make the result decimal number
            # 1/4 -> 0.25
            x_curr = float(x_curr.evalf())
            x_curr = round(x_curr, precision)

            self.__log_iter[i + 1] = {
                "iter": i + 1,
                "x": x_prev,
                "xi": x_curr,
                "f(x)": f_res,
                "f'(x)": f1_res,
            }

            x_prev = x_curr

        return x_prev

    def get_log(self) -> dict:
        return self.__log_iter


if __name__ == "__main__":
    init_x = 1

    newton = NewtonRaphson(fun, init_x)
    print(f"From {fun} = 0, init_x = {init_x} \n")

    x = newton.solve(n_iter=10, precision=4)

    pprint(newton.get_log(), indent=4)


# Output:
# From x**3 + x**2 - 3*x - 3 = 0, init_x = 1
#
# {   1: {"f'(x)": 2, 'f(x)': -4, 'iter': 1, 'x': 1, 'xi': 3.0},
#     2: {   "f'(x)": 30.0000000000000,
#            'f(x)': 24.0000000000000,
#            'iter': 2,
#            'x': 3.0,
#            'xi': 2.2},
#     3: {"f'(x)": 15.9200, 'f(x)': 5.8880, 'iter': 3, 'x': 2.2, 'xi': 1.8302},
#     4: {"f'(x)": 10.7093, 'f(x)': 0.9895, 'iter': 4, 'x': 1.8302, 'xi': 1.7378},
#     5: {"f'(x)": 9.5354, 'f(x)': 0.0546, 'iter': 5, 'x': 1.7378, 'xi': 1.7321},
#     6: {"f'(x)": 9.4647, 'f(x)': 0.0005, 'iter': 6, 'x': 1.7321, 'xi': 1.732},
#     7: {"f'(x)": 9.4635, 'f(x)': -0.0005, 'iter': 7, 'x': 1.732, 'xi': 1.7321},
#     8: {"f'(x)": 9.4647, 'f(x)': 0.0005, 'iter': 8, 'x': 1.7321, 'xi': 1.732},
#     9: {"f'(x)": 9.4635, 'f(x)': -0.0005, 'iter': 9, 'x': 1.732, 'xi': 1.7321},
#     10: {"f'(x)": 9.4647, 'f(x)': 0.0005, 'iter': 10, 'x': 1.7321, 'xi': 1.732}}
