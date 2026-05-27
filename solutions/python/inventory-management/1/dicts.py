"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory
        

def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
    


def decrement_items(inventory, items):
    for item in items:
        if item not in inventory:
            continue
        else:
            if inventory[item] == 0:
                continue
            else:
                inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory



def list_inventory(inventory):
    inv = []
    for item in inventory:
        if inventory[item] > 0:
            inv.append((item, inventory[item]))
    return inv