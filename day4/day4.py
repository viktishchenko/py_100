import random
# import test_module

# random_integer = random.randint(1,10)
# print('random integer >>>', random_integer)

# print('it\'s from module >>>',test_module.test_num_from_module)

# random from 0 to 1 (not include)
# random_from_0_to_1 = random.random()*10
# print('random_from_0_to_1>>>', random_from_0_to_1)

# random from 0 to 1 (include)
# random_float = random.uniform(1,10)
# print('random_float>>>', random_float)

# friends = ['Alice', 'Bob', 'Charlie','David', 'Emanuel']
# print(friends[random.randint(0,len(friends)-1)])
# # OR
# print(random.choice(friends))

# derty_dozen = [
# 'Strawberries',
# 'Spinach',
# 'Kale',
# 'Nectarines',
# 'Apples',
# 'Grapes',
# 'Peaches',
# 'Cherries',
# 'Pears',
# 'Tomatoes' ,
# 'Celery',
# 'Potatoes']

# fruits = ['Strawberries', 'Nectarines', 'Apples','Grapes', 'Peaches','Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']


# derty_dozen = [fruits, vegetables]
# print(derty_dozen)
# print(len(derty_dozen))

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print('Wellcome to the Rock, Scissors, Paper game!')
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
data_list = [rock, paper, scissors]
random_chose = random.randint(0,2)
chose = ''
if(random_chose == 0):
  chose = 'Rock'
elif(random_chose == 1):
  chose = 'Peper'
else:
  chose = 'Scissors'

if(user_choice == 0):
  print('You chose Rock:', data_list[0])

  computer_chose = data_list[random_chose]

  print(f'Computer chose {chose} : {computer_chose}')

  if(computer_chose == data_list[0]):
    print('One more time!')
  elif(computer_chose == data_list[1]):
    print('You lose!')
  else:
    print('You win!')

elif(user_choice == 1):
  print('You chose Peper:', data_list[1])

  computer_chose = data_list[random_chose]
  print(f'Computer chose {chose} : {computer_chose}')

  if(computer_chose == data_list[0]):
    print('You win!')
  elif(computer_chose == data_list[1]):
    print('One more time!')
  else:
    print('You lose!')

elif(user_choice == 2):
  print('You chose Scissors:', data_list[2])

  computer_chose = data_list[random_chose]
  print(f'Computer chose {chose} : {computer_chose}')

  if(computer_chose == data_list[0]):
    print('You lose!')
  elif(computer_chose == data_list[1]):
    print('You win!')
  else:
    print('One more time!')
else :
  print('You type something special!')


