import tkinter as tk
from tkinter import ttk
import time

win= tk.Tk()
win.geometry('500x500')

label_frame=ttk.LabelFrame(win, text='Calculator',width=500)
label_frame.grid(row=0, column=0)
label_frame1=ttk.LabelFrame(win, text='', width=500)
label_frame1.grid(row=1, column=0)
def btn1():
    entry_var.set(entry_var.get()+'1')
def btn2():
    entry_var.set(entry_var.get()+'2')
def btn3():
    entry_var.set(entry_var.get()+'3')
def btn4():
    entry_var.set(entry_var.get()+'4')
def btn5():
    entry_var.set(entry_var.get()+'5')
def btn6():
   entry_var.set(entry_var.get()+'6')
def btn7():
    entry_var.set(entry_var.get()+'7')
def btn8():
   entry_var.set(entry_var.get()+'8')
def btn9():
   entry_var.set(entry_var.get()+'9')
def btn0():
   entry_var.set(entry_var.get()+'0')
def btnplus():
    entry_var.set(entry_var.get()+'+')
def btnx():
   entry_var.set(entry_var.get()+'x')
def btndvd():
   entry_var.set(entry_var.get()+'/')
def btnminus():
   entry_var.set(entry_var.get()+'-')

def btnequal():
    numbers=entry_var.get()
    elements= numbers.split(',')
    for i in elements:
        if i=='/':
            d=elements[i-1]//elements[i+1]
    for i in elements:
        if i=='x':
            m=
    print(elements)


def clear():
    entry_var.set('')



b1=tk.Button(label_frame1, text='1', width=7, height=4, command=btn1).grid(row=0, column=0)
b2=tk.Button(label_frame1, text='2', width=7, height=4, command=btn2).grid(row=0, column=1)
b3=tk.Button(label_frame1, text='3', width=7, height=4, command=btn3).grid(row=0, column=2)
b0=tk.Button(label_frame1, text='0', width=7, height=4, command=btn0).grid(row=0, column=3)
b4=tk.Button(label_frame1, text='4', width=7, height=4, command=btn4).grid(row=1, column=0)
b5=tk.Button(label_frame1, text='5', width=7, height=4, command=btn5).grid(row=1, column=1)
b6=tk.Button(label_frame1, text='6', width=7, height=4, command=btn6).grid(row=1, column=2)
bplus=tk.Button(label_frame1, text='+', width=7, height=4, command=btnplus).grid(row=1, column=3)
b7=tk.Button(label_frame1, text='7', width=7, height=4, command=btn7).grid(row=2, column=0)
b8=tk.Button(label_frame1, text='8', width=7, height=4, command=btn8).grid(row=2, column=1)
b9=tk.Button(label_frame1, text='9', width=7, height=4, command=btn9).grid(row=2, column=2)
bequal=tk.Button(label_frame1, text='=', width=7, height=4, command=btnequal).grid(row=2, column=3)
bdivide=tk.Button(label_frame1, text='/', width=7, height=4, command=btndvd).grid(row=3, column=0)
bx=tk.Button(label_frame1, text='X', width=7, height=4, command=btnx).grid(row=3, column=1)
bminus=tk.Button(label_frame1, text='-', width=7, height=4, command=btnminus).grid(row=3, column=2)
bequal=tk.Button(label_frame1, text=' ', width=7, height=4, command=btnequal).grid(row=3, column=3)
bclear= tk.Button(label_frame1, text='Clear', width=33, height=4, command=clear).grid(row=4, column=0, columnspan=4)

entry_var=tk.StringVar()
entrybox=ttk.Entry(label_frame, width=82,textvariable=entry_var)
entrybox.grid(row=0, column=0)
win.mainloop()