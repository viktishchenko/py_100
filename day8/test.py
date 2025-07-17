import re
word = input('Enter word:\n')
print('word>>', word)

if re.search(r'\d', word):
  print('with digits')
if re.search(r'[a-z]', word):
  print('with small letter')
if re.search(r' ', word):
  print('with spaces')
if re.search(r'[A-Z]', word):
  print('with big letters')