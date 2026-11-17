products = ["P", "Q"]
quantity = [20, 12]
material_per_unit = [3, 2]
defects = [1, 2]
available_material = 75
quality_limit = 10.0
required_total = 0

for i in range(len(products)):
    required = quantity[i] * material_per_unit[i]
    required_total += required
    defect_rate = defects[i] / quantity[i] * 100
    print(f"Product {products[i]}: material required {required} units | defects {defects[i]}/{quantity[i]} = {defect_rate:.1f}%")
print(f"Total material required: {required_total} units")
print(f"Available material:      {available_material} units")
shortage = required_total - available_material
if shortage > 0:
    print(f"Material shortage:         {shortage} units")
else:
    print(f"Material surplus:          {-shortage} units")
print(f"\nQuality limit: {quality_limit:.1f}%")
for i in range(len(products)):
    rate = defects[i] / quantity[i] * 100
    if rate > quality_limit:
        print(f"Product {products[i]}: QUALITY VIOLATION")
print("Production feasible: " + ("YES" if shortage <= 0 else "NO (material shortage)"))
