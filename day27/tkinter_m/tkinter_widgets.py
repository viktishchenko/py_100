from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")
    spinbox_label.config(text='Value: 0')
    scale.set(0)
    checked_state.set(0)
    check_state()
    tmp_var.set(0)

#calls action() when pressed
button = Button(text="Reset scale&spin", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
tmp_var = IntVar()
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
    spinbox_label.config(text=f'Value: {spinbox.get()}')
spinbox = Spinbox(from_=0, to=10, width=5, textvariable=tmp_var, command=spinbox_used)
spinbox.pack()

spinbox_label = Label(text='Value: 0')
spinbox_label.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
    value_label.config(text=f"Current Value: {int(float(value))}") # Convert to int if desired

scale = Scale(from_=0, to=100, orient=HORIZONTAL, command=scale_used)
scale.pack()

value_label = Label( text="Current Value: 0")
value_label.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get())
    ch_label.config(text=f'chlabel: {check_state()}')

def check_state():
    if checked_state.get() == 1:
      ch_label.config(text=f'chlabel: True')
      return True
    if checked_state.get() == 0:
      ch_label.config(text=f'chlabel: False')
      return False
    
    #Prints 1 if On button checked, otherwise 0.
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

ch_label = Label(text=f'chlabel: False')
ch_label.pack()


#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=231, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=456, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

