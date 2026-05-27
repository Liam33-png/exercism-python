"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    return (dish_name, dish_ingredients)
    
    



def check_drinks(drink_name, drink_ingredients):
    if not ALCOHOLS.isdisjoint(drink_ingredients):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    if dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    if dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    if dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    return f"{dish_name}: OMNIVORE"

def tag_special_ingredients(dish):
    dish_name, dish_ingredients = dish
    dish_ingredients = set(dish_ingredients)
    dish_special_ingredients = dish_ingredients.intersection(SPECIAL_INGREDIENTS)
    return (dish_name, dish_special_ingredients)

def compile_ingredients(dishes):
    master_list = set()
    for dish in dishes:
        master_list = master_list.union(dish)
    return master_list
        


def separate_appetizers(dishes, appetizers):
    non_appetizers = []
    for dish in dishes:
        if dish not in appetizers and dish not in non_appetizers:
            non_appetizers.append(dish)
    return non_appetizers

def singleton_ingredients(dishes, intersection):
    indepdent_ingredients = []
    for dish in dishes:
        indepdent_ingredients.extend(dish.difference(intersection))
    return set(indepdent_ingredients)
