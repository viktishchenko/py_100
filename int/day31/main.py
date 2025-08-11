from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
  data = pandas.read_csv('int/day31/data/words_to_learn.csv')
except FileNotFoundError:
  original_data = pandas.read_csv('int/day31/data/data_ru.csv')
  to_learn = original_data.to_dict(orient='records')
else:
  to_learn = data.to_dict(orient='records')
# data = pandas.read_csv('int/day31/data/data_ru.csv')
#          English          Russian
# 0           the               то
# ...         ...              ...
# 1046       Paul              Пол

# type(data) # <class 'pandas.core.frame.DataFrame'>

# pandas.DataFrame.to_dict
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
# to_learn = data.to_dict() # {'English': {0: 'the', ... 1046: 'Paul'}, 'Russian': {0: 'то', ... 1046: 'Пол'}}
# to_learn = data.to_dict(orient='records') # [{'English': 'the', 'Russian': 'то'}, ...  {'English': 'Paul', 'Russian': 'Пол'}]

current_card ={}

def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canvas.itemconfig(card_title, text='English', fill='black')
  canvas.itemconfig(card_word, text=current_card['English'], fill='black')
  canvas.itemconfig(card_background, image=card_front_img)
  flip_timer = window.after(3000,func=flip_card)

def flip_card():
  canvas.itemconfig(card_title, text='Русский', fill='white')
  canvas.itemconfig(card_word, text=current_card['Russian'], fill='white')
  canvas.itemconfig(card_background, image=card_back_img)

def is_known():
  '''удаляем из списка известные слова,
     запускаем следующую карточку'''
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  # 
  data.to_csv('int/day31/data/words_to_learn.csv', index=False)
  print(len(to_learn))

  next_card()


window = Tk()
window.minsize(450, 200)
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='int/day31/images/card_front.png')
card_back_img = PhotoImage(file='int/day31/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic') )
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold') )

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file='int/day31/images/wrong.png')
unknown_btn = Button(image=cross_img, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file='int/day31/images/right.png')
known_btn = Button(image=check_img, command=is_known)
known_btn.grid(row=1, column=1)



next_card()

window.mainloop()




