import pandas

data_src = 'int/day26/flags/nato_phonetic_alphabet.csv'
data_tbl = pandas.read_csv(data_src)
data_dict = {row.letter: row.code for (_,row) in data_tbl.iterrows()}

def generate_list():
  input_word = input('Enter a word: ').upper()

  try:
    output_list = [data_dict[letter] for letter in input_word]
  except KeyError:
    print('Sorry, only letters in the alphabet please.')
    generate_list()
  else:
    print(output_list)

generate_list()

# BASIC.EXTENDED___________________________________________________
# data_src = 'int/day26/flags/nato_phonetic_alphabet.csv'
# data_tbl = pandas.read_csv(data_src) # <class 'pandas.core.frame.       DataFrame'>
#   #    letter      code
#   # 0       A      Alfa
#   # 1       B     Bravo
#   # ...
#   # ...
#   # 23      X     X-ray
#   # 25      Z      Zulu
# data_dict = {row.letter: row.code for (_,row) in data_tbl.iterrows()}
# # {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}
# input_word = input('Enter a word: ').upper()
# output_list = [data_dict[letter] for letter in input_word]
# print(output_list) # ['Hotel', 'Alfa', 'Lima', 'Oscar']