# print('Let\'s check number')
# entered_num = int(input('Enter number: '))

# if(entered_num % 2 == 0) :
#   print('Your number is even')
# else :
#   print('It\'s odd')

# print('Buy tickets app!')
# height = int(input('What is your height in cm? '))
# if (height >= 120):
#   print('Wellcom to our Roll!')
#   bill = 0
#   user_age = int(input('How old are you? '))
#   if(user_age < 12 ):
#     bill +=5
#     print(f'Children ticket price is: ${bill}')
#   elif (12 <= user_age <= 18):
#     bill +=7
#     print(f'Youth ticket price is: ${bill}')
#   elif (45<=user_age<=55):
#     print(f'Youth ticket price is: Free')
#   else:
#     bill +=12
#     print(f'Adult ticket price is: ${bill}')
#   get_photo = input('Do you want take a photo? Type y for Yes, or n for Not: ')
#   if (get_photo == 'y'):
#     bill += 3

#   print(f'Your ticket price is ${bill}')
# else: 
#   print('Sorry, you can\'t entry!')

# print('Python pizza app!')
# size = input('What size do you want? S, M or L: ')
# pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')
# sm = 15
# md = 20
# lg = 25

# if(size == 'S'):
#   if(pepperoni == 'Y'):
#     sm += 2
#   if(extra_cheese == 'Y'):
#     sm += 1
#   print(f'Your final bill: ${sm}')

# elif(size == 'M'):
#   if(pepperoni == 'Y'):
#    md += 3
#   if(extra_cheese == 'Y'):
#    md += 1
#   print(f'Your final bill: ${md}')

# elif(size == 'L'):
#   if(pepperoni == 'Y'):
#    lg += 3
#   if(extra_cheese == 'Y'):
#    lg += 1
#   print(f'Your final bill: ${lg}')

# else :
#   print('You typed the wrong inputs.')

# https://ascii.co.uk/art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print('Welcome to Treasure Island')
first = input('left or right? (l/r)')
if(first == 'r'): 
  print('Game over')
elif(first == 'l'):
  second = input('swim or wait? (s/w) ')
  if(second == 's'):
    print('Game over')
  elif(second == 'w'):
    third = input('Which door? (r/b/y) ')
    if(third != 'y'):
      print('Game over')
    elif(third == 'y'):
      print('You Win!')
else:
  print('Print First Small Letter!')
