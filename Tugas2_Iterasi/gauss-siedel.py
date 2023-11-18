import sympy as sym
from pprint import pprint

eq = [
    "10*x1 - x2 + 2*x3 - 6",
    "-x1 + 11*x2 - x3 + 3*x4 - 25",
    "2*x1 - x2 + 10*x3 - x4 + 11",
    "3*x2 - x3 + 8*x4 - 15",
]


class GaussSiedel:
    def __init__(self, _eq: list) -> None:
        self.eq = []

        for i in range(len(_eq)):
            _eq[i] = sym.sympify(_eq[i])
            _eq[i] = sym.solve(_eq[i], sym.Symbol(f"x{i + 1}"))[0]

        for i in range(len(_eq) + 1):
            globals()[f"x{i + 1}"] = sym.Symbol(f"x{i + 1}")

        for i in range(len(_eq)):
            self.eq.append(sym.sympify(str(_eq[i])))

        self.x = {0: ["0"] * len(_eq)}

        self.__log_iter = {
            0: {
                "iter": 0,
                "xi": self.x[0],
            }
        }

    def solve(self, n_iter: int) -> list:
        for i in range(n_iter):
            x_curr = []
            for j in range(len(self.eq)):
                subs_dict = {
                    sym.Symbol(f"x{k+1}"): float(self.x[i][k])
                    for k in range(len(self.x[i]))
                }

                # For update x1, x2, x3, etc
                if len(x_curr) > 0:
                    subs_dict.update(
                        {
                            sym.Symbol(f"x{k+1}"): float(x_curr[k])
                            for k in range(len(x_curr))
                        }
                    )

                x_curr.append(self.eq[j].subs(subs_dict).evalf())

            self.x[i + 1] = x_curr

            self.__log_iter[i + 1] = {
                "iter": i + 1,
                "xi": self.x[i + 1],
            }
        return self.x[n_iter]

    def get_log(self) -> dict:
        return self.__log_iter


if __name__ == "__main__":
    gauss = GaussSiedel(eq)
    print(f"From {eq} = 0 \n")

    x = gauss.solve(n_iter=5)
    pprint(gauss.get_log())
