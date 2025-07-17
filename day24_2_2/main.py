with open('D:/pyAngela/day24_2_2/Input/Names/invited_names.txt', 'r') as n:
  for name in n.readlines():
    with open('D:/pyAngela/day24_2_2/Input/Letters/starting_letter.txt', 'r') as l:
      greet = l.readline().replace('[name]', name.strip())
      message = l.readlines()[1:]
      str = f'{greet}'
      src =f'letter_for_{name.strip()}'
      with open(f'D:/pyAngela/day24_2_2/Output/ReadyToSend/{src}.txt', 'w') as letter:
        separator = ""
        result_string = separator.join(message)
        res = str +'\n'+result_string
        letter.write(res)