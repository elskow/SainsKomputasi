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
        self.eq = []

        for i in range(len(_eq)):
            _eq[i] = sym.sympify(_eq[i])
            _eq[i] = sym.solve(_eq[i], sym.Symbol(f"x{i + 1}"))[0]

        for i in range(len(_eq) + 1):
            globals()[f"x{i+1}"] = sym.Symbol(f"x{i+1}")

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
    jacobi = Jacobi(eq)
    pprint(jacobi.solve(5))
    pprint(jacobi.get_log())

# Output:
# [0.988991301652893, 2.01141472577010, -1.01028590392562, 1.02135051007231]
# {0: {'iter': 0, 'xi': ['0', '0', '0', '0']},
#  1: {'iter': 1,
#      'xi': [0.600000000000000,
#             2.27272727272727,
#             -1.10000000000000,
#             1.87500000000000]},
#  2: {'iter': 2,
#      'xi': [1.04727272727273,
#             1.71590909090909,
#             -0.805227272727273,
#             0.885227272727273]},
#  3: {'iter': 3,
#      'xi': [0.932636363636364,
#             2.05330578512397,
#             -1.04934090909091,
#             1.13088068181818]},
#  4: {'iter': 4,
#      'xi': [1.01519876033058,
#             1.95369576446281,
#             -0.968108626033058,
#             0.973842716942149]},
#  5: {'iter': 5,
#      'xi': [0.988991301652893,
#             2.01141472577010,
#             -1.01028590392562,
#             1.02135051007231]}}
