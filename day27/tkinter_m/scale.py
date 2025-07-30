from tkinter import *

root = Tk()
root.geometry("300x150")

def update_label(val):
    value_label.config(text=f"Current Value: {int(float(val))}") # Convert to int if desired

my_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=update_label)
my_scale.pack(pady=20)

value_label = Label(root, text="Current Value: 0")
value_label.pack()

root.mainloop()