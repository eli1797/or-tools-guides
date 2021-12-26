def printCPSolverStats(solver, status):
    """Prints statistics about the solver and solution"""
    print('\nStatistics')
    print(f'  status      : {solver.StatusName(status)}')
    print(f'  conflicts   : {solver.NumConflicts()}')
    print(f'  branches    : {solver.NumBranches()}')
    print(f'  solving time: {solver.WallTime()} s')
