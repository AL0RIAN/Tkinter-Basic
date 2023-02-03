import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
        name.delete(0, tk.END)
    else:
        print("Empty")


def del_text():
    name.delete(0, tk.END)


win = tk.Tk()
win.title("Fifth Lesson")
h = win.winfo_screenheight()
w = win.winfo_screenwidth()
photo = tk.PhotoImage(file="..\\img\\logo_lesson1.png")
win.iconphoto(False, photo)
win.geometry(f"{w // 3}x{h // 2}")

tk.Label(win, text="Enter name").grid(row=0, column=0, stick="w")
tk.Label(win, text="Password").grid(row=1, column=0, stick="w")

name = tk.Entry(win)
name1 = tk.Entry(win, show="*")
name.grid(row=0, column=1)
name1.grid(row=1, column=1)

tk.Button(win, text="GET", command=get_entry).grid(row=0, column=2, stick="e")
tk.Button(win, text="DEL", command=del_text).grid(row=0, column=3)
tk.Button(win, text="INS", command=lambda: name.insert(tk.END, "@gmail.com")).grid(row=0, column=4)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_rowconfigure(1, minsize=100)

win.mainloop()
