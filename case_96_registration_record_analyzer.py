books = ["Algorithms", "Python"]
branches = ["Central", "East", "West"]
stock = [20, 15]
demand = [[12, 10], [10, 9], [5, 4]]
allocated = [[0, 0], [0, 0], [0, 0]]
for book_index in range(len(books)):
    for branch_index in range(len(branches)):
        copies = min(stock[book_index], demand[branch_index][book_index])
        allocated[branch_index][book_index] = copies
        stock[book_index] -= copies

print("Branch priority: Central > East > West\n")
for i in range(len(branches)):
    print(f"{branches[i]:<8} " + " | ".join(
        f"{books[j]} {allocated[i][j]}/{demand[i][j]}" for j in range(len(books))))
unmet = []
for j in range(len(books)):
    total = 0
    for i in range(len(branches)):
        total += demand[i][j] - allocated[i][j]
    unmet.append(total)
print(f"\nUnmet demand: Algorithms {unmet[0]} copies, Python {unmet[1]} copies")
print("All available copies allocated." if stock == [0, 0] else f"Remaining stock: {stock}")
