import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import os

win= tk.Tk()
win.title('Menu Bar')
win.geometry('1400x700')
#=======================================================FUNCTIONS=======================================================
def pass1():
    m_box.showinfo('sucesful', 'You have clicked this button')


def exit():
    win.destroy()


def save():
    pass
def open():
    pass

def save_as():
    pass


#=======================================================FUNCTIONS=======================================================
main_menu=tk.Menu(win)
file_menu=tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=pass1)
file_menu.add_command(label='Save', command=save)
file_menu.add_command(label='Save as', command=pass1)
file_menu.add_command(label='Exit', command=exit)


edit_menu=tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=pass1)
edit_menu.add_command(label='Cut', command=pass1)
edit_menu.add_command(label='Copy', command=pass1)
edit_menu.add_command(label='Paste', command=pass1)
edit_menu.add_command(label='Delete', command=pass1)
edit_menu.add_command(label='Find', command=pass1)
edit_menu.add_command(label='Replace', command=pass1)



view_menu= tk.Menu(main_menu, tearoff=0)
view_menu.add_command(label='Zoom', command=pass1)
view_menu.add_command(label='Status bar Enabel', command=pass1)
view_menu.add_command(label='Run', command=pass1)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='View', menu=view_menu)
win.config(menu=main_menu)


win.mainloop()


