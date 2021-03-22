import cplex

problem = cplex.Cplex()

problem.objective.set_sense(problem.objective.sense.minimize)

name = ["x1", "x2"]

objetive = [20.0, 40.0]

lower_bounds = [0.0, 0.0]

upper_bounds = [cplex.infinity, cplex.infinity]

v_types = [problem.variables.type.continuous]*2

problem.variables.add(obj = objetive, lb = lower_bounds, ub = upper_bounds, names = name, types = v_types)



constraint_names = ["s1", "s2"]

first_constraint = [["x1", "x2"], [5.0, 2.0]]

second_constraint = [["x1", "x2"], [3.0, 9.0]]

constraints = [first_constraint, second_constraint]

rhs = [100.0, 250.0]

constraint_sense = ["G", "G"]

problem.linear_constraints.add(lin_expr = constraints, senses = constraint_sense, rhs = rhs, names = constraint_names)



problem.solve()

print(problem.solution.get_values())