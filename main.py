# Задание 1
from pprint import pprint


def import_cooked_book_from_file(file_name):
    cookbook = {}
    with open(file_name, encoding='UTF-8') as f:
        while True:
            string = f.readline()[:-1]
            if string == "" or string == "\n":
                break
            dish_name = string
            dish_ingredients = []
            ingredients_count = int(f.readline())
            for _ in range(ingredients_count):
                local_list = f.readline()[:-1].split(" | ")
                dish_ingredients.append({'ingredient_name': local_list[0],
                                         'quantity': int(local_list[1]),
                                         'measure': local_list[2]})
            f.readline()
            cookbook[dish_name] = dish_ingredients
    return cookbook


cook_book = import_cooked_book_from_file('recipes.txt')
pprint(cook_book)


# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_card = {}
    for dish in dishes:
        ingredient = cook_book[dish]
        for ingredient in ingredient:
            if ingredient['ingredient_name'] in shop_card:
                shop_card[ingredient['ingredient_name']]['quantity'] +=\
                    ingredient['quantity'] * person_count
            else:
                shop_card[ingredient['ingredient_name']] = \
                    {'quantity': ingredient['quantity'] * person_count,
                     'measure': 'кг'}
    return shop_card


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
