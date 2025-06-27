import json
import os

class ItemManager:
    def __init__(self, filename='items.json'):
        self.filename = filename
        self.items = self.load_items()

    def load_items(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    if len(data) != 6 or any(len(row) != 10 for row in data):
                        raise ValueError("Item matrix must be 6x10.")
                    for row in data:
                        for item in row:
                            if "stock" not in item:
                                item["stock"] = 0
                    return data
            except Exception as e:
                print(f"[ERROR] Couldn't load items, using default. Reason: {e}")

        # اگر فایل وجود نداشت یا خراب بود
        default_items = [[{"name": "Empty", "price": 0, "stock": 0} for _ in range(10)] for _ in range(6)]
        self.save_items(default_items)
        return default_items

    def get_item(self, row, col):
        try:
            return self.items[row][col]
        except IndexError:
            return {"name": "Invalid", "price": 0, "stock": 0}

    def get_stock(self, row, col):
        item = self.get_item(row, col)
        return item.get("stock", 0)

    def decrement_stock(self, row, col):
        self.items[row][col]["stock"] -= 1
        self.save_items(self.items)

    def save_items(self, data=None):
        if data is None:
            data = self.items
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def print_item(self):
        for r, row in enumerate(self.items):
            for c, item in enumerate(row):
                print(f"({r},{c}) {item['name']} - {item['price']} IRR - Stock: {item['stock']}")

if __name__ == "__main__":
    manager = ItemManager()
    manager.print_item()