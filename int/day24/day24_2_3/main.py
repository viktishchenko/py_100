SRC_NAMES = 'D:/pyAngela/day24_2_3/Input/Names/invited_names.txt'
SRC_TEMPLATE = 'D:/pyAngela/day24_2_3/Input/Letters/starting_letter.txt'
SRC_LETTER = 'D:/pyAngela/day24_2_3/Output/ReadyToSend/'

PLACEHOLDER = '[name]'

with open(SRC_NAMES) as n:
  names = n.readlines() # names>>> ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph\n']

with open(SRC_TEMPLATE) as t:
  tmpl = t.read()
  for name in names:
    stripped_name = name.strip() # stripped_name>>> 'Toph'
    new_letter = tmpl.replace(PLACEHOLDER, stripped_name)
    with open(SRC_LETTER + 'letter_for_' + stripped_name, 'w') as l:
      l.write(new_letter)