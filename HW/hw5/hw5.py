import sympy as sp
import pandas as pd

# Defining P as a symbolic variable for power output in MW
P = sp.symbols("P")

# Given values from the problem
gas_cost = 1.20  # $/MJ
min_power = 200  # MW
max_power = 500  # MW

# Market prices for each period
market_data = {
    "Period": [1, 2, 3, 4, 5, 6],
    "Price ($/MWh)": [12.50, 10.00, 13.00, 13.50, 15.00, 11.00],
}
df = pd.DataFrame(market_data)

# Input-output curve H(P)
H_P = 120 + 9.3 * P + 0.0025 * P**2

# Total Cost function C(P) = H(P) * Gas Cost
C_P = H_P * gas_cost

# Marginal Cost function MC(P) is the derivative of the Total Cost function
MC_P = sp.diff(C_P, P)

# This converts the symbolic sympy expressions into numeric python functions
cost_func = sp.lambdify(P, C_P, "numpy")
marginal_cost_func = sp.lambdify(P, MC_P, "numpy")

print(f"Total Cost Function C(P) = {C_P}")
print(f"Marginal Cost Function MC(P) = {MC_P}")
print("-" * 50)


results = []
for index, row in df.iterrows():
    price = row["Price ($/MWh)"]

    # Profit is maximized where Market Price = Marginal Cost
    # We solve for P: price = 11.16 + 0.006*P
    # P = (price - 11.16) / 0.006

    # Calculate the unconstrained optimal power output
    optimal_P_eq = sp.Eq(MC_P, price)
    unconstrained_P = sp.solve(optimal_P_eq, P)[0]

    # Apply the operational constraints (200 MW to 500 MW)
    if unconstrained_P < min_power:
        optimal_P = min_power
    elif unconstrained_P > max_power:
        optimal_P = max_power
    else:
        optimal_P = unconstrained_P

    # Calculate financial results for the period
    revenue = price * optimal_P
    cost = cost_func(optimal_P)
    profit = revenue - cost

    results.append(
        {
            "Output P (MW)": optimal_P,
            "Revenue ($)": revenue,
            "Cost ($)": cost,
            "Profit ($)": profit,
        }
    )

# Combine original data with the calculated results
results_df = pd.DataFrame(results)
final_df = pd.concat([df, results_df], axis=1)

# Set pandas display options to show all columns and format floats
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.float_format", "{:,.2f}".format)

# Print start of table and rest of table or something
print("Profit/Loss Calculation per Period:")
print(final_df.to_string(index=False))
print("-" * 50)

# Calculate and print the total profit for the 6-hour period
total_profit = final_df["Profit ($)"].sum()
print(f"Total Profit for the 6-hour period: ${total_profit:,.2f}")
