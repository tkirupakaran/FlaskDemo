# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from random import random
from tkinter import messagebox, Tk


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def msgbox(txt):
    top = Tk()
    top.geometry("100x100")
    messagebox.showinfo("HI", txt)
    top.mainloop()


def CreateRndmNum():
    n = datetime.now()
    strNum = str(n)
    val = strNum.replace(" ", "").replace("-", "").replace(":", "").replace(".", "")
    return val
