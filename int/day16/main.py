from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

# menu.get_items() # latte/espresso/cappuccino/

# menu.find_drink('latte') #     "latte": "ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,}

coffee_maker = CoffeeMaker()

# coffee_maker.report() }')   # Water: 300ml\nMilk: 200ml\nCoffee: 100g
# coffee_maker.is_resource_sufficient(menu.find_drink('latte')) # True

# coffee_maker.make_coffee(menu.find_drink('latte')) # Here is your latte ☕️. Enjoy!

money_machine = MoneyMachine()
# money_machine.report()}') Money: $0
# money_machine.make_payment(2.75) Please insert coins.\nHow many quarters?: 12\nHow many dimes?: 12\nHow many nickles?: 12\nHow many pennies?: 12\nHere is $2.17 in change.

while True:
  choice = input(f'What would you like? {menu.get_items()}: ')

  if choice == 'off':
    break
  elif choice == 'report': 
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)







