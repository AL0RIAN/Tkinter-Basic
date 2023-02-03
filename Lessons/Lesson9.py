import tkinter as tk
from tkinter import ttk


def show_day():
    print(combo.get())


weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

win = tk.Tk()
win.geometry("300x400")
win.title("Ninth lesson")

combo = ttk.Combobox(win, values=weekDays, justify="center")
combo.current(0)
combo.pack()

ttk.Button(win, text="Show Day", command=show_day).pack()

win.mainloop()
