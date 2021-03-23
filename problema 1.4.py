# Marco Antonio Vázquez Rivera
# Judith Alejandra Candelaria Sánchez

import cplex

problem = cplex.Cplex()

problem.objective.set_sense(problem.objective.sense.minimize)

name = ["x1", "x2", "x3", "x4", "x5"]

objetive = [2.0, 3.0, 5.0, 2.0, 3.0]

lower_bounds = [0.0]*5

upper_bounds = [cplex.infinity]*5

v_types = [problem.variables.type.continuous]*5

problem.variables.add(obj = objetive, lb = lower_bounds, ub = upper_bounds, names = name, types = v_types)



constraint_names = ["s1", "s2"]

first_constraint = [["x1", "x2", "x3", "x4", "x5"], [1.0, 1.0, 2.0, 1.0, 3.0]]

second_constraint = [["x1", "x2", "x3", "x4", "x5"], [2.0, -1.0, 3.0, 1.0, 1.0]]

constraints = [first_constraint, second_constraint]

rhs = [4.0, 3.0]

constraint_sense = ["G", "G"]

problem.linear_constraints.add(lin_expr = constraints, senses = constraint_sense, rhs = rhs, names = constraint_names)



problem.solve()

print(problem.solution.get_values())