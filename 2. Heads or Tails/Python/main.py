from Widgets.tk_widgets import *


class NameGenerator:

    def __init__(self, master=None):

        self.master = master

        self.master.geometry("500x500")
        self.master.resizable(0, 0)
        self.master.title("Heads or Tails")


def main():

    root = Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
