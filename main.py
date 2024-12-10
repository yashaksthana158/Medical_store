from tkinter import *
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk



def main():
    app = Tk()
    obj = LoginPage(app)
    app.mainloop()


class LoginPage:
    def __init__(self, win):
        self.win = win
         # Get screen width and height
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()

        # Calculate position and size for the window
        win_width = int(screen_width * 0.8)  # 80% of the screen width
        win_height = int(screen_height * 0.8)  # 80% of the screen height
        x_offset = (screen_width - win_width) // 2
        y_offset = (screen_height - win_height) // 2

        self.win.geometry(f"{win_width}x{win_height}+{x_offset}+{y_offset}")

        #self.win.geometry("1580x850")
        self.win.title("Medical Store Management System | Login")


        self.conn=mysql.connector.connect(host='localhost',user='root',password='ae-1265',
                                          database='medical_store')

        self.cur=self.conn.cursor()

        
        
        self.title_lbl = Label(self.win, text="Medical store Management System",
                               bg="#003366", fg="White", bd=0, relief=GROOVE, font=("Arial", 50, "bold"),pady=30,padx=20)
        self.title_lbl.pack(side=TOP, fill=X)

        self.title2_lbl = Label(self.win, text="A Database Management Systems Project",
                               bg="#003366", fg="white", bd=0, font=("Arial", 25),
                               highlightthickness=0)
        self.title2_lbl.pack(side=TOP, fill=X)

        
        self.title3_lbl = Label(self.win, text="Department Of Computer Science",
                               bg="#003366", fg="white", bd=0, font=("Arial", 18),pady=5,
                               highlightthickness=0)
        self.title3_lbl.pack(side=TOP, fill=X)

        self.med_frame=Frame(self.win ,bd=0,height=520)
        self.med_frame.pack(side=TOP,fill=BOTH)

        self.background_image = Image.open("pharm1.png")  # Open the image
        self.background_photo = ImageTk.PhotoImage(self.background_image)  # Convert image to PhotoImage
        self.background_label = Label(self.med_frame, image=self.background_photo)
        self.background_label.config(image=self.background_photo)
        #self.background_label.pack(side=TOP, fill=BOTH)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1) 

        

        
        self.main_frame = Frame(self.win, bg='white', bd=2, relief="solid")
        self.main_frame.place(x=500, y=350, width=565, height=300)

        self.bottom_frame=Frame(self.win, bd=0)
        self.bottom_frame.pack(side=BOTTOM, fill=BOTH,)

        self.bottom_label=Label(self.bottom_frame, text="Developed By ,Yash Asthana, Aditya Gupta, Mohd. Zeeshan Alam, B.Sc(H) Computer Science,2024",
                                      bg="#003366", fg="white", bd=0, font=("Arial", 15),pady=30,highlightthickness=0)
        self.bottom_label.pack(side=TOP, fill=BOTH,)

        self.login_as_frame = LabelFrame(self.main_frame, text="Login As",
                                         bg="#003366", fg="white",bd=0, font=("Arial", 20, "bold"), relief=RIDGE)
        self.login_as_frame.pack(side=TOP, fill=BOTH)

        self.user_type = StringVar()
        self.user_type.set("employee")

        self.rb_indicator_color = "grey"  # Color of the selection indicator


        self.employee_radio = Radiobutton(self.login_as_frame, text="Employee", font=("Arial", 14),
                                          bg="#003366", fg="white", variable=self.user_type, value="employee",selectcolor=self.rb_indicator_color)
        self.employee_radio.grid(row=0, column=0, padx=80, pady=10)

        self.admin_radio = Radiobutton(self.login_as_frame, text="Admin",
                                       font=("Arial", 14), bg="#003366", fg="white", variable=self.user_type,
                                       value="admin",selectcolor=self.rb_indicator_color)
        self.admin_radio.grid(row=0, column=1, padx=80, pady=10)

        self.entry_frame =Frame(self.main_frame, bg="white", bd=0, pady=5, relief=FLAT)
        self.entry_frame.pack(side=TOP, fill=BOTH)

        


        self.username_ent = Entry(self.entry_frame, border=2, relief="solid", font=("Arial", 15),width=45)
        self.add_placeholder(self.username_ent,"Username")
        self.username_ent.grid(row=0, column=0, padx=15, pady=5)

        
        

        self.password_ent =Entry(self.entry_frame,border=2, relief="solid", font=("Arial", 15),width=45 ,show="*")
        self.add_placeholder(self.password_ent,"password")
        self.password_ent.grid(row=1, column=0, padx=15, pady=5)



        #=============================Main Buttons===========================================

        self.button_frame = Frame(self.main_frame, 
                                       bg="white", bd=0, relief=RIDGE)
        self.button_frame.pack(side=TOP, fill=BOTH)

        self.submit_btn = Button(self.button_frame, text="Submit", font=("Arial", 14), bg="#002040",activebackground="#194D75", fg="white",
                                 command=self.submit_func,width=45,justify="center")
        self.submit_btn.grid(row=0, column=0, padx=15, pady=10)

        self.reset_btn = Button(self.button_frame, text="Reset",
                                font=("Arial", 14), bg="white",bd=0,highlightthickness=0, fg="black", activebackground="lightgrey",command=self.reset_func)
        self.reset_btn.grid(row=1, column=0, padx=15, pady=10)

        #==================================functionalities=========================================


    


    def add_placeholder(self,entry_widget, placeholder_text):
        entry_widget.insert(0, placeholder_text)
        entry_widget.bind("<FocusIn>", lambda event: self.remove_placeholder(entry_widget, placeholder_text))
        entry_widget.bind("<FocusOut>", lambda event: self.insert_placeholder(entry_widget, placeholder_text))

    def remove_placeholder(self,entry_widget, placeholder_text):
        current_text = entry_widget.get()
        if current_text == placeholder_text:
            entry_widget.delete(0, "end")

    def insert_placeholder(self,entry_widget, placeholder_text):
        current_text = entry_widget.get()
        if current_text == "":
            entry_widget.insert(0, placeholder_text)


            

    def submit_func(self):
        user_type = self.user_type.get()
        username=self.username_ent.get()
        password=self.password_ent.get()
        if user_type == "employee":
            self.cur.execute("SELECT * FROM emp_login WHERE E_username=%s AND E_password=%s",(username,password))
        elif user_type == "admin":
            self.cur.execute("SELECT * FROM admin WHERE A_username=%s AND A_password=%s",(username,password))

        user=self.cur.fetchone()



        if user is not None:
            if user_type == "employee":
                employee_win = Toplevel(self.win)
                employee_page = EmployeePage(employee_win)
            elif user_type == "admin":
                admin_win = Toplevel(self.win)
                admin_page = AdminPage(admin_win)
        else:
            messagebox.showerror("Invalid Credentials","Wrong Username or Password") # message box to be added

    def reset_func(self):
        self.username_ent.delete(0, END)
        self.password_ent.delete(0, END)

    def exit_func(self):
        self.win.destroy()


class EmployeePage:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1550x8000")
        self.win.title("Employee Page")

##       self.win.configure(background="#e6e6e6")
        self.create_widgets()

    def create_widgets(self):


        def switch(page):
            
            for frame in content_frame.winfo_children():
                frame.destroy()
                self.win.update()
            page()

        def Inventory_toggle_menu():
            def collapse_Inventory_menu():
                Inventory_menu_frame.destroy()
                Inventory_button.config(text='Inventory ▼')
                Inventory_button.config(command=Inventory_toggle_menu)

            Inventory_menu_frame=Frame(sidebar_frame,bg="#003366")
            temp_frame=Frame(Inventory_menu_frame,bg="white")
            temp_frame.pack(fill=X)
            window_height=80    #root.winfo_height() gives current height of the window
            Manage_Inventory_btn=Button(Inventory_menu_frame,text="Manage Inventory", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(Manage_Inventory),highlightthickness=0)
            Manage_Inventory_btn.pack(pady=5)
            View_Inventory_btn=Button(Inventory_menu_frame,text="View Inventory", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(Inventory_view_page),highlightthickness=0)
            View_Inventory_btn.pack(pady=5)
            Inventory_menu_frame.place(x=0,y=275,height=window_height,width=250)
            Inventory_button.config(text='Inventory ▽')
            Inventory_button.config(command=collapse_Inventory_menu)

        def Reports_toggle_menu():
            def collapse_Reports_menu():
                Reports_menu_frame.destroy()
                Reports_button.config(text='Reports ▼')
                Reports_button.config(command=Reports_toggle_menu)

            Reports_menu_frame = Frame(sidebar_frame, bg="#003366")
            temp_frame=Frame(Reports_menu_frame,bg="white")
            temp_frame.pack(fill=X)
            window_height = 80
            Manage_Reports_btn = Button(Reports_menu_frame, text="Medicines-Low Stock", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda:switch(Med_LowStock), highlightthickness=0)
            Manage_Reports_btn.pack(pady=5)

            View_Reports_btn = Button(Reports_menu_frame, text="Medicines-Soon to Expire", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda:switch(Med_ExpireSoon), highlightthickness=0)
            View_Reports_btn.pack(pady=5)

            Reports_menu_frame.place(x=0, y=395, height=window_height, width=250)
            Reports_button.config(text='Reports ▽')
            Reports_button.config(command=collapse_Reports_menu)


        #main frame 
        main_frame = Frame(self.win)
        main_frame.pack(fill=BOTH)

         # Header
        header_label = Label(self.win, text="Medical Store Management System | ADMIN", font=("Times New Roman", 18), bg="#003366", fg="white", pady=10)  
        header_label.pack(side=TOP,fill=X)

        # Sidebar
        sidebar_frame = Frame(self.win, bg="#003366", width=250,padx=0)  
        sidebar_frame.pack(side=LEFT, fill=Y)

        sidebar_label = Label(sidebar_frame, text="Menu", font=("Arial", 18), bg="#003366", fg="white")
        sidebar_label.pack(pady=10)

        Dashboard_button = Button(sidebar_frame, text="Dashboard ", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(Dashboard))
        Dashboard_button.pack(fill=X, pady=10)

        customer_view_btn = Button(sidebar_frame, text="View Customers", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(customer_view_page))
        customer_view_btn.pack(fill=X, pady=10)

        Sales_invoicebtn = Button(sidebar_frame, text="View Sales Invoice Details", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(sales_view_page))
        Sales_invoicebtn.pack(fill=X, pady=10)


        Inventory_button = Button(sidebar_frame, text="Inventory ▼", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=Inventory_toggle_menu,relief="flat",activebackground="#003366")
        Inventory_button.pack(fill=X, pady=25)

       
        Reports_button = Button(sidebar_frame, text="Reports ▼", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=Reports_toggle_menu)
        Reports_button.pack(fill=X, pady=60)


        # Content
        content_frame = Frame(self.win, bg="white")
        content_frame.pack(fill=BOTH, expand=True)

        
        topnav_frame = Frame(content_frame, bg="#003366")
        topnav_frame.pack(side=TOP, fill=X)

        logout_button = Button(topnav_frame, text="Logout (Logged in as Employee)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
        logout_button.pack(side=RIGHT, padx=20, pady=10)

        main_content_frame = Frame(content_frame, bg="white")
        main_content_frame.pack( padx=10)

        Employeedash_frame =Frame(main_content_frame, bg="lightgrey",pady=10, bd=0)  
        Employeedash_frame.pack(side=TOP,pady=20)

        Employeedash_label =Label(Employeedash_frame, text="EMPLOYEE DASHBOARD", font=("Arial", 15), bg="lightgrey", fg="white",width=100)  
        Employeedash_label.pack()



        self.photoimg1 =PhotoImage(file="carticon1.png").subsample(2)

        sale_button = Button(main_content_frame, image=self.photoimg1, text="Add New Sale", font=("Arial", 18), bg="white",fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=self.Add_new_sale)
        sale_button.image = self.photoimg1  # Keep a reference to avoid garbage collection
        sale_button.pack(side=LEFT,padx=5,pady=40)

        
        self.photoimg2 = PhotoImage(file="inventory.png").subsample(2)
        
        inventory_button = Button(main_content_frame, image=self.photoimg2, text="View Inventory", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Inventory_view_page))
        inventory_button.image = self.photoimg2 
        inventory_button.pack(side=LEFT,padx=5,pady=40)

        self.photoimg4 =PhotoImage(file="moneyicon.png").subsample(2)

        transaction_button = Button(main_content_frame, image=self.photoimg4, text="View Transactions", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(transaction_view_page))
        transaction_button.image = self.photoimg4
        transaction_button.pack(side=LEFT,padx=5,pady=40)

        self.photoimg5 =PhotoImage(file="alert.png").subsample(2)

        alert_button = Button(main_content_frame, image=self.photoimg5, text="Low stock alert", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Med_LowStock))
        alert_button.image = self.photoimg5
        alert_button.pack(side=LEFT,padx=5,pady=40)

        def Dashboard():
            
            topnav_frame = Frame(content_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Employee)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            main_content_frame = Frame(content_frame, bg="white")
            main_content_frame.pack( padx=10)

            Employeedash_frame =Frame(main_content_frame, bg="lightgrey",pady=10, bd=0)  
            Employeedash_frame.pack(side=TOP,pady=20)

            Employeedash_label =Label(Employeedash_frame, text="Employee DASHBOARD", font=("Arial", 15), bg="lightgrey", fg="white",width=100)  
            Employeedash_label.pack()



            self.photoimg1 =PhotoImage(file="carticon1.png").subsample(2)

            sale_button = Button(main_content_frame, image=self.photoimg1, text="Add New Sale", font=("Arial", 18), bg="white",fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=self.Add_new_sale)
            sale_button.image = self.photoimg1  # Keep a reference to avoid garbage collection
            sale_button.pack(side=LEFT,padx=5,pady=40)

            
            self.photoimg2 = PhotoImage(file="inventory.png").subsample(2)
            
            inventory_button = Button(main_content_frame, image=self.photoimg2, text="View Inventory", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Inventory_view_page))
            inventory_button.image = self.photoimg2 
            inventory_button.pack(side=LEFT,padx=5,pady=40)

            self.photoimg4 =PhotoImage(file="moneyicon.png").subsample(2)

            transaction_button = Button(main_content_frame, image=self.photoimg4, text="View Transactions", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(transaction_view_page))
            transaction_button.image = self.photoimg4
            transaction_button.pack(side=LEFT,padx=5,pady=40)

            self.photoimg5 =PhotoImage(file="alert.png").subsample(2)

            alert_button = Button(main_content_frame, image=self.photoimg5, text="Low stock alert", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Med_LowStock))
            alert_button.image = self.photoimg5
            alert_button.pack(side=LEFT,padx=5,pady=40)




        def customer_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame,bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)
            
            table_frame.pack(expand=True, fill=BOTH)

            style=ttk.Style()

            print(style.theme_names())
            style.theme_use('clam')
            style.configure("New.Treeview.Heading",background="#0077b3",foreground="white",font=("Arial",17))
            style.configure("New.Treeview",rowheight=50,fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Customer ID", "First Name", "Last Name","Sex", "Phone Number", "Email Address"),show="headings",style="New.Treeview")
            table.heading("Customer ID", text="Customer ID",anchor=CENTER)
            table.heading("First Name", text="First Name",anchor=CENTER)
            table.heading("Last Name", text="Last Name",anchor=CENTER)
            table.heading("Sex", text="Sex",anchor=CENTER)
            table.heading("Phone Number", text="Phone Number",anchor=CENTER)
            table.heading("Email Address", text="Email Address",anchor=CENTER)

            

            table.column("Customer ID", width=100,anchor=CENTER)
            table.column("First Name", width=100,anchor=CENTER)
            table.column("Last Name", width=100,anchor=CENTER)
            table.column("Sex", width=50,anchor=CENTER)
            table.column("Phone Number", width=120,anchor=CENTER)
            table.column("Email Address", width=200,anchor=CENTER)
            #table.column("Action", width=150,anchor=CENTER)

           

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)

            conn=mysql.connector.connect(host="localhost",username="root",password="ae-1265",database="medical_store")
            cursor=conn.cursor()

            cursor.execute("Select * from customer_view_page")
            result=cursor.fetchall()

            for row in result:
                table.insert("","end",values=row)
            print(result)

            cursor.close()
            conn.close()



        def sales_view_page():
        # Create a new frame to contain the table
            table_frame = Frame(content_frame,bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)
            
            table_frame.pack(expand=True, fill=BOTH)

             
            style=ttk.Style()

            print(style.theme_names())
            style.theme_use('clam')
            style.configure("New.Treeview.Heading",background="#0077b3",foreground="white",font=("Arial",17))
            style.configure("New.Treeview",rowheight=50,fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Sale ID", "Sale Date", "Sale Time", "Sale Amount", "Customer ID", "Employee ID"),show="headings",style="New.Treeview")
            table.heading("Sale ID", text="Sale ID",anchor=CENTER)
            table.heading("Sale Date", text="Sale Date",anchor=CENTER)
            table.heading("Sale Time", text="Sale Time",anchor=CENTER)
            table.heading("Sale Amount", text="Sale Amount",anchor=CENTER)
            table.heading("Customer ID", text="Customer ID",anchor=CENTER)
            table.heading("Employee ID", text="Employee ID",anchor=CENTER)

                            
            table.column("Sale ID", width=100,anchor=CENTER)
            table.column("Sale Date", width=100,anchor=CENTER)
            table.column("Sale Time", width=100,anchor=CENTER)
            table.column("Sale Amount", width=50,anchor=CENTER)
            table.column("Customer ID", width=50,anchor=CENTER)
            table.column("Employee ID", width=120,anchor=CENTER)


            conn=mysql.connector.connect(host="localhost",username="root",password="ae-1265",database="medical_store")
            cursor=conn.cursor()

            cursor.execute("Select * from sales_view_page")
            result=cursor.fetchall()

            for row in result:
                table.insert("","end",values=row)

            cursor.close()
            conn.close()

   

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)



        
#===========================================================MANAGE INVENTORY PAGE================================================================================================================================================================
        def Manage_Inventory():
            # Create the main window
            main_frame = Frame(content_frame, bg="#e6e6e6")
            main_frame.pack(expand=True, fill="both")

            
            topnav_frame = Frame(main_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            def insert_medicine(medid, medname, qty, cat, price, loc):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "INSERT INTO meds (med_id, med_name, med_qty, category, med_price, location_rack) VALUES (%s, %s, %s, %s, %s, %s)"
                    data = (medid, medname, qty, cat, price, loc)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def add_medicine():
                medid = medid_entry.get()
                medname = medname_entry.get()
                qty = qty_entry.get()
                cat = cat_entry.get()
                price = price_entry.get()
                loc = loc_entry.get()
                if insert_medicine(medid, medname, qty, cat, price, loc):
                    print("Medicine added successfully!")
                else:
                    print("Failed to add medicine.")


            def update_medicine1(medid, medname, qty, cat, price, loc):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "UPDATE meds SET med_name=%s, med_qty=%s, category=%s, med_price=%s, location_rack=%s WHERE med_id=%s"
                    data = (medname, qty, cat, price, loc, medid)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def update_medicine():
                medid = medid_entry.get()
                medname = medname_entry.get()
                qty = qty_entry.get()
                cat = cat_entry.get()
                price = price_entry.get()
                loc = loc_entry.get()
                if update_medicine1(medid, medname, qty, cat, price, loc):
                    print("Medicine updated successfully!")
                else:
                    print("Failed to update medicine.")


            # Add a header
            header_label = Label(main_frame, text="MANAGE MEDICINE DETAILS", font=("Arial", 20), bg="#e6e6e6", fg="Black", padx=10, pady=5)
            header_label.pack(fill="x",padx=30,pady=20)

            # Create a frame for form elements
            form_frame = Frame(main_frame, bg="#f2f2f2")
            form_frame.pack(fill=BOTH,padx=30,pady=5)

            # Medicine ID
            medid_label = Label(form_frame, text="Medicine ID:", font=("Arial", 15), bg="#f2f2f2")
            medid_label.grid(row=0, column=0, padx=50, pady=15, sticky="w")
            medid_entry = Entry(form_frame, font=("Arial", 15),width=40)
            medid_entry.grid(row=1, column=0, padx=50, pady=15)
              

            # Medicine Name
            medname_label = Label(form_frame, text="Medicine Name:", font=("Arial", 15), bg="#f2f2f2")
            medname_label.grid(row=2, column=0, padx=50, pady=15, sticky="w")
            medname_entry = Entry(form_frame, font=("Arial", 15),width=40)
            medname_entry.grid(row=3, column=0, padx=50, pady=15)

            # Quantity
            qty_label = Label(form_frame, text="Quantity:", font=("Arial", 15), bg="#f2f2f2")
            qty_label.grid(row=4, column=0, padx=50, pady=15, sticky="w")
            qty_entry = Entry(form_frame, font=("Arial", 15),width=40)
            qty_entry.grid(row=5, column=0, padx=50, pady=15)

            # Category
            cat_label = Label(form_frame, text="Category:", font=("Arial", 15), bg="#f2f2f2")
            cat_label.grid(row=6, column=0, padx=50, pady=15, sticky="w")
            cat_entry = Entry(form_frame, font=("Arial", 15),width=40)
            cat_entry.grid(row=7, column=0, padx=50, pady=15)

            # Price
            price_label = Label(form_frame, text="Price:", font=("Arial", 15), bg="#f2f2f2")
            price_label.grid(row=0, column=1, padx=100, pady=15, sticky="w")
            price_entry = Entry(form_frame, font=("Arial", 15),width=40)
            price_entry.grid(row=1, column=1, padx=100, pady=15)

            # Location
            loc_label =Label(form_frame, text="Location:", font=("Arial", 15), bg="#f2f2f2")
            loc_label.grid(row=2, column=1, padx=100, pady=15, sticky="w")
            loc_entry = Entry(form_frame, font=("Arial", 15),width=40)
            loc_entry.grid(row=3, column=1, padx=100, pady=15)

            #ADD button
            Add_medicine_btn = Button(form_frame, text="Add Medicine", font=("Arial", 15), bg="#0077b3", fg="white", command=add_medicine,width=20)
            Add_medicine_btn.grid(row=4,column=1, padx=100, pady=15)

            # Update button
            update_btn = Button(form_frame, text="Update", font=("Arial", 15), bg="#0077b3", fg="white", command=update_medicine,width=20)
            update_btn.grid(row=5,column=1, padx=100, pady=15)


        def Inventory_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 17))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Med ID", "Med Name", "Med Qty", "Category", "Med Price", "Location Rack"), show="headings", style="New.Treeview")
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Med Name", text="Med Name", anchor=CENTER)
            table.heading("Med Qty", text="Med Qty", anchor=CENTER)
            table.heading("Category", text="Category", anchor=CENTER)
            table.heading("Med Price", text="Med Price", anchor=CENTER)
            table.heading("Location Rack", text="Location Rack", anchor=CENTER)

            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Med Name", width=150, anchor=CENTER)
            table.column("Med Qty", width=100, anchor=CENTER)
            table.column("Category", width=100, anchor=CENTER)
            table.column("Med Price", width=100, anchor=CENTER)
            table.column("Location Rack", width=120, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM meds_view_page")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)

        
        def Med_LowStock():
            
            Report_table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(Report_table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            

            Report_table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 17))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(Report_table_frame, columns=("Med ID", "Med Name", "Med Qty", "Category", "Med Price", "Location Rack"), show="headings", style="New.Treeview")
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Med Name", text="Med Name", anchor=CENTER)
            table.heading("Med Qty", text="Med Qty", anchor=CENTER)
            table.heading("Category", text="Category", anchor=CENTER)
            table.heading("Med Price", text="Med Price", anchor=CENTER)
            table.heading("Location Rack", text="Location Rack", anchor=CENTER)

            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Med Name", width=150, anchor=CENTER)
            table.column("Med Qty", width=100, anchor=CENTER)
            table.column("Category", width=100, anchor=CENTER)
            table.column("Med Price", width=100, anchor=CENTER)
            table.column("Location Rack", width=120, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM meds_view_page where med_qty < 200")
            result = cursor.fetchall()

            if result:
                for row in result:
                    table.insert("", "end", values=row)
            else:
                messagebox.showinfo(Report_table_frame,"No medicines are on low stock")

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(Report_table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)



        def Med_ExpireSoon():
                pass
        

        def transaction_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            print(style.theme_names())
            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 17))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Med ID", "Sale ID", "Sale Quantity", "Medicine Name", "Medicine Price"), show="headings", style="New.Treeview")
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Sale ID", text="Sale ID", anchor=CENTER)
            table.heading("Sale Quantity", text="Sale Quantity", anchor=CENTER)
            table.heading("Medicine Name", text="Medicine Name", anchor=CENTER)
            table.heading("Medicine Price", text="Medicine Price", anchor=CENTER)

            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Sale ID", width=100, anchor=CENTER)
            table.column("Sale Quantity", width=100, anchor=CENTER)
            table.column("Medicine Name", width=200, anchor=CENTER)
            table.column("Medicine Price", width=100, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM transaction")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            table.pack(fill=BOTH,expand=True)







        


    def Add_new_sale(self):
        twin=Toplevel(self.win)
        transaction_page=TransactionPage(twin)



#===================================================================================Admin Page==============================================================================================================      





class AdminPage:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1580x850")
        self.win.title("Admin DashBoard")

        self.win.configure(background="#e6e6e6")
        self.create_widgets()

    def create_widgets(self):

 
        def switch(page):     #===================Actual mechanism behind different pages is this function====================================================
            
            for frame in content_frame.winfo_children():
                frame.destroy()
                self.win.update()
            page()
#========================================================Inventory toggle menu================================================
        def Inventory_toggle_menu():
            def collapse_Inventory_menu():
                Inventory_menu_frame.destroy()
                Inventory_button.config(text='Inventory ▼')
                Inventory_button.config(command=Inventory_toggle_menu)

            Inventory_menu_frame=Frame(sidebar_frame,bg="#003366")
            temp_frame=Frame(Inventory_menu_frame,bg="white")
            temp_frame.pack(fill=X)
            window_height=80    #root.winfo_height() gives current height of the window
            Manage_Inventory_btn=Button(Inventory_menu_frame,text="Manage Inventory", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(Manage_Inventory),highlightthickness=0)
            Manage_Inventory_btn.pack(pady=5)
            View_Inventory_btn=Button(Inventory_menu_frame,text="View Inventory", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(Inventory_view_page),highlightthickness=0)
            View_Inventory_btn.pack(pady=5)
            Inventory_menu_frame.place(x=0,y=318,height=window_height,width=250)
            Inventory_button.config(text='Inventory ▽')
            Inventory_button.config(command=collapse_Inventory_menu)
#===============================================================================Employee Toggle menu=============================================
        def Employee_toggle_menu():
            def collapse_Employee_menu():
                Employee_menu_frame.destroy()
                Employee_button.config(text='Employee ▼')
                Employee_button.config(command=Employee_toggle_menu)

            Employee_menu_frame = Frame(sidebar_frame, bg="#003366")
            temp_frame=Frame(Employee_menu_frame,bg="white")
            temp_frame.pack(fill=X)
            window_height = 80
            Manage_Employee_btn = Button(Employee_menu_frame, text="Manage Employee", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda: switch(Manage_Employee), highlightthickness=0)
            Manage_Employee_btn.pack(pady=5)
            View_Employee_btn = Button(Employee_menu_frame, text="View Employees", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda: switch(employee_view_page), highlightthickness=0)
            View_Employee_btn.pack(pady=5)
            Employee_menu_frame.place(x=0, y=420, height=window_height, width=250)
            Employee_button.config(text='Employee ▽')
            Employee_button.config(command=collapse_Employee_menu)


#============================================================================Stock purchase Toggle menu============================================
        def Stock_Purchase_toggle_menu():
            def collapse_Stock_Purchase_menu():
                Stock_Purchase_menu_frame.destroy()
                Stock_Purchase_button.config(text='Stock Purchase ▼')
                Stock_Purchase_button.config(command=Stock_Purchase_toggle_menu)

            Stock_Purchase_menu_frame = Frame(sidebar_frame, bg="#003366")
            temp_frame=Frame(Stock_Purchase_menu_frame,bg="white")
            temp_frame.pack(fill=X)
            window_height = 80
            Manage_Stock_Purchase_btn = Button(Stock_Purchase_menu_frame, text="Manage Stock Purchase", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda: switch(Manage_stock_purchase), highlightthickness=0)
            Manage_Stock_Purchase_btn.pack(pady=5)

            View_Stock_Purchase_btn = Button(Stock_Purchase_menu_frame, text="View Stock Purchase", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda: switch(stock_purchase_view_page), highlightthickness=0)
            View_Stock_Purchase_btn.pack(pady=5)

            Stock_Purchase_menu_frame.place(x=0, y=545, height=window_height, width=250)
            Stock_Purchase_button.config(text='Stock Purchase ▽')
            Stock_Purchase_button.config(command=collapse_Stock_Purchase_menu)

#============================================Report Toggle Menu==================================================================
        def Reports_toggle_menu():
            def collapse_Reports_menu():
                Reports_menu_frame.destroy()
                Reports_button.config(text='Reports ▼')
                Reports_button.config(command=Reports_toggle_menu)

            Reports_menu_frame = Frame(sidebar_frame, bg="#003366")
            temp_frame=Frame(Reports_menu_frame,bg="white")
            temp_frame.pack(fill=X)
            window_height = 80
            Manage_Reports_btn = Button(Reports_menu_frame, text="Medicines-Low Stock", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda:switch(Med_LowStock), highlightthickness=0)
            Manage_Reports_btn.pack(pady=5)

            View_Reports_btn = Button(Reports_menu_frame, text="Medicines-Soon to Expire", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0, command=lambda:switch(Med_ExpireSoon), highlightthickness=0)
            View_Reports_btn.pack(pady=5)

            Reports_menu_frame.place(x=0, y=660, height=window_height, width=250)
            Reports_button.config(text='Reports ▽')
            Reports_button.config(command=collapse_Reports_menu)



    
        # Header
        header_label = Label(self.win, text="Medical Store Management System | ADMIN", font=("Times New Roman", 18), bg="#003366", fg="white", pady=10)  
        header_label.pack(side=TOP,fill=X)

        # Sidebar
        sidebar_frame = Frame(self.win, bg="#003366", width=250,padx=0)  
        sidebar_frame.pack(side=LEFT, fill=Y)

        sidebar_label = Label(sidebar_frame, text="Menu", font=("Arial", 18), bg="#003366", fg="white")
        sidebar_label.pack(pady=10)

        Dashboard_button = Button(sidebar_frame, text="Dashboard ", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(Dashboard))
        Dashboard_button.pack(fill=X, pady=10)

        Suppliers_button = Button(sidebar_frame, text="Suppliers", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(suppliers))
        Suppliers_button.pack(fill=X, pady=10)

        customer_view_btn = Button(sidebar_frame, text="View Customers", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(customer_view_page))
        customer_view_btn.pack(fill=X, pady=10)

        Sales_invoicebtn = Button(sidebar_frame, text="View Sales Invoice Details", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=lambda:switch(sales_view_page))
        Sales_invoicebtn.pack(fill=X, pady=10)


        Inventory_button = Button(sidebar_frame, text="Inventory ▼", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=Inventory_toggle_menu,relief="flat",activebackground="#003366")
        Inventory_button.pack(fill=X, pady=15)

        Employee_button = Button(sidebar_frame, text="Employee ▼", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=Employee_toggle_menu,relief="flat",activebackground="#003366")
        Employee_button.pack(fill=X, pady=50)

        Stock_Purchase_button = Button(sidebar_frame, text="Stock Purchase ▼", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=Stock_Purchase_toggle_menu)
        Stock_Purchase_button.pack(fill=X, pady=40)

        Reports_button = Button(sidebar_frame, text="Reports ▼", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=0,command=Reports_toggle_menu)
        Reports_button.pack(fill=X, pady=40)



        


       





        # Content
        content_frame = Frame(self.win, bg="white")
        content_frame.pack(fill=BOTH, expand=True)

        topnav_frame = Frame(content_frame, bg="#003366")
        topnav_frame.pack(side=TOP, fill=X)

        logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
        logout_button.pack(side=RIGHT, padx=20, pady=10)

        main_content_frame = Frame(content_frame, bg="white")
        main_content_frame.pack(expand=True, fill=BOTH)

        Admindash_frame =Frame(main_content_frame, bg="lightgrey",pady=10, bd=0)  
        Admindash_frame.pack(side=TOP,pady=10)

        Admindash_label =Label(Admindash_frame, text="ADMIN DASHBOARD", font=("Arial", 15), bg="lightgrey", fg="white",width=100)  
        Admindash_label.pack(pady=2)


        

        
        # Main Content
        self.photoimg1 =PhotoImage(file="carticon1.png").subsample(2)

        sale_button = Button(main_content_frame, image=self.photoimg1, text="Add New Sale", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=self.Add_new_sale)
        sale_button.image = self.photoimg1  # Keep a reference to avoid garbage collection
        sale_button.place(x=250, y=100)

        self.photoimg2 = PhotoImage(file="inventory.png").subsample(2)
        
        inventory_button = Button(main_content_frame, image=self.photoimg2, text="View Inventory", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Inventory_view_page))
        inventory_button.image = self.photoimg2 
        inventory_button.place(x=550, y=100)

        self.photoimg3 =PhotoImage(file="emp.png").subsample(2)

        employee_button = Button(main_content_frame, image=self.photoimg3, text="View Employees", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid" ,command=lambda:switch(employee_view_page))
        employee_button.image = self.photoimg3
        employee_button.place(x=850, y=100)

        self.photoimg4 =PhotoImage(file="moneyicon.png").subsample(2)

        transaction_button = Button(main_content_frame, image=self.photoimg4, text="View Transactions", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(transaction_view_page))
        transaction_button.image = self.photoimg4
        transaction_button.place(x=400, y=400)

        self.photoimg5 =PhotoImage(file="alert.png").subsample(2)

        alert_button = Button(main_content_frame, image=self.photoimg5, text="Low stock alert", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Med_LowStock))
        alert_button.image = self.photoimg5
        alert_button.place(x=700, y=400)

#=====================================================================DashBoard==================================================

        def Dashboard():
            topnav_frame = Frame(content_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            main_content_frame = Frame(content_frame, bg="white")
            main_content_frame.pack(expand=True, fill=BOTH)

            Admindash_frame =Frame(main_content_frame, bg="lightgrey",pady=10, bd=0)  
            Admindash_frame.pack(side=TOP,pady=10)

            Admindash_label =Label(Admindash_frame, text="ADMIN DASHBOARD", font=("Arial", 15), bg="lightgrey", fg="white",width=100)  
            Admindash_label.pack(pady=2)

            # Main Content
            self.photoimg1 =PhotoImage(file="carticon1.png").subsample(2)

            sale_button = Button(main_content_frame, image=self.photoimg1, text="Add New Sale", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=self.Add_new_sale)
            sale_button.image = self.photoimg1  # Keep a reference to avoid garbage collection
            sale_button.place(x=250, y=100)

            self.photoimg2 = PhotoImage(file="inventory.png").subsample(2)
            
            inventory_button = Button(main_content_frame, image=self.photoimg2, text="View Inventory", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Inventory_view_page))
            inventory_button.image = self.photoimg2 
            inventory_button.place(x=550, y=100)

            self.photoimg3 =PhotoImage(file="emp.png").subsample(2)

            employee_button = Button(main_content_frame, image=self.photoimg3, text="View Employees", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid" ,command=lambda:switch(employee_view_page))
            employee_button.image = self.photoimg3
            employee_button.place(x=850, y=100)

            self.photoimg4 =PhotoImage(file="moneyicon.png").subsample(2)

            transaction_button = Button(main_content_frame, image=self.photoimg4, text="View Transactions", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(transaction_view_page))
            transaction_button.image = self.photoimg4
            transaction_button.place(x=400, y=400)

            self.photoimg5 =PhotoImage(file="alert.png").subsample(2)

            alert_button = Button(main_content_frame, image=self.photoimg5, text="Low stock alert", font=("Arial", 18), bg="white", fg="#003366", bd=2,highlightthicknes=2,relief="solid",command=lambda:switch(Med_LowStock))
            alert_button.image = self.photoimg5
            alert_button.place(x=700, y=400)


#======================================================Customer View Page============================================================

        def customer_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame,bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)
            
            table_frame.pack(expand=True, fill=BOTH)

            style=ttk.Style()

            print(style.theme_names())
            style.theme_use('clam')
            style.configure("New.Treeview.Heading",background="#0077b3",foreground="white",font=("Arial",17))
            style.configure("New.Treeview",rowheight=50,fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Customer ID", "First Name", "Last Name","Sex", "Phone Number", "Email Address"),show="headings",style="New.Treeview")
            table.heading("Customer ID", text="Customer ID",anchor=CENTER)
            table.heading("First Name", text="First Name",anchor=CENTER)
            table.heading("Last Name", text="Last Name",anchor=CENTER)
            table.heading("Sex", text="Sex",anchor=CENTER)
            table.heading("Phone Number", text="Phone Number",anchor=CENTER)
            table.heading("Email Address", text="Email Address",anchor=CENTER)

            

            table.column("Customer ID", width=100,anchor=CENTER)
            table.column("First Name", width=100,anchor=CENTER)
            table.column("Last Name", width=100,anchor=CENTER)
            table.column("Sex", width=50,anchor=CENTER)
            table.column("Phone Number", width=120,anchor=CENTER)
            table.column("Email Address", width=200,anchor=CENTER)
            #table.column("Action", width=150,anchor=CENTER)

           

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)

            conn=mysql.connector.connect(host="localhost",username="root",password="ae-1265",database="medical_store")
            cursor=conn.cursor()

            cursor.execute("Select * from customer_view_page")
            result=cursor.fetchall()

            for row in result:
                table.insert("","end",values=row)
            print(result)

            cursor.close()
            conn.close()

#====================================================Sales View Page==========================================================================

        def sales_view_page():
        # Create a new frame to contain the table
            table_frame = Frame(content_frame,bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)
            
            table_frame.pack(expand=True, fill=BOTH)

             
            style=ttk.Style()

            print(style.theme_names())
            style.theme_use('clam')
            style.configure("New.Treeview.Heading",background="#0077b3",foreground="white",font=("Arial",17))
            style.configure("New.Treeview",rowheight=50,fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Sale ID", "Sale Date", "Sale Time", "Sale Amount", "Customer ID", "Employee ID"),show="headings",style="New.Treeview")
            table.heading("Sale ID", text="Sale ID",anchor=CENTER)
            table.heading("Sale Date", text="Sale Date",anchor=CENTER)
            table.heading("Sale Time", text="Sale Time",anchor=CENTER)
            table.heading("Sale Amount", text="Sale Amount",anchor=CENTER)
            table.heading("Customer ID", text="Customer ID",anchor=CENTER)
            table.heading("Employee ID", text="Employee ID",anchor=CENTER)

                            
            table.column("Sale ID", width=100,anchor=CENTER)
            table.column("Sale Date", width=100,anchor=CENTER)
            table.column("Sale Time", width=100,anchor=CENTER)
            table.column("Sale Amount", width=50,anchor=CENTER)
            table.column("Customer ID", width=50,anchor=CENTER)
            table.column("Employee ID", width=120,anchor=CENTER)


            conn=mysql.connector.connect(host="localhost",username="root",password="ae-1265",database="medical_store")
            cursor=conn.cursor()

            cursor.execute("Select * from sales_view_page")
            result=cursor.fetchall()

            for row in result:
                table.insert("","end",values=row)

            cursor.close()
            conn.close()

   

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)



        
#===========================================================MANAGE INVENTORY PAGE================================================================================================================================================================
        def Manage_Inventory():
            # Create the main window
            main_frame = Frame(content_frame, bg="#e6e6e6")
            main_frame.pack(expand=True, fill="both")

            
            topnav_frame = Frame(main_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            def insert_medicine(medid, medname, qty, cat, price, loc):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "INSERT INTO meds (med_id, med_name, med_qty, category, med_price, location_rack) VALUES (%s, %s, %s, %s, %s, %s)"
                    data = (medid, medname, qty, cat, price, loc)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def add_medicine():
                medid = medid_entry.get()
                medname = medname_entry.get()
                qty = qty_entry.get()
                cat = cat_entry.get()
                price = price_entry.get()
                loc = loc_entry.get()
                if insert_medicine(medid, medname, qty, cat, price, loc):
                    print("Medicine added successfully!")
                else:
                    print("Failed to add medicine.")


            def update_medicine1(medid, medname, qty, cat, price, loc):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "UPDATE meds SET med_name=%s, med_qty=%s, category=%s, med_price=%s, location_rack=%s WHERE med_id=%s"
                    data = (medname, qty, cat, price, loc, medid)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def update_medicine():
                medid = medid_entry.get()
                medname = medname_entry.get()
                qty = qty_entry.get()
                cat = cat_entry.get()
                price = price_entry.get()
                loc = loc_entry.get()
                if update_medicine1(medid, medname, qty, cat, price, loc):
                    print("Medicine updated successfully!")
                else:
                    print("Failed to update medicine.")


            # Add a header
            header_label = Label(main_frame, text="MANAGE MEDICINE DETAILS", font=("Arial", 20), bg="#e6e6e6", fg="Black", padx=10, pady=5)
            header_label.pack(fill="x",padx=30,pady=20)

            # Create a frame for form elements
            form_frame = Frame(main_frame, bg="#f2f2f2")
            form_frame.pack(fill=BOTH,padx=30,pady=5)

            # Medicine ID
            medid_label = Label(form_frame, text="Medicine ID:", font=("Arial", 15), bg="#f2f2f2")
            medid_label.grid(row=0, column=0, padx=50, pady=15, sticky="w")
            medid_entry = Entry(form_frame, font=("Arial", 15),width=40)
            medid_entry.grid(row=1, column=0, padx=50, pady=15)
              

            # Medicine Name
            medname_label = Label(form_frame, text="Medicine Name:", font=("Arial", 15), bg="#f2f2f2")
            medname_label.grid(row=2, column=0, padx=50, pady=15, sticky="w")
            medname_entry = Entry(form_frame, font=("Arial", 15),width=40)
            medname_entry.grid(row=3, column=0, padx=50, pady=15)

            # Quantity
            qty_label = Label(form_frame, text="Quantity:", font=("Arial", 15), bg="#f2f2f2")
            qty_label.grid(row=4, column=0, padx=50, pady=15, sticky="w")
            qty_entry = Entry(form_frame, font=("Arial", 15),width=40)
            qty_entry.grid(row=5, column=0, padx=50, pady=15)

            # Category
            cat_label = Label(form_frame, text="Category:", font=("Arial", 15), bg="#f2f2f2")
            cat_label.grid(row=6, column=0, padx=50, pady=15, sticky="w")
            cat_entry = Entry(form_frame, font=("Arial", 15),width=40)
            cat_entry.grid(row=7, column=0, padx=50, pady=15)

            # Price
            price_label = Label(form_frame, text="Price:", font=("Arial", 15), bg="#f2f2f2")
            price_label.grid(row=0, column=1, padx=100, pady=15, sticky="w")
            price_entry = Entry(form_frame, font=("Arial", 15),width=40)
            price_entry.grid(row=1, column=1, padx=100, pady=15)

            # Location
            loc_label =Label(form_frame, text="Location:", font=("Arial", 15), bg="#f2f2f2")
            loc_label.grid(row=2, column=1, padx=100, pady=15, sticky="w")
            loc_entry = Entry(form_frame, font=("Arial", 15),width=40)
            loc_entry.grid(row=3, column=1, padx=100, pady=15)

            #ADD button
            Add_medicine_btn = Button(form_frame, text="Add Medicine", font=("Arial", 15), bg="#0077b3", fg="white", command=add_medicine,width=20)
            Add_medicine_btn.grid(row=4,column=1, padx=100, pady=15)

            # Update button
            update_btn = Button(form_frame, text="Update", font=("Arial", 15), bg="#0077b3", fg="white", command=update_medicine,width=20)
            update_btn.grid(row=5,column=1, padx=100, pady=15)



#==========================================Inventory View Page======================================================================================

        def Inventory_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 17))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Med ID", "Med Name", "Med Qty", "Category", "Med Price", "Location Rack"), show="headings", style="New.Treeview")
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Med Name", text="Med Name", anchor=CENTER)
            table.heading("Med Qty", text="Med Qty", anchor=CENTER)
            table.heading("Category", text="Category", anchor=CENTER)
            table.heading("Med Price", text="Med Price", anchor=CENTER)
            table.heading("Location Rack", text="Location Rack", anchor=CENTER)

            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Med Name", width=150, anchor=CENTER)
            table.column("Med Qty", width=100, anchor=CENTER)
            table.column("Category", width=100, anchor=CENTER)
            table.column("Med Price", width=100, anchor=CENTER)
            table.column("Location Rack", width=120, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM meds_view_page")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)

#=====================================================================Employee view Page============================================================================
        def employee_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 15))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("E_ID","E_Fname", "E_Lname", "Bdate", "E_gender", "E_JDate", "E_ADD", "E_phno", "E_Salary", "E_username","E_password"), show="headings", style="New.Treeview")
            table.heading("E_Fname", text="First Name", anchor=CENTER)
            table.heading("E_Lname", text="Last Name", anchor=CENTER)
            table.heading("Bdate", text="Birth Date", anchor=CENTER)
            table.heading("E_gender", text="Sex", anchor=CENTER)
            table.heading("E_JDate", text="Join Date", anchor=CENTER)
            table.heading("E_ADD", text="Address", anchor=CENTER)
            table.heading("E_phno", text="Phone Number", anchor=CENTER)
            table.heading("E_Salary", text="Salary", anchor=CENTER)
            table.heading("E_ID", text="E_ID", anchor=CENTER)
            table.heading("E_username", text="E_Username", anchor=CENTER)
            table.heading("E_password", text="E_password", anchor=CENTER)


            table.column("E_ID", width=100, anchor=CENTER)
            table.column("E_Fname", width=100, anchor=CENTER)
            table.column("E_Lname", width=100, anchor=CENTER)
            table.column("Bdate", width=100, anchor=CENTER)
            table.column("E_gender", width=50, anchor=CENTER)
            table.column("E_JDate", width=100, anchor=CENTER)
            table.column("E_ADD", width=100, anchor=CENTER)
            table.column("E_phno", width=100, anchor=CENTER)
            table.column("E_Salary", width=100, anchor=CENTER)
            table.column("E_password", width=100, anchor=CENTER)
            table.column("E_username", width=100, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM employee_view_page")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)
#=============================================================Stock Purchased view Page==============================================================

        def stock_purchase_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 15))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Purchase ID", "Med ID", "Supplier ID", "Quantity", "Cost", "Purchase Date", "Manufacture Date", "Expiry Date"), show="headings", style="New.Treeview")
            table.heading("Purchase ID", text="Purchase ID", anchor=CENTER)
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Supplier ID", text="Supplier ID", anchor=CENTER)
            table.heading("Quantity", text="Quantity", anchor=CENTER)
            table.heading("Cost", text="Cost", anchor=CENTER)
            table.heading("Purchase Date", text="Purchase Date", anchor=CENTER)
            table.heading("Manufacture Date", text="Manufacture Date", anchor=CENTER)
            table.heading("Expiry Date", text="Expiry Date", anchor=CENTER)

            table.column("Purchase ID", width=100, anchor=CENTER)
            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Supplier ID", width=100, anchor=CENTER)
            table.column("Quantity", width=80, anchor=CENTER)
            table.column("Cost", width=80, anchor=CENTER)
            table.column("Purchase Date", width=120, anchor=CENTER)
            table.column("Manufacture Date", width=120, anchor=CENTER)
            table.column("Expiry Date", width=120, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM stock_purchase_view_page")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)

        def Manage_Employee():
            # Create the main window
            main_frame = Frame(content_frame, bg="#e6e6e6")
            main_frame.pack(expand=True, fill="both")

            
            topnav_frame = Frame(main_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            def insert_employee(E_idP, E_fname, E_Lname, E_Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "INSERT INTO employee (E_id, E_fname, E_Lname, Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    data = (E_idP, E_fname, E_Lname, E_Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def add_employee_personal():
                E_idP = E_idP_entry.get()
                E_fname = E_fname_entry.get()
                E_Lname = E_Lname_entry.get()
                E_Bdate = E_Bdate_entry.get()
                E_Gender = E_Gender_entry.get()
                E_jDate = E_jDate_entry.get()
                E_ADD = E_ADD_entry.get()
                E_phno = E_phno_entry.get()
                E_Salary = E_Salary_entry.get()
                if insert_employee(E_idP, E_fname, E_Lname, E_Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary):
                    print("Employee personal information added successfully!")
                else:
                    print("Failed to add employee personal information.")

            def update_employee(E_idP, E_fname, E_Lname, E_Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "UPDATE employee SET E_fname=%s, E_Lname=%s, Bdate=%s, E_Gender=%s, E_jDate=%s, E_ADD=%s, E_phno=%s, E_Salary=%s WHERE E_id=%s"
                    data = (E_fname, E_Lname, E_Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary, E_idP)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def update_employee_personal():
                E_idP = E_idP_entry.get()
                E_fname = E_fname_entry.get()
                E_Lname = E_Lname_entry.get()
                E_Bdate = E_Bdate_entry.get()
                E_Gender = E_Gender_entry.get()
                E_jDate = E_jDate_entry.get()
                E_ADD = E_ADD_entry.get()
                E_phno = E_phno_entry.get()
                E_Salary = E_Salary_entry.get()
                if update_employee(E_idP, E_fname, E_Lname, E_Bdate, E_Gender, E_jDate, E_ADD, E_phno, E_Salary):
                    print("Employee personal information updated successfully!")
                else:
                    print("Failed to update employee personal information.")


            E_personal_frame=LabelFrame(main_frame,text="Employee Personal Information",font=("Arial", 15),relief="solid",width=770,bg="#e6e6e6")
            E_idP_label = Label(E_personal_frame, text="Employee ID:", font=("Arial", 15), bg="#e6e6e6")
            E_idP_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            E_idP_entry = Entry(E_personal_frame, font=("Arial", 15),width=40,relief="flat")
            E_idP_entry.grid(row=1, column=0, padx=10, pady=5)

            # E_fname
            E_fname_label = Label(E_personal_frame, text="First Name:", font=("Arial", 15), bg="#e6e6e6")
            E_fname_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
            E_fname_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_fname_entry.grid(row=3, column=0, padx=10, pady=5)

            # E_Lname
            E_Lname_label = Label(E_personal_frame, text="Last Name:", font=("Arial", 15), bg="#e6e6e6")
            E_Lname_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
            E_Lname_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_Lname_entry.grid(row=5, column=0, padx=10, pady=5)

            # E_Bdate
            E_Bdate_label = Label(E_personal_frame, text="Birth Date:", font=("Arial", 15), bg="#e6e6e6")
            E_Bdate_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
            E_Bdate_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_Bdate_entry.grid(row=7, column=0, padx=10, pady=5)

            # E_Gender
            E_Gender_label = Label(E_personal_frame, text="Gender:", font=("Arial", 15), bg="#e6e6e6")
            E_Gender_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
            E_Gender_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_Gender_entry.grid(row=9, column=0, padx=10, pady=5)

            # E_jDate
            E_jDate_label = Label(E_personal_frame, text="Join Date:", font=("Arial", 15), bg="#e6e6e6")
            E_jDate_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
            E_jDate_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_jDate_entry.grid(row=1, column=1, padx=10, pady=5)

            # E_ADD
            E_ADD_label = Label(E_personal_frame, text="Address:", font=("Arial", 15), bg="#e6e6e6")
            E_ADD_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
            E_ADD_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_ADD_entry.grid(row=3, column=1, padx=10, pady=5)

            # E_phno
            E_phno_label = Label(E_personal_frame, text="Phone Number:", font=("Arial", 15), bg="#e6e6e6")
            E_phno_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
            E_phno_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_phno_entry.grid(row=5, column=1, padx=10, pady=5)

            # E_Salary
            E_Salary_label = Label(E_personal_frame, text="Salary:", font=("Arial", 15), bg="#e6e6e6")
            E_Salary_label.grid(row=6, column=1, padx=10, pady=5, sticky="w")
            E_Salary_entry = Entry(E_personal_frame, font=("Arial", 15), width=40,relief="flat")
            E_Salary_entry.grid(row=7, column=1, padx=10, pady=5)

            E_personal_frame.pack(side=TOP,padx=5,pady=10)

            #ADD button
            Add_EP_btn = Button(E_personal_frame, text="Add", font=("Arial", 15), bg="#0077b3", fg="white",width=20,command=add_employee_personal)
            Add_EP_btn.grid(row=9,column=1, padx=20, pady=5)

            # Update button
            update_EP_btn = Button(E_personal_frame, text="Update", font=("Arial", 15), bg="#0077b3", fg="white", width=20,command=update_employee_personal)
            update_EP_btn.grid(row=9,column=2, padx=20, pady=5)

            def insert_employee_login(E_idL, E_username, E_password):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "INSERT INTO emp_login (E_id, E_username, E_password) VALUES (%s, %s, %s)"
                    data = (E_idL, E_username, E_password)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def add_employee_login():
                E_idL = E_idL_entry.get()
                E_username = E_username_entry.get()
                E_password = E_password_entry.get()
                if insert_employee_login(E_idL, E_username, E_password):
                    print("Employee login information added successfully!")
                else:
                    print("Failed to add employee login information.")

            def update_employee_login(E_username, E_password,E_idL):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "UPDATE emp_login SET E_username=%s, E_password=%s WHERE E_id=%s"
                    data = (E_username, E_password, E_idL)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def update_employee_login_info():
                E_idL = E_idL_entry.get()
                E_username = E_username_entry.get()
                E_password = E_password_entry.get()
                if update_employee_login( E_username, E_password,E_idL):
                    print("Employee login information updated successfully!")
                else:
                    print("Failed to update employee login information.")


            
            E_login_frame=LabelFrame(main_frame,text="Employee Login Information",font=("Arial", 15),relief="solid",width=770,bg="#e6e6e6")
            E_idL_label = Label(E_login_frame, text="Employee ID:", font=("Arial", 15), bg="#e6e6e6")
            E_idL_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            E_idL_entry = Entry(E_login_frame, font=("Arial", 15),width=40,relief="flat")
            E_idL_entry.grid(row=1, column=0, padx=10, pady=5)

            # E_username
            E_username_label = Label(E_login_frame, text="Username:", font=("Arial", 15), bg="#e6e6e6")
            E_username_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
            E_username_entry = Entry(E_login_frame, font=("Arial", 15), width=40,relief="flat")
            E_username_entry.grid(row=3, column=0, padx=10, pady=5)

            # E_password
            E_password_label = Label(E_login_frame, text="Password:", font=("Arial", 15), bg="#e6e6e6")
            E_password_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
            E_password_entry = Entry(E_login_frame, font=("Arial", 15), width=40,relief="flat")
            E_password_entry.grid(row=1, column=1, padx=10, pady=5)

            E_login_frame.pack(side=TOP,padx=5,pady=10)

            #ADD button
            Add_EL_btn = Button(E_login_frame, text="Add", font=("Arial", 15), bg="#0077b3", fg="white", width=20,command=add_employee_login)
            Add_EL_btn.grid(row=3,column=1, padx=20, pady=5)

            # Update button
            update_EL_btn = Button(E_login_frame, text="Update", font=("Arial", 15), bg="#0077b3", fg="white",width=20,command=update_employee_login_info)
            update_EL_btn.grid(row=3,column=2, padx=20, pady=5)

        def suppliers():

            main_frame = Frame(content_frame, bg="#e6e6e6")
            main_frame.pack(expand=True, fill="both")

            
            topnav_frame = Frame(main_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            
            table_frame = Frame(main_frame, bg="white",width=770,height=400)
            table_frame.pack(fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 15))
            style.configure("New.Treeview", rowheight=35, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Supplier ID", "Supplier Name", "Supplier Address", "Supplier Phone"), show="headings", style="New.Treeview")
            table.heading("Supplier ID", text="Supplier ID", anchor=CENTER)
            table.heading("Supplier Name", text="Supplier Name", anchor=CENTER)
            table.heading("Supplier Address", text="Supplier Address", anchor=CENTER)
            table.heading("Supplier Phone", text="Supplier Phone", anchor=CENTER)

            table.column("Supplier ID", width=100, anchor=CENTER)
            table.column("Supplier Name", width=200, anchor=CENTER)
            table.column("Supplier Address", width=200, anchor=CENTER)
            table.column("Supplier Phone", width=150, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM suppliers")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(fill=BOTH)


            def insert_supplier(sup_id, sup_name, sup_Add, sup_phno):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "INSERT INTO suppliers (sup_id, sup_name, sup_Add, sup_phno) VALUES (%s, %s, %s, %s)"
                    data = (sup_id, sup_name, sup_Add, sup_phno)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def add_supplier():
                sup_id = S_id_entry.get()
                sup_name = S_name_entry.get()
                sup_Add = S_add_entry.get()
                sup_phno = S_phno_entry.get()
                if insert_supplier(sup_id, sup_name, sup_Add, sup_phno):
                    print("Supplier added successfully!")
                else:
                    print("Failed to add supplier.")

            def update_supplier(sup_id, sup_name, sup_Add, sup_phno):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "UPDATE suppliers SET sup_name=%s, sup_Add=%s, sup_phno=%s WHERE sup_id=%s"
                    data = (sup_name, sup_Add, sup_phno, sup_id)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def update_supplier_info():
                sup_id = S_id_entry.get()
                sup_name = S_name_entry.get()
                sup_Add = S_add_entry.get()
                sup_phno = S_phno_entry.get()
                if update_supplier(sup_id, sup_name, sup_Add, sup_phno):
                    print("Supplier information updated successfully!")
                else:
                    print("Failed to update supplier information.")


            
            
            

            # Create a LabelFrame for Supplier Information
            S_info_frame = LabelFrame(main_frame, text="Supplier Information", font=("Arial", 15), relief="solid", width=770, bg="#e6e6e6")

            # Supplier ID
            S_id_label = Label(S_info_frame, text="Supplier ID:", font=("Arial", 15), bg="#e6e6e6")
            S_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            S_id_entry = Entry(S_info_frame, font=("Arial", 15), width=40, relief="flat")
            S_id_entry.grid(row=1, column=0, padx=10, pady=5)

            # Supplier Name
            S_name_label = Label(S_info_frame, text="Supplier Name:", font=("Arial", 15), bg="#e6e6e6")
            S_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
            S_name_entry = Entry(S_info_frame, font=("Arial", 15), width=40, relief="flat")
            S_name_entry.grid(row=3, column=0, padx=10, pady=5)

            # Supplier Address
            S_add_label = Label(S_info_frame, text="Supplier Address:", font=("Arial", 15), bg="#e6e6e6")
            S_add_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
            S_add_entry = Entry(S_info_frame, font=("Arial", 15), width=40, relief="flat")
            S_add_entry.grid(row=1, column=1, padx=10, pady=5)

            # Supplier Phone Number
            S_phno_label = Label(S_info_frame, text="Supplier Phone:", font=("Arial", 15), bg="#e6e6e6")
            S_phno_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
            S_phno_entry = Entry(S_info_frame, font=("Arial", 15), width=40, relief="flat")
            S_phno_entry.grid(row=3, column=1, padx=10, pady=5)
            
            S_info_frame.pack(side=TOP, padx=20,expand=True,fill=BOTH)
           

            # ADD button
            Add_sup_btn = Button(S_info_frame, text="Add", font=("Arial", 15), bg="#0077b3", fg="white", width=20,command=add_supplier)
            Add_sup_btn.grid(row=4, column=0, padx=20, pady=5)

            # Update button
            update_sup_btn = Button(S_info_frame, text="Update", font=("Arial", 15), bg="#0077b3", fg="white", width=20,command=update_supplier_info)
            update_sup_btn.grid(row=4, column=1, padx=20, pady=5)
#============================================Add/Update Stock purchase=============================================================================
        def Manage_stock_purchase():

            


            def insert_in_stock(purchase_id,medid,supplier_id,p_qty,p_cost,p_date,mfg_date,exp_date):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "INSERT INTO purchase (purchase_id,med_id, supplier_id,p_qty,p_cost, p_date,mfg_date,exp_date) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"
                    data = (purchase_id,medid,supplier_id,p_qty,p_cost,p_date,mfg_date,exp_date)
                    cursor.execute(query, data)
                    conn.commit()

                    #-- Add the medicine quantity to the medicine table
                    update_medtable_query="UPDATE meds SET med_qty = med_qty + %s WHERE med_id = %s"
                    cursor.execute(update_medtable_query,(p_qty,medid))
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def add_stock():
                 
                purchase_id=purchase_id_entry.get()
                medid = med_id_entry.get()
                supplier_id = supplier_id_entry.get()
                p_qty = p_qty_entry.get()
                p_cost=p_cost_entry.get()
                p_date = p_date_entry.get()
                mfg_date = mfg_date_entry.get()
                exp_date = exp_date_entry.get()
                if insert_in_stock(purchase_id,medid, supplier_id,p_qty,p_cost, p_date,mfg_date,exp_date):
                    print("Stock added successfully!")
                else:
                    print("Failed to add stock.")


            def update_stockfunc(medid,supplier_id,p_qty,p_cost,p_date,mfg_date,exp_date,purchase_id):
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
                    cursor = conn.cursor()
                    query = "UPDATE purchase SET med_id=%s, supplier_id=%s, p_qty=%s,p_cost=%s, p_date=%s, mfg_date=%s,, exp_date=%s WHERE purchase_id=%s"
                    data = (medid, supplier_id,p_qty,p_cost, p_date,mfg_date,exp_date,purchase_id)
                    cursor.execute(query, data)
                    conn.commit()
                    conn.close()
                    return True
                except Exception as e:
                    print("Error:", e)
                    return False

            def update_stock():
                
                purchase_id=purchase_id_entry.get()
                medid = med_id_entry.get()
                supplier_id = supplier_id_entry.get()
                p_qty = p_qty_entry.get()
                p_cost=p_cost_entry.get()
                p_date = p_date_entry.get()
                mfg_date = mfg_date_entry.get()
                exp_date = exp_date_entry.get()
                if update_stockfunc(medid, supplier_id,p_qty,p_cost, p_date,mfg_date,exp_date,purchase_id,):
                    print("Stock updated successfully!")
                else:
                    print("Failed to update Stock.")


            main_frame = Frame(content_frame, bg="#e6e6e6")
            main_frame.pack(expand=True, fill="both")

            topnav_frame = Frame(main_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2,relief=FLAT,command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            # Add a header
            header_label = Label(main_frame, text="MANAGE PURCHASED STOCK", font=("Arial", 20), bg="lightgrey", fg="Black", padx=10, pady=5)
            header_label.pack(fill="x",padx=30,pady=20)

            stock_purchase_frame = Frame(main_frame, relief="solid", width=770, bg="#e6e6e6",height=600)

            purchase_id_label = Label(stock_purchase_frame, text="Purchase ID:", font=("Arial", 15), bg="#e6e6e6")
            purchase_id_label.grid(row=0, column=0, padx=50, pady=10, sticky="w")
            purchase_id_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            purchase_id_entry.grid(row=1, column=0, padx=50, pady=10)

            med_id_label = Label(stock_purchase_frame, text="Medicine ID:", font=("Arial", 15), bg="#e6e6e6")
            med_id_label.grid(row=2, column=0, padx=50, pady=10, sticky="w")
            med_id_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            med_id_entry.grid(row=3, column=0, padx=50, pady=10)

            supplier_id_label = Label(stock_purchase_frame, text="Supplier ID:", font=("Arial", 15), bg="#e6e6e6")
            supplier_id_label.grid(row=4, column=0, padx=50, pady=10, sticky="w")
            supplier_id_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            supplier_id_entry.grid(row=5, column=0, padx=50, pady=10)

            p_qty_label = Label(stock_purchase_frame, text="Quantity:", font=("Arial", 15), bg="#e6e6e6")
            p_qty_label.grid(row=6, column=0, padx=50, pady=10, sticky="w")
            p_qty_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            p_qty_entry.grid(row=7, column=0, padx=50, pady=10)

            p_cost_label = Label(stock_purchase_frame, text="Purchase Cost:", font=("Arial", 15), bg="#e6e6e6")
            p_cost_label.grid(row=0, column=1, padx=80, pady=10, sticky="w")
            p_cost_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            p_cost_entry.grid(row=1, column=1, padx=80, pady=10)

            p_date_label = Label(stock_purchase_frame, text="Purchase Date:", font=("Arial", 15), bg="#e6e6e6")
            p_date_label.grid(row=2, column=1, padx=80, pady=10, sticky="w")
            p_date_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            p_date_entry.grid(row=3, column=1, padx=80, pady=10)

            mfg_date_label = Label(stock_purchase_frame, text="Manufacturing Date:", font=("Arial", 15), bg="#e6e6e6")
            mfg_date_label.grid(row=4, column=1, padx=80, pady=10, sticky="w")
            mfg_date_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            mfg_date_entry.grid(row=5, column=1, padx=80, pady=10)

            exp_date_label = Label(stock_purchase_frame, text="Expiry Date:", font=("Arial", 15), bg="#e6e6e6")
            exp_date_label.grid(row=6, column=1, padx=80, pady=10, sticky="w")
            exp_date_entry = Entry(stock_purchase_frame, font=("Arial", 15), width=40, relief="flat")
            exp_date_entry.grid(row=7, column=1, padx=80, pady=10)

            stock_purchase_frame.pack(side=TOP, padx=10, pady=30,expand=True,fill=BOTH)

            # Add button
            add_stock_purchase_btn = Button(stock_purchase_frame, text="Add", font=("Arial", 15), bg="#0077b3", fg="white", width=20,command=add_stock)
            add_stock_purchase_btn.grid(row=8, column=1, padx=80, pady=20)

            # Update button
            update_stock_purchase_btn = Button(stock_purchase_frame, text="Update", font=("Arial", 15), bg="#0077b3", fg="white", width=20,command=update_stock)
            update_stock_purchase_btn.grid(row=9, column=1, padx=80, pady=20)
        
#=============================================================Med on Low stock=============================================================================
    
        def Med_LowStock():
            
            Report_table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(Report_table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            

            Report_table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 17))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(Report_table_frame, columns=("Med ID", "Med Name", "Med Qty", "Category", "Med Price", "Location Rack"), show="headings", style="New.Treeview")
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Med Name", text="Med Name", anchor=CENTER)
            table.heading("Med Qty", text="Med Qty", anchor=CENTER)
            table.heading("Category", text="Category", anchor=CENTER)
            table.heading("Med Price", text="Med Price", anchor=CENTER)
            table.heading("Location Rack", text="Location Rack", anchor=CENTER)

            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Med Name", width=150, anchor=CENTER)
            table.column("Med Qty", width=100, anchor=CENTER)
            table.column("Category", width=100, anchor=CENTER)
            table.column("Med Price", width=100, anchor=CENTER)
            table.column("Location Rack", width=120, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM meds_view_page where med_qty < 200")
            result = cursor.fetchall()

            if result:
                for row in result:
                    table.insert("", "end", values=row)
            else:
                messagebox.showinfo(Report_table_frame,"No medicines are on low stock")

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(Report_table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            # Pack the Treeview widget
            table.pack(expand=True, fill=BOTH)



        def Med_ExpireSoon():
                pass
        

        def transaction_view_page():
            # Create a new frame to contain the table
            table_frame = Frame(content_frame, bg="white")

            topnav_frame = Frame(table_frame, bg="#003366")
            topnav_frame.pack(side=TOP, fill=X)

            logout_button = Button(topnav_frame, text="Logout (Logged in as Admin)", font=("Arial", 14), bg="#003366", fg="#bfbfbf", bd=2, relief=FLAT, command=self.win.destroy)
            logout_button.pack(side=RIGHT, padx=20, pady=10)

            table_frame.pack(expand=True, fill=BOTH)

            style = ttk.Style()

            print(style.theme_names())
            style.theme_use('clam')
            style.configure("New.Treeview.Heading", background="#0077b3", foreground="white", font=("Arial", 17))
            style.configure("New.Treeview", rowheight=50, fieldbackground="white")

            # Create the Treeview widget
            table = ttk.Treeview(table_frame, columns=("Med ID", "Sale ID", "Sale Quantity", "Medicine Name", "Medicine Price"), show="headings", style="New.Treeview")
            table.heading("Med ID", text="Med ID", anchor=CENTER)
            table.heading("Sale ID", text="Sale ID", anchor=CENTER)
            table.heading("Sale Quantity", text="Sale Quantity", anchor=CENTER)
            table.heading("Medicine Name", text="Medicine Name", anchor=CENTER)
            table.heading("Medicine Price", text="Medicine Price", anchor=CENTER)

            table.column("Med ID", width=100, anchor=CENTER)
            table.column("Sale ID", width=100, anchor=CENTER)
            table.column("Sale Quantity", width=100, anchor=CENTER)
            table.column("Medicine Name", width=200, anchor=CENTER)
            table.column("Medicine Price", width=100, anchor=CENTER)

            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM transaction")
            result = cursor.fetchall()

            for row in result:
                table.insert("", "end", values=row)

            cursor.close()
            conn.close()

            # Create a scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")

            # Set the scrollbar to scroll the table's y-axis
            table.configure(yscrollcommand=scrollbar.set)

            table.pack(fill=BOTH,expand=True)




            

            









        

            
                


        
    def Add_new_sale(self):
        twin=Toplevel(self.win)
        transaction_page=TransactionPage(twin)

from tkinter import messagebox
from datetime import datetime

class TransactionPage:
    def __init__(self,twin):
        self.twin=twin
        self.twin.title("Transaction Page")
        self.twin.geometry("1550x800")

        # Classy Background
        #self.twin.configure(bg="#f0f0f0")

        # Customer Details Frame
        customer_frame = LabelFrame(self.twin, text="Customer Details", bg="#f0f0f0", font=("Arial", 12))
        customer_frame.pack(padx=10, pady=10, fill=BOTH)
        
        CID_label = Label(customer_frame, text="Customer ID:", bg="#f0f0f0", font=("Arial", 10))
        CID_label.grid(row=0, column=0, padx=2, pady=2, sticky="w")
        CID_entry = Entry(customer_frame, font=("Arial", 10))
        CID_entry.grid(row=0, column=1, padx=15, pady=10, sticky="w")

        def display_customer_error_message():
            messagebox.showerror("Error", "No customer found with the entered phone number. This is a new customer.")

        def get_new_customer_id():
            try:
                # Establish a connection to the database
                conn = mysql.connector.connect(host='localhost', user='root', password='ae-1265', database='medical_store')

                # Create a cursor object to execute SQL queries
                cursor = conn.cursor()

                # Define the SQL query to get the largest customer ID
                query = "SELECT MAX(Cust_ID) FROM customer"
                cursor.execute(query)

                # Fetch the result
                result = cursor.fetchone()

                # Close cursor and connection
                cursor.close()
                conn.close()

                if result[0]:
                    return result[0] + 1  # Return the largest customer ID + 1
                else:
                    return 1  # If no customer ID exists, start from 1

            except mysql.connector.Error as error:
                print("Error: {}".format(error))
                return None

        def search_customer_id_by_phone(phone_number):
            try:
                # Establish a connection to the database
                conn = mysql.connector.connect(host='localhost', user='root', password='ae-1265',
                                               database='medical_store')

                # Create a cursor object to execute SQL queries
                cursor = conn.cursor()

                # Define the SQL query to search for the customer ID based on the phone number
                query = "SELECT Cust_ID FROM customer WHERE C_phno = %s"
                cursor.execute(query, (phone_number,))

                # Fetch the result
                result = cursor.fetchone()

                # Close cursor and connection
                cursor.close()
                conn.close()

                if result:
                    return result[0]  # Return the customer ID if found
                else:
                    return None

            except mysql.connector.Error as error:
                print("Error: {}".format(error))
                return None

        Fname_label = Label(customer_frame, text="First Name", bg="#f0f0f0", font=("Arial", 10))
        Fname_label.grid(row=0, column=2, padx=2, pady=2, sticky="w")
        Fname_entry = Entry(customer_frame, font=("Arial", 10))
        Fname_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        Lname_label = Label(customer_frame, text="Last Name", bg="#f0f0f0", font=("Arial", 10))
        Lname_label.grid(row=0, column=4, padx=2, pady=2, sticky="w")
        Lname_entry = Entry(customer_frame, font=("Arial", 10))
        Lname_entry.grid(row=0, column=5, padx=10, pady=10, sticky="w")

        Phno_label = Label(customer_frame, text="Phone Number:", bg="#f0f0f0", font=("Arial", 10))
        Phno_label.grid(row=0, column=6, padx=2, pady=2, sticky="w")
        Phno_entry = Entry(customer_frame, font=("Arial", 10))
        Phno_entry.grid(row=0, column=7, padx=10, pady=10, sticky="w")
            
        Email_label = Label(customer_frame, text="Email:", bg="#f0f0f0", font=("Arial", 10))
        Email_label.grid(row=0, column=8, padx=2, pady=2, sticky="w")
        Email_entry = Entry(customer_frame, font=("Arial", 10))
        Email_entry.grid(row=0, column=9, padx=10, pady=10, sticky="w")

        label_Gender = Label(customer_frame, text="Gender:", bg="#f0f0f0", font=("Arial", 10))
        label_Gender.grid(row=0, column=10, padx=2, pady=2, sticky="w")

        Gender_combo= ttk.Combobox(customer_frame, font=("Arial", 10),state="readonly")
        Gender_combo["values"]=("Male","Female")
        Gender_combo.grid(row=0, column=11, padx=10, pady=10, sticky="w")
        Gender_combo.current(1)

        def update_customer_id_entry():
            phone_number = Phno_entry.get()
            customer_id = search_customer_id_by_phone(phone_number)
            if customer_id:
                CID_entry.delete(0, END)
                CID_entry.insert(0, str(customer_id))
            else:
                display_customer_error_message()
                new_customer_id = get_new_customer_id()
                CID_entry.delete(0, END)
                CID_entry.insert(0, str(new_customer_id))


        search_button = Button(customer_frame, text="Search", command=update_customer_id_entry)
        search_button.grid(row=0, column=12, columnspan=2, padx=5, pady=5)

        #======================== Sale Details Frame===========================

        # Sale Details Frame
        sale_frame = LabelFrame(self.twin, text="Sale Details", bg="#f0f0f0", font=("Arial", 12))
        sale_frame.pack(padx=10, pady=10, fill=BOTH)

        SID_label = Label(sale_frame, text="Sale ID:", bg="#f0f0f0", font=("Arial", 10))
        SID_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        SID_entry = Entry(sale_frame, font=("Arial", 10))
        SID_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        SDate_label = Label(sale_frame, text="Sale Date:", bg="#f0f0f0", font=("Arial", 10))
        SDate_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        SDate_entry = Entry(sale_frame, font=("Arial", 10))
        SDate_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        STime_label = Label(sale_frame, text="Sale Time:", bg="#f0f0f0", font=("Arial", 10))
        STime_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        STime_entry = Entry(sale_frame, font=("Arial", 10))
        STime_entry.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        EMP_ID_label = Label(sale_frame, text="Employee ID:", bg="#f0f0f0", font=("Arial", 10))
        EMP_ID_label.grid(row=0, column=6, padx=5, pady=5, sticky="w")

        EMP_ID_entry = Entry(sale_frame, font=("Arial", 10))
        EMP_ID_entry.grid(row=0, column=7, padx=5, pady=5, sticky="w")

        def get_new_sale_id():
            try:
                # Establish a connection to the database
                conn = mysql.connector.connect(host='localhost', user='root', password='ae-1265', database='medical_store')

                # Create a cursor object to execute SQL queries
                cursor = conn.cursor()

                # Define the SQL query to get the largest customer ID
                query = "SELECT MAX(Sale_ID) FROM sales"
                cursor.execute(query)

                # Fetch the result
                result = cursor.fetchone()

                # Close cursor and connection
                cursor.close()
                conn.close()

                if result[0]:
                    new_sale_id = result[0] + 1  # Return the largest customer ID + 1
                else:
                    new_sale_id= 1  # If no customer ID exists, start from 1

                return new_sale_id

            except mysql.connector.Error as error:
                print("Error: {}".format(error))
                return None

        def update_sale_id_entry(SID_entry):
            new_sale_id = get_new_sale_id()
            if new_sale_id is not None:
                SID_entry.delete(0, END)
                SID_entry.insert(0, str(new_sale_id))

            current_date = datetime.now().date().strftime('%Y-%m-%d')
            SDate_entry.delete(0, END)
            SDate_entry.insert(0, current_date)

            # Set current time
            current_time = datetime.now().time().strftime('%H:%M:%S')
            STime_entry.delete(0, END)
            STime_entry.insert(0, current_time)


        check_button = Button(sale_frame, text="CHECK", command=lambda: update_sale_id_entry(SID_entry))
        check_button.grid(row=0, column=8, columnspan=2, padx=5, pady=5)



        #=====================Transaction Details===========================

        # Items Details Frame
        Tran_frame = LabelFrame(self.twin, text="Transaction Details", bg="#f0f0f0", font=("Arial", 12))
        Tran_frame.pack(padx=10, pady=10, fill=BOTH)

        MedID_label = Label(Tran_frame, text="Medicine ID:", bg="#f0f0f0", font=("Arial", 10))
        MedID_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        MedID_entry = Entry(Tran_frame, font=("Arial", 10))
        MedID_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        Medname_label = Label(Tran_frame, text="Medicine Name:", bg="#f0f0f0", font=("Arial", 10))
        Medname_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        Medname_entry = Entry(Tran_frame, font=("Arial", 10))
        Medname_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        

        price_label = Label(Tran_frame, text="Price:", bg="#f0f0f0", font=("Arial", 10))
        price_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        price_entry = Entry(Tran_frame, font=("Arial", 10))
        price_entry.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        PQty_label = Label(Tran_frame, text="Product Quantity:", bg="#f0f0f0", font=("Arial", 10))
        PQty_label.grid(row=0, column=6, padx=5, pady=5, sticky="w")

        PQty_entry = Entry(Tran_frame, font=("Arial", 10))
        PQty_entry.grid(row=0, column=7, padx=5, pady=5, sticky="w")

        total_label = Label(Tran_frame, text="Total:", bg="#f0f0f0", font=("Arial", 10))
        total_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        total_entry = Entry(Tran_frame, font=("Arial", 10))
        total_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        
        discount_label = Label(Tran_frame, text="Discount(%):", bg="#f0f0f0", font=("Arial", 10))
        discount_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        discount_entry = Entry(Tran_frame, font=("Arial", 10))
        discount_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        
        CGST_label = Label(Tran_frame, text="CGST(%):", bg="#f0f0f0", font=("Arial", 10))
        CGST_label.grid(row=1, column=4, padx=5, pady=5, sticky="w")

        CGST_entry = Entry(Tran_frame, font=("Arial", 10))
        CGST_entry.grid(row=1, column=5, padx=5, pady=5, sticky="w")


        
        SGST_label = Label(Tran_frame, text="SGST(%):", bg="#f0f0f0", font=("Arial", 10))
        SGST_label.grid(row=1, column=6, padx=5, pady=5, sticky="w")

        SGST_entry = Entry(Tran_frame, font=("Arial", 10))
        SGST_entry.grid(row=1, column=7, padx=5, pady=5, sticky="w")


        discount_entry.insert(0, "18")  # Set default value for discount
        CGST_entry.insert(0, "18")  # Set default value for CGST
        SGST_entry.insert(0, "18")  # Set default value for SGST





        






        #================= Scrollable Table===============================#

            


        table_frame = Frame(self.twin, bg="#f0f0f0")
        table_frame.pack(padx=10, pady=10, fill=BOTH, side=TOP)

         # Create a custom style name
        style_name = "Custom.Treeview"

        # Create the custom style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(style_name + ".Heading", background="#0077b3", foreground="white", font=("Arial", 13))
        style.configure(style_name,fieldbackground="white")


        scroll_x=Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=Scrollbar(table_frame ,orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        table =ttk.Treeview(table_frame, columns=("Med ID","Medicine Id","price", "Product Qty", "Total",
                                                   "Discount", "CGST (%)", "SGST (%)"),
                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,style="Custom.Treeview")

        scroll_x.config(command=table.xview)
        scroll_y.config(command=table.yview)

        table["show"]="headings"
        
        table.heading("#1", text="Med ID")
        table.heading("#2", text="Medicine Name")
        table.heading("#3", text="Price")
        table.heading("#4", text="Product Qty")
        table.heading("#5", text="Discount")
        table.heading("#6", text="CGST (%)")
        table.heading("#7", text="SGST (%)")
        table.heading("#8", text="Total")
        table.pack(fill=BOTH, expand=1)

       

        table.column("#1",width=150)
        table.column("#2",width=150)
        table.column("#3",width=150)
        table.column("#4",width=150)
        table.column("#5",width=150)
        table.column("#6",width=150)
        table.column("#7",width=150)
        table.column("#8",width=150)
        
                

        def display_medprice_error_message():
            messagebox.showerror("Error", "No medicine found with the entered medicine id.")

        def get_Med_price(med_id):
            try:
                conn=mysql.connector.connect(host="localhost", user="root",
                                             password="ae-1265",database="medical_store")
                cursor=conn.cursor()
                query="SELECT med_price from meds where med_id=%s"
                cursor.execute(query,(med_id,))
                result=cursor.fetchone()
                cursor.close()
                conn.close()

                if result:
                    return result[0]
                else:
                    return None

            except mysql.connector.Error as error:
                print("Error: {}".format(error))
                return None



        def update_med_price():
            med_id = MedID_entry.get()
            med_price = get_Med_price(med_id)
            if med_price is not None:  # Check if med_price is not None
                price_entry.delete(0, END)
                price_entry.insert(0, med_price)  # Insert med_price into the entry field
                return med_price  # Return the med_price value
            else:
                display_medprice_error_message()
                return None  # Return None if med_price is not found
            
        def display_medname_error_message():
            messagebox.showerror("Error", "No medicine found with the entered medicine id.")

        def get_Med_name(med_id):
            try:
                conn = mysql.connector.connect(host="localhost", user="root",
                                                password="ae-1265", database="medical_store")
                cursor = conn.cursor()
                query = "SELECT med_name FROM meds WHERE med_id = %s"
                cursor.execute(query, (med_id,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()

                if result:
                    return result[0]
                else:
                    return None

            except mysql.connector.Error as error:
                print("Error: {}".format(error))
                return None

       

        def update_med_name():
            med_id = MedID_entry.get()
            med_name = get_Med_name(med_id)
            if med_name is not None:  
                Medname_entry.delete(0, END)
                Medname_entry.insert(0, med_name)
                return med_name  
            else:
                display_medname_error_message()
                return None  


        global S_No
        S_No=0

        def proceed(MedID_entry,Medname_entry, price_entry, PQty_entry, discount_entry, CGST_entry, SGST_entry):
            # Retrieve medicine price using the update_med_price function
            med_price = update_med_price()
            med_name=update_med_name()
            if med_price is not None:  # Check if med_price is not None
                # Retrieve data from Entry fields
                med_id = MedID_entry.get()
                med_name=Medname_entry.get()
                price_str = price_entry.get().strip()  # Strip whitespace characters
                quantity_str = PQty_entry.get().strip()  # Strip whitespace characters
                discount_str = discount_entry.get().strip()  # Strip whitespace characters
                cgst_str = CGST_entry.get().strip()  # Strip whitespace characters
                sgst_str = SGST_entry.get().strip()  # Strip whitespace characters

                print("Price String:", price_str)
                print("Quantity String:", quantity_str)
                print("Discount String:", discount_str)
                print("CGST String:", cgst_str)
                print("SGST String:", sgst_str)

                # Validate and convert strings to float
                try:
                    med_price = float(price_str)
                    quantity = float(quantity_str)
                    discount = float(discount_str)
                    cgst = float(cgst_str)
                    sgst = float(sgst_str)
                except ValueError as e:
                    # Handle the case where the strings cannot be converted to float
                    print("Error:", e)  # Print the specific error message
                    return 

                # Calculate total
                total = med_price * quantity

                total_entry.delete(0,END)
                total_entry.insert(0,total)
                
                # Insert data into scrollable table

                table.insert("", "end", values=(med_id,med_name,med_price,quantity,discount,cgst,sgst,total))
                
#====================================================Proceed Button of Tran Frame===============================================================                

        # Proceed Button
        proceed_button = Button(Tran_frame, text="Proceed",command=lambda:proceed(MedID_entry,Medname_entry, price_entry, PQty_entry, discount_entry, CGST_entry, SGST_entry))
        proceed_button.grid(row=1, column=8, columnspan=8, padx=5, pady=5)



        #============================ Total Summary Frame============================================================


        summary_frame = Frame(self.twin, bg="#f0f0f0")
        summary_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

        total_item_price_label = Label(summary_frame, text="Total Item Price:", bg="#f0f0f0", font=("Arial", 10))
        total_item_price_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        total_item_price_entry = Entry(summary_frame, font=("Arial", 10))
        total_item_price_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        total_discount_label = Label(summary_frame, text="Total Discount:", bg="#f0f0f0", font=("Arial", 10))
        total_discount_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        total_discount_entry = Entry(summary_frame, font=("Arial", 10))
        total_discount_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        total_sgst_label = Label(summary_frame, text="Total SGST:", bg="#f0f0f0", font=("Arial", 10))
        total_sgst_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        total_sgst_entry = Entry(summary_frame, font=("Arial", 10))
        total_sgst_entry.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        total_cgst_label = Label(summary_frame, text="Total CGST:", bg="#f0f0f0", font=("Arial", 10))
        total_cgst_label.grid(row=0, column=6, padx=5, pady=5, sticky="w")

        total_cgst_entry = Entry(summary_frame, font=("Arial", 10))
        total_cgst_entry.grid(row=0, column=7, padx=5, pady=5, sticky="w")

        total_amount_label = Label(summary_frame, text="Total Amount:", bg="#f0f0f0", font=("Arial", 10))
        total_amount_label.grid(row=0, column=8, padx=5, pady=5, sticky="w")

        total_amount_entry = Entry(summary_frame, font=("Arial", 10))
        total_amount_entry.grid(row=0, column=9, padx=5, pady=5, sticky="w")


        def calculate_summary():
            total_item_price = 0
            total_discount = 0
            total_sgst = 0
            total_cgst = 0
            total_amount = 0

            # Iterate through the items in the scrollable table
            for child in table.get_children():
                values = table.item(child, 'values')
                print("Values:", values)  # Print the values to understand the structure
                if values and len(values) <= 8: 
                    total_item_price += float(values[2]) * float(values[3])  # Price * Quantity
                    total_discount += float(values[4])
                    total_sgst += float(values[5])
                    total_cgst += float(values[6])

            total_amount = (total_item_price - total_discount) + total_sgst + total_cgst

            # Update the entry fields with the calculated values
            total_item_price_entry.delete(0, END)
            total_item_price_entry.insert(0, total_item_price)

            total_discount_entry.delete(0, END)
            total_discount_entry.insert(0, total_discount)

            total_sgst_entry.delete(0, END)
            total_sgst_entry.insert(0, total_sgst)

            total_cgst_entry.delete(0, END)
            total_cgst_entry.insert(0, total_cgst)

            total_amount_entry.delete(0, END)
            total_amount_entry.insert(0, total_amount)

        # calculate_summary Button
        calculate_summary_button = Button(summary_frame, text="calculate_summary", command=calculate_summary)
        calculate_summary_button.grid(row=0, column=10, padx=5, pady=5)

        # Call calculate_summary initially to display the initial summary
        calculate_summary()


        # New frame for the receipt section
        receipt_frame = Frame(self.twin, bg="#f0f0f0")
        receipt_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Function to calculate and print the receipt

        def print_receipt():
            # Retrieve customer details
            customer_id = CID_entry.get()
            customer_Fname = Fname_entry.get()
            customer_Lname = Lname_entry.get()
            customer_phono = Phno_entry.get()
            customer_email = Email_entry.get()
            customer_gender = Gender_combo.get()

            # Insert customer details into the customer table
            conn = mysql.connector.connect(host="localhost", username="root", password="ae-1265", database="medical_store")
            cursor = conn.cursor()
            customer_query = "INSERT INTO customer (cust_id, C_Fname, C_Lname, C_gender, C_phno, C_Mail) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(customer_query, (customer_id, customer_Fname, customer_Lname, customer_gender, customer_phono, customer_email))
            conn.commit()

            # Retrieve sale details
            Sale_ID = SID_entry.get()
            Sale_Date = SDate_entry.get()
            Sale_Time = STime_entry.get()
            Employee_ID = EMP_ID_entry.get()
            Total_amount = total_amount_entry.get()

            # Insert sale details into the sales table
            sale_query = "INSERT INTO sales (customer_id, employee_id, Sale_id, S_Date, S_Time, total_amount) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sale_query, (customer_id, Employee_ID, Sale_ID, Sale_Date, Sale_Time, Total_amount))
            conn.commit()

            # Insert sales items into the sales_items table
            for child in table.get_children():
                values = table.item(child, 'values')
                print("Values:", values)
                Medicine_ID = values[0]  # Assuming Medicine_ID is at index 0
                product_Qty = values[2]  # Assuming product quantity is at index 2

                sale_items_query = "INSERT INTO sales_items (med_id, sale_id, sale_Qty) VALUES (%s, %s, %s)"
                cursor.execute(sale_items_query, (Medicine_ID, Sale_ID, product_Qty))
                conn.commit()



                # -- Subtract the medicine quantity from the medicine table

                update_med_qty_in_medtable_query="UPDATE meds SET med_qty = med_qty - %s WHERE med_id = %s"
                cursor.execute(update_med_qty_in_medtable_query,(product_Qty,Medicine_ID))
                conn.commit()

          
            # Close cursor and connection
            cursor.close()
            conn.close()




        # Button to print the receipt
        print_receipt_button = Button(receipt_frame, text="Print Receipt", command=print_receipt)
        print_receipt_button.pack(padx=5, pady=5)



if __name__ == "__main__":
    main()
