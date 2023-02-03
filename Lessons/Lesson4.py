import tkinter as tk

win = tk.Tk()
win.title("Fourth Lesson")
h = win.winfo_screenheight()
w = win.winfo_screenwidth()
photo = tk.PhotoImage(file="..\\img\\logo_lesson1.png")
win.iconphoto(False, photo)
win.geometry(f"{w // 3}x{h // 2}")

for row in range(5):
    for col in range(2):
        tk.Button(win, text=f"Hello {row} {col}").grid(row=row, column=col, sticky="ew")

# btn1 = tk.Button(win, text="Hello 1")
# btn2 = tk.Button(win, text="Hello 2")
# btn3 = tk.Button(win, text="Hello 3")
# btn4 = tk.Button(win, text="Hello world")
# btn5 = tk.Button(win, text="Hello 5")
# btn6 = tk.Button(win, text="Hello 6")
# btn7 = tk.Button(win, text="Hello 7")
# btn8 = tk.Button(win, text="Hello 8")
#
# btn1.grid(row=0, column=0, stick="we")
# btn2.grid(row=0, column=1, stick="we")
# btn3.grid(row=1, column=0, stick="we")
# btn4.grid(row=1, column=1, stick="we")
# btn5.grid(row=2, column=0, stick="we")
# btn6.grid(row=2, column=1, stick="ew")
# btn7.grid(row=3, column=0, columnspan=2, stick="we")
# btn8.grid(row=0, column=2, rowspan=4, stick="sn")

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()