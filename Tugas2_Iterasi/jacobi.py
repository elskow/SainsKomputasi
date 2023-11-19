import sympy as sym
from pprint import pprint

eq = [
    "10*x1 - x2 + 2*x3 - 6",
    "-x1 + 11*x2 - x3 + 3*x4 - 25",
    "2*x1 - x2 + 10*x3 - x4 + 11",
    "3*x2 - x3 + 8*x4 - 15",
]


class Jacobi:
    def __init__(self, _eq: list) -> None:
        self.eq = [
            sym.sympify(str(sym.solve(sym.sympify(__eq), sym.Symbol(f"x{i + 1}"))[0]))
            for i, __eq in enumerate(_eq)
        ]
        self.x = {0: [0] * len(_eq)}
        self.__log_iter = {
            0: {"iter": 0, "xi": self.x[0], "norm": "-", "norm_inf": "-"}
        }

    def solve(self, n_iter: int) -> list:
        for i in range(n_iter):
            subs_dict = {
                sym.Symbol(f"x{k+1}"): float(self.x[i][k])
                for k in range(len(self.x[i]))
            }
            x_curr = [_eq.subs(subs_dict).evalf() for _eq in self.eq]
            self.x[i + 1] = x_curr
            self.__log_iter[i + 1] = {
                "iter": i + 1,
                "xi": self.x[i + 1],
                "norm": self.norm(self.x[i + 1], self.x[i]),
                "norm_inf": self.norm_inf(self.x[i + 1], self.x[i]),
            }
        return self.x[n_iter]

    @staticmethod
    def norm(x1: list, x2: list) -> float:
        return sum((a - b) ** 2 for a, b in zip(x1, x2)) ** 0.5

    @staticmethod
    def norm_inf(x1: list, x2: list) -> float:
        return max(abs(a - b) for a, b in zip(x1, x2))

    def get_iterations(self) -> dict:
        n_iter = len(self.__log_iter) - 1
        self.__log_iter[n_iter]["norm"] = self.__log_iter[n_iter - 1]["norm"]
        self.__log_iter[n_iter]["norm_inf"] = self.__log_iter[n_iter - 1]["norm_inf"]
        return self.__log_iter


if __name__ == "__main__":
    jacobi = Jacobi(eq)
    pprint(jacobi.solve(n_iter=41))
    pprint(jacobi.get_iterations())
