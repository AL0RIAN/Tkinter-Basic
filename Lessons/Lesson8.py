import tkinter as tk


def select_level():
    level = level_var.get()
    print(levels[level])


levels = {
    1: "Easy",
    2: "Middle",
    3: "Hard"
}

win = tk.Tk()
win.geometry("300x400")
win.title("Eighth lesson")

level_var = tk.IntVar()
level_text = tk.StringVar()

tk.Label(win, text="Chose difficult").pack()
tk.Radiobutton(win, text="Easy", variable=level_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text="Normal", variable=level_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text="Hard", variable=level_var, value=3, command=select_level).pack()

level_label = tk.Label(win, textvariable=level_text)
level_label.pack()

win.mainloop()
