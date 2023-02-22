### Home work ###
import pprint

# Creating a cook book
cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        dish = line.strip()
        amount_of_ingridients = int(f.readline())
        ing = []
        for _ in range (amount_of_ingridients):
            ingridient = f.readline().strip()
            ing_name, amount, units = ingridient.split(' | ')
            ingridients = {'ingredient_name' : ing_name,'quantity' : amount,'measure' : units}
            ing.append(ingridients)
        cook_book[dish] = ing
        f.readline()
f.close()
# pprint.pprint(cook_book)


# Task 2 : Нужно написать функцию, которая на 
# вход принимает список блюд из cook_book
#  и количество персон для кого мы будем готовить
def get_shop_list_by_dishes(dishes, person_count):
    needed_ing = {}
    for dish in dishes:
        if dish in cook_book:
            for i in range(len(cook_book[dish])):
                ing_name = cook_book[dish][i]['ingredient_name']
                measure = cook_book[dish][i]['measure']
                quantity = int(cook_book[dish][i]['quantity'])
                if ing_name in needed_ing:
                    needed_ing[ing_name]['quantity'] += quantity
                else:
                    needed_ing[ing_name] = {'measure':measure,'quantity':quantity}
    for ing in needed_ing:
        needed_ing[ing]['quantity'] *= person_count
    pprint.pprint(needed_ing)
    
get_shop_list_by_dishes(['Омлет','Омлет'],2)