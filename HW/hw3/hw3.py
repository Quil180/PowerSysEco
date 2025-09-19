import pandas as pd

# all of the bid data
bids_data = [
    {"Company": "Red", "Amount": 100, "Price": 12.5},
    {"Company": "Red", "Amount": 100, "Price": 14.0},
    {"Company": "Red", "Amount": 50, "Price": 18.0},
    {"Company": "Blue", "Amount": 200, "Price": 10.5},
    {"Company": "Blue", "Amount": 200, "Price": 13.0},
    {"Company": "Blue", "Amount": 100, "Price": 15.0},
    {"Company": "Green", "Amount": 50, "Price": 13.5},
    {"Company": "Green", "Amount": 50, "Price": 14.5},
    {"Company": "Green", "Amount": 50, "Price": 15.5},
]


# some helper functions to do the market analysis
def calculate_dispatch(total_demand, market_price, supply_curve):
    production = {"Blue": 0, "Red": 0, "Green": 0}
    demand_remaining = total_demand

    # going through the supply curve from cheapest to most expensive
    for _, bid in supply_curve.iterrows():
        if demand_remaining <= 0:
            break

        # only considering bids at or below the market price ("in the money")
        if bid["Price"] <= market_price:
            amount_to_produce = min(bid["Amount"], demand_remaining)
            production[bid["Company"]] += amount_to_produce
            demand_remaining -= amount_to_produce

    return production


# now im building the supply curve
print("Building the Supply Curve (Merit Order)")

bids_df = pd.DataFrame(bids_data)

# sorting bids by price to create the supply curve (merit order)
supply_curve = bids_df.sort_values(by="Price").reset_index(drop=True)

# this calculates the cumulative (running) total of power available
supply_curve["Cumulative_Amount"] = supply_curve["Amount"].cumsum()
print(supply_curve)
print("\n" + "=" * 50 + "\n")


# now im analyzing the unilateral market with fixed demand
print("Analyzing Fixed Demand Scenarios")
fixed_loads = [400, 600, 875]

for load in fixed_loads:
    # finding the first bid that can satisfy the total demand to set the market price
    market_price_row = supply_curve[supply_curve["Cumulative_Amount"] >= load].iloc[0]
    market_price = market_price_row["Price"]

    production = calculate_dispatch(load, market_price, supply_curve)
    revenue = {co: p * market_price for co, p in production.items()}

    print(f"\nScenario: Demand is fixed at {load} MW")
    print(f"  -> Market Price: ${market_price:.2f}/MWh")
    for company in sorted(production.keys()):
        print(
            f"     - {company}: Produces {production[company]} MWh, Revenue: ${revenue[company]:.2f}"
        )

print("\n" + "=" * 50 + "\n")


# ok NOW we get to the market with a demand curve
print("Analyzing Scenarios with a Demand Curve")
forecast_loads = [400, 600, 875]

for L in forecast_loads:
    # finding the equilibrium where supply equals demand
    for index, bid in supply_curve.iterrows():
        price = bid["Price"]

        # calculating what the demand would be at this price
        demand_at_price = L - 4.0 * price

        # checking if the calculated demand falls within this bid's supply range
        cumulative_supply_before_this_bid = (
            0 if index == 0 else supply_curve.loc[index - 1, "Cumulative_Amount"]
        )

        if (
            cumulative_supply_before_this_bid
            < demand_at_price
            <= bid["Cumulative_Amount"]
        ):
            market_price = price
            total_demand = demand_at_price
            break

    production = calculate_dispatch(total_demand, market_price, supply_curve)
    revenue = {co: p * market_price for co, p in production.items()}

    print(f"\nScenario: Forecast Load (L) is {L} MW")
    print(
        f"  -> Market Equilibrium: Price=${market_price:.2f}/MWh, Demand={total_demand:.2f} MW"
    )
    for company in sorted(production.keys()):
        print(
            f"     - {company}: Produces {production[company]:.2f} MWh, Revenue: ${revenue[company]:.2f}"
        )
