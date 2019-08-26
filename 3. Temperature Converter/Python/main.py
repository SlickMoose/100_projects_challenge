from Widgets.tk_widgets import *


class TemperatureConverter:

    def __init__(self, master=None):

        self.master = master

        self.master.geometry("300x340")
        self.master.resizable(0, 0)
        self.master.title("Temperature Converter")

        self.set_layout()

    def set_layout(self):

        pass

    def convert(self):

        pass


def main():

    root = Tk()

    _ = TemperatureConverter(root)
    root.mainloop()


if __name__ == '__main__':
    main()
