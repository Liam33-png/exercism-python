"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
            current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart
def read_notes(notes):
    return dict.fromkeys(notes, 1)
def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    return sorted(cart.items())

def send_to_store(cart, aisle_mapping):
    fufillment_cart = {}
    for item in cart:
        fufillment_cart[item] = [cart[item]]
        fufillment_cart[item].extend(aisle_mapping[item])
    return sorted(fufillment_cart.items(),reverse=True)

def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        store_inventory[item] = [store_inventory[item][0] - fulfillment_cart[item][0]]
        if store_inventory[item][0] <= 0:
            store_inventory[item] = ["Out of Stock"]
        store_inventory[item].extend(fulfillment_cart[item][1:])
    return store_inventory
