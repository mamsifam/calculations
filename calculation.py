
import tkinter as tk

window = tk.Tk()
window.title('CounTer')
window.geometry('800x500')
def button_fun():
    amount=int(entry1.get())
    amount2=int(entry2.get())
    total_amount=amount+ amount2
    string_var3.set(total_amount)
    print(total_amount)
   

string_var1=tk.StringVar()
label=tk.Label(window,text='value1')
label.pack(side='left')
entry1 =tk.Entry(window,textvariable=string_var1)
entry1.pack(side='left')

string_var2=tk.StringVar()
labe2=tk.Label(window,text='value2')
labe2.pack(side='left')
entry2 =tk.Entry(window,textvariable=string_var2)
entry2.pack(side='left')

button=tk.Button(window,text='plus button',command=button_fun)
button.pack(side='left')
string_var3=tk.StringVar(value='Total')
label3=tk.Label(window,text='Total',bg='red',textvariable=string_var3,font=('bold',23))
label3.pack(side='bottom')
window.mainloop()