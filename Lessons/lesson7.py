import tkinter as tk


def select_all():
    for check in [check1, check2, check3]:
        check.select()


def deselect_all():
    for check in [check1, check2, check3]:
        check.deselect()


def switch():
    for check in [check1, check2, check3]:
        check.toggle()


def show():
    print(str_var.get())


win = tk.Tk()
win.geometry("300x400")
win.title("Seventh lesson")

str_var = tk.StringVar()
str_var.set("no")

check1 = tk.Checkbutton(win, text="Check1", variable=str_var, offvalue="no", onvalue="yes")
check2 = tk.Checkbutton(win, text="Check2")
check3 = tk.Checkbutton(win, text="Check3", indicatoron=False)
check1.pack()
check2.pack()
check3.pack()
tk.Button(win, text="select_all", command=select_all).pack()
tk.Button(win, text="deselect_all", command=deselect_all).pack()
tk.Button(win, text="switch", command=switch).pack()
tk.Button(win, text="show", command=show).pack()

win.mainloop()
