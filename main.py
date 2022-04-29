from datetime import datetime
from decimal import *
import tkinter
from tkinter import *
from tkinter import ttk

from forex_python.converter import CurrencyRates


class ConvertCurrency(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Pycurrency Converter")
        self.window.geometry("800x600")

        self.amount_label = Label(self.window, text="Amount", bg="pink")
        self.amount_label.place(x=100, y=200)
        self.amount_entry = tkinter.StringVar()
        self.amount_entry.set("0")
        self.amount = tkinter.Entry(self.window, textvariable=self.amount_entry)
        self.amount.place(x=100, y=230)

        self.base_currency_label = Label(self.window, text="Base currency", bg="pink")
        self.base_currency_label.place(x=300, y=200)
        self.currency = self.currencies()
        self.base_currency_var = tkinter.StringVar()
        self.currency_combobox = ttk.Combobox(self.window, width=20, textvariable=self.base_currency_var,
                                              state="readonly")
        self.currency_combobox["values"] = self.currency
        self.currency_combobox.place(x=300, y=230)

        self.dest_currency_label = Label(self.window, text="To", bg="pink")
        self.dest_currency_label.place(x=500, y=200)
        self.dest_currency_var = tkinter.StringVar()
        self.dest_currency_combobox = ttk.Combobox(self.window, width=20, textvariable=self.dest_currency_var,
                                                   state="readonly")
        self.dest_currency_combobox["values"] = self.currency
        self.dest_currency_combobox.place(x=500, y=230)

    def currencies(self):
        with open("currency_codes.txt") as file:
            currency_list = []
            lines = file.readlines()
            for line in lines:
                replaced_line = line.replace("\n", "").replace(",", "")
                currency_list.append(replaced_line)
            return currency_list

    def calculate_currency(self):
        now = datetime.now()
        currency = CurrencyRates(force_decimal=True)
        base = self.base_currency_var.get()[:3]
        dest = self.dest_currency_var.get()[:3]
        amount = int(self.amount_entry.get())
        converted_currency = currency.convert(base_cur=base, dest_cur=dest, amount=Decimal(amount),
                                              date_obj=now)
        return converted_currency

    def set_text(self, text):
        result_text.delete(0, END)
        result_text.insert(0, text)
        return


if __name__ == "__main__":
    window = ConvertCurrency()
    convert_btn = Button(text="CONVERT", bg="blue",
                         command=lambda: window.set_text(window.calculate_currency()))
    convert_btn.place(x=600, y=260)
    result_text = tkinter.Entry()
    result_text.place(x=500, y=300)

    window.window.mainloop()
