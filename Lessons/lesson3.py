import tkinter as tk


def say_hello():
    print("Hello")

    for btn in [btn2, btn3, btn4]:
        btn.config(state=tk.DISABLED)


def add_label():
    label = tk.Label(win, text="new")
    label.pack()


def counter():
    global count
    global x
    if count == 50:
        btn4.config(state=tk.DISABLED)
    else:
        count += 1
        x += 10
        btn4.config(text=f"Counter {count}", padx=x)
    # btn4["text"] = f"Counter {count}"


win = tk.Tk()
win.title("Third Lesson")
h = win.winfo_screenheight()
w = win.winfo_screenwidth()
photo = tk.PhotoImage(file="..\\img\\logo_lesson1.png")
win.iconphoto(False, photo)
win.geometry(f"{w // 3}x{h // 2}")
count = 0
x = 0

btn1 = tk.Button(win, text="Hello",
                 command=say_hello
                 )

btn2 = tk.Button(win, text="New Label",
                 command=add_label)

btn3 = tk.Button(win, text="New Label (lambda)",
                 command=lambda: tk.Label(win, text="new").pack()
                 )

btn4 = tk.Button(win, text=f"Counter {count}",
                 command=counter,
                 bg="#0000FF",
                 activebackground="#FF0000",
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()
