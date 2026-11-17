products = [("Notebook", 100, 50), ("Pen", 20, 100)]
orders = [(0, 10, 8, 1), (1, 20, 20, 0)]
stock_after = [product[2] for product in products]
rows = []
total_gross = 0
total_discount = 0
net_revenue = 0
discrepancies = 0
returned_total = 0
for product_index, ordered, dispatched, returned in orders:
    name, price, opening_stock = products[product_index]
    subtotal = ordered * price
    discount = subtotal * 0.05 if subtotal >= 500 else 0
    pending = ordered - dispatched
    delivered = dispatched - returned
    stock_after[product_index] = opening_stock - dispatched + returned
    revenue = delivered * price - (discount * delivered / ordered if ordered > 0 else 0)
    if dispatched > ordered or returned > dispatched:
        discrepancies += 1
    returned_total += returned
    total_gross += subtotal
    total_discount += discount
    net_revenue += revenue
    rows.append((name, ordered, dispatched, returned, pending, stock_after[product_index]))
print("Product      Ordered  Dispatched  Returned  Pending  Stock after")
for row in rows:
    print(f"{row[0]:<12} {row[1]:>7} {row[2]:>11} {row[3]:>9} {row[4]:>8} {row[5]:>12}")
print(f"\nGross order value: Rs {total_gross:,.0f}")
print(f"Discounts:         Rs {total_discount:,.0f}")
print(f"Net revenue:       Rs {net_revenue:,.0f}")
print(f"Returned units restocked: {returned_total} | Data discrepancies: {discrepancies}")
