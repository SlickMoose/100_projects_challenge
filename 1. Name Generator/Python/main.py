from Widgets.tk_widgets import *


class NameGenerator:

    def __init__(self, master=None):

        self.master = master

        self.master.geometry("500x250")
        self.master.resizable(0, 0)
        self.master.title("Name Generator")

        self.name_cat = self.set_categories()
        self.set_layout()

    def set_categories(self):

        name_cat = [config_names[cat]['display_name'] for cat in config_names.keys()]
        name_cat.sort()

        return name_cat

    def set_layout(self):

        btn_width = 30

        main_frame = MyFrame(self.master)
        main_frame.pack(expand=1, fill=BOTH)

        btn_label = MyLabel(main_frame)
        btn_label.pack(side=LEFT, expand=1, fill=BOTH, padx=10)

        output_label = MyLabel(main_frame)
        output_label.pack(side=LEFT, expand=1, fill=BOTH, padx=10)

        #   btn_label - buttons

        gen_label = MyLabel(btn_label, text='Select Name Category!')
        gen_label.pack(fill=X)

        cat_var = StringVar()
        cat_var.set(self.name_cat[0])

        drop_down = MyCombobox(btn_label, self.name_cat, textvariable=cat_var, state='readonly')
        drop_down.pack(fill=X, pady=20)

        start_gen = MyButton(btn_label, text='Generate Name & Surname',
                                command=self.generate_names, width=btn_width)
        start_gen.pack(fill=X, pady=5)

        start_gen = MyButton(btn_label, text='Generate Names Only',
                                command=self.generate_names, width=btn_width)
        start_gen.pack(fill=X, pady=5)

        start_gen = MyButton(btn_label, text='Generate Surnames Only',
                                command=self.generate_names, width=btn_width)
        start_gen.pack(fill=X, pady=5)

        close_app = MyButton(btn_label, text='Quit',
                                command=self.master.destroy, width=btn_width)
        close_app.pack(fill=X, pady=5)

        #   output_label - listbox

        output_text = MyLabel(output_label, text='Generated Names!', anchor=N)
        output_text.pack(fill=X)

        list_box = Listbox(output_label)
        list_box.pack(fill=BOTH, pady=20, expand=1)

    def generate_names(self):

        pass


def main():

    root = Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
