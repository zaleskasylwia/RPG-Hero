from item import Item


class Inventory:
    def __init__(self, capacity, max_weight):
        if type(capacity) is int and type(max_weight) is int:
            self.capacity = capacity
            self.max_weight = max_weight
            self.items = []
        else:
            raise TypeError

    def count_item(self):
        count_items = 0
        for item in self.items:
            count_items += 1
        return count_items

    def check_capacity_space(self, count_items):
        if count_items < self.capacity:
            return True
        return False

    def add_item(self, item):
        if isinstance(item, Item):
            count_items = count_item()
            if check_capacity_space(count_item):
                item_weight = calculate_item_weight()
                if check_space_for_item(item_weight):
                    space_for_item = self.max_weight - item_weight
                    if item.weight <= space_for_item:
                        self.items.append(item)
        else:
            print("You can't add an item")

    def calculate_item_weight(self):
        item_weight = 0
        for item in self.items:
            item_weight += item.weight
        return item_weight

    def check_space_for_item(self, item_weight):
        if item_weight < self.max_weight:
            return True
        return False

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("There is no item like this in inventory")

    def get_inventory_size(self):
        return len(self.items)

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

    def __str__(self):
        return '{} capacity, {} max weight, {} list of items'.format(self.capacity, self.max_weight, self.items)


def main():
    item1 = Item('knife', 'weapon', 2)
    i = Inventory(30, 80)
    print(i)
    print(i.get_inventory_size())

    print(item1)
    #i.add_item(item1)

if __name__ == '__main__':
    main()
