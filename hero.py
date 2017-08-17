from character import Character
from inventory import Inventory


class Hero:
    def __init__(self, first_name, last_name, race):
        if type(first_name) is str nad type(last_name) is str and type(race) is str:
            self.character = Character(first_name, last_name, race)
            self.inventory = Inventory()
            self.experience = experience
            self.level = level

    def get_items(self):
        items = [item for item in self.inventory]
        return items

    def pick_an_item(self, item):
        items = []
        if item not in self.inventory:
            items.append(item)
        return items

    def drop_item(self, item):
        if item in self.inventory:

        pass