from tk_widgets import *

DEGREE_SIGN = u'\N{DEGREE SIGN}'


class TemperatureConverter:

    def __init__(self, master=None):

        self.master = master

        self.master.resizable(False, False)
        self.master.title("Temperature Converter")
        self.master.geometry('350x250')

        self.temp_cat = self.set_categories()
        self.set_layout()

    @staticmethod
    def set_categories():
        return [DEGREE_SIGN + 'F (Fahrenheit)', DEGREE_SIGN + 'C (Celsius)', DEGREE_SIGN + 'K (Kelvin)']

    def set_layout(self):

        input_validation = self.master.register(self.check_input)

        temp_from, temp_to = StringVar(), StringVar()

        master_frame = MyFrame(master=self.master)
        master_frame.pack(fill=BOTH)

        # output section
        output_label = MyLabel(master=master_frame)
        output_label.pack(fill=X)
        output_label.configure(text='>>  <<', font=('Bold', 20), padx=20, pady=20)

        # combobox section
        combobox_frame = MyFrame(master=master_frame)
        combobox_frame.pack(fill=X, padx=50)

        combobox_frame.grid_columnconfigure(0, weight=1)
        combobox_frame.grid_columnconfigure(1, weight=2)

        placeholder_from = 'Temperature'

        user_entry = MyEntry(master=combobox_frame,
                             placeholder=placeholder_from,
                             justify='center',
                             validate='key',
                             validatecommand=(input_validation, '%S', placeholder_from))

        user_entry.grid(row=0, columnspan=2, sticky=NSEW)

        label_from = MyLabel(master=combobox_frame, text='From:', anchor='w')
        label_from.grid(row=1, column=0, sticky=NSEW)

        temp_from = MyCombobox(master=combobox_frame,
                               menu_values=self.temp_cat,
                               textvariable=temp_from,
                               state='readonly')
        temp_from.current(0)
        temp_from.grid(row=1, column=1, sticky=NSEW)

        label_to = MyLabel(master=combobox_frame, text='To:', anchor='w')
        label_to.grid(row=2, column=0, sticky=NSEW)

        temp_to = MyCombobox(master=combobox_frame,
                             menu_values=self.temp_cat,
                             textvariable=temp_to,
                             state='readonly')

        temp_to.current(1)
        temp_to.grid(row=2, column=1, sticky=NSEW)

        # button section
        btn_frame = MyFrame(master=master_frame)
        btn_frame.pack(pady=20)

        gen_sur = MyButton(master=btn_frame, text='Convert', width=30)
        gen_sur.pack(fill=X, pady=5)
        gen_sur.config(command=lambda button=gen_sur: self.convert(user_entry,
                                                                   temp_from.get(),
                                                                   temp_to.get(),
                                                                   output_label))

        exit_button = MyButton(master=btn_frame, text='Quit', command=self.master.destroy, width=30)
        exit_button.pack(fill=X, pady=5)

    def convert(self, user_entry, temp_from, temp_to, output_label):

        if user_entry.get() != user_entry.placeholder:

            entry_float = float(user_entry.get())

            # from Fahrenheit
            if temp_from == self.temp_cat[0]:

                # to Fahrenheit
                if temp_to == self.temp_cat[0]:
                    temperature = entry_float

                # to Celsius
                elif temp_to == self.temp_cat[1]:
                    temperature = (entry_float - 32) * 0.5556

                # to Kelvin
                else:
                    temperature = (entry_float + 459.67) * 0.5556

            # from Celsius
            elif temp_from == self.temp_cat[1]:

                # to Celsius
                if temp_to == self.temp_cat[1]:
                    temperature = entry_float

                # to Fahrenheit
                elif temp_to == self.temp_cat[0]:
                    temperature = (entry_float * 1.8) + 32

                # to Kelvin
                else:
                    temperature = (entry_float + 273.15)

            # from Kelvin
            else:

                # to Kelvin
                if temp_to == self.temp_cat[2]:
                    temperature = entry_float

                # to Fahrenheit
                elif temp_to == self.temp_cat[0]:
                    temperature = (entry_float - 273.15) * 1.8 + 32

                # to Celsius
                else:
                    temperature = (entry_float - 273.15)

            output = f'{round(temperature, 2)}{temp_to}'
            output_label.configure(text=output)


    @staticmethod
    def check_input(input_value, acceptable_str):
        if input_value == acceptable_str:
            return True
        else:
            try:
                float(input_value)
                return True
            except ValueError:
                return False


def main():

    root = Tk()
    TemperatureConverter(root)
    root.mainloop()


if __name__ == '__main__':
    main()
