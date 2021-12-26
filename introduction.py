from ortools.sat.python import cp_model
from utils import printCPSolverStats

"""
How to start constraint programming
"""


def MazimizeMath():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    x = model.NewIntVar(0, 10, 'x')
    y = model.NewIntVar(0, 10, 'y')

    # Creates the constraints.
    model.Add(x != y)

    model.Maximize(x + y)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'x = {solver.Value(x)}')
        print(f'y = {solver.Value(y)}')
    else:
        print('No solution found.')

    printCPSolverStats(solver, status)


if __name__ == '__main__':
    MazimizeMath()


