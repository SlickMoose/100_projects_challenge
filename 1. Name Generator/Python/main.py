from Widgets.tk_widgets import *
import random


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

        #   output_label - listbox

        list_box = Listbox(output_label, selectmode=MULTIPLE)
        list_box.pack(fill=BOTH, expand=1, pady=10)

        rb_frame = MyFrame(output_label)
        rb_frame.pack()

        rb_option = StringVar()

        rb_male = MyRadioButton(rb_frame, text='Male', value='male', variable=rb_option, indicatoron=0)
        rb_male.pack(side=LEFT, padx=15, pady=15)

        rb_female = MyRadioButton(rb_frame, text='Female', value='female', variable=rb_option, indicatoron=0)
        rb_female.pack(side=LEFT, padx=15, pady=15)

        rb_option.set('male')

        #   btn_label - buttons

        gen_label = MyLabel(btn_label, text='Select Name Category!')
        gen_label.pack(fill=X)

        cat_var = StringVar()

        drop_down = MyCombobox(btn_label, self.name_cat, textvariable=cat_var, state='readonly')
        drop_down.pack(fill=X, pady=20)

        cat_var.set(self.name_cat[0])

        gen_name_sur = MyButton(btn_label, text='Generate Name & Surname', width=btn_width)
        gen_name_sur.configure(command=lambda button=gen_name_sur:
                                self.generate_names(gen_name_sur, list_box, drop_down, rb_option))

        gen_name_sur.pack(fill=X, pady=5)

        gen_name = MyButton(btn_label, text='Generate Names Only',  width=btn_width)
        gen_name.configure(command=lambda button=gen_name:
                                self.generate_names(gen_name, list_box, drop_down, rb_option))

        gen_name.pack(fill=X, pady=5)

        gen_sur = MyButton(btn_label, text='Generate Surnames Only', width=btn_width)
        gen_sur.configure(command=lambda button=gen_sur:
                                self.generate_names(gen_sur, list_box, drop_down, rb_option))

        gen_sur.pack(fill=X, pady=5)

        close_app = MyButton(btn_label, text='Quit', command=self.master.destroy, width=btn_width)
        close_app.pack(fill=X, pady=5)

    def generate_names(self, button, listbox, dropdown, radiobutton):

        cb_current = dropdown['textvariable']

        if not cb_current == '':

            listbox.delete(0, END)
            names = {}
            gender, surname_count = '', ''

            names_count, surname_count = 0, 0

            if radiobutton.get() == 'male':
                gender = 'male_first'
            else:
                gender = 'female_first'

            for cat in config_names.keys():
                if config_names[cat]['display_name'] == cb_current:
                    names = config_names[cat]
                    names_count = len(config_names[cat][gender]) + 1
                    surname_count = len(config_names[cat]['surnames']) + 1

            for i in range(10):

                if button['text'] == 'Generate Name & Surname':
                    listbox.insert(END, names[gender][random.randrange(0, names_count)] + ' ' +
                                        names['surnames'][random.randrange(0, surname_count)])

                elif button['text'] == 'Generate Names Only':
                    listbox.insert(END, names[gender][random.randrange(0, names_count)])

                elif button['text'] == 'Generate Surnames Only':
                    listbox.insert(END, names['surnames'][random.randrange(0, surname_count)])


def main():

    root = Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
