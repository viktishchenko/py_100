from tkinter import *

window = Tk()
window.minsize(450,200)
window.title('Miles to Km Converter')
window.config(padx=50,pady=50)

text_lable = Label(text='is equal to', font=('Arial', 16, 'normal'))
text_lable.grid(column=0,row=1,ipady=5)

output_lable = Label(text=0, font=('Arial', 18, 'normal'))
output_lable.grid(column=1,row=1,ipady=5, ipadx=5)

text_lable = Label(text='Km', font=('Arial', 16, 'normal'))
text_lable.grid(column=2,row=1,ipady=5, ipadx=5)


input = Entry(font=('Arial', 16, 'normal'))
input.focus()
input.grid(column=1,row=0, ipady=7 )
input_lable = Label(text='Miles', font=('Arial', 16, 'normal'))
input_lable.grid(column=2,row=0)
input_lable.config(padx=10)

def convert_value():
  input_val = float(input.get())
  res_value = round(input_val*1.609, 2)
  output_lable.config(text=res_value)
  input.delete(0,END)
  print('halo')

button = Button(text='Calculate', font=('Arial', 16, 'normal'), command=convert_value, highlightcolor="#bdbdbd", highlightbackground="#bdbdbd",borderwidth=1)
button.grid(column=1,row=2,ipady=5, ipadx=5)


window.mainloop()