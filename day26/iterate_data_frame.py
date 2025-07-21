student_dict = {
  'student': ['Ann','Tom','Dave','Helen','John', 'Rendy'],
  'score': [45,34,67,46,78,97]
}


# LOOPTHROUGH DICTIONARY
# ——————————————————————————

# for (key,value) in student_dict.items():
#   print(f'key>>> {key} | value>>> {value}')
# >>> ['Ann', 'Tom', 'Dave', 'Helen', 'John', 'Rendy']
# >>> [45, 34, 67, 46, 78, 97]


# LOOP THROUGH DATA FRAME WITH  PANDAS
# ———————————————————————————————————————

import pandas

p_dict = pandas.DataFrame(student_dict)
    #     student  score
    # 0     Ann     45
    # 1     Tom     34
    # 2    Dave     67
    # 3   Helen     46
    # 4    John     78
    # 5   Rendy     97

# for (key,value) in p_dict.items():
#   print(f'key>>> {key} | value>>> {value}')
    # 0      Ann
    # 1      Tom
    # 2     Dave
    # 3    Helen
    # 4     John
    # 5    Rendy
    # Name: student, dtype: object
    # ————————————————————————————
    # 0    45
    # 1    34
    # 2    67
    # 3    46
    # 4    78
    # 5    97

# LOOP THROUGH ROWS OF DATA FRAME WITH  PANDAS
# ————————————————————————————————————————————

for (idx,row) in p_dict.iterrows():
  # print(row)

  # student    Ann
  # score       45
  # Name: 0, dtype: object
  # student    Tom
  # score       34
  # Name: 1, dtype: object
  # student    Dave
  # score        67
  # Name: 2, dtype: object

  # print(row.student)
  # Ann
  # Tom
  # Dave
  # Helen
  # John
  # Rendy
  
  # print(row.score)
  # 45
  # 34
  # 67
  # 46
  # 78
  # 97
  if row.student == 'Rendy':
    print(row.score) # 97
