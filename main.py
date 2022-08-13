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

#Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:

#        dish.ingredients = cook_book[dish]
#        for ingredient_name, quantity, measure in dish.ingredients:

#    if course in lecturer.lectures_grades:
#        lecturer.lectures_grades[course] += [grade]
#    else:
#        lecturer.lectures_grades[course] = [grade]


shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)