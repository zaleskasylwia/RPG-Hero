from item import Item


class Inventory:
    def __init__(self, capacity=10, max_weight=50):
        if type(capacity) is int and type(max_weight) is int:
            self.capacity = capacity
            self.max_weight = max_weight
            self.items = []
        else:
            raise TypeError

    def add_item(self, item):
        if isinstance(item, Item):
            if self.get_inventory_size() < self.capacity and self.get_inventory_weight() + item.weight < self.max_weight:
                self.items.append(item)
            else:
                print('too heavy')
        else:
            print("It's not and item")

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
    item1 = Item('knife', 'weapon', 92)
    i = Inventory(30, 80)
    print(i)
    print(i.get_inventory_size())
    print(i.get_inventory_weight())

    print(item1)
    print()
    i.add_item(item1)
    print(i)
    print(i.get_inventory_size())
    print(i.get_inventory_weight())


if __name__ == '__main__':
    main()
