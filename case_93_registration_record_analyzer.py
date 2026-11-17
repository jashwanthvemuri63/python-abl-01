routes = [("North", [(12, 40), (5, 20)]),
          ("South", [(10, 55), (4, 30)])]
collected_revenue = 1240
route_totals = []
expected_revenue = 0
for route_name, categories in routes:
    route_total = 0
    for passenger_count, fare in categories:
        route_total += passenger_count * fare
    route_totals.append((route_name, route_total))
    expected_revenue += route_total
for route_name, route_total in route_totals:
    print(f"Route {route_name}: expected revenue  Rs {route_total}")
difference = collected_revenue - expected_revenue
print(f"Total expected:               Rs {expected_revenue:,}")
print(f"Total collected:              Rs {collected_revenue:,}")
print(f"Difference:                   Rs {difference:>5}")
if difference == 0:
    print("Result: RECONCILED")
else:
    direction = "short" if difference < 0 else "surplus"
    print(f"Result: DISCREPANCY (Rs {abs(difference)} {direction})")
