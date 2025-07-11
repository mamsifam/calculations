from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox 
import pandas as pd

window = tk.Tk()
window.geometry('800x500')
window.title('School Mark Sheet')
window.config(bg='light blue')

global id
id=1
def input():
    first =strigvar.get()
    last =strigvar2.get()
    email=strigvar3.get()
    total=+int(last)+int(email)
    average=total/2
    print(total)
    print(average)
    
    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
    global id 
    table.insert(parent='',index=END,text='',values=( id,first,last,email,total,average))
    print(id,first,last,email)
    id+=1
   

    sql="insert into students (name,maths,science,total,average) values (%s,%s,%s,%s,%s)"
    value=(first,last,email,total,average)
    mysql.execute(sql,value)
    con.commit()
    con.close()
    print('Insert succesfully!')
    messagebox.showinfo('message','Insert Succesfully !')
    entryid.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def delete_all():
    records=table.get_children()
    for record in records:
        table.delete(record)

    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
    sql='truncate table students'
    mysql.execute(sql)
    con.commit()
    con.close()
    messagebox.YESNO("Warrning!",'This will erase all the data')

def delete():

    
    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
    x=table.selection()[0]
    print(table.item(x)['values'])
    sid=table.item(x)['values'][0]
    print(sid)
    table.delete(x)
    entryid.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    
    print(x)
    sql="delete from students where id=%s"
    id=(x)
    mysql.execute(sql,sid)
  
    con.commit()
    con.close()
    print('Delete Succesfully !!')
    
    
count=0
def show_records():
    datas=table.get_children()
    for data in datas:
        table.delete(data)

    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
    
    global count
    sql="select *from students"
    mysql.execute(sql)
    records=mysql.fetchall()
    for record in records:
        if count %2==0:
            table.insert(parent='',text='',index='end',iid=count,values=(record),tags='evenrow')
            print(record)
        else:
            table.insert(parent='',text='',index='end',iid=count,values=(record),tags='oddrow')
            print(record)
        count+=1

    con.commit()
    con.close()

def select():
    entryid.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    selected=table.focus()
    value=table.item(selected,'values')
    entryid.insert(0,value[0])
    entry.insert(0,value[1])
    entry2.insert(0,value[2])
    entry3.insert(0,value[3])

def update():
    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
   
    selected=table.focus()
    value=table.item(selected,text='',values=(entryid.get(),entry.get(),entry2.get(),entry3.get()))
    i=entryid.get()
    n=entry.get()
    s=entry2.get()
    m=entry3.get()
    sql='update students set id=%s,name=%s,science=%s,maths=%s where id=%s'
    values=(i,n,s,m,i)
    mysql.execute(sql,values)
    con.commit()
    con.close()
    entryid.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def decending():
    records=table.get_children()
    for record in records:
        table.delete(record)
    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
    sql='select *from students order by total DESC'
    mysql.execute(sql)
   
    datas=mysql.fetchall()
    for data in datas:
        table.insert(parent='',text='',index='end',values=(data))
        

    
def decending_science():
    records=table.get_children()
    for record in records:
        table.delete(record)
    con =pymysql.connect(host='localhost',user='root',password='Mamsifam1',database='school')
    mysql=con.cursor()
    sql='select *from students order by science DESC'
    mysql.execute(sql)
    global count
   
    datas=mysql.fetchall()
    for data in datas:
        
        if count %2==0:
            table.insert(parent='',text='',index='end',iid=count,values=(data),tags='evenrow')
        
        else:
            table.insert(parent='',text='',index='end',iid=count,values=(data),tags='oddrow')
            
        count+=1

# Saving file
    save_stuf=open('save_text','w')
    save_stuf.writelines(str(datas))
    save_stuf.close()

    panda_save=pd.DataFrame(datas,columns=['ID','Name','Maths','Science','Total','Average'])
    panda_save.to_excel('save_exel_science.xlsx','sheet 1')
    print(panda_save)    
    
def print_previw():
    top=Toplevel() 
    top.geometry('300x100')

    top.config(background='white')
    l=tk.Label(top,text='--------- Printpreview-----------')
    l.pack()


#create lable frame
lab_frame=tk.Frame(window,borderwidth=5,relief="groove",bg='lightblue')
lab_frame.grid(row=5,column=5)

labele_id =tk.Label(window,text='ID',bg='light blue',pady=10,padx=10).place(x=10,y=20)
labele =tk.Label(window,text='Name',bg='light blue').place(x=10,y=50)
labele2 =tk.Label(window,text='Maths',bg='light blue').place(x=10,y=80)
labele3 =tk.Label(window,text='Science',bg='light blue').place(x=10,y=110)

strigvar=tk.StringVar()
strigvar2=tk.StringVar()
strigvar3=tk.StringVar()
entryid=tk.Entry(window)
entry =tk.Entry(window,textvariable=strigvar)
entry2 =tk.Entry(window,textvariable=strigvar2)
entry3 =tk.Entry(window,textvariable=strigvar3)
entryid.place(x=80,y=20)
entry.place(x=80,y=50)
entry2.place(x=80,y=80)
entry3.place(x=80,y=110)

button=tk.Button(window,text='Input',command=input,width=9,height=1)
button.place(x=80,y=150)
button2=tk.Button(window,text='Delete All',command=delete_all,width=9,height=1)
button2.place(x=220,y=150)
button3=tk.Button(window,text='Delete',command=delete,width=9,height=1)
button3.place(x=150,y=150)
button4=tk.Button(window,text='Show',command=show_records,width=9,height=1)
button4.place(x=290,y=150)
button5=tk.Button(window,text='select',command=select,width=9,height=1)
button5.place(x=360,y=150)
button6=tk.Button(window,text='Update',command=update,width=9,height=1)
button6.place(x=430,y=150)
button_print=tk.Button(window,text='Print all',command=print_previw,width=9,height=1,bg='orange')
button_print.place(x=430,y=50)
#Decending frame
frame_decend=tk.Frame(window,borderwidth=5,relief='groove')
frame_decend.place(x=430,y=20)

#creat decending button
button_dcecen=tk.Button(window,text='A - Z',command=decending,width=9,height=1,bg='lightgreen')
button_dcecen.place(x=430,y=20)
button_dcecen=tk.Button(window,text='A-Z science',command=decending_science,bg='lightgreen',width=9,height=1)
button_dcecen.place(x=430,y=50)

#create treeview fframe
tree_frame =Frame(window,borderwidth=20,relief='raised')
tree_frame.place(y=180)

#treeview scrolbar
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)


table =ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,columns=('id','name','maths','science','total','average'),show=('headings'))

table.heading('id',text='Id',anchor='center')
table.heading('name', text='Name')
table.heading('maths', text='Maths',anchor='center')
table.heading('science', text='Science',anchor='center')
table.heading('total',text='Total')
table.heading('average',text='Average')
table.pack()

#configure the scrollbar
tree_scroll.config(command=table.yview)

#Hedding boder
style=ttk.Style()
style.theme_use("clam")

#create stripped tag
table.tag_configure('oddrow',background='white')
table.tag_configure('evenrow',background='yellow')




#table.insert(parent="",index=0,values=(2,'Jhone','Deo','jhonedeo@gmail,com'))
#table.insert(parent="",index=0,values=(1,'Aravinda','Silva','aravinda@gmail,com'))
#table.insert(parent="",index=0,values=(data,data2,data3))

window.mainloop()