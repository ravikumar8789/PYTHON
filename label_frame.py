from tkinter import ttk
import tkinter  as tk

win= tk.Tk()
win.title('Labeled Window')

label_frame= ttk.LabelFrame(win, text='Enter your details below ',)
label_frame.grid(row=0, column=0, padx=20)

labels=['name', 'age', 'Country', 'roll']

for i in range(len(labels)):
    current_label = 'label'+str(i)
    current_label= ttk.Label(label_frame, text=labels[i]).grid(row=i, column=0, sticky=tk.W, padx=2, pady=2)



dict_user={
    'name': tk.StringVar(),
    'age':tk.StringVar(),
    'country':tk.StringVar(),
    'roll':tk.StringVar(),
}
count=0
for i in dict_user:
    current_entrybox= 'entry'+i
    current_entrybox=ttk.Entry(label_frame,width=16, textvariable=dict_user[i]).grid(row=count,column=1, padx=2, pady=2)
    count+=1

def submit_btn():
    pass
submit_button= ttk.Button(label_frame, text='submit', command=submit_btn, width=16).grid(row=5, column=1,)

win.mainloop()