import math
from tkinter import *
from tkinter import ttk
from config import config_names, config_colors


class NameGenerator(ttk.Frame):

    def __init__(self, master=None):

        ttk.Frame.__init__(self, master)

        self.style = self.configure_styles()
        self.master = master

        self.master.geometry("500x500")
        self.master.resizable(0, 0)
        self.master.title("Name Generator")
        self.master.configure(background=config_colors['dark_blue'])

        self.name_cat = self.set_categories()
        self.set_frame()

    def set_categories(self):

        name_cat = [config_names[cat]['display_name'] for cat in config_names.keys()]

        return name_cat

    def set_frame(self):

        btn_width = 30

        mainframe = Frame(self.master)
        mainframe.pack(fill=Y)

        cat_var = StringVar(self.master)
        cat_var.set(self.name_cat[0])

        btn_label = ttk.Label(mainframe, text='Select Name Category!', style='TLabel')
        btn_label.pack()

        output_label = ttk.Label(mainframe, text='Select Name Category!', style='TLabel')
        output_label.pack()

        drop_down = ttk.OptionMenu(btn_label, cat_var, *self.name_cat)
        drop_down.pack()

        start_gen = ttk.Button(btn_label, text='Generate Name & Surname',
                               command=self.generate_names, width=btn_width, style='TButton')
        start_gen.pack()

        start_gen = ttk.Button(btn_label, text='Generate Name Only',
                               command=self.generate_names, width=btn_width, style='TButton')
        start_gen.pack()

        start_gen = ttk.Button(btn_label, text='Generate Surname Only',
                               command=self.generate_names, width=btn_width, style='TButton')
        start_gen.pack()

        close_app = ttk.Button(btn_label, text='Quit',
                               command=self.master.destroy, width=btn_width, style='TButton')
        close_app.pack()

    def generate_names(self):

        pass

    def configure_styles(self):

        style = ttk.Style()

        style.theme_create('modern_app', parent='xpnative', settings={

            'TLabel':      {'configure': {'background': config_colors['dark_blue'],
                                               'foreground': config_colors['light_gray'],
                                               'padding': 10,
                                               'font': ('Calibri', 12)
                                               }
                                 },

            'TButton':     {'configure': {'background': config_colors['dark_blue'],
                                               'foreground': config_colors['light_gray'],
                                               'padding': 10,
                                               'font': ('Calibri', 12)
                                               }
                                 },

            'TChechbox':   {'configure': {'background': config_colors['dark_blue'],
                                               'foreground': config_colors['light_gray'],
                                               'padding': 10,
                                               'font': ('Calibri', 12)
                                               }
                                 },

            'TMenuButton':     {'configure': {'background': config_colors['dark_blue'],
                                               'foreground': config_colors['light_gray'],
                                               }
                                 }
        })
        style.theme_use("modern_app")

        return style


def main():

    root = Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
