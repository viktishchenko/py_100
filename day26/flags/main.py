student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


word_dict = pandas.read_csv('day26/flags/nato_phonetic_alphabet.csv')
# print(word_dict)
# #    letter      code
# # 0       A      Alfa
# # 1       B     Bravo

alphabet_dict = {row.letter: row.code for (_,row) in word_dict.iterrows()}
# print(f'alphabet_dict>>> {alphabet_dict}')
# {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'} 
# print(f'alphabet_dict>>> {alphabet_dict['A']}') # alphabet_dict>>> Alfa
# res = dict((v,k) for k,v in alphabet_dict.items()) # res["Alfa"]>>> A
# print(f"res.get('Alfa')>>>, {res.get('Alfa')}") # res.get('Alfa')>>>, A
# print(f'res["Alfa"]>>> {res["Alfa"]}')  # res["Alfa"]>>> A
user_word = input('Enter your word: ').upper()
# # print(f'user_words>>> {user_words}') # user_words>>> Tomas
word_list = [alphabet_dict[letter] for letter in user_word]
print(f'word_list>>> {word_list}') # word_list>>> ['Tango', 'Oscar', 'Mike', 'Alfa', 'Sierra']





   