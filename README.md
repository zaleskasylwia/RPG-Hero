# 5 - RPG Hero

Let's make a part of an RPG game responsible for storing information about our hero

# Classes:

## Character

represents basic information about our hero

### Attributes:

first_name

last_name

race

### Methods:

__str__()

## Item

represents an item that a hero can put into inventory

### Attributes:

name

description

weight

## Inventory

represents hero's inventory

### Attributes:

capacity - max number of items that can be stored in the inventory

max_weight - max weight that can be stored in the inventory

items - list of items

### Methods:

add_item(item) - adds item to the inventory, but first checks if it's possible (capacity or max_weight are not reached)

drop_item(item) - removes item from the inventory

get_inventory_size() - returns number of items in the inventory

get_inventory_weight() - returns total weight of all items in the inventory

get_the_heaviest_item() - return the heaviest item in the inventory

## Hero

represents our hero

### Attributes:

character - Character object

inventory - Inventory object

experience

level

### Methods:

__init__(firs_name, last_name, race) - creates an hero instance

get_items() - returns list of items in hero's inventory

pick_an_item(item) - adds item to the inventory

drop_item(item) - removes item from the inventory
