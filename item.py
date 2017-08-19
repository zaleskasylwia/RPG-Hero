class Item:
    def __init__(self, name, description, weight):
        if type(name) is str and type(description) is str and type(weight) is int:
            self.name = name
            self.description = description
            self.weight = weight
        else:
            raise TypeError

    def __str__(self):
        return '{} {} {}'.format(self.name, self.description, self.weight)


def main():
    item1 = Item('knife', 'weapon', 2)
    item2 = Item('rose', 'flower', 1)
    print(item1)

if __name__ == '__main__':
    main()
