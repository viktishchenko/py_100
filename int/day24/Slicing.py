piano_key = ['a','b','c','d','e','f','g']
piano_tuple = ('do','re','mi','fa','so','la','ti')

print(piano_key[2:5],'со второго по четвертый: 2,3,4') # ['c', 'd', 'e']
print(piano_key[2:5:2], 'со второго по пятый, каждый второй') # ['c', 'e']
print(piano_key[2:]) # ['c', 'd', 'e', 'f', 'g']
print(piano_key[:5]) # ['a', 'b', 'c', 'd', 'e']
print(piano_key[1:]) # ['b', 'c', 'd', 'e', 'f', 'g']
print(piano_key[::5]) # ['a', 'f'] # каждый пятый, начиная с нулевого
print(piano_key[::3]) # ['a', 'd', 'g'] # каждый третий, начиная с нулевого
print(piano_key[::-1]) # ['g', 'f', 'e', 'd', 'c', 'b', 'a'] # разворот списка

print(piano_tuple[2:5]) # ('mi', 'fa', 'so')
print(piano_tuple[::2]) # ('do','mi','so','ti')