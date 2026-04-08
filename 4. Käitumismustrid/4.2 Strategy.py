import cmath

class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b*b - 4*a*c

class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        rds = b*b - 4*a*c
        if rds < 0:
            return float('nan')
        else:
            return rds

class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)
        root_d = cmath.sqrt(d)
        sol1 = (-b + root_d) / (2 * a)
        sol2 = (-b - root_d) / (2 * a)

        return sol1, sol2

if __name__ == '__main__':
    solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    print(solver.solve(1, 10, 16))
    solver = QuadraticEquationSolver(RealDiscriminantStrategy())
    print(solver.solve(1, 4, 5))
    solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    print(solver.solve(1, 4, 5))
    solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    print(solver.solve(1, -5, 6))