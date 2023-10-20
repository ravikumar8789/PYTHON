import tkinter as tk
from tkinter import ttk 


win= tk.Tk()

win.title('Welcome')

labels=['name : ', 'age : ', 'coountry :', 'address : ', 'subscribed : ', 'roll :']

for i in range(len(labels)):
    current_label= 'label'+str(i)
    current_label=ttk.Label(win, text=labels[i]).grid(row=i, column=0, sticky=tk.W, padx=20, pady=0)



dict_user={
    'name': tk.StringVar(),
    'age':tk.StringVar(),
    'country':tk.StringVar(),
    'address':tk.StringVar(),
    'subscribed':tk.StringVar(),
    'roll':tk.StringVar()
}
count=0
for i in dict_user:
    current_entrybox= 'entry'+i
    current_entrybox=ttk.Entry(win,width=16, textvariable=dict_user[i]).grid(row=count,column=1, padx=20, pady=0)
    count+=1


def submit_button():
    for i in dict_user:
        print(dict_user.get(i).get())
        # print(dict_user[i].get())
    # print(dict_user['name'].get())

ttk.Button(win, text='submit',command=submit_button).grid(row=6, column=0)


win.mainloop()