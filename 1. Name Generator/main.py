import math
import tkinter as tk
from config import config_names


class NameGenerator:

    def __init__(self, master):

        self.master = master
        self.name_cat = self.set_categories()
        self.set_frame()

    def set_categories(self):

        name_cat = [config_names[cat]['display_name'] for cat in config_names.keys()]

        return name_cat

    def set_frame(self):

        btn_width = 30
        row_padding = 50

        mainframe = tk.Frame(master=self.master)
        mainframe.grid()
        mainframe.pack(pady=100)
        mainframe.grid_rowconfigure(1, minsize=row_padding)
        mainframe.grid_rowconfigure(2, minsize=row_padding)
        mainframe.grid_rowconfigure(3, minsize=row_padding)
        mainframe.grid_rowconfigure(4, minsize=row_padding)

        cat_var = tk.StringVar(self.master)
        cat_var.set(self.name_cat[0])

        info = tk.Label(master=mainframe, text='Select Name Category!', fg='black')
        info.grid()

        drop_down = tk.OptionMenu(mainframe, cat_var, *self.name_cat)
        drop_down.grid()

        start_gen = tk.Button(master=mainframe, text='Generate Name & Surname',
                              command=self.generate_names, width=btn_width)
        start_gen.grid()

        start_gen = tk.Button(master=mainframe, text='Generate Name Only',
                              command=self.generate_names, width=btn_width)
        start_gen.grid()

        start_gen = tk.Button(master=mainframe, text='Generate Surname Only',
                              command=self.generate_names, width=btn_width)
        start_gen.grid()

        close_app = tk.Button(master=mainframe, text='Quit',
                              command=self.master.destroy, width=btn_width)
        close_app.grid()

    def generate_names(self):

        pass


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    root.title("Name Generator")

    app = NameGenerator(root)
    root.mainloop()
