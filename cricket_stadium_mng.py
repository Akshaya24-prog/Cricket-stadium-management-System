# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 19:26:10 2025

@author: HP
"""

# Using python version 3.11 64-bit , mysql-8.3.0

from tkinter import Tk, Button, Label, CENTER, X, BOTTOM, Entry, Y,RIGHT, END, Frame, Button , PhotoImage
import mysql.connector 
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as mb

# Create the main window
root = tk.Tk()
root.title("MySQL Connect Window")
root.geometry("700x500")
root.configure(bg="#2f2f55")  # Dark blue background

def connect_to_database():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        # Create a connection to the MySQL server
        con = mysql.connector.connect(
            host='localhost',
            user=username,
            password=password,
            auth_plugin='mysql_native_password'
        )
        
        if con.is_connected():
            mb.showinfo("Success", "Connection Established!")
            cur = con.cursor()
            root.destroy()

            
            # Create a connection to the MySQL server
            #con = mysql.connector.connect(host='localhost', password='Me#2024', user='root')
            # Create a cursor object to execute SQL statements
            #cur = con.cursor()
            # Check if the 'acsproject' database exists
            cur.execute("SHOW DATABASES")
            databases = cur.fetchall()
            database_exists = False
            for database in databases:
              if 'acsproject' in database:
                database_exists = True
                break
            if database_exists:
              print("Database exists")
            else:
              print("Database does not exist")
              cur.execute("CREATE DATABASE IF NOT EXISTS acsproject")
              cur.execute("USE acsproject")

              # Create matchmanagement table without primary key constraints
              cur.execute( """CREATE TABLE IF NOT EXISTS matchmanagement (
                  Match_Id VARCHAR(9) NOT NULL,
                  Date DATE NOT NULL,
                  Time TIME NOT NULL,
                  Team1 VARCHAR(80) NOT NULL,
                  Team2 VARCHAR(80) NOT NULL,
                  Match_type VARCHAR(10) NOT NULL,
                  Match_status VARCHAR(20) NOT NULL)""" )
              
              # Insert data into matchmanagement table
              cur.execute(
                  """INSERT INTO matchmanagement 
                  VALUES 
                  ('MN00001', '2022-08-10', '19:30:00', 'Indian National Cricket Team', 'New Zealand National Cricket Team', 'T20', 'completed'),
                  ('MN00002', '2022-09-14', '14:00:00', 'Indian National Cricket Team','New Zealand National Cricket Team', 'ODI', 'completed'),
                  ('MN00003', '2024-05-14', '19:00:00', 'Chennai Super Kings','Royal Challengers Banglore', 'T20', 'completed'),
                  ('MN00004', '2025-04-30', '15:00:00', 'Chennai Super Kings','Sunrisers Hyderabad', 'T20', 'completed')""")

              # Create seatingarrangement table without primary key constraints
              cur.execute("""CREATE TABLE IF NOT EXISTS seatingarrangement (
                  total_seats INT NOT NULL,
                  booking_type VARCHAR(20) NOT NULL,
                  cost VARCHAR(10) NOT NULL,
                  availability VARCHAR(20) NOT NULL,
                  block_name VARCHAR(50) NOT NULL   )"""  )

              # Insert data into seatingarrangement table
              insert_query1 = """INSERT INTO seatingarrangement 
              (total_seats, booking_type, cost, availability, block_name)
              VALUES (%s, %s, %s, %s, %s)"""

              # Data to be inserted
              data1 = [
                  (84, 'whole', '30,000 Rs.', 'available', 'C A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'C LOWER'),
                  (1172, 'per seat', '270 Rs.', 'available', 'C UPPER'),
                  (84, 'whole', '30,000 Rs.', 'available', 'D A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'D LOWER'),
                  (1172, 'per seat', '270 Rs.', 'available', 'D UPPER'),
                  (84, 'whole', '30,000 Rs.', 'available', 'E A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'E LOWER'),
                  (1172, 'per seat', '270 Rs.', 'available', 'E UPPER'),
                  (84, 'whole', '30,000 Rs.', 'available', 'F A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'F LOWER'),
                  (2344, 'per seat', '270 Rs.', 'available', 'F UPPER'),
                  (84, 'per seat', '1,000 Rs.', 'available', 'G A/C BOX'),
                  (1250, 'per seat', '600 Rs.', 'available', 'G LOWER'),
                  (2344, 'per seat', '270 Rs.', 'available', 'G UPPER'),
                  (84, 'whole', '30,000 Rs.', 'available', 'H A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'H LOWER'),
                  (2344, 'per seat', '270 Rs.', 'available', 'H UPPER'),
                  (84, 'whole', '30,000 Rs.', 'available', 'I A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'I LOWER'),
                  (2344, 'per seat', '270 Rs.', 'available', 'I UPPER'),
                  (84, 'whole', '30,000 Rs.', 'available', 'J A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'available', 'J LOWER'),
                  (2344, 'per seat', '270 Rs.', 'available', 'J UPPER'),
                  (1350, 'per seat', '600 Rs.', 'available', 'K LOWER'),
                  (2344, 'per seat', '270 Rs.', 'available', 'K UPPER'),
                  (396, 'per seat', '1,000 Rs.', 'available', 'KALAIGNAR M.KARUNANIDHI STAND A/C BOX'),
                  (1350, 'per seat', '600 Rs.', 'not available', 'KALAIGNAR M.KARUNANIDHI STAND LOWER'),
                  (2930, 'per seat', '270 Rs.', 'available', 'KALAIGNAR M.KARUNANIDHI STAND UPPER'),
                  (80, 'per seat', '1,000 Rs.', 'available', 'L A/C BOX MCC'),
                  (1300, 'per seat', '600 Rs.', 'not available', 'L LOWER MCC'),
                  (1758, 'per seat', '270 Rs.', 'available', 'L UPPER MCC')]
              # Execute the insert command for each record
              cur.executemany(insert_query1, data1)

              # Create staff_mng table without primary key constraints
              cur.execute(
                  """CREATE TABLE IF NOT EXISTS staff_mng (
                  emp_id CHAR(6) NOT NULL,
                  emp_dept VARCHAR(40) NOT NULL,
                  deptno CHAR(3) NOT NULL,
                  emp_subdept VARCHAR(40) NOT NULL,
                  emp_name VARCHAR(45) NOT NULL,
                  emp_role VARCHAR(50) NOT NULL
                  )"""
              )

              # Insert data into staff_mng table
              insert_query2 = """INSERT INTO staff_mng 
              (emp_id, emp_dept, deptno, emp_subdept, emp_name, emp_role)
              VALUES (%s, %s, %s, %s, %s, %s)"""
              data2 = [('A00001', 'seating', '003', 'Block C', 'Richa', 'Manager'),
                  ('A00002', 'ground', '001', 'Pitch', 'Deepak R', 'Pitch curator'),
                  ('A00003', 'seating', '003', 'Block D', 'Vivek', 'cleaner'),
                  ('A00004', 'sound', '002', 'sound system 2', 'Preethi', 'DJ'),
                    ('A00005', 'Emergency', '010', 'Medical', 'Raju', 'Paramedic'),
                    ('A00006', 'External Facility', '011', 'Pool Area', 'Rohit', 'Life Guard')]
              cur.executemany(insert_query2, data2)
              # Commit the changes
              con.commit()
              print("Database setup completed.")

            def disp2():
                # Create the main window
                r2 = tk.Tk()
                r2.geometry("1000x500")
                r2.config(bg="#75c9b7")
                r2.title("Seating Arrangement Details")
                Lt2 = Label(r2, text="Seating Arrangement Details", fg="black", bg="#75c9b7", font=("calibri", 30))
                Lt2.pack()
                con= mysql.connector.connect(host='localhost', passwd=password, user=username,auth_plugin='mysql_native_password', database='acsproject')
                cur = con.cursor()
                cur.execute('SELECT * FROM seatingarrangement')
                # Create and configure Treeview widget
                seatingarrangement = ttk.Treeview(r2, show='headings')
                s2 = ttk.Style(r2)
                s2.theme_use("vista")
                s2.configure("Treeview", font=('default', 11))
                s2.configure("Treeview.Heading", foreground='#75c9b7', font=('Helvetica', 11))

                # Define the columns
                seatingarrangement['columns'] = ('total_seats', 'booking_type', 'cost', 'availability', 'block_name')
                seatingarrangement.column("total_seats", width=100, minwidth=100, anchor=CENTER)
                seatingarrangement.column("booking_type", width=200, minwidth=100, anchor=CENTER)
                seatingarrangement.column("cost", width=100, minwidth=100, anchor=CENTER)
                seatingarrangement.column("availability", width=200, minwidth=100, anchor=CENTER)
                seatingarrangement.column("block_name", width=250, minwidth=100, anchor=CENTER)
                # Assign the heading names
                seatingarrangement.heading("total_seats", text="No. of Seats", anchor=CENTER)
                seatingarrangement.heading("booking_type", text="Booking Type", anchor=CENTER)
                seatingarrangement.heading("cost", text="Cost", anchor=CENTER)
                seatingarrangement.heading("availability", text="Availability", anchor=CENTER)
                seatingarrangement.heading("block_name", text="Name of the Block", anchor=CENTER)

                # Insert data into the Treeview
                i = 0
                for row in cur:
                    seatingarrangement.insert("", i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
                    i += 1
                seatingarrangement.pack()
                # Add a horizontal scrollbar
                hsb2 = ttk.Scrollbar(r2, orient="horizontal")
                hsb2.configure(command=seatingarrangement.xview)
                seatingarrangement.configure(xscrollcommand=hsb2.set)
                hsb2.pack(fill=X, side=BOTTOM)

                exitbutton=tk.Button(r2,text='Exit',command=r2.destroy)
                exitbutton.configure(font=('calibri',14,'bold'),bg='black',fg='white')
                exitbutton.place(x=470,y=400)

            def disp1():
               con = mysql.connector.connect(host='localhost', passwd=password, user=username, auth_plugin='mysql_native_password', database='acsproject')
               cur = con.cursor()
               r1 = tk.Toplevel()
               r1.geometry("1200x700")
               r1.config(bg="#16123f")
               Lt1 = Label(r1, text="Match Management", fg="white", bg="#16123f", font=("calibri", 30))
               Lt1.pack()
               match_mng = ttk.Treeview(r1, show='headings')
               s1 = ttk.Style(r1)
               s1.theme_use("alt")
               s1.configure(",", font=('default', 11))
               s1.configure("Treeview.Heading", foreground='#16123f', font=('Helvetica', 11))
               match_mng['columns'] = ('Match ID', 'Date', 'Time', 'Team 1', 'Team 2', 'Match type', 'Match status')
             
               match_mng.column("Match ID", width=100, minwidth=100, anchor=CENTER)
               match_mng.column("Date", width=100, minwidth=100, anchor=CENTER)
               match_mng.column("Time", width=50, minwidth=50, anchor=CENTER)
               match_mng.column("Team 1", width=250, minwidth=250, anchor=CENTER)
               match_mng.column("Team 2", width=250, minwidth=250, anchor=CENTER)
               match_mng.column("Match type", width=150, minwidth=150, anchor=CENTER)
               match_mng.column("Match status", width=150, minwidth=150, anchor=CENTER)
             
               match_mng.heading("Match ID", text="Match ID", anchor=CENTER)
               match_mng.heading("Date", text="Date", anchor=CENTER)
               match_mng.heading("Time", text="Time", anchor=CENTER)
               match_mng.heading("Team 1", text="Team 1", anchor=CENTER)
               match_mng.heading("Team 2", text="Team 2", anchor=CENTER)
               match_mng.heading("Match type", text="Match type", anchor=CENTER)
               match_mng.heading("Match status", text="Match status", anchor=CENTER)
             
               # Populate the Treeview with data from the database
               cur.execute('SELECT * FROM matchmanagement ORDER BY Match_Id')
               for row in cur:
                 match_mng.insert("", "end", values=row)
              #scroll bar (to view all the columns)
               vsb1=ttk.Scrollbar(r1,orient="vertical",command=match_mng.yview)
              #here "yview" means that it will modify the vertical position of the match 
              #to connect the scroll bar to the widget "match", so we are setting the xscroll command to "hsb.set"
               match_mng.configure(yscrollcommand=vsb1.set)
               vsb1.pack(fill=Y,side=RIGHT)
              #scroll bar (to view all the columns)
               hsb1=ttk.Scrollbar(r1,orient="horizontal",command=match_mng.xview)
              #here "xview" means that it will modify the horizontal position of the match
              #to connect the scroll bar to the widget "match", so we are setting the xscroll command to "hsb.set"
               match_mng.configure(xscrollcommand=hsb1.set)
               hsb1.pack(fill=X,side=BOTTOM)
               match_mng.pack()
              
              # Define and set tk.StringVar() and tk.IntVar()
               match_id = tk.StringVar()
               date = tk.StringVar()
               time = tk.StringVar()
               team1 = tk.StringVar()
               team2 = tk.StringVar()
               match_type = tk.StringVar()
               match_status = tk.StringVar()

               def add_data1(table):
                 f1 = Frame(r1, width=600, height=420, bg='#219ebc')
                 f1.place(x=150, y=300)

                 l11 = Label(f1, text="Match ID", width=20, font=('Times', 11, 'bold'))
                 e11 = Entry(f1, textvariable=match_id, width=25)
                 l11.place(x=20, y=30)
                 e11.place(x=300, y=30)

                 l21 = Label(f1, text="Date", width=20, font=('Times', 11, 'bold'))
                 e21 = Entry(f1, textvariable=date, width=25)
                 l21.place(x=20, y=70)
                 e21.place(x=300, y=70)
             
                 l31 = Label(f1, text="Time", width=20, font=('Times', 11, 'bold'))
                 e31 = Entry(f1, textvariable=time, width=25)
                 l31.place(x=20, y=110)
                 e31.place(x=300, y=110)

                 l41 = Label(f1, text="Team 1", width=20, font=('Times', 11, 'bold'))
                 e41 = Entry(f1, textvariable=team1, width=25)
                 l41.place(x=20, y=150)
                 e41.place(x=300, y=150)

                 l51 = Label(f1, text="Team 2", width=20, font=('Times', 11, 'bold'))
                 e51 = Entry(f1, textvariable=team2, width=25)
                 l51.place(x=20, y=190)
                 e51.place(x=300, y=190)

                 l61 = Label(f1, text="Match Type", width=20, font=('Times', 11, 'bold'))
                 c61 = ttk.Combobox(f1, width=25)
                 c61['values'] = ("ODI", "Test", "T20")
                 l61.place(x=20, y=230)
                 c61.place(x=300, y=230)

                 l71 = Label(f1, text="Match Status", width=20, font=('Times', 11, 'bold'))
                 c71 = ttk.Combobox(f1, width=25)
                 c71['values'] = ("completed", "pending", "cancelled")
                 l71.place(x=20, y=270)
                 c71.place(x=300, y=270)

                #To blank value of each variable.
                 match_id.set('')
                 date.set('')
                 time.set('')
                 team1.set('')
                 team2.set('')
                 match_type.set('')
                 match_status.set('')
               

                 def insert_data1():
                    try:
                        mi = match_id.get()
                        d = date.get()
                        t = time.get()
                        t1 = team1.get()
                        t2 = team2.get()
                        mt = c61.get()
                        ms = c71.get()

                        cur.execute('INSERT INTO matchmanagement(Match_Id, Date, Time, Team1, Team2, Match_type, Match_status) VALUES (%s, %s, %s, %s, %s, %s, %s)', (mi, d, t, t1, t2, mt, ms))
                     
                        con.commit()

                        match_mng.insert("", 'end', values=(mi, d, t, t1, t2, mt, ms))
                        mb.showinfo("Success", "Match details entered!")

                        e11.delete(0, END)
                        e21.delete(0, END)
                        e31.delete(0, END)
                        e41.delete(0, END)
                        e51.delete(0, END)
                        
                        f1.destroy()
                        r1.deiconify()
                    except mysql.connector.Error as err:
                        mb.showerror("Database Error", f"Error: {err}")
                    # Database errors: These are problems related to the database itself, like trying to connect to \
                    #a wrong database or having issues with the SQL query.
                    # The error message is displayed using mb.showerror("Database Error", f"Error: {err}")
                    except Exception as e:
                        mb.showerror("Error", f"Unexpected error: {e}")
                    # Unexpected errors: These are any other errors that might occur, like a programming mistake or a system problem.
                    # The error message is displayed using mb.showerror("Error", f"Unexpected error: {e}")
                 def cancel_1():
                   f1.destroy()
                   r1.deiconify()
                   
                 sub_button=tk.Button(f1,text="submit",command=insert_data1)
                 sub_button.configure(font=('calibri',14,'bold'),bg='green',fg='white')
                 sub_button.place(x=100,y=320)
                #cancel button closes the frame
                 can_button=tk.Button(f1,text="cancel",command=cancel_1)
                 can_button.configure(font=('calibri',14,'bold'),bg='red',fg='white')
                 can_button.place(x=190,y=320)

               def delete_data1(table):
                curitem = match_mng.focus()  # Get the selected item
                # Check if any item is selected
                if not curitem:
                    mb.showwarning("Selection Error", "Please select a record to delete.")
                    r1.deiconify()
                    return
                values = match_mng.item(curitem, 'values')  # Get the values of the selected item
                # Check if values is empty
                if not values:
                    mb.showwarning("Selection Error", "No data found for the selected record.")
                    r1.deiconify()
                    return
                mi = values[0]  # Assuming the employee ID is the first value

                try:
                    # Replace with your actual database connection and cursor
                    del_query = 'DELETE FROM matchmanagement WHERE Match_Id = %s'
                    sel_data = (mi,)
                    cur.execute(del_query, sel_data)
                    con.commit()
                    
                    table.delete(curitem)  # Deleting it from treeview
                    mb.showinfo('Success', 'Match data deleted!')
                except Exception as e:
                    mb.showerror('Error', f'An error occurred: {e}')
                    con.rollback()  # Rollback in case of error
                    
                r1.deiconify()    
              
               def select_data1(table):
                curitem = match_mng.focus()  # Get the selected item
                if not curitem:  # Check if any item is selected
                    mb.showwarning("Selection Error", "Please select a record to update.")#executes only if curitem is False
                    r1.deiconify()
                    return

                values = match_mng.item(curitem, 'values')  # Get the values of the selected item
                
                if not values:
                    mb.showwarning("Selection Error", "No data found for the selected record.")
                    #displays a warning message if values is empty, indicating there's no data to update.
                    r1.deiconify()
                    return

                # Create a frame for updating the data

                f1 = Frame(r1, width=600, height=420, bg='#FF7F50')
                f1.place(x=150, y=300)

                l11 = Label(f1, text="Match ID", width=20, font=('Times', 11, 'bold'))
                e11 = Entry(f1, textvariable=match_id, width=25)
                l11.place(x=20, y=30)
                e11.place(x=300, y=30)

                l21 = Label(f1, text="Date", width=20, font=('Times', 11, 'bold'))
                e21 = Entry(f1, textvariable=date, width=25)
                l21.place(x=20, y=70)
                e21.place(x=300, y=70)

                l31 = Label(f1, text="Time", width=20, font=('Times', 11, 'bold'))
                e31 = Entry(f1, textvariable=time, width=25)
                l31.place(x=20, y=110)
                e31.place(x=300, y=110)

                l41 = Label(f1, text="Team 1", width=20, font=('Times', 11, 'bold'))
                e41 = Entry(f1, textvariable=team1, width=25)
                l41.place(x=20, y=150)
                e41.place(x=300, y=150)

                l51 = Label(f1, text="Team 2", width=20, font=('Times', 11, 'bold'))
                e51 = Entry(f1, textvariable=team2, width=25)
                l51.place(x=20, y=190)
                e51.place(x=300, y=190)

                l61 = Label(f1, text="Match Type", width=20, font=('Times', 11, 'bold'))
                c61 = ttk.Combobox(f1,textvariable=match_type, width=25)
                c61['values'] = ("ODI", "Test", "T20")
                l61.place(x=20, y=230)
                c61.place(x=300, y=230)

                l71 = Label(f1, text="Match Status", width=20, font=('Times', 11, 'bold'))
                c71 = ttk.Combobox(f1,textvariable=match_status, width=25)
                c71['values'] = ("completed", "pending", "cancelled")
                l71.place(x=20, y=270)
                c71.place(x=300, y=270)

                #The set() method is used to assign the corresponding value from the values list to each variable.
                match_id.set(values[0])
                date.set(values[1])
                time.set(values[2])
                team1.set(values[3])
                team2.set(values[4])
                match_type.set(values[5])
                match_status.set(values[6])

                def update_data1():#made inside the loop so that it can access all the entry widgets
                    
                    
                    try:
                        mi = values[0]
                        d = date.get()
                        t = time.get()
                        t1 = team1.get()
                        t2 = team2.get()
                        mt = match_type.get()
                        ms = match_status.get()
                        update_query = '''UPDATE matchmanagement 
                                              SET Date=%s, Time=%s, Team1=%s, Team2=%s, Match_type=%s, Match_status=%s 
                                              WHERE Match_Id=%s'''
                        cur.execute(update_query, (d, t, t1, t2, mt, ms, mi))
                        con.commit()
                        match_mng.item(curitem, values=(mi, d, t, t1, t2, mt, ms))
                        mb.showinfo("Success", "Match data updated!")

                        e11.delete(0, END)
                        e21.delete(0, END)
                        e31.delete(0, END)
                        e41.delete(0, END)
                        e51.delete(0, END)
                        c61.delete(0, END)                
                        c71.delete(0, END)
                        f1.destroy()
                        r1.deiconify()

                    except mysql.connector.Error as err:
                        mb.showerror("Database Error", f"Error: {err}")
                        # Database errors: These are problems related to the database itself, like trying to connect to \
                    #a wrong database or having issues with the SQL query.
                    # The error message is displayed using mb.showerror("Database Error", f"Error: {err}")
                        
                    except Exception as e:
                        mb.showerror("Error", f"Unexpected error: {e}")
                        


                def cancel_1():
                   f1.destroy()
                   r1.deiconify()
                       
                    
                sub_button = tk.Button(f1, text="Update", command=update_data1)
                sub_button.configure(font=('calibri',14,'bold'),bg='green',fg='white')
                sub_button.place(x=100, y=320)

                can_button = tk.Button(f1, text="Cancel", command=cancel_1)
                can_button.configure(font=('calibri',14,'bold'),bg='red',fg='white')
                can_button.place(x=190, y=320)

               insertbutton=tk.Button(r1,text='Insert',command=lambda:add_data1(match_mng))
            #lambda functions can contain only a single expression and cannot contain multiple lines of code
               insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
               insertbutton.place(x=400,y=400)
               deletebutton=tk.Button(r1,text='Delete',command=lambda:delete_data1(match_mng))
               deletebutton.configure(font=('calibri',14,'bold'),bg='red',fg='white')
               deletebutton.place(x=500,y=400)
               updatebutton=tk.Button(r1,text='Update',command=lambda:select_data1(match_mng))
               updatebutton.configure(font=('calibri',14,'bold'),bg='blue',fg='white')
               updatebutton.place(x=600,y=400)
               exitbutton=tk.Button(r1,text='Exit',command=r1.destroy)
               exitbutton.configure(font=('calibri',14,'bold'),bg='black',fg='white')
               exitbutton.place(x=700,y=400)

            
            def disp3():
              r3 = tk.Toplevel()
              r3.geometry("1100x800")
              r3.config(bg="#c7ddcc")
              photo2 = tk.PhotoImage(file="img2.png")
              w3 = tk.Label(r3, image=photo2)
              w3.photo = photo2
              w3.place(x=50, y=50)
              exitbutton=tk.Button(r3,text='Exit',command=r3.destroy)
              exitbutton.configure(font=('calibri',14,'bold'),bg='black',fg='white')
              exitbutton.place(x=550,y=10)


            def disp4():
              con = mysql.connector.connect(host='localhost', passwd=password, user=username, auth_plugin='mysql_native_password',database='acsproject')
              cur = con.cursor()
              r4 = tk.Toplevel()
              r4.geometry("800x700")
              r4.config(bg="#16123f")
              Lt4 = Label(r4, text="Staff Management", fg="white", bg="#16123f", font=("calibri", 30))
              Lt4.pack()
              staff_mng = ttk.Treeview(r4, show='headings')
              s4 = ttk.Style(r4)
              s4.theme_use("alt")
              s4.configure(",", font=('default', 11))
              s4.configure("Treeview.Heading", foreground='#16123f', font=('Helvetica', 11))
              staff_mng['columns'] = ('emp_id', 'emp_dept', 'deptno', 'emp_subdept', 'emp_name', 'emp_role')
              staff_mng.column("emp_id", width=100, minwidth=100, anchor=CENTER)
              staff_mng.column("emp_dept", width=150, minwidth=100, anchor=CENTER)
              staff_mng.column("deptno", width=150, minwidth=100, anchor=CENTER)
              staff_mng.column("emp_subdept", width=150, minwidth=100, anchor=CENTER)
              staff_mng.column("emp_name", width=100, minwidth=100, anchor=CENTER)
              staff_mng.column("emp_role", width=100, minwidth=100, anchor=CENTER)

              staff_mng.heading("emp_id", text="Employee No.", anchor=CENTER)
              staff_mng.heading("emp_dept", text="Department", anchor=CENTER)
              staff_mng.heading("deptno", text="Department No.", anchor=CENTER)
              staff_mng.heading("emp_subdept", text="Sub-Department", anchor=CENTER)
              staff_mng.heading("emp_name", text="Name", anchor=CENTER)
              staff_mng.heading("emp_role", text="Role", anchor=CENTER)
              # Populate the Treeview with data from the database
              cur.execute('SELECT * FROM staff_mng ORDER BY  emp_id')
              for row in cur:
                staff_mng.insert("", "end", values=row)
              #scroll bar (to view all the columns)
              vsb4=ttk.Scrollbar(r4,orient="vertical",command=staff_mng.yview)
              #here "yview" means that it will modify the vertical position of the match 
              #to connect the scroll bar to the widget "match", so we are setting the xscroll command to "hsb.set"
              staff_mng.configure(yscrollcommand=vsb4.set)
              vsb4.pack(fill=Y,side=RIGHT)
              #scroll bar (to view all the columns)
              hsb4=ttk.Scrollbar(r4,orient="horizontal",command=staff_mng.xview)
              #here "xview" means that it will modify the horizontal position of the match
              #to connect the scroll bar to the widget "match", so we are setting the xscroll command to "hsb.set"
              staff_mng.configure(xscrollcommand=hsb4.set)
              hsb4.pack(fill=X,side=BOTTOM)
              staff_mng.pack()
              Employee_number=tk.StringVar()
              Department=tk.StringVar()
              dept_no=tk.StringVar()
              employee_subdept=tk.StringVar()
              employee_name=tk.StringVar()
              employee_role=tk.StringVar()
              def add_data(table):
                f=Frame(r4,width=600,height=420,bg='#25B396')
                f.place(x=150,y=300)# lable and entry widgets will be created inside the frame

                l14=Label(f,text="Employee number",width=20,font=('Times',11,'bold'))
                e14=Entry(f,textvariable=Employee_number,width=25)
                l14.place(x=20,y=30)
                e14.place(x=300,y=30)

                l24=Label(f,text="Department",width=20,font=('Times',11,'bold'))
                e24=Entry(f,textvariable=Department,width=25)
                l24.place(x=20,y=70)
                e24.place(x=300,y=70)

                l34=Label(f,text="Dept. No.",width=20,font=('Times',11,'bold'))
                e34=Entry(f,textvariable=dept_no,width=25)
                l34.place(x=20,y=110)
                e34.place(x=300,y=110)

                l44=Label(f,text="employee subdept",width=20,font=('Times',11,'bold'))
                e44=Entry(f,textvariable=employee_subdept,width=25)
                l44.place(x=20,y=150)
                e44.place(x=300,y=150)

                l54=Label(f,text="employee name",width=20,font=('Times',11,'bold'))
                e54=Entry(f,textvariable=employee_name,width=25)
                l54.place(x=20,y=190)
                e54.place(x=300,y=190)

                l64=Label(f,text="employee role",width=20,font=('Times',11,'bold'))
                e64=Entry(f,textvariable=employee_role,width=25)
                l64.place(x=20,y=230)
                e64.place(x=300,y=230)

                #To blank value of each variable.
                Employee_number.set('')
                Department.set('')
                dept_no.set('')
                employee_subdept.set('')
                employee_name.set('')
                employee_role.set('')


                def insert_data():
                    try:
                        en = Employee_number.get()
                        d = Department.get()
                        dn = dept_no.get()
                        es = employee_subdept.get()
                        ena = employee_name.get()
                        er = employee_role.get()
                        cur.execute('INSERT INTO staff_mng(emp_id, emp_dept, deptno, emp_subdept, emp_name, emp_role) \
                                         VALUES (%s, %s, %s, %s, %s, %s)', (en, d, dn, es, ena, er))
                        con.commit()

                        staff_mng.insert("", 'end', values=(en, d, dn, es, ena, er))
                        mb.showinfo("Success", "Staff entered!")

                        e14.delete(0, END)
                        e24.delete(0, END)
                        e34.delete(0, END)
                        e44.delete(0, END)
                        e54.delete(0, END)
                        e64.delete(0, END)
                        f.destroy()
                        r4.deiconify()

                    except mysql.connector.Error as err:
                        mb.showerror("Database Error", f"Error: {err}")
                        r4.deiconify()
                    # Database errors: These are problems related to the database itself, like trying to connect to \
                    #a wrong database or having issues with the SQL query.
                    # The error message is displayed using mb.showerror("Database Error", f"Error: {err}")
                    except Exception as e:
                        mb.showerror("Error", f"Unexpected error: {e}")
                        r4.deiconify()
                    # Unexpected errors: These are any other errors that might occur, like a programming mistake or a system problem.
                    # The error message is displayed using mb.showerror("Error", f"Unexpected error: {e}")

                def cancel_4():
                   f.destroy()
                   r4.deiconify()

              
                sub_button=tk.Button(f,text="submit",command=insert_data)
                sub_button.configure(font=('calibri',14,'bold'),bg='green',fg='white')
                sub_button.place(x=100,y=280)
                #cancel button closes the frame
                can_button=tk.Button(f,text="cancel",command=cancel_4)
                can_button.configure(font=('calibri',14,'bold'),bg='red',fg='white')
                can_button.place(x=190,y=280)

              def delete_data(table):
                curitem = staff_mng.focus()  # Get the selected item
                # Check if any item is selected
                if not curitem:
                    mb.showwarning("Selection Error", "Please select a record to delete.")
                    r4.deiconify()
                    return
                values = staff_mng.item(curitem, 'values')  # Get the values of the selected item
                # Check if values is empty
                if not values:
                    mb.showwarning("Selection Error", "No data found for the selected record.")
                    return
                empid = values[0]  # Assuming the employee ID is the first value

                try:
                    # Replace with your actual database connection and cursor
                    del_query = 'DELETE FROM staff_mng WHERE emp_id = %s'
                    sel_data = (empid,)
                    cur.execute(del_query, sel_data)
                    con.commit()
                    
                    table.delete(curitem)  # Deleting it from treeview
                    mb.showinfo('Success', 'Employee data deleted!')
                except Exception as e:
                    mb.showerror('Error', f'An error occurred: {e}')
                    con.rollback()  # Rollback in case of error

                r4.deiconify()
               

              def select_data(table):
                curitem = staff_mng.focus()  # Get the selected item
                if not curitem:  # Check if any item is selected
                    mb.showwarning("Selection Error", "Please select a record to update.")#executes only if curitem is False
                    r4.deiconify()
                    return

                values = staff_mng.item(curitem, 'values')  # Get the values of the selected item
                
                if not values:
                    mb.showwarning("Selection Error", "No data found for the selected record.")
                    #displays a warning message if values is empty, indicating there's no data to update.
                    r4.deiconify()
                    return

                # Create a frame for updating the data
                f = Frame(r4, width=600, height=420, bg='#d8315b')
                f.place(x=150, y=300)#label and widgets will be created inside the frame

                l14=Label(f,text="Employee number",width=20,font=('Times',11,'bold'))
                e14=Entry(f,textvariable=Employee_number,width=25)
                l14.place(x=20,y=30)
                e14.place(x=300,y=30)

                l24=Label(f,text="Department",width=20,font=('Times',11,'bold'))
                e24=Entry(f,textvariable=Department,width=25)
                l24.place(x=20,y=70)
                e24.place(x=300,y=70)

                l34=Label(f,text="Dept. No.",width=20,font=('Times',11,'bold'))
                e34=Entry(f,textvariable=dept_no,width=25)
                l34.place(x=20,y=110)
                e34.place(x=300,y=110)

                l44=Label(f,text="employee subdept",width=20,font=('Times',11,'bold'))
                e44=Entry(f,textvariable=employee_subdept,width=25)
                l44.place(x=20,y=150)
                e44.place(x=300,y=150)

                l54=Label(f,text="employee name",width=20,font=('Times',11,'bold'))
                e54=Entry(f,textvariable=employee_name,width=25)
                l54.place(x=20,y=190)
                e54.place(x=300,y=190)

                l64=Label(f,text="employee role",width=20,font=('Times',11,'bold'))
                e64=Entry(f,textvariable=employee_role,width=25)
                l64.place(x=20,y=230)
                e64.place(x=300,y=230)
                #The set() method is used to assign the corresponding value from the values list to each variable.
                Employee_number.set(values[0])
                Department.set(values[1])
                dept_no.set(values[2])
                employee_subdept.set(values[3])
                employee_name.set(values[4])
                employee_role.set(values[5])

                def update_data():#made inside the loop so that it can access all the entry widgets
                    
                    
                    try:
                        empid = values[0]  # Assuming emp_id is the primary key
                        en = Employee_number.get()
                        d = Department.get()
                        dn = dept_no.get()
                        es = employee_subdept.get()
                        ena = employee_name.get()
                        er = employee_role.get()
                        update_query = '''UPDATE staff_mng SET emp_dept=%s, deptno=%s, emp_subdept=%s,\
            emp_name=%s, emp_role=%s WHERE emp_id=%s'''

                        #updating mysql table
                        cur.execute(update_query, (d, dn, es, ena, er, empid))
                        con.commit()

                        #updating the treeview table
                        staff_mng.item(curitem, values=(empid, d, dn, es, ena, er))
                        mb.showinfo("Success", "Employee data updated!")

                        e14.delete(0, END)
                        e24.delete(0, END)
                        e34.delete(0, END)
                        e44.delete(0, END)
                        e54.delete(0, END)
                        e64.delete(0, END)
                        f.destroy()
                        r4.deiconify()

                    except mysql.connector.Error as err:
                        mb.showerror("Database Error", f"Error: {err}")
                        # Database errors: These are problems related to the database itself, like trying to connect to \
                    #a wrong database or having issues with the SQL query.
                    # The error message is displayed using mb.showerror("Database Error", f"Error: {err}")
                    except Exception as e:
                        mb.showerror("Error", f"Unexpected error: {e}")

                def cancel_4():
                   f.destroy()
                   r4.deiconify()

                    
                sub_button = tk.Button(f, text="Update", command=update_data)
                sub_button.configure(font=('calibri',14,'bold'),bg='green',fg='white')
                sub_button.place(x=100, y=280)

                can_button = tk.Button(f, text="Cancel", command=cancel_4)
                can_button.configure(font=('calibri',14,'bold'),bg='red',fg='white')
                can_button.place(x=190, y=280)

              insertbutton=tk.Button(r4,text='Insert',command=lambda:add_data(staff_mng))
            #lambda functions can contain only a single expression and cannot contain multiple lines of code
              insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
              insertbutton.place(x=200,y=400)
              deletebutton=tk.Button(r4,text='Delete',command=lambda:delete_data(staff_mng))
              deletebutton.configure(font=('calibri',14,'bold'),bg='red',fg='white')
              deletebutton.place(x=300,y=400)
              updatebutton=tk.Button(r4,text='Update',command=lambda:select_data(staff_mng))
              updatebutton.configure(font=('calibri',14,'bold'),bg='blue',fg='white')
              updatebutton.place(x=400,y=400)
              exitbutton=tk.Button(r4,text='Exit',command=r4.destroy)
              exitbutton.configure(font=('calibri',14,'bold'),bg='black',fg='white')
              exitbutton.place(x=500,y=400)




            

            def disp5():
                r.destroy()
            #main window   
            r=Tk()
            r.title("Cricket Stadium management system ") # changing the title of the gui
            r.geometry("1600x1000")
            r.config(bg="#abd699")

            photo1=PhotoImage(file="img1.png")
            
            w=Label(r,image=photo1)
            w.place(x=0,y=0)

            L1 = Label(r, text="Cricket Stadium", fg="White",bg="#283cbd", font=("helvetica", 30,"bold italic"))
            L1.place(x=580, y=20)
            b1=Button(r,text="Match Management",fg="white",bg="#1A237E",font=("Arial",20),command=disp1)
            #button that opens to match management window
            b1.place(x=300,y=170)
            b2=Button(r,text="Seating Arrangement Details",fg="white",bg="#4CAF50",font=("Arial",20),command=disp2)
            #button that opens to Seating Management window
            b2.place(x=250,y=400)
            b3=Button(r,text="Staff Management",fg="white",bg="#1A237E",font=("Arial",20),command=disp4)
            #button that opens to Seating arrangement window
            b3.place(x=900,y=170)
            b4=Button(r,text="Seating Arrangement View",fg="white",bg="#4CAF50",font=("Arial",20),command=disp3)
            #button that opens to Staff Management window
            b4.place(x=850,y=400)

            b5=Button(r,text="Exit",fg="white",bg="#283cbd",font=("Arial",20),command=disp5)
            #button that opens to Staff Management window
            b5.place(x=700,y=550)
            r.mainloop()

            

        else:
            mb.showerror("Error", "Failed to connect to the database.")
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            
    except mysql.connector.Error as err:
        mb.showerror("Error", f"Error: {err}")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
# MySQL Login Details Label
label1 = tk.Label(root, text="MySQL Login Details", bg="#2f2f55", fg="white", font=("Arial", 14))
label1.pack(pady=10)
label2 = tk.Label(root, text="User authentication", bg="#2f2f55", fg="white", font=("Arial", 14))
label2.pack(pady=10)


# Username entry
username_label = tk.Label(root, text="MySQL Username", bg="#2f2f55", fg="white")
username_label.pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password entry
password_label = tk.Label(root, text="MySQL Password", bg="#2f2f55", fg="white")
password_label.pack()
password_entry = tk.Entry(root,show="*", width=30)
password_entry.pack(pady=5)

# Connect button
connect_button = tk.Button(root, text="Submit", command=connect_to_database)
connect_button.pack(pady=20)

root.mainloop()
