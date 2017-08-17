class Inventory:
    def __init__(self, capacity, max_weight):
        if type(capacity) is int and type(max_weight) is int:
            self.capacity = capacity
            self.max_weight = max_weight
            self.items = []
        else:
            raise TypeError

    def add_item(self, item):
        #
        if type(item) is str:
            if item < self.capacity or item.weight < self.max_weight:
                return self.items.append(item)
            else:
                #raise?
                print("It's too heavy")
        else:
            raise TypeError

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("There is no item like this in inventory")

    def get_inventory_size(self):
        number of items = sum(self.items)
        number_of_items = 0
        for item in self.items:
            number_of_items += 1
        return number_of_items

    def get_inventory_weight(self):
        weight = 0
        for item in self.items:
            weight += item.weight
        return weight

    def get_the_heaviest_item(self):
        if len(self.items) == 0:
            return IndexError

        heaviest = self.items[0]
        for item in self.items:
            if item.weight > heaviest.weight:
                heaviest = item
        return heaviest
