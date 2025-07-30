from tkinter import *

window = Tk()
window.minsize(450, 200)
window.title('Miles to Km Converter')
window.config(padx=50, pady=50)

# Labels
equal_label = Label(text='is equal to', font=('Arial', 16, 'normal'))
equal_label.grid(column=0, row=1, pady=5)

output_label = Label(text='0', font=('Arial', 18, 'normal'))
output_label.grid(column=1, row=1, padx=5, pady=5)

km_label = Label(text='Km', font=('Arial', 16, 'normal'))
km_label.grid(column=2, row=1, padx=5)

# Entry
miles_entry = Entry(font=('Arial', 16, 'normal'), width=10)
miles_entry.focus()
miles_entry.grid(column=1, row=0, pady=10)

miles_label = Label(text='Miles', font=('Arial', 16, 'normal'))
miles_label.grid(column=2, row=0, padx=10)

def convert_value():
    try:
        input_val = float(miles_entry.get())  # Используем float вместо int для дробных чисел
        result_value = round(input_val * 1.609, 2)
        output_label.config(text=result_value)
    except ValueError:
        output_label.config(text="Invalid input")

convert_button = Button(
    text='Calculate', 
    font=('Arial', 16, 'normal'), 
    command=convert_value,
    borderwidth=1
)
convert_button.grid(column=1, row=2, pady=10)

window.mainloop()