import cplex

problem = cplex.Cplex()

problem.objective.set_sense(problem.objective.sense.maximize)

name = ["x1", "x2", "x3"]

objetive = [160.0, 320.0, 250.0]

lower_bounds = [0.0, 0.0, 0.0]

upper_bounds = [cplex.infinity, cplex.infinity, cplex.infinity]

v_types = [problem.variables.type.continuous]*3

problem.variables.add(obj = objetive, lb = lower_bounds, ub = upper_bounds, names = name, types = v_types)



constraint_names = ["s1", "s2", "s3"]

first_constraint = [["x1", "x2", "x3"], [1.0, 5.0, 5.0]]

second_constraint = [["x1", "x2", "x3"], [7.0, 3.0, 5.0]]

third_constraint = [["x1", "x2", "x3"], [6.0, 8.0, 2.0]]

constraints = [first_constraint, second_constraint, third_constraint]

rhs = [50.0, 90.0, 60.0]

constraint_sense = ["L", "L", "L"]

problem.linear_constraints.add(lin_expr = constraints, senses = constraint_sense, rhs = rhs, names = constraint_names)



problem.solve()

print(problem.solution.get_values())