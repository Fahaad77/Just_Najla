"""Generate a reproducible synthetic inventory analysis portfolio sample."""
import csv
import random
from pathlib import Path

random.seed(356)
categories = ["Safety", "Electrical", "Mechanical", "Office"]
warehouses = ["North", "Central", "South"]
out = Path(__file__).parent / "data" / "inventory_sample.csv"
out.parent.mkdir(exist_ok=True)

with out.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["item_id", "category", "warehouse", "stock", "reorder_point", "unit_cost_sar", "count_variance"])
    for n in range(1, 121):
        category = categories[(n - 1) % len(categories)]
        warehouse = warehouses[(n - 1) % len(warehouses)]
        reorder = random.randint(12, 36)
        stock = max(0, reorder + random.randint(-22, 55))
        cost = random.randint(18, 490)
        variance = random.choices([-3, -2, -1, 0, 1, 2, 3], [2, 3, 8, 68, 11, 5, 3])[0]
        writer.writerow([f"INV-{n:04d}", category, warehouse, stock, reorder, cost, variance])

print(out)