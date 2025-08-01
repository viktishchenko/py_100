# tuple = (1, 2, 'hi')
# print(len(tuple))  ## 3
# print(tuple[2])    ## hi
# # tuple[2] = 'bye'  ## NO, tuples cannot be changed
# # tuple = (1, 2, 'bye')  ## this works

# print(tuple)
  # Echo the contents of a text file
f = open('day7/test.txt', 'rt', encoding='utf-8')
for line in f:   ## iterates over the lines of the file
  print(line, end='')    ## end='' so print does not add an end-of-line char
                          ## since 'line' already includes the end-of-line.
f.close()

# https://developers.google.com/edu/python/regular-expressions?hl=ru
import re

str = 'an example word:pencil!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')