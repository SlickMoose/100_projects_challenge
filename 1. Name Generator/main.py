import math
import tkinter as tk
from config import config_names
from tkinter import ttk


class NameGenerator(ttk.Frame):

    def __init__(self, master=None):

        ttk.Frame.__init__(self, master)

        self.style = ""
        self.configure_style()
        self.master = master

        self.master.geometry("500x500")
        self.master.resizable(0, 0)
        self.master.title("Name Generator")
        self.master.configure(background='#19232D')

        self.name_cat = self.set_categories()
        self.set_frame()

    def set_categories(self):

        name_cat = [config_names[cat]['display_name'] for cat in config_names.keys()]

        return name_cat

    def set_frame(self):

        btn_width = 30

        mainframe = tk.Frame(self.master)
        mainframe.pack(pady=100)

        cat_var = tk.StringVar(self.master)
        cat_var.set(self.name_cat[0])

        info = tk.Label(self.master, text='Select Name Category!')
        info.pack()

        drop_down = ttk.OptionMenu(info, cat_var, *self.name_cat)
        drop_down.grid()

        start_gen = ttk.Button(info, text='Generate Name & Surname',
                               command=self.generate_names, width=btn_width, style="MyButton")
        start_gen.grid()

        start_gen = ttk.Button(info, text='Generate Name Only',
                               command=self.generate_names, width=btn_width)
        start_gen.grid()

        start_gen = ttk.Button(info, text='Generate Surname Only',
                               command=self.generate_names, width=btn_width)
        start_gen.grid()

        close_app = ttk.Button(info, text='Quit',
                               command=self.master.destroy, width=btn_width)
        close_app.grid()

    def generate_names(self):

        pass

    def configure_style(self):

        self.style = ttk.Style()

        self.style.configure('MyFrame',
                             background='#19232D')

        self.style.configure('MyLabel',
                             background='#19232D',
                             foreground="#F0F0F0",
                             font="Arial 20 bold")

        self.style.configure('MyButton',
                             background='#19232D',
                             foreground="#F0F0F0",
                             font="Arial 12")

        self.style.configure('MyChechbox',
                             background='#19232D',
                             foreground="#F0F0F0",
                             font="Arial 12")

        self.style.configure('MyOption',
                             background='#19232D',
                             foreground="#F0F0F0",
                             font="Arial 12")


def main():

    root = tk.Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
