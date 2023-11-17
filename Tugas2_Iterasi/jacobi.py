import sympy as sym
from pprint import pprint
import numpy as np

eq = [
    "10*x1 - x2 + 2*x3 = 6",
    "-x1 + 11x2 - x3 + 3*x4 = 25",
    "2*x1 - x2 + 10*x3 - x4 = -11",
    "3*x1 - x3 + 8*x4 = 15",
]


def clean_eq(eq: str) -> str:
    return eq.replace("+", "").replace("*", "").replace("/", "").replace(" ", "")


class Jacobi:
    def __init__(self, _eq: list) -> None:
        self.eq = _eq
        self.__var = []

        # Get the constanta. This method is not good enough
        # This method only works if the constanta is on the right side of the equation
        # All code are hardcoded

        for i in range(len(self.eq)):
            res_const = self.eq[i].split("=")[1]

            var_const = clean_eq(self.eq[i].split("=")[0])

            if 0 < i < len(self.eq) - 1:
                var_const = var_const.split(f"x{i + 1}")[0].split(f"x{i}")[1]
            elif i == len(self.eq) - 1:
                var_const = var_const.split(f"x{i}")[1].split(f"x{i + 1}")[0]
            else:
                var_const = var_const.split(f"x{i + 1}")[0]

            try:
                globals()[f"x{i + 1}"] = eval(res_const) / eval(var_const)
            except ZeroDivisionError:
                globals()[f"x{i + 1}"] = eval("0")
            except SyntaxError:
                globals()[f"x{i + 1}"] = eval(res_const)

            self.__var.append(globals()[f"x{i + 1}"])

        self.__log_iter = {
            0: {
                "iter": 0,
            }
        }

        for i in range(len(self.eq)):
            self.__log_iter[0][f"x{i + 1}"] = 0

    def solve(self, n_iter: int = 3) -> dict:
        self.__log_iter[1] = {
            "iter": 1,
        }

        for i in range(len(self.eq)):
            self.__log_iter[1][f"x{i + 1}"] = self.__var[i]

        for i in range(1, n_iter):
            self.__log_iter[i + 1] = {
                "iter": i + 1,
            }

            for j in range(len(self.eq)):
                for k in range(len(self.eq)):
                    if k != j:
                        self.eq[j] = self.eq[j].replace(f"x{k + 1}", str(self.__var[k]))

            for j in range(len(self.eq)):
                res_const = self.eq[j].split("=")[1]
                var_const = clean_eq(self.eq[j].split("=")[0])
                try:
                    if 0 < j < len(self.eq) - 1:
                        var_const = var_const.split(f"x{j + 1}")[0].split(f"x{j}")[1]
                    elif j == len(self.eq) - 1:
                        var_const = var_const.split(f"x{j}")[1].split(f"x{j + 1}")[0]
                    else:
                        var_const = var_const.split(f"x{j + 1}")[0]

                except IndexError:
                    var_const = var_const.split(f"x{j + 1}")[0]

                self.__var[j] = eval(res_const) / eval(var_const)

                self.__log_iter[i + 1][f"x{j + 1}"] = self.__var[j]

        return self.__var

    def get_log(self) -> dict:
        return self.__log_iter


if __name__ == "__main__":
    jacobi = Jacobi(eq)
    res = jacobi.solve(n_iter=3)

    pprint(jacobi.get_log())
