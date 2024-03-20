from tkinter import *


def button_clicked():
    get_miles = int(entry.get())
    convert = round(get_miles * 1.609)
    label_sum.config(text=f"{convert}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=7)
entry.grid(column=1, row=0)
label_m = Label(text="Miles")
label_m.grid(column=2, row=0)

label_out = Label(text="is equal")
label_out.grid(column=0, row=1)
label_sum = Label(text="0")
label_sum.grid(column=1, row=1)
label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
