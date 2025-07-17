chosen_word = 'apple'

display = ['_' for _ in chosen_word]

tmp = ""
for lt in chosen_word:
  tmp += lt
print(' '.join(tmp))

print(' '.join(display))

for i, lt in enumerate(chosen_word):
  print('i>>>', i)
  print('lt>>>', lt)