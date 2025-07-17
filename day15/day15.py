
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

total_machine_sum = 0
is_check_coins = False
init_machine = [
  {'water': 300},
  {'milk': 200},
  {'coffee': 100},
]

def check_ingredients(choice, ingredients):
  global is_check_coins
  if choice !='espresso':
    if ingredients[0]['water'] >=  MENU[choice]['ingredients']['water']  and ingredients[2]['coffee'] >= MENU[choice]['ingredients']['coffee']  and ingredients[1]['milk'] >= MENU[choice]['ingredients']['milk'] :
        check_money(check_coins(), choice) 
        if is_check_coins:
          ingredients[0]['water'] -= MENU[choice]['ingredients']['water']
          ingredients[1]['milk'] -= MENU[choice]['ingredients']['milk']
          ingredients[2]['coffee'] -= MENU[choice]['ingredients']['coffee']
          is_check_coins = False
    else:
      ing = ''
      if ingredients[0]['water'] <  MENU[choice]['ingredients']['water']:
        ing = 'water'
      elif ingredients[2]['coffee'] < MENU[choice]['ingredients']['coffee']:
        ing = 'coffee'
      else:
        ing = 'milk'
      print(f"\nSorry there is not enough {ing} for {choice}\n")
  else:
    if ingredients[0]['water'] >= MENU[choice]['ingredients']['water']  and ingredients[2]['coffee'] >= MENU[choice]['ingredients']['coffee']:
      check_money(check_coins(), choice)
      if is_check_coins:
        ingredients[0]['water'] -= MENU[choice]['ingredients']['water']
        ingredients[2]['coffee'] -= MENU[choice]['ingredients']['coffee']
        is_check_coins = False
    else:
      ing = ''
      if ingredients[0]['water'] <  MENU[choice]['ingredients']['water']:
        ing = 'water'
      else:
        ing = 'coffee'
      print(f"\nSorry there is not enough {ing} for {choice}\n")


def check_coins():
    print('\nPlease incert coins.')
    quarters = input('How many quarters?: ')
    dimes = input('How many dimes?: ')
    nickles = input('How many nickles?: ')
    pennies = input('How many pennies?: ')
    coins_sum = round(0.25*int(quarters) + 0.10*int(dimes) + 0.05 *int(nickles) + 0.01*int(pennies),2)
    return coins_sum

def check_money(money, goods):
  global total_machine_sum
  global is_check_coins
  if goods == 'espresso':
    if money > MENU['espresso']['cost']:
      is_check_coins = True
      change = round(money - MENU['espresso']['cost'],2)
      total_machine_sum += MENU['espresso']['cost']
      return print(f'Here\'s ${change} in change.')
    elif money == MENU['espresso']['cost']:
      total_machine_sum += MENU['espresso']['cost'] 
      return print(f'Here\'s your {goods}')
    else:
      lack = MENU['espresso']['cost'] - money
      return print(f'You have not enough money: -${lack}')
  
  if goods == 'latte':
    if money > MENU['latte']['cost']:
      is_check_coins = True
      change = round(money - MENU['latte']['cost'],2)
      total_machine_sum += MENU['latte']['cost'] 
      return print(f'Here\'s ${change} in change.')
    elif money == MENU['latte']['cost']:
      total_machine_sum += MENU['latte']['cost']
      return f'Here\'s your {goods}'
    else:
      lack = round(MENU['latte']['cost'] - money, 2)
      return print(f'You have not enough money: -${lack}')
  
  if goods == 'cappuccino':
    if money > MENU['cappuccino']['cost']:
      is_check_coins = True
      change = round(money - MENU['cappuccino']['cost'],2)
      total_machine_sum += MENU['cappuccino']['cost']
      return print(f'Here\'s ${change} in change.')
    elif money == MENU['cappuccino']['cost']:
      total_machine_sum += MENU['cappuccino']['cost']
      return print(f'Here\'s your {goods}.')
    else:
      lack = MENU['cappuccino']['cost'] - money
      return print(f'You have not enough money: -${lack}.')


def count_remains(goods):
  return f'\nwater: { goods[0]['water']}ml\nmilk: {goods[1]['milk']}ml\ncoffee: {goods[2]['coffee']}g\n-----------\nmoney: ${total_machine_sum}\n'


def coffee_machine():
  print('start mashine: off/service/report/espresso/latte/capuchino')

  while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if choice == 'report':
      print(count_remains(init_machine))
      continue

    elif choice == 'service':
      water = int(input('\nEnter the amount of water (ml): '))
      milk = int(input('Enter the amount of milk (ml): '))
      coffee = int(input('Enter the amount of coffee (g): '))
      print('----------------------')

      init_machine[0]['water'] += water
      init_machine[1]['milk'] += milk
      init_machine[2]['coffee'] += coffee

    elif choice == 'off':
      break

    elif choice == 'espresso':
      check_ingredients(choice, init_machine)
      if not is_check_coins == False:
        print(f'Enjoy your {choice}.')

    elif choice == 'latte':
      check_ingredients(choice, init_machine)
      if not is_check_coins == False:
        print(f'Enjoy your {choice}.')

    elif choice == 'cappuccino':
      check_ingredients(choice, init_machine)
      if not is_check_coins == False:
        print(f'Enjoy your {choice}.')

    else:
      print('\nInvalid input!')

coffee_machine()