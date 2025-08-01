# ПИШЕМ, ЧИТАЕМ, ДОБАВЛЯЕМ('r', 'w', 'a')

# Открываетм файл, читаем его и закрываем в ручную
# file = open('D:/pyAngela/day24/file_reader/text.txt')
# contents = file.read()
# print(f'contents>>> {contents}')
# file.close()

# Можно не закрывать файл, это будет сделано автоматически
# with open('D:/pyAngela/day24/file_reader/text.txt') as file:
#   contents = file.read()
#   print(f'contents>>> {contents}')

# Пишем
# with open('D:/pyAngela/day24/file_reader/text.txt', 'w' ) as file:
#   contents = file.write('\nHalo, there!')

# Читаем
with open('D:/pyAngela/day1/test_text.txt' ) as file:
  contents = file.read()
  print(f'contents>>> {contents}')
with open('D:/pyAngela/day1/test_text.txt', 'a' ) as file:
  contents = file.write('\nHalo from file-reader!')
  print(f'contents>>> {contents}')
# with open('D:/pyAngela/day24/file_reader/text.txt', 'a' ) as file:
#   contents = file.read()
#   print(f'contents>>> {contents}')

# Создаем новый файл и пишем с модом 'w'
# with open('D:/pyAngela/day24/file_reader/new_file.txt', mode='w') as file:
#   file.write('New text.')

# Пререзаписываем на новую строку с модом: a(append)
# with open('D:/pyAngela/day24/file_reader/text.txt', mode='a' ) as file:
#   contents = file.write('\nHalo, there!')