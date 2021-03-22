import cplex

problem = cplex.Cplex()

problem.objective.set_sense(problem.objective.sense.maximize)

name = ["x1", "x2"]

objetive = [5.0, 4.0]

lower_bounds = [0.0, 0.0]

upper_bounds = [cplex.infinity, cplex.infinity]

v_types = [problem.variables.type.continuous]*2

problem.variables.add(obj = objetive, lb = lower_bounds, ub = upper_bounds, names = name, types = v_types)



constraint_names = ["s1", "s2", "s3", "s4"]

first_constraint = [["x1", "x2"], [6.0, 4.0]]

second_constraint = [["x1", "x2"], [1.0, 2.0]]

third_constraint = [["x1", "x2"], [-1.0, 1.0]]

fourth_constraint = [["x1", "x2"], [0.0, 1.0]]

constraints = [first_constraint, second_constraint, third_constraint, fourth_constraint]

rhs = [24.0, 6.0, 1.0, 2.0]

constraint_sense = ["L", "L", "L", "L"]

problem.linear_constraints.add(lin_expr = constraints, senses = constraint_sense, rhs = rhs, names = constraint_names)



problem.solve()

print(problem.solution.get_values())