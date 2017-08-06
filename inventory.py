class Inventory:
    def __init__(self, capacity, max_weight, items=None):
        self.capacity = capacity
        self.max_weight = max_weight
        self.items = items or []

    def add_item(self, item):
        if item < self.capacity or item < self.max_weight:
            return self.items.append(item)
        else:
            #raise?
            print("It's too heavy")

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("There is no item like this in inventory")
