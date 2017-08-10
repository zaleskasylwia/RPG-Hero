class Item:
    def __init__(self, name, description, weight):
        if type(name) is str nad type(description) is str and type(weight) is int:
            self.name = name
            self.description = description
            self.weight = weight
