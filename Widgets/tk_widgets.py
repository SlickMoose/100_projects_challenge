from tkinter import *
from config import *
from tkinter import ttk


class MyButton(Button):

    def __init__(self, master, **kw):

        Button.__init__(self, master=master, **kw)

        self.set_settings()

        self.defaultBackground = self['background']

        self.bind('<Enter>', self.hover_on)
        self.bind('<Leave>', self.hover_off)

    def set_settings(self):

        self['activebackground'] = config_layout['pressed']
        self['activeforeground'] = config_layout['light_gray']

        self['background'] = config_layout['dark_blue']
        self['foreground'] = config_layout['light_gray']

    def hover_on(self, _):
        self['background'] = config_layout['hover_on']

    def hover_off(self, _):
        self['background'] = self.defaultBackground


class MyCheckbox(Checkbutton):

    def __init__(self, master, **kw):

        Checkbutton.__init__(self, master=master, **kw)

        self.defaultBackground = self['background']

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['highlightcolor']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class MyFrame(Frame):

    def __init__(self, master, **kw):

        Frame.__init__(self, master=master, **kw)

        self.set_settings()

    def set_settings(self):

        self['background'] = config_layout['dark_blue']


class MyLabel(Label):

    def __init__(self, master, **kw):

        Label.__init__(self, master=master, **kw)

        self.set_settings()

    def set_settings(self):

        self['background'] = config_layout['dark_blue']
        self['foreground'] = config_layout['light_gray']
        self['font'] = ('Bold', 15)


class MyRadioButton(Radiobutton):

    def __init__(self, master, **kw):

        Radiobutton.__init__(self, master=master, **kw)

        self.defaultBackground = self['background']

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['highlightcolor']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class MyCombobox(ttk.Combobox):

    def __init__(self, master, menu_values, **kw):

        ttk.Combobox.__init__(self, master=master, **kw)

        self.set_settings()

        self.cb_value = StringVar()

        self['values'] = menu_values
        self.current(0)

        self.bind('<<ComboboxSelected>>', self.combobox_selected)

    def set_settings(self):

        self['justify'] = CENTER
        self['background'] = config_layout['dark_blue']
        self['foreground'] = config_layout['light_gray']

    def combobox_selected(self, _):

        self['textvariable'] = self.cb_value.get()


class MyLabelFrame(LabelFrame):

    def __init__(self, master, **kw):

        LabelFrame.__init__(self, master=master, **kw)

        self.set_settings()

    def set_settings(self):

        self['background'] = config_layout['dark_blue']
