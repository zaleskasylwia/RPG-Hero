class Inventory:
    def __init__(self, capacity, max_weight, items=None):
        self.capacity = capacity
        self.max_weight = max_weight
        self.items = items or []


