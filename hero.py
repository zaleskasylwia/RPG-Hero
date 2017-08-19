from character import Character
from inventory import Inventory


class Hero:
    def __init__(self, first_name, last_name, race):
        if type(first_name) is str nad type(last_name) is str and type(race) is str:
            self.character = Character(first_name, last_name, race)
            self.inventory = Inventory(10, 100)
            self.experience = 0
            self.level = 0

    def get_items(self):
        items = [item for item in self.inventory.items]
        #return self.inventory.items
        return items

    def pick_an_item(self, item):
        items = []
        if item not in self.inventory:
            items.append(item)
        return items

    def drop_item(self, item):
        self.inventory.drop_item(item)