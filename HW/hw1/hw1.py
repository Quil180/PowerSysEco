import sympy as sp

p, q = sp.symbols('p q')

# Given these...
p_demand = 2000 - 10*q
q_supply = 0.2 * p - 40
q_demand = 200 - 0.1 * p

# Solve for the price and quantity equilibriums
p_eq = sp.solve(sp.Eq(q_supply, q_demand), p)[0]
q_eq = q_supply.subs(p, p_eq)

# Find the Gross Consumers' Surplus, Net Consumers' Surplus, and Revenue, and Producers' Surplus, and Global Surplus...
GCS = sp.integrate(p_demand, (q, 0, q_eq))
NCS = GCS - (p_eq * q_eq)
R = p_eq * q_eq
p_min = sp.solve(sp.Eq(q_supply, 0), p)[0]
PS = 0.5 * q_eq * (p_eq - p_min)
W = NCS + PS

# Printing the output.
print("Equilibrium Price ($/Unit) =", float(p_eq))
print("Equilibrium Quantity (in Units) =", float(q_eq))
print("Consumers' Gross Surplus (Dollars) =", float(GCS))
print("Consumers' Net Surplus (Dollars) =", float(NCS))
print("Producers' Revenue (Dollars) =", float(R))
print("Producers' Profit (Dollars) =", float(PS))
print("Global Welfare (Dollars) =", float(W))
