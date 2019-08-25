from Widgets.tk_widgets import *


class NameGenerator(object):

    def __init__(self, master=None):

        self.master = master

        self.master.geometry("300x340")
        self.master.resizable(0, 0)
        self.master.title("Heads or Tails")

        self.set_layout()

    def set_layout(self):

        mainframe = MyFrame(self.master)
        mainframe.pack(fill=BOTH, expand=1)

        coin_frame = MyFrame(mainframe, width=300, height=300)
        coin_frame.pack(fill=Y, expand=1)

        canvas = MyCanvas(coin_frame)
        canvas.pack(fill=BOTH)

        coin = Coin(canvas, 265, 250, 35, 20)

        btn_frame = MyFrame(mainframe)
        btn_frame.pack(fill=BOTH)

        btn_flip = MyButton(btn_frame, text='Flip the Coin!', width=30)
        btn_flip.configure(command=lambda button=btn_flip: self.flip_coin(coin))
        btn_flip.pack(fill=BOTH)

        close_app = MyButton(btn_frame, text='Quit', command=self.master.destroy, width=30)
        close_app.pack(fill=BOTH)

    def flip_coin(self, coin):

        coin.update_coin()


class Coin:

    def __init__(self, canvas, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.fill = config_layout['pressed']
        self.outline = config_layout['light_gray']

        self.canvas = canvas
        self.coin = canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                                       fill=self.fill, outline=self.outline, width=2)

        self.heads_tails = canvas.create_text((self.x1+self.x2)*0.5, (self.y1+self.y2)*0.5,
                                              text='Flip the Coin!', font='Times 25 bold')

    def update_coin(self):

        x1, y1, x2, y2 = self.canvas.coords(self.coin)

        if y1 < 100:
            y1 += 1
            y2 -= 1
            self.canvas.itemconfig(self.heads_tails, text='HEADS')
        else:
            y1 -= 1
            y2 += 1
            self.canvas.itemconfig(self.heads_tails, text='TAILS')

        self.canvas.coords(self.coin, x1, y1, x2, y2)


def main():

    root = Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
