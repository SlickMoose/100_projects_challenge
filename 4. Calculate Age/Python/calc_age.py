from tk_widgets import *
import threading
from time import sleep


class CalculateAgeApp:

    def __init__(self, master=None):

        self.master = master

        self.master.resizable(False, False)
        self.master.title("Calculate Age")
        self.master.geometry('350x300')

        self.thread_object = None
        self.stop_thread = True

        self.set_layout()

    def set_layout(self):

        day_str, month_str, year_str = StringVar(), StringVar(), StringVar()

        # master frame to occupy whole root space
        master_frame = MyFrame(master=self.master)
        master_frame.pack(fill=BOTH, expand=1)

        # label to display user output

        output_str = 'Your age equal to:\n'
        output_str = output_str + f'Months: 0\n'
        output_str = output_str + f'Days: 0\n'
        output_str = output_str + f'Hours: 0\n'
        output_str = output_str + f'Minutes: 0\n'
        output_str = output_str + f'Seconds: 0'

        output_label = MyLabel(master=master_frame)
        output_label.pack(fill=X)
        output_label.configure(text=output_str, font=('Bold', 10), padx=20, pady=20)

        # section for user input
        combobox_frame = MyFrame(master=master_frame)
        combobox_frame.pack(fill=X, padx=50)

        combobox_frame.grid_columnconfigure(0, weight=2)
        combobox_frame.grid_columnconfigure(1, weight=1)
        combobox_frame.grid_columnconfigure(2, weight=2)

        date_label = MyLabel(master=combobox_frame,
                             text='Select your date of birth:',
                             justify='center')
        date_label.grid(row=0, columnspan=3, sticky=NSEW)

        start_date = datetime(1900, 1, 1)
        current_date = datetime.now()

        # pick year of the birth

        years_list = [y for y in range(current_date.year + 1, start_date.year, -1)]
        cb_year = MyCombobox(master=combobox_frame,
                             menu_values=years_list,
                             textvariable=year_str,
                             state='readonly')

        cb_year.current(0)
        cb_year.grid(row=1, column=0)

        # pick month of the birth

        months_list = [datetime.strptime(str(m), "%m").strftime("%B") for m in range(1, 13)]
        cb_month = MyCombobox(master=combobox_frame,
                              menu_values=months_list,
                              textvariable=month_str,
                              state='readonly')

        cb_month.current(0)
        cb_month.grid(row=1, column=1)

        # pick day of the birth

        days_list = [d for d in range(1, 32)]
        cb_day = DayCheckbox(master=combobox_frame,
                             cb_month=cb_month,
                             cb_year=cb_year,
                             menu_values=days_list,
                             textvariable=day_str,
                             state='readonly')

        cb_day.current(0)
        cb_day.grid(row=1, column=2)

        # update days for leap years
        cb_year.bind('<<ComboboxSelected>>', lambda event: self.update_days(cb_day))
        cb_month.bind('<<ComboboxSelected>>', lambda event: self.update_days(cb_day))

        # button section
        btn_frame = MyFrame(master=master_frame)
        btn_frame.pack(pady=20)

        calc_button = MyButton(master=btn_frame, text='Calculate', width=30)
        calc_button.pack(fill=X, pady=5)
        calc_button.config(command=lambda button=calc_button: self.thread_start(cb_year.get(),
                                                                                cb_month.get(),
                                                                                cb_day.get(),
                                                                                output_label))

        exit_button = MyButton(master=btn_frame, text='Quit', command=self.close_app, width=30)
        exit_button.pack(fill=X, pady=5)

    def calculate(self, cb_year, cb_month, cb_day, output_label):

        while not self.stop_thread:

            year = int(cb_year)
            month = datetime.strptime(cb_month, "%B").month
            day = int(cb_day)

            current_date = datetime.now()
            user_date = datetime(year, month, day)
            diff = current_date - user_date
            total_seconds = diff.total_seconds()

            months_between_dates = (current_date.year - user_date.year) * 12 + (current_date.month - user_date.month)

            output_str = 'Your age equal to:\n'
            output_str = output_str + f'Months: {months_between_dates}\n'
            output_str = output_str + f'Days: {int(total_seconds/(60*60*24))}\n'
            output_str = output_str + f'Hours: {int(total_seconds/(60*60))}\n'
            output_str = output_str + f'Minutes: {int(total_seconds/60)}\n'
            output_str = output_str + f'Seconds: {int(total_seconds)}'

            output_label.configure(text=output_str)
            sleep(1)

    def close_app(self):
        # stop all active threads before closing app
        self.wait_thread_stop()
        self.master.destroy()

    def wait_thread_stop(self):
        self.stop_thread = True
        sleep(1)
        self.stop_thread = False

    def thread_start(self, cb_year, cb_month, cb_day, output_label):

        if all([len(cb_year), len(cb_month), len(cb_day)]):

            self.wait_thread_stop()
            self.thread_object = threading.Thread(target=self.calculate,
                                                  args=(cb_year, cb_month, cb_day, output_label,))
            self.thread_object.start()

    @staticmethod
    def update_days(cb_day):
        cb_day.refresh()


if __name__ == '__main__':

    root = Tk()
    CalculateAgeApp(root)
    root.mainloop()
