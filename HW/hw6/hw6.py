import sympy

# defining the symbols of price (a, b, and c) and lambda for marginal cost
P_A, P_B, P_C, lamb = sympy.symbols("P_A P_B P_C lamb")
total_load = 350 # the total load allowed by the system before excess must be sold

# defining marginal cost (MC) functions for use later
# using the derivatives of the cost functions given in the homework for ease of use
MC_A = 1.4 + 0.08 * P_A
MC_B = 1.6 + 0.10 * P_B
MC_C = 1.8 + 0.04 * P_C

# for economic dispatch, all marginal costs are equal to the system lambda that will be found later
# we also have the power balance equation where total generation equals total load for finding any excess power!
eq1 = sympy.Eq(MC_A, lamb)
eq2 = sympy.Eq(MC_B, lamb)
eq3 = sympy.Eq(MC_C, lamb)
eq4 = sympy.Eq(P_A + P_B + P_C, total_load)

# sympy can solve this system of 4 equations with 4 unknowns for us so that what I'm doing here.
solution = sympy.solve([eq1, eq2, eq3, eq4], (P_A, P_B, P_C, lamb))

# extracting the results from the solution dictionary, yah know standard stuff
p_a_val = solution[P_A]
p_b_val = solution[P_B]
p_c_val = solution[P_C]
lambda_val = solution[lamb]

# calculating the total cost now since we need to calculate that incase we want profit
cost_A = 15 + 1.4 * p_a_val + 0.04 * p_a_val**2
cost_B = 25 + 1.6 * p_b_val + 0.05 * p_b_val**2
cost_C = 20 + 1.8 * p_c_val + 0.02 * p_c_val**2
total_cost = cost_A + cost_B + cost_C

# now we print the results!!!!!!!!!!!!!
print("4.6, Economic Dispatch Verification")
print(f"System Load: {total_load} MW\n")
print(f"Solved System Lambda: ${lambda_val:.3f}/MWh\n")
print("Optimal Dispatch:")
print(f"Unit A (P_A): {p_a_val:.1f} MW")
print(f"Unit B (P_B): {p_b_val:.1f} MW")
print(f"Unit C (P_C): {p_c_val:.1f} MW\n")
print(f"Total Hourly Cost: ${total_cost:.2f}/h")
