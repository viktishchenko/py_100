from tkinter import *


window = Tk()
window.minsize(width=1000,height=500)
window.title('self check')
window.config(padx=25,pady=25)

# LABEL
lable = Label(text='test title',font=('Arial', 18, 'bold'))
# lable.pack()
lable.grid(column=0,row=0)

def button_clicked():
  print('Button was clicked!')
  input_label.config(text=f'input text: {input.get()}')

# BUTTON
button = Button(text='Button', command=button_clicked)
# button.pack(pady=10)
button.grid(column=1,row=1)

# new BUTTON
new_button = Button(text='New Button', command=button_clicked)
# button.pack(pady=10)
new_button.grid(column=2,row=0)


# INPUT|ENTRY
input = Entry(width=20)
# input.pack()
input.grid(column=3,row=2)
input_label = Label(text='input text:')
# input_label.pack(pady=10)
input_label.grid(column=3,row=3)


window.mainloop()