import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box


from csv import writer
win=tk.Tk()
win.title('Welcome')

#create labels
name_label=ttk.Label(win, text='Enter your name :')
name_label.grid(row=0, column=0, sticky=tk.W)
name_label.configure(foreground='Red')
name_var=tk.StringVar()
name=ttk.Entry(win, width=16, textvariable=name_var)
name.grid(row=0, column=1)
name.focus()



age_label=ttk.Label(win,text="Enter your age :")
age_label.grid(row=1, column=0, sticky=tk.W)
age_label.configure(foreground='Red')
age_var=tk.StringVar()
age_entry= ttk.Entry(win, width=16, textvariable=age_var)
age_entry.grid(row=1, column=1)

email_label=ttk.Label(win, text='Enter your email : ')
email_label.grid(row=2, column=0, sticky=tk.W)
email_label.configure(foreground='Red')
email_var= tk.StringVar()
email_entry= ttk.Entry(win, width=16, textvariable=email_var)
email_entry.grid(row=2,column=1)


address_label= tk.Label(win, text='Enter your address : ')
address_label.grid(row=3, column=0, sticky=tk.W)
address_label.configure(foreground='Red')
address_var=tk.StringVar()
address_entry= ttk.Entry(win, width=16, textvariable=address_var)
address_entry.grid(row=3, column=1)

# gender_label= ttk.Label(win, text='Select Gender : ')
# gender_label.grid(row=4,column=0,sticky=tk.W)
# gender_var= tk.StringVar()
# gender_combobox=ttk.Combobox(win, width=13, textvariable=gender_var, state='readonly')
# gender_combobox.grid(row=4, column=1)
# gender_combobox['values']=('Male', 'Female')
# gender_combobox.current(0)

gender_label=ttk.Label(win,text='Select Gender : ')
gender_label.grid(row=4, column=0, sticky=tk.W)
gender_label.configure(foreground='Red')
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win, width=16, textvariable=gender_var, state='readonly')
gender_combobox.grid(row=4, column=1)
gender_combobox['values']=('Male','Female')
gender_combobox.current(0)

# radio_label=ttk.Label(win, text='Select occupation : ')
# radio_label.grid(row=5, column=0, sticky=tk.W)
radio_var= tk.StringVar()
radio_button1= ttk.Radiobutton(win, text='Student', value='Student', variable=radio_var)
radio_button1.grid(row=5,column=0)
# radio_button1.configure(foreground='Blue')
radio_button2= ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=radio_var)
radio_button2.grid(row= 5, column=1)
# radio_button2.configure(foreground='Blue')





checkbutton_var=tk.IntVar()
check_button= ttk.Checkbutton(win, text='Subscribe to our blog to stay updated', variable=checkbutton_var)
check_button.grid(row=6, columnspan=3)
# check_button.configure(foreground='Blue')


Display_label= ttk.Label(win,text='')
Display_label.grid(row=7, columnspan=4, sticky=tk.W)




def action_button():
    with open('database.csv', 'a', newline='') as f:
        if checkbutton_var.get()==1:
            check_var='YES'
        else:
            check_var='NO'
        write_csv= writer(f)
        if len(name_var.get())==0 or len(age_var.get())==0 or len(email_var.get())==0 or len(address_var.get())==0 or len(gender_var.get())==0 or len(radio_var.get())==0:
            m_box.showwarning('Error', 'Please fill form correctly')
        else:   
            write_csv.writerow([name_var.get(), age_var.get(), email_var.get(),address_var.get(), gender_var.get(), radio_var.get(),check_var])
            Display_label= ttk.Label(win,text=f'Name: {name_var.get()}, Age: {age_var.get()}, Email: {email_var.get()}, Address: {address_var.get()}, Gender: {gender_var.get()}')
            Display_label.grid(row=7, columnspan=4, sticky=tk.W)
            m_box.showinfo('Sucessful', 'Your data has been saved sucessfully')
            
submit_button=ttk.Button(win, text='Submit', command=action_button)
submit_button.grid(row=8, column=0)

def exit():
    win.destroy()
Exit_button=ttk.Button(win,text='Exit', command=exit).grid(row=9, column=0)



def view_information():
    # win.destroy()
    win2=tk.Tk()
    win2.title('ENTERED INFORMATION')
    name_l=ttk.Label(win2, text='Name : '+name_var.get())
    name_l.grid(row=0, columnspan=3)
    age_l=ttk.Label(win2, text='Age : '+age_var.get())
    age_l.grid(row=1, columnspan=3)
    emai_l=ttk.Label(win2, text='Email : '+email_var.get())
    emai_l.grid(row=2, columnspan=3)
    address_l=ttk.Label(win2, text='Address : '+address_var.get())
    address_l.grid(row=3, columnspan=3)
    gender_l=ttk.Label(win2, text='Gender : '+gender_var.get())
    gender_l.grid(row=4, columnspan=3)
    radio_l=ttk.Label(win2, text='Occupation : '+radio_var.get())
    radio_l.grid(row=5, columnspan=3)
    def exit_view_information():
        win2.destroy()
    ttk.Button(win2, text='Exit', command=exit_view_information).grid(row=6, column=0)



view_button=ttk.Button(win, text='View Informations', command=view_information)
view_button.grid(row=8, column=1)

win.mainloop()
