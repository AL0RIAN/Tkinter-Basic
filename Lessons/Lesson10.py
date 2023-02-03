import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from random import shuffle

colors = {
    1: "blue",
    2: "green",
    3: "red",
    4: "purple",
    5: "#0707a8",
    6: "#003d00",
    7: "#ff003c",
    8: "#820082"
}


class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font="Calibri 15 bold", *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self) -> str:
        return f"MyButton {self.x} {self.y} {self.number} {self.is_mine}"


class MineSweeper:
    ROW = 10
    COLUMNS = 10
    window = tk.Tk()
    MINES = 15
    FLAGS = MINES
    IS_GAME_OVER = False
    IS_WIN = False
    IS_FIRST_CLICK = True

    def __init__(self):
        self.buttons = []
        MineSweeper.window.title("Сапёр")
        for row in range(MineSweeper.ROW + 2):
            temp = []
            for col in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.window, x=row, y=col)
                btn.config(command=lambda button=btn: self.click(button))
                btn.bind("<Button-3>", self.right_click)
                temp.append(btn)

            self.buttons.append(temp)

    def right_click(self, event):
        """


        :param event:
        :return:
        """

        current_btn = event.widget
        if MineSweeper.IS_GAME_OVER or MineSweeper.IS_WIN:
            return
        elif current_btn["state"] == "normal" and MineSweeper.FLAGS != 0:
            current_btn["state"] = "disabled"
            current_btn["text"] = "🚩"
            MineSweeper.FLAGS -= 1
            current_btn["disabledforeground"] = "red"
        elif current_btn["text"] == "🚩":
            current_btn["text"] = ""
            current_btn["state"] = "normal"
            MineSweeper.FLAGS += 1
        self.check_win()

    def click(self, clicked_button: MyButton) -> None:
        if MineSweeper.IS_GAME_OVER or MineSweeper.IS_WIN:
            return

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines()
            self.print_buttons()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_button.is_mine:
            clicked_button.config(text="*", background="red", disabledforeground="black")
            clicked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            for row in range(MineSweeper.ROW + 2):
                for col in range(MineSweeper.COLUMNS + 2):
                    btn = self.buttons[row][col]
                    if btn.is_mine:
                        btn.config(text="*")
            showinfo("Game over", "Вы проиграли")
        else:
            color = colors.get(clicked_button.count_bomb, "black")
            if clicked_button.count_bomb > 0:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            else:
                self.breadth_first_search(clicked_button)
                clicked_button.is_open = True
        clicked_button.config(state="disabled", relief=tk.SUNKEN)
        self.check_win()

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, "black")
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text="")

            cur_btn.is_open = True
            cur_btn.config(state="disabled", relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # if not abs(dx - dy) == 1:
                        #     continue

                        next_btn = self.buttons[x + dx][y + dy]
                        if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and \
                                1 <= next_btn.y <= MineSweeper.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

    def create_widgets(self) -> None:
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Играть", command=self.reload)
        settings_menu.add_command(label="Настройки", command=self.create_settings_win)
        settings_menu.add_command(label="Выход", command=self.window.destroy)
        menubar.add_cascade(label="Файл", menu=settings_menu)

        count = 1
        for row in range(1, MineSweeper.ROW + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                btn.number = count
                btn.grid(row=row, column=col, stick="news")
                count += 1

        for row in range(1, MineSweeper.ROW + 1):
            self.window.rowconfigure(row, weight=1)

        for col in range(1, MineSweeper.COLUMNS + 1):
            self.window.columnconfigure(col, weight=1)

    def open_all_buttons(self) -> None:
        for row in range(MineSweeper.ROW + 2):
            for col in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[row][col]
                if btn.is_mine:
                    btn.config(text="*", background="red", disabledforeground="white")
                else:
                    btn.config(text=btn.count_bomb, fg=colors.get(btn.count_bomb, "black"))

    def start(self) -> None:
        self.create_widgets()
        # self.open_all_buttons()
        MineSweeper.window.mainloop()

    def reload(self) -> None:
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_WIN = False
        MineSweeper.IS_GAME_OVER = False

    def create_settings_win(self):
        win_settings = tk.Toplevel(self.window)
        win_settings.title("Настройки")
        tk.Label(win_settings, text="Количество строк").grid(row=0, column=0)
        row_entry = tk.Entry(win_settings)
        row_entry.grid(row=0, column=1, padx=20, pady=20)
        row_entry.insert(0, MineSweeper.ROW)
        tk.Label(win_settings, text="Количество столбцов").grid(row=1, column=0)
        col_entry = tk.Entry(win_settings)
        col_entry.grid(row=1, column=1, padx=20, pady=20)
        col_entry.insert(0, MineSweeper.COLUMNS)
        tk.Label(win_settings, text="Количество мин").grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)
        mines_entry.insert(0, MineSweeper.MINES)
        save_btn = tk.Button(win_settings, text="Сохранить",
                             command=lambda: self.change_settings(row_entry, col_entry, mines_entry))
        save_btn.grid(row=3, column=0, columnspan=2, pady=5)

    def change_settings(self, row: tk.Entry, col: tk.Entry, mines: tk.Entry):
        try:
            int(row.get()), int(col.get()), int(mines.get())
        except ValueError:
            showerror("Ошибка", "Неправильные значения")
            return

        MineSweeper.ROW = int(row.get())
        MineSweeper.COLUMNS = int(col.get())
        MineSweeper.MINES = int(mines.get())
        MineSweeper.FLAGS = MineSweeper.MINES
        self.reload()

    def print_buttons(self) -> None:
        for row in range(1, MineSweeper.ROW + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                if btn.is_mine:
                    print("B", end=" ")
                else:
                    print(btn.count_bomb, end=" ")
            print()

    @staticmethod
    def get_mines_places(exclude_number: int):
        pos = list(range(1, MineSweeper.ROW * MineSweeper.COLUMNS + 1))
        pos.remove(exclude_number)
        shuffle(pos)
        return pos[:MineSweeper.MINES]

    def insert_mines(self, number: int):
        pos = self.get_mines_places(number)
        for row in range(1, MineSweeper.ROW + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                if btn.number in pos:
                    btn.is_mine = True

    def count_mines(self):
        for row in range(1, MineSweeper.ROW + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[row + row_dx][col + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    def check_win(self):
        for row in range(1, MineSweeper.ROW + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                if not btn["state"] == "disabled":
                    return

        showinfo("Победа!", "Вы победили!")
        MineSweeper.IS_WIN = True


if __name__ == "__main__":
    game = MineSweeper()
