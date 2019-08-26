from Widgets.tk_widgets import *
import random


class NameGenerator(object):

    def __init__(self, master=None):

        self.master = master

        self.master.geometry("300x340")
        self.master.resizable(0, 0)
        self.master.title("Heads or Tails")

        self.coin = None
        self.set_layout()

    def set_layout(self):

        mainframe = MyFrame(self.master)
        mainframe.pack(fill=BOTH, expand=1)

        coin_frame = MyFrame(mainframe, width=300, height=300)
        coin_frame.pack(fill=Y, expand=1)

        canvas = MyCanvas(coin_frame)
        canvas.pack(fill=BOTH)

        btn_frame = MyFrame(mainframe)
        btn_frame.pack(fill=BOTH)

        btn_flip = MyButton(btn_frame, text='Flip the Coin!', width=30)
        btn_flip.configure(command=lambda button=btn_flip: self.flip_coin(btn_flip))
        btn_flip.pack(fill=BOTH)

        close_app = MyButton(btn_frame, text='Quit', command=self.master.destroy, width=30)
        close_app.pack(fill=BOTH)

        self.coin = Coin(canvas, btn_flip, 265, 250, 35, 20)

    def flip_coin(self, btn_flip):

        btn_flip.configure(state=DISABLED)

        self.coin.canvas.coords(self.coin.coin,
                                self.coin.default_x1, self.coin.default_y1, self.coin.default_x2, self.coin.default_y2)

        self.coin.repeat_count = 1
        self.coin.repeat = random.randrange(5, 10)
        self.coin.update_coin()


class Coin:

    def __init__(self, canvas, btn_flip, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.default_x1 = x1
        self.default_y1 = y1
        self.default_x2 = x2
        self.default_y2 = y2

        self.callback = None
        self.btn_flip = btn_flip

        self.repeat = 5
        self.repeat_count = 1
        self.interval = 10
        self.flip = ['HEADS', 'TAILS']
        self.flip_int = 1
        self.outline_width = 2
        self.width_interval = 0.20

        self.fill = config_layout['pressed']
        self.outline = config_layout['light_gray']

        self.canvas = canvas
        self.coin = canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                                       fill=self.fill, outline=self.outline, width=self.outline_width)

        self.heads_tails = canvas.create_text((self.x1+self.x2)*0.5, (self.y1+self.y2)*0.5,
                                              text='Flip the Coin!', font='Times 25 bold')

    def update_coin(self):

        self.x2, self.y2, self.x1, self.y1 = self.canvas.coords(self.coin)

        if self.y2 > 120:
            self.interval *= -1
            self.flip_int = int(not self.flip_int)
            self.width_interval *= -1
            self.canvas.itemconfig(self.heads_tails, text=self.flip[self.flip_int])

        if self.y2 < 20:
            self.width_interval *= -1
            self.interval *= -1
            self.repeat_count += 1

        self.y2 += self.interval
        self.y1 -= self.interval
        self.outline_width += self.width_interval

        self.canvas.coords(self.coin, self.x1, self.y1, self.x2, self.y2)
        self.canvas.itemconfig(self.coin, width=self.outline_width)
        self.callback = self.canvas.after(30, self.update_coin)

        if self.repeat_count == self.repeat:
            self.btn_flip.configure(state=NORMAL)
            self.canvas.after_cancel(self.callback)


def main():

    root = Tk()

    _ = NameGenerator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
