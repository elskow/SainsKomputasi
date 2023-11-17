class MathFunc:
    def eq3(a: int, b: int, c: int) -> int:
        X = a * 6 + b * 8 + c * 8
        return X

    def eq4(a: int, b: int, c: int) -> tuple:
        X = 2 * a + 3 * b + 4 * c
        y = a * b * c
        return X, y
