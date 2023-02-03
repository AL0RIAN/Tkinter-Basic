import tkinter as tk

win = tk.Tk()
win.title("Second Lesson")
h = win.winfo_screenheight()
w = win.winfo_screenwidth()
photo = tk.PhotoImage(file="..\\img\\logo_lesson1.png")

win.iconphoto(False, photo)
win.geometry(f"{w // 3}x{h // 2}+500+0")
win.minsize(width=200, height=400)
win.maxsize(width=700, height=800)
win.resizable(width=True, height=True)

label_1 = tk.Label(win, text='''Hello 
world''',
                   bg="#000",
                   fg="#fff",
                   font=("Arial", 20, "bold"),
                   padx=20,
                   pady=20,
                   width=10,
                   height=10,
                   anchor="sw",
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT
                   )
label_1.pack()

win.mainloop()
