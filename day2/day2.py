# Subscripting
# print(len('Halo!')) # 5
# print('Halo!'[0]) # H
# print('Halo!'[-1]) # !

# String
# num_str = '123' + '345' # '123345'
# print(type(num_str)) # <class 'str'>

# Integer
# num_int = 123 + 345 # 468
# print(type(num_int)) # <class 'int'>

# Large interges
# print(3456789) # 3456789
# print(3,456,789) # 3 456 789
# print(3_456_789) # 3456789

# Float
# pi_num = 3,14159
# print(pi_num) # (3, 14159)
# print(type(pi_num)) # <class 'tuple'>
# pi_num_1 = 3.14159
# print(pi_num_1) # 3.14159
# print(type(pi_num_1)) # <class 'float'> 

# pi_num = 3,14159
# print(pi_num) # (3, 14159)
# print(len(pi_num)) # 2

# Boolean
# print(True) # True
# print(type(True)) # <class 'bool'>
# print(False) # False
# print(type(False)) # False

# print(len('12345')) # 5
# print(len(str(123))) # 3

# Data Types
# print(type('abc')) # <class 'str'>
# print(type(123)) # <class 'int'> 
# print(type(12.3)) # <class 'float'> 
# print(type(True)) # <class 'bool'> 

# Convert data types
# print (int('123')) # 123
# print(type(int('123')) ) # <class 'int'>

# print(float('123')) # 123.0
# print(type(float('123')) ) # <class 'float'>

# print(str(123)) # 123
# print(type(str(123)) ) # <class 'str'>

# print(bool('123')) # True
# print(bool(-123)) # True
# print(bool(0)) # False
# print(type(bool('123')) ) # <class 'bool'>

# name_of_the_user = input('Enter your name: ')
# print(type(name_of_the_user)) # <class 'str'> 
# print(type(len(name_of_the_user))) # <class 'int'>
# length_of_the_name = len(name_of_the_user)
# print('Number of letters in your name: ' + str(len(input('Enter your name: ')))) # Number of letters in your name: 3
# OR
# print('Number of letters in your name: ' + str(length_of_the_name)) # Number of letters in your name: 5

# print('My age: ' + str(12) ) # My age: 12
# print(123 + 456) # 579
# print(7 - 3)
# print(3 * 2)
# print(6 / 2) # 3.0 <class 'float>
# print(6 // 2) # 3 <class 'int'>
# print(5 // 2) # 2 <class 'int'>
# print(6 ** 2) # 36

# PENDAS + LR (left to right) Parentheses, Exponents, Multipication/Division, Addition/Substraction

# ()
# **
# * OR /
# + OR -

# print(3 * 3 + 3 / 3 - 3) # 7.0
# print(3 * (3 + 3) / 3 - 3) # 3.0 LEFT to RIGHT

# bmi = 84 / 1.65 ** 2
# print(bmi) # 30.85399449035813

# print(int(bmi)) # 30

# print(round(bmi)) # 31
# print(round(3.5)) # 4
# print(round(3.4)) # 3
# print(round(bmi, 2)) # 30.85

# score = 2

# print(score) # 2

# score += 1
# print(score) # 3
# score -= 1
# print(score) # 2
# score *= 2
# print(score) # 4
# score /= 3 
# print(score) # 1.3333333

# f-strings

# score = 0
# height = 1.8
# is_winning = True
# print(f'That\'s your score: {score}, and your hieght is: {height} so, your are win, it\'s {is_winning}') # That's your score: 0, and your hieght is: 1.8 so, your are win, it's True


# Tip project
print('Welcom to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip_value = int(input('How much tip would you like to give? 10, 12, or 15? '))
person_quantity = int(input('How many people to split the bill? '))
print(f'Each person should pay: ${round((total_bill + total_bill * tip_value / 100) / person_quantity, 2)}')