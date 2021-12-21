import calendar
from datetime import datetime
from tkinter import *
from tkinter import ttk

from config import *


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


class MyEntry(Entry):

    def __init__(self, master, placeholder='Placeholder', **kw):

        Entry.__init__(self, master=master, **kw)

        self.placeholder = placeholder
        self.default_fg = self['foreground']
        self.placeholder_fg = 'grey'

        self.insert(0, self.placeholder)
        self['foreground'] = self.placeholder_fg

        self.bind("<Button-1>", self.click)
        self.bind("<FocusOut>", self.focus_out)

    def click(self, *args):
        if self.get() == self.placeholder:
            self.delete(0, 'end')
            self['foreground'] = self.default_fg

    def focus_out(self, *args):
        if not len(self.get()):
            self.delete(0, 'end')
            self.insert(0, self.placeholder)
            self['foreground'] = self.placeholder_fg


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
        self['font'] = ('Bold', 12)


class MyRadioButton(Radiobutton):

    def __init__(self, master, **kw):

        Radiobutton.__init__(self, master=master, **kw)

        self.set_settings()

        self.defaultBackground = self['background']

        self.bind('<Enter>', self.hover_on)
        self.bind('<Leave>', self.hover_off)

    def set_settings(self):
        self['activebackground'] = config_layout['pressed']
        self['activeforeground'] = config_layout['dark_blue']

        self['selectcolor'] = config_layout['pressed']

        self['background'] = config_layout['dark_blue']
        self['foreground'] = config_layout['light_gray']

    def hover_on(self, _):
        self['background'] = config_layout['hover_on']

    def hover_off(self, _):
        self['background'] = self.defaultBackground


class MyCombobox(ttk.Combobox):

    def __init__(self, master, menu_values, **kw):

        ttk.Combobox.__init__(self, master=master, **kw)
        self.set_settings()
        self['values'] = menu_values
        self.bind('<<ComboboxSelected>>', self.combobox_selected)

    def set_settings(self):

        self['justify'] = CENTER
        self['background'] = config_layout['dark_blue']
        self['foreground'] = config_layout['dark_blue']

    def combobox_selected(self, _):
        self.set(self.get())


class DayCheckbox(MyCombobox):

    def __init__(self, master, cb_month, cb_year, **kw):
        MyCombobox.__init__(self, master=master, **kw)
        self.month = cb_month
        self.year = cb_year

    def refresh(self):
        if all([len(self.month.get()), len(self.year.get())]):
            month = datetime.strptime(self.month.get(), "%B").month
            self['values'] = [d for d in range(1, calendar.monthrange(int(self.year.get()), month)[1] + 1)]
            self.current(0)


class MyLabelFrame(LabelFrame):

    def __init__(self, master, **kw):

        LabelFrame.__init__(self, master=master, **kw)

        self.set_settings()

    def set_settings(self):

        self['background'] = config_layout['dark_blue']


class MyCanvas(Canvas):

    def __init__(self, master, **kw):

        Canvas.__init__(self, master=master, **kw)

        self.set_settings()

    def set_settings(self):

        self['background'] = config_layout['dark_blue']
