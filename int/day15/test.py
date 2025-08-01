# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }


# resources = {
#     'water': 300,
#     'milk': 200,
#     'coffee': 100,
#     'money': 0.0
# }
# # drink = 'espresso'
# missing = []

# def check_resources(drink):
#     """Проверяет достаточно ли ингредиентов для напитка"""
#     missing = []
#     for ingredient, amount in MENU[drink]['ingredients'].items():
#         print(f'ingredient: {ingredient}, amount: {amount}')
#         if resources[ingredient] < amount:
#             missing.append(ingredient)
#             print(f'missing: {missing}')
#     return missing if missing else None

# check_resources('espresso')

# print('resources',resources)
# # print('resources-items',resources.items()[0])

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# # my_dict.items()  # [('a', 1), ('c', 3), ('b', 2)]
# # my_dict.items()[0]  # ('a', 1)

# print(f'my+dict: {my_dict}')
# print(f'my+dict: {my_dict.items()}')
# print(f'my+dict: {list(my_dict.items())[0]}')

# coins = {
#     'quarters': 0.25,
#     'dimes': 0.10,
#     'nickles': 0.05,
#     'pennies': 0.01
# }
# total = 0.0
# for coin, value in coins.items():
#   print(f'coin: {coin}, value: {value}')

# coins = {
#     'quarters': 0.25,
#     'dimes': 0.10,
#     'nickles': 0.05,
#     'pennies': 0.01
# }
# total = 0.0
# for coin, value in coins.items():
#   print( bool(coins.items()))

import sys
print(sys.version)