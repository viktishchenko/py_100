# DICTIONARY COMPREHENSION (create dict use short syntax)
# —————————————————————————————————————————————————————————
# new_dict = {new_key:new_value for (key:value) in dict.items()}
# new_dict = {new_key:new_value for (key:value) in dict.items() if test}

names = ['Ann','Tom','Dave','Helen','John', 'Rendy']

# students_score = {new_key:new_value for name in names}
import random
students_score = {student:random.randint(1,100) for student in names} # {'Ann': 94, 'Tom': 23, 'Dave': 16, 'Helen': 73, 'John': 28, 'Rendy': 64}
print(f'{students_score.keys() }') #dict_keys(['Ann', 'Tom', 'Dave', 'Helen', 'John', 'Rendy'])
print(f'{students_score.values() }') #dict_values([32, 79, 40, 58, 36, 28])
print(f'{students_score.items() }') #dict_items([('Ann', 32), ('Tom', 79), ('Dave', 40), ('Helen', 58), ('John', 36), ('Rendy', 28)])

# passed_students = {student for student in students_score if student }
# passed_students = {student for student in students_score.items() if student[1] > 50 }
# passed_students>>> {('Helen', 52), ('Dave', 75), ('Tom', 82)}

# OR
# —————————————————————————————————————————————————————————
passed_students = {student:score for (student,score) in students_score.items() if score > 50 }
# passed_students>>> {'Dave': 58, 'Rendy': 98}

