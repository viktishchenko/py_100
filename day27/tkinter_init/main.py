# GUI (graphical user interface)
# https://www.tcl-lang.org/man/tcl9.0/TkCmd/index.html

import tkinter

# from tkinter import *
# button = Button()

window = tkinter.Tk()
window.title('Первая программа')
window.minsize(width=1000, height=700)


# Label
my_label = tkinter.Label(text='Главный заголовок (label)', font=('Arial', 26, 'bold'))
my_label.pack() # top. center
# my_label.pack(side='bottom') # bottom
# my_label.pack(expand=True) # center

# CHANGE PROPERTY
new_text = 'Halo everyone!'
my_label['text'] = new_text # Halo
# my_label.config(text='Halo, there!') # Halo, there!
# my_label['text'] = 'Halo' # Halo
# my_label.config(text='Halo, there!') # Halo, there!

# BUTTON

def button_clicked():
  print('i got clicked')
  my_label.config(text=input.get() or new_text)

button = tkinter.Button(text='halo', command=button_clicked)
button.pack()

# ENTRY COMPONENT

input = tkinter.Entry(width=20)
input.pack(pady=10)






window.mainloop()