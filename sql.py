import sqlite3
from tkinter import ttk

import tkinter as tk
  
# Connection with the DataBase
# 'library.db'
connection = sqlite3.connect("library.db")
crsr = connection.cursor()


crsr.executescript("""

create table if not exists account
(
account_number char(5) not null primary key,
branch_name varchar(10),
balance double
);
create table if not exists branch
(
branch_name varchar(10) not null primary key,
branch_city varchar(10),
assets double
);
create table if not exists customer
(
customer_name varchar(20) not null primary key,
customer_street varchar(20),
customer_city varchar(10)
);
create table if not exists loan
(
loan_number varchar(5) not null primary key,
branch_name varchar(10),
amount double
);
create table if not exists borrower
(
customer_name varchar(20) not null,
loan_number varchar(5) not null,
primary key(customer_name, loan_number)
);
create table if not exists depositor
(
customer_name varchar(20) not null,
account_number char(5) not null,
primary key(customer_name, account_number)
);
create table if not exists employee
(
employee_name varchar(20) not null,
branch_name varchar(10) not null,
salary double,
primary key(employee_name,branch_name)
);

insert or ignore into account values('A-101', 'Downtown', 500);
insert or ignore into account values('A-102', 'Perryridge', 400);
insert or ignore into account values('A-201', 'Brighton', 900);
insert or ignore into account values('A-215', 'Mianus', 700);
insert or ignore into account values('A-217', 'Brighton', 750);
insert or ignore into account values('A-222', 'Redwood', 700);
insert or ignore into account values('A-305', 'Round Hill', 350);
insert or ignore into branch values('Brighton', 'Brooklyn', 7100000);
insert or ignore into branch values('Downtown', 'Brooklyn', 9000000);
insert or ignore into branch values('Mianus', 'Horseneck', 400000);
insert or ignore into branch values('North Town', 'Rye', 3700000);
insert or ignore into branch values('Perryridge', 'Horseneck', 1700000);
insert or ignore into branch values('Pownal', 'Bennington', 300000);
insert or ignore into branch values('Redwood', 'Palo Alto', 2100000);
insert or ignore into branch values('Round Hill', 'Horseneck', 8000000);
insert or ignore into customer values('Adams', 'Spring', 'Pittsfield');
insert or ignore into customer values('Brooks', 'Senator', 'Brooklyn');
insert or ignore into customer values('Curry', 'North', 'Rye');
insert or ignore into customer values('Glenn', 'Sand Hill', 'Woodside');
insert or ignore into customer values('Green', 'Walnut', 'Stamford');
insert or ignore into customer values('Hayes', 'Main', 'Harrison');
insert or ignore into customer values('Johnson', 'Alma', 'Palo Alto');
insert or ignore into customer values('Jones', 'Main', 'Harrison');
insert or ignore into customer values('Lindsay', 'Park', 'Pittsfield');
insert or ignore into customer values('Smith', 'North', 'Rye');
insert or ignore into customer values('Turner', 'Putnam', 'Stamford');
insert or ignore into customer values('Williams', 'Nassau', 'Princeton');
insert or ignore into depositor values('Hayes', 'A-102');
insert or ignore into depositor values('Johnson', 'A-102');
insert or ignore into depositor values('Johnson', 'A-201');
insert or ignore into depositor values('Jones', 'A-217');
insert or ignore into depositor values('Lindsay', 'A-222');
insert or ignore into depositor values('Smith', 'A-215');
insert or ignore into depositor values('Turner', 'A-305');
insert or ignore into loan values('L-11', 'Round Hill', 900);
insert or ignore into loan values('L-14', 'Downtown', 1500);
insert or ignore into loan values('L-15', 'Perryridge', 1500);
insert or ignore into loan values('L-16', 'Perryridge', 1300);
insert or ignore into loan values('L-17', 'Downtown', 1000);
insert or ignore into loan values('L-23', 'Redwood', 2000);
insert or ignore into loan values('l-93', 'Mianus', 500);
insert or ignore into borrower values('Adams', 'L-16');
insert or ignore into borrower values('Curry', 'L-93');
insert or ignore into borrower values('Hayes', 'L-15');
insert or ignore into borrower values('Jackson', 'L-14');
insert or ignore into borrower values('Jones', 'L-17');
insert or ignore into borrower values('Smith', 'L-11');
insert or ignore into borrower values('Smith', 'L-23');
insert or ignore into borrower values('Williams', 'L-17');
insert or ignore into employee values('Adams', 'Perryridge', 1500);
insert or ignore into employee values('Brown', 'Perryridge', 1300);
insert or ignore into employee values('Gopal', 'Perryridge', 5300);
insert or ignore into employee values('Johnson', 'Downtown', 1500);
insert or ignore into employee values('Loreena', 'Downtown', 1300);
insert or ignore into employee values('Peterson', 'Downtown', 2500);
insert or ignore into employee values('Rao', 'Austin', 1500);
insert or ignore into employee values('Sato', 'Austin', 1600);
""")



crsr.execute("SELECT * FROM customer;")
  
# store all the fetched data in the ans variable
ans = crsr.fetchall()
  

for i in ans:
    print(i)

connection.commit()



crsr.execute("select depositor.customer_name, account.account_number, balance from depositor, account where depositor.account_number = account.account_number and balance <= 400;")
  
# store all the fetched data in the ans variable
ans = crsr.fetchall()
  

for i in ans:
    print(i)

connection.commit()





def View():

    
    naam = []
    naam.append(lps.get())
    print(naam[0])


    if naam[0] == 'Bank details':
         root = tk.Tk()
         tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
         root.title('Bank Details')
         tree.column("#1", anchor=tk.CENTER)
         tree.heading("#1", text="Branch Name")
         tree.column("#2", anchor=tk.CENTER)
         tree.heading("#2", text="Branch City")
         tree.column("#3", anchor=tk.CENTER)
         tree.heading("#3", text="Assets")
         tree.pack()
 
    if naam[0] == 'Customer details':
        root = tk.Tk()
        tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
        root.title('Customer Details')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Customer Name")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Customer Street")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Customer City")
        tree.pack()
    if naam[0] == 'Loan details':
        root = tk.Tk()
        tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
        root.title('Loan Details')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Loan Number")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Branch Name")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Ammount")
        tree.pack()
    if naam[0] == 'Empolyee details':
        root = tk.Tk()
        tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
        root.title('Employee Details')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Employee Name")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Branch")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Salary")
        tree.pack()

    r1 = crsr.fetchall()
    print(r1)


 


   

    if naam[0] == 'Bank details':
        crsr.execute("SELECT * FROM branch;")
    if naam[0] == 'Customer details':
        crsr.execute("SELECT * FROM customer;")
    if naam[0] == 'Loan details':
        crsr.execute("SELECT * FROM loan;")
    if naam[0] == 'Empolyee details':
        crsr.execute("SELECT * FROM employee;")
   



        
    rows = crsr.fetchall()

    ele = []

    for row in rows:
        ele.append(row)
    print(ele[0][0])

    for i in ele:
        tree.insert("", tk.END, values=(i[0],i[1],i[2]))
 

    root.mainloop()

# GUI

#imports Libraries
from tkinter import *
import os
import image
from tkinter import Entry, IntVar, Tk
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter.ttk import Combobox

from PIL import Image, ImageTk




#Main Screen of GUI
master = Tk()
master.title('Bank Management System')



#img = PhotoImage(file = "SBI.png")

img = Image.open("SBI-1.png")
img = img.resize((550, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(img)

img1 = Image.open("SBI-YONO.jpg")
img1 = img1.resize((500, 200), Image.ANTIALIAS)
render1 = ImageTk.PhotoImage(img1)

img2 = Image.open("Risk.jpg")
img2 = img2.resize((505, 200), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(img2)

def f_1():

    crit = lps4.get()
    val = entry3.get()

    disp.delete('1.0', END)
    disp.insert(INSERT,'Name, Account Numbers, and Balance are: \n')

    if crit == 'Less than':
        s1 = "select depositor.customer_name, account.account_number, balance from depositor, account where depositor.account_number = account.account_number and balance <"
        s2 = str(val)
        s3 = s1 + s2
        crsr.execute(s3)


    if crit == 'More than':
        s1 = "select depositor.customer_name, account.account_number, balance from depositor, account where depositor.account_number = account.account_number and balance >"
        s2 = str(val)
        s3 = s1 + s2
        crsr.execute(s3)


    if crit == 'Equal to':
        s1 = "select depositor.customer_name, account.account_number, balance from depositor, account where depositor.account_number = account.account_number and balance ="
        s2 = str(val)
        s3 = s1 + s2
        crsr.execute(s3)

    rows = crsr.fetchall()

    ele = []

    for row in rows:
        ele.append(row)
    print(ele[0][0])

    for i in ele:
        disp.insert(INSERT, i)
        disp.insert(INSERT, '\n')


def f_2():

    crit = lps2.get()
   

    disp.delete('1.0', END)
    disp.insert(INSERT,'Name of Customers whose city' + ' '+  crit + ' '+'are :' + '\n')
    s1 = "select customer_name from customer where customer_city =  "
    s2 = str(crit)
    s3 = s1 + '"' + s2 + '"'
    crsr.execute(s3)


    rows = crsr.fetchall()

    ele = []

    for row in rows:
        ele.append(row)
    print(ele[0][0])

    for i in ele:
        disp.insert(INSERT, i)
        disp.insert(INSERT, '\n')


def f_3():

    
    disp.delete('1.0', END)
    disp.insert(INSERT,'Account Number, Branch Name, and Branch City are :' + '\n')

    crsr.execute("select account_number, branch.branch_name, branch_city from account, branch where account.branch_name=branch.branch_name;")


    rows = crsr.fetchall()

    ele = []

    for row in rows:
        ele.append(row)
    print(ele[0][0])

    for i in ele:
        disp.insert(INSERT, i)
        disp.insert(INSERT, '\n')

        
def f_4():

    val1 = entry4.get()
    val2 = entry2.get()

    disp.delete('1.0', END)
    disp.insert(INSERT,'name of all branches with assets between are : \n')
    s1 = "select branch_name from branch where assets between"
    s2 = str(val1)
    s3 = str(val2)
    s4 = s1 + ' ' + s2 + ' ' + 'and' + ' ' + s3
    crsr.execute(s4)


    rows = crsr.fetchall()

    ele = []

    for row in rows:
        ele.append(row)
    print(ele)

    if len(ele) == 0:
        disp.insert(INSERT, 'None')
    for i in ele:
        disp.insert(INSERT, i)
        disp.insert(INSERT, '\n')

 
def f_5():

    crit = lps1.get()
    val = entry1.get()

    disp.delete('1.0', END)
    disp.insert(INSERT,'Account Numbers are : \n')

    if crit == 'Less than':
        s1 = "select account_number from account where balance <"
        s2 = str(val)
        s3 = s1 + s2
        crsr.execute(s3)

    if crit == 'More than':
        s1 = "select account_number from account where balance >"
        s2 = str(val)
        s3 = s1 + s2
        crsr.execute(s3)


    if crit == 'Equal to':
        s1 = "select account_number from account where balance ="
        s2 = str(val)
        s3 = s1 + s2
        crsr.execute(s3)

    rows = crsr.fetchall()

    ele = []

    for row in rows:
        ele.append(row)
    print(ele[0][0])

    for i in ele:
        disp.insert(INSERT, i)
        disp.insert(INSERT, '\n')
        
master.configure(bg='#65A8E1')
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#DCDCDC", background= "#DCDCDC",borderwidth=2.5,relief="solid")

Label(master, text = "State Bank of India", font =('Calibri',30) ,bg='#65A8E1', borderwidth=3,relief="solid").place(x=600, y=10)
#Label(master, text = "SBI is the most secure bank you've probably used", font=('Calibri',12),bg='#65A8E1').place(x =700, y = 40)
Label(master, image= render1).place(x =15,y = 90 )

Label(master, image= render).place(x =483,y = 90 )
Label(master, image= render2).place(x =1000,y = 90 )

Label(master, text = "Select Features & Perform Querries", font =('Calibri',14) ,bg='#65A8E1',borderwidth=0.5,relief="solid").place(x=30, y=310)

Label(master, text = "Display ", font =('Calibri',14) ,bg='#65A8E1',borderwidth=0.5,relief="solid").place(x=150, y=370)


c = Canvas(master)

c.create_line(15, 280, 1200, 280)

lps = ttk.Combobox(master, width = 27)
  
B_LPS = ['Bank details','Customer details','Loan details', 'Empolyee details','Deposit details']

# Adding combobox drop down list
lps['values'] = B_LPS

lps.place(x= 230, y= 375)
lps.current()


# Find the name, account number, and balance of all customers who have an account with a balance of $400 or less.


Label(master, text = "Find the name, account number, and balance of all customers who have an account with a balance", borderwidth=0.5,relief="solid",font =('Calibri',14),bg='#65A8E1' ).place(x=150, y=458)
lps4 = ttk.Combobox(master, width = 12)
Cr4 = ['Less than','More than','Equal to']
lps4['values'] = Cr4
lps4.place(x= 920, y= 460)
lps4.current()
entry3 = tk.Entry(master,width = 15, bg='#DCDCDC')
entry3.place(x= 1030, y= 460)
button6 = tk.Button(text="Show", width = 6,command=f_1,bg='blue',borderwidth=2,relief="solid")
button6.place(x = 1130, y =457)



# Find all name of customers whose city is in Brooklyn

Label(master, text = "Find all name of customers whose city is", font =('Calibri',14),bg='#65A8E1',borderwidth=0.5,relief="solid" ).place(x=150, y=510)
lps2 = ttk.Combobox(master, width = 12)
Cr2 = ['Pittsfield','Brooklyn','Rye','Woodside','Stamford','Harrison','Palo Alto','Harrison','Pittsfield','Rye','Stamford','Princeton']
lps2['values'] = Cr2
lps2.place(x= 490, y= 510)
lps2.current()
button3 = tk.Button(text="Show", width = 6,command=f_2,bg='blue',borderwidth=2,relief="solid")
button3.place(x = 600, y =508)




# Show all account_number, branch_name and corresponding branch_city

Label(master, text = "Show all account_number, branch_name and corresponding branch_city", font =('Calibri',14),bg='#65A8E1' ,borderwidth=0.5,relief="solid").place(x=150, y=560)
button4 = tk.Button(text="Show", width = 6,command=f_3,bg='blue',borderwidth=2,relief="solid")
button4.place(x = 720, y =560)


# Find the name of all branches with assets between one and four million dollars 

Label(master, text = "Find the name of all branches with assets between", font =('Calibri',14),bg='#65A8E1',borderwidth=0.5,relief="solid").place(x=150, y=610)
entry4 = tk.Entry(master,width = 10, bg='#DCDCDC')
entry4.place(x= 550, y= 612)
Label(master, text = "and", font =('Calibri',14) ,bg='#65A8E1',borderwidth=0.5,relief="solid").place(x=625, y=609)
entry2 = tk.Entry(master,width = 10, bg='#DCDCDC')
entry2.place(x= 667, y= 612)
button5 = tk.Button(text="Show", width = 6,command=f_4,bg='blue',borderwidth=2,relief="solid")
button5.place(x = 760, y =608)


# Account whose balance less than given value

Label(master, text = "Display all the accounts whose balance is", font =('Calibri',14) , bg='#65A8E1',borderwidth=0.5,relief="solid").place(x=150, y=658)
lps1 = ttk.Combobox(master, width = 12)
Cr1 = ['Less than','More than','Equal to']
lps1['values'] = Cr1
lps1.place(x= 490, y= 658)
lps1.current()
entry1 = tk.Entry(master,width = 10, bg='#DCDCDC')
entry1.place(x= 600, y= 658)
button2 = tk.Button(text="Show", width = 6,command=f_5,bg='blue',borderwidth=2,relief="solid")
button2.place(x = 690, y =658)



button3 = tk.Button(text="Add Values in Tables", width =  30,bg='blue',borderwidth=2,relief="solid")
button3.place(x = 600, y =370)

button4 = tk.Button(text="Delete Values in Table", width =  30,bg='blue',borderwidth=2,relief="solid")
button4.place(x = 850, y =370)

button5 = tk.Button(text="Update Values in Table", width= 30,bg='blue',borderwidth=2,relief="solid")
button5.place(x = 1100, y =370)


# Main text box to display put
disp =  Text(master, height = 10, width = 60,borderwidth=2.5,relief="solid", bg='#00B2EE')
disp.place(x=950,y = 530)

button1 = tk.Button(text="Display data", command=View, bg='blue',borderwidth=2,relief="solid")

button1.place(x = 450, y =373)

Label(master, text = "@Manage your bank with reliable services", font =('Calibri',20) , bg='#65A8E1').place(x=550, y=750)



master.mainloop()

connection.close()

