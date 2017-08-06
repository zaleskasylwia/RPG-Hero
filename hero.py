from character import Character
from inventory import Inventory


class Hero:
    def __init__(self, first_name, last_name, race):
        '''
        Zgupiałam. w README powiedziane są, jakie mają miec atrybutu
        i pozniej metody, gdzie metoda init wyglada dla mnie jak dziedziczona po character
        a z drugiej strony piszą, że character - Character object
        inventory - Inventory object

        Oraz w zadnej innej klasie nie mam napisane jak ma wygladac metoda init
        to czy znaczy, ze ma nie byc jej w gl?
        '''
        self.character = Character()
        self.inventory = Inventory()
        self.experience = experience
        self.level = level

    def get_items(self):
        pass

    def pick_an_item(self, item):
        pass

    def drop_item(self, item):
        pass