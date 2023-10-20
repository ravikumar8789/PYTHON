import tkinter as tk
from tkinter import ttk

win= tk.Tk()
win.title('Tab Widigt')

# notebook= ttk.Notebook(win, )
# page1= ttk.Frame(notebook)
# page2= ttk.Frame(notebook)

# notebook.add(page1, text='Page 1')
# notebook.add(page2, text='Page 2')
# notebook.grid(row=0, column=0)

nb= ttk.Notebook(win)
p1=ttk.Frame(nb)
p2= ttk.Frame(nb)

nb.add(p1, text='Page 1')
nb.add(p2, text='Page 2')

nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')


p1_label1= ttk.Label(p1, text='This is label for page 1 ')
p1_label1.grid(row=0, column=0)
p1_label1.configure(foreground='RED')

p1_label2= ttk.Label(p1, text='Enter your name : ')
p1_label2.grid(row=1, column=0, sticky=tk.W)
p1_entry2=ttk.Entry(p1)
p1_entry2.grid(row=1, column=1)

p2_label2= ttk.Label(p2, text='This is label for page 2')
p2_label2.grid(row=0, column=0)
p2_label2.configure(foreground='RED')
p2_label2= ttk.Label(p2, text='Enter your name : ')
p2_label2.grid(row=1, column=0, sticky=tk.W)
p2_entry2=ttk.Entry(p2)
p2_entry2.grid(row=1, column=1)




win.mainloop()