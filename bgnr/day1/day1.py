# print('Hello World!') # вывод в консоль

# print('Hello World!\nNew Line?') # перенос строки

# print('Hello, ' + 'World' + '!') # Hello, World! конкатенация

# sign = '!'
# name = input('What is your name? ')
# print('Hello', name, sign) # Hello John !

# sign = '!'
# name = input('What is your name? ')
# print('Hello ', name, sign, sep="") # Hello Tomas!

# string = 'halo, string'
# print(len(string)) # длина строки 12 символов, включая пробелы и знаки препинания

# print('Your name consists of',len(input('Enter your name: ')), 'characters', '!') # Your name consists of 6 characters !
# print('Your name consists of',len(input('Enter your name: ')), 'characters' + '!') # Your name consists of 3 characters!
# name = input('Enter your name: ')
# length = len(name)
# print('Your name consists of', length, 'characters' + '!') # Your name consists of 3 characters!

print('Welcom to the Band Name Generator.')
city_name = input('What\'s the name of the city you grew up in? \n')
pet_name = input('What is your pet name? \n')
print('Your Band Name could be: \n', '\"' , city_name + ' ' + pet_name, '\"', sep="")