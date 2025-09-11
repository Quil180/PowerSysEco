import sympy as sp
import pandas as pd
import numpy as np

# defining symbolic variables for the equations
q_sym, pi_sym = sp.symbols("q pi")

# defining the list of demand values
q_values = [0, 50, 100, 150, 200]

# Demand curve 1, q = 200 - pi
print("Verifying Demand Curve 1: q = 200 - pi")

# defining the demand equation
demand_eq1 = sp.Eq(q_sym, 200 - pi_sym)

# solving for pi to get the inverse demand function
pi_expr1 = sp.solve(demand_eq1, pi_sym)[0]

# now we differentiate q with respect to pi to find dq/dpi
dq_dpi1 = sp.diff(200 - pi_sym, pi_sym)

# creating the elasticity formula
epsilon_expr1 = (dq_dpi1) * (pi_sym / q_sym)

# calculating the results for each q value
results1 = []
for q_val in q_values:
    if q_val == 0:
        pi_val = 200
        # if elasticity is undefined (approaches -infinity)
        epsilon_val = -np.inf
    else:
        # substitute q to find pi
        pi_val = pi_expr1.subs(q_sym, q_val)
        # substitute pi and q to find elasticity
        epsilon_val = epsilon_expr1.subs([(pi_sym, pi_val), (q_sym, q_val)])

    results1.append(
        {
            "Demand (q)": q_val,
            "Price (pi)": pi_val,
            "Elasticity (epsilon)": float(epsilon_val),
        }
    )

# display these results in a table
df1 = pd.DataFrame(results1)
print(df1.to_string(index=False))
print("\n" + "=" * 50 + "\n")


# Demand Curve 2: q = 10000 / pi
print("Verifying Demand Curve 2: q = 10000 / pi")

# defining the demand equation
demand_eq2 = sp.Eq(q_sym, 10000 / pi_sym)

# solving for pi
pi_expr2 = sp.solve(demand_eq2, pi_sym)[0]

# differentiating q with respect to pi
dq_dpi2 = sp.diff(10000 / pi_sym, pi_sym)

# create the elasticity formula
epsilon_expr2 = (dq_dpi2) * (pi_sym / q_sym)
# sympy can simplify this for me
epsilon_simplified2 = sp.simplify(epsilon_expr2)

results2 = []
for q_val in q_values:
    if q_val == 0:
        pi_val = np.inf
        # if elasticity is constant at -1, even at the limit
        epsilon_val = -1
    else:
        pi_val = pi_expr2.subs(q_sym, q_val)
        # the elasticity is always -1, but im going to calculate it for consistency
        epsilon_val = epsilon_expr2.subs([(pi_sym, pi_val), (q_sym, q_val)])

    results2.append(
        {
            "Demand (q)": q_val,
            "Price (pi)": float(pi_val),
            "Elasticity (epsilon)": int(epsilon_val),
        }
    )

# display these results in a table
df2 = pd.DataFrame(results2)
print(df2.to_string(index=False))
