# LIST COMPREHENSION
# ПОНИМАНИЕ СПИСКА
# ——————————————————

# # WITH FOR LOOP
# number = [1,2,3]
# new_list = []
# for n in number:
#   add_1 = n + 1
#   new_list.append(add_1)

# # OR
# ————

# new_list = [n + 1 for n in number]

# new_list = [n +1 for n in [1,2,3]] # new_list>>> [2, 3, 4]
# name = 'Viktor'
# new_list = [letter for letter in name] # new_list>>> ['V','i','k','t','o','r']
# print(f'new_list>>> {new_list}')

# double_num = [num*2 for num in range(1,5)] # double_num>>> [2, 4, 6, 8]

# CONDITIONAL LIST COMPREHENSION
# ПОНИМАНИЕ СПИСКА С УСЛОВИЕМ
# —————————————————————————————
# new_LIST = [new_item for item in list if test]

names = ['Ann','Tom','Dave','Helen','John', 'Rendy']

# check_list = [name == 'Rendy' for name in names] # check_list>>>? [False, False, False, False, False, True]
# check_list = [name == 'Tomas' for name in names] #  check_list>>> [False, False, False, False, False, False]
# check_list = [name for name in names if len(name) < 5] #  check_list>>> ['Ann', 'Tom', 'Dave', 'John']
# up_list = [n.upper() for n in names if len(n) >= 5] # up_list>>> ['HELEN', 'RENDY']
