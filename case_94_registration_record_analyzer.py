supply_names = ["Rice", "Water", "Kits"]
stock = [100, 60, 30]
areas = ["Area A", "Area B"]
demand = [[70, 40, 20], [50, 30, 10]]
allocations = [[0, 0, 0], [0, 0, 0]]
for area_index in range(len(areas)):
    for supply_index in range(len(supply_names)):
        amount = min(stock[supply_index], demand[area_index][supply_index])
        allocations[area_index][supply_index] = amount
        stock[supply_index] -= amount
        demand[area_index][supply_index] -= amount

for i in range(len(areas)):
    print(f"Priority {i + 1} - {areas[i]}")
    parts = []
    for j in range(len(supply_names)):
        served = allocations[i][j]
        original = served + demand[i][j]
        parts.append(f"{supply_names[j]} {served}/{original}")
    print("  " + "   ".join(parts))
unmet = []
for j in range(len(supply_names)):
    total_unmet = demand[0][j] + demand[1][j]
    if total_unmet > 0:
        unmet.append(f"{supply_names[j]} {total_unmet}")
if unmet:
    print("\nUnmet demand: Area B - " + ", ".join(unmet))
else:
    print("\nUnmet demand: none")
print("Remaining stock: " + ", ".join(f"{supply_names[i]} {stock[i]}" for i in range(len(stock))))
