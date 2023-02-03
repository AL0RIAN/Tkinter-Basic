import tkinter as tk

win = tk.Tk()
win.title("First Lesson")
# С помощью +x+y можно сместить изначальное расположение окна относительно левого верхнего края экрана
h = win.winfo_screenheight()
w = win.winfo_screenwidth()
photo = tk.PhotoImage(file="..\\img\\logo_lesson1.png")

win.iconphoto(False, photo)
win.config(bg="#D58D52")
win.geometry(f"{w // 2}x{h // 2}+500+0")
win.minsize(width=200, height=400)
win.maxsize(width=700, height=800)

win.resizable(width=True, height=True)

win.mainloop()
