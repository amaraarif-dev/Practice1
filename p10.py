class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        return sum(
            qty * price for qty, price in self.items.values()
        )

    def __len__(self):
        return len(self.items)


inventory = Inventory()

with open("stock.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        parts = line.strip().split(",")

        if len(parts) != 3:
            print(f"Skipping line {line_number}: invalid format")
            continue

        name, qty_text, price_text = parts

        try:
            qty = int(qty_text)
            price = int(price_text)

            if qty < 0 or price < 0:
                raise ValueError("Numbers cannot be negative")

            inventory.add_item(name, qty, price)

        except ValueError:
            print(f"Skipping {name}: bad number")

print(f"{len(inventory)} items, total value {inventory.total_value()}")

inventory.remove_item("pen")
print(f"{len(inventory)} items, total value {inventory.total_value()}")

try:
    inventory.remove_item("laptop")
except KeyError as error:
    print(f"Error: {error}")