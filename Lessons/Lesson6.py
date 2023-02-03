from tkinter import *
from tkinter import messagebox


def add_digit(number: str) -> None:
    value = calc.get()

    if value == "error":
        value = "0"

    if value == "0":
        calc.delete(0, END)
    calc.insert(END, number)


def add_operation(operation: str) -> None:
    value = calc.get()
    if value == "error":
        value = "0"
    if value[-1] in "+/*-":
        value = calc.get()[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        equal()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + operation)


def equal() -> None:
    value = calc.get()
    if value[-1] in "+-*/" and len(value) == 2:
        value += value[0]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except (ZeroDivisionError, NameError, SyntaxError):
        calc.insert(0, "error")
        messagebox.showinfo("Ошибка ввода", "Недопустимый ввод!")


def clear() -> None:
    calc.delete(0, END)
    calc.insert(0, "0")


def make_button(number: int) -> Button:
    return Button(root, text=number, bd=5, font=("Arial", 13), bg="#4BB2C1", command=lambda: add_digit(str(number)))


def make_operation_button(operation: str) -> Button:
    return Button(root, text=operation, bd=5, fg="red", font=("Arial", 13), bg="#41909B",
                  command=lambda: add_operation(operation))


def make_calc_button(operation: str) -> Button:
    return Button(root, text=operation, bd=5, fg="red", font=("Arial", 13), bg="#41909B", command=equal)


def make_clear_button(operation: str) -> Button:
    return Button(root, text=operation, bd=5, fg="red", font=("Arial", 13), bg="#41909B", command=clear)


def press_key(event: Event) -> None:
    print(event)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-/*" and event.keycode != 16:
        add_operation(event.char)
    elif event.keycode == 13:
        equal()


if __name__ == "__main__":
    root = Tk()

    root.geometry("240x270")
    root.title("Калькулятор")
    root.resizable(False, False)
    root.wm_attributes("-alpha", 0.7)
    root["bg"] = "#38727A"

    root.bind("<Key>", press_key)

    calc = Entry(root, justify=RIGHT, font=("Arial", 15), width=15, bg="#4BB2C1")
    calc.insert(0, "0")
    calc.grid(row=0, column=0, columnspan=4, padx=5, stick="ew")

    make_button(7).grid(row=1, column=0, stick="news", padx=5, pady=5)
    make_button(8).grid(row=1, column=1, stick="news", padx=5, pady=5)
    make_button(9).grid(row=1, column=2, stick="news", padx=5, pady=5)
    make_button(4).grid(row=2, column=0, stick="news", padx=5, pady=5)
    make_button(5).grid(row=2, column=1, stick="news", padx=5, pady=5)
    make_button(6).grid(row=2, column=2, stick="news", padx=5, pady=5)
    make_button(1).grid(row=3, column=0, stick="news", padx=5, pady=5)
    make_button(2).grid(row=3, column=1, stick="news", padx=5, pady=5)
    make_button(3).grid(row=3, column=2, stick="news", padx=5, pady=5)
    make_button(0).grid(row=4, column=0, stick="news", padx=5, pady=5)

    make_operation_button("+").grid(row=1, column=3, stick="news", padx=5, pady=5)
    make_operation_button("-").grid(row=2, column=3, stick="news", padx=5, pady=5)
    make_operation_button("/").grid(row=3, column=3, stick="news", padx=5, pady=5)
    make_operation_button("*").grid(row=4, column=3, stick="news", padx=5, pady=5)

    make_clear_button("C").grid(row=4, column=1, stick="news", padx=5, pady=5)
    make_calc_button("=").grid(row=4, column=2, stick="news", padx=5, pady=5)

    for col in range(4):
        root.grid_columnconfigure(col, minsize=60)

    for row in range(1, 5):
        root.grid_rowconfigure(row, minsize=60)

    root.mainloop()
