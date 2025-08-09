from tkinter import *
from tkinter import messagebox
import random
# py -m pip install pyperclip
import pyperclip
import json

WHITE = "#FFFFFF"
FONT_NAME = ('New Roman', 14, 'normal')
FONT_INPUT = ('New Roman', 12, 'normal')
# FONT_NAME = 'Courier'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  password = ''
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  symbols = ['!','#','$','%','&','(', ')','*','+']

  pass_letter = [random.choice(letters) for _ in range(random.randint(8,10))]
  pass_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
  pass_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

  res = pass_letter + pass_symbols + pass_numbers

  random.shuffle(res)
  password = ''.join(res)
  pass_input.delete(0,END)
  pass_input.insert(0, password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def gen_passdata():
  try:
    site = web_input.get()
    email = email_input.get()
    psd = pass_input.get()
    new_data = {
      site: {
        'email': email,
        'password': psd
      }
    }
  except ValueError:
    print('Something went wrong...')

  if len(site) == 0 or len(email) == 0 or len(psd) == 0:
    messagebox.showerror(title='ERROR', message='Please fill all of the fields!')
  else:
    output_path = 'int/day30/task/data.json'
    with open(output_path, 'r') as new_file:
      # # WRITE DATA
    # with open(output_path, 'w') as new_file:
    #   # #____________________________________________
    #   # # human read json.value: indent=4
    #   json.dump(new_data, new_file, indent=4)

      # READ DATA FROM FILE
      # #______________________________________________
      # read_file = json.load(new_file )
      # print(read_file) # {'Amazon': {'email': 'amazon@mail.com', 'password': '0!+5yblU4Aw5iU!r'}}
      # # print(type(read_file)) # <class 'dict'>

      # UPDATE DATA FROM FILE
      # #______________________________________________
      # READING OLD DATA
      data = json.load(new_file )
      # UPDATING OLD DATA WITH NEW DATA
      data.update(new_data)
      # SAVING UPDEATING DATA
    with open(output_path, 'w') as new_file:
      json.dump(data, new_file, indent=4)

    
    web_input.delete(0, END)
    pass_input.delete(0, END)
    email_input.delete(0, END)
    web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password generator')
window.config(padx=50,pady=50, bg=WHITE)

canvas = Canvas(width=200,height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file='int/day29/img/logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

# Label
web_label = Label(text='Website:', font=FONT_NAME,bg=WHITE)
email_label = Label(text='Email/Username:', font=FONT_NAME,bg=WHITE)
pass_label = Label(text='Password:', font=FONT_NAME,bg=WHITE)

web_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
pass_label.grid(column=0,row=3)

# Input
web_input = Entry(width=35,font=FONT_NAME,border=2)
web_input.focus()
email_input = Entry(width=35, font=FONT_NAME,border=2)
email_input.insert(0,'test@mail.com')
pass_input = Entry(width=21, font=FONT_NAME,border=2)

web_input.grid(column=1,row=1,columnspan=2,pady=5)
email_input.grid(column=1,row=2,columnspan=2,pady=5)
pass_input.grid(column=1,row=3,pady=5)

# Button
gen_button = Button(text='Generate Password', font=FONT_INPUT, command=generate_password)
add_button = Button(text='Add', width=42, font=FONT_INPUT, command=gen_passdata)

gen_button.grid(column=2,row=3,pady=5)
add_button.grid(column=1,row=4,columnspan=2, pady=5)





window.mainloop()