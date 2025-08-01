
import random
# student_score = [56,43,234,45,32,56,76,86,34,122,34,99,34,145,11,45,78] # 234
# # print(max(student_score))


# max_val = 0

# for score in student_score:
#   if(max_val < score):
#     max_val = score

# print('max_val>>', max_val) # 234

# total = 0
# for score in student_score:
#   total += score

# total = sum(student_score)

# print('total>>>', total) # 1230

# Range
# sum = 0
# for num in range(1,16):
#   sum += num
# print('sum>>>', sum) # 120

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','#','$','%','&','(', ')','*','+']

print('Welcome to pass generator')
nr_letters = int(input('How many letters would like in your pass?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

pass_length = nr_letters + nr_numbers + nr_symbols
gen_pass_list = []
# pass_array = ''

pass_letters = ''
for l in range(0,nr_letters):
  gen_pass_list += random.choice(letters)

pass_symbols = ''
for s in range(0,nr_symbols):
  gen_pass_list += random.choice(symbols)

pass_numbers = ''
for n in range(0,nr_numbers):
  gen_pass_list += str(random.choice(numbers))

# flat_pass = [
#   x
#   for xs in gen_pass_list
#   for x in xs
# ]

random.shuffle(gen_pass_list)
# print('gen_pass_list>>', gen_pass_list)

# pass_array = random.sample(flat_pass, len(flat_pass))
# random.shuffle(flat_pass)
# print('You password is:', flat_pass)
# final_pass = ''.join(flat_pass)
# final_pass = ''.join(pass_array)
final_pass = ''
for char in gen_pass_list:
  final_pass += char
print('You password is:', final_pass)






