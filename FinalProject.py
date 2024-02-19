import tkinter as tk
from tkinter import messagebox
from tabulate import tabulate

#-----------------------------Class-----------------------------
class User():
    def __init__(self,name,pas,sp):
        self.Name = name
        self._Password =pas
        if sp not in {"A", "C", "U"}:
            raise ValueError("Invalid input. Service provider must be A (Admin), C (Captain), or U (User).")
        self.SP = sp
         
    def __str__(self):
        return f"UserName : {self.Name} \n Password : {self.getPassword()}"
    
    def getPassword(self):
        return self._Password
    
    def setPassword(self,newPassword):
        self._Password = newPassword


class captain(User):
    def __init__(self, name, pas , sp , typeCar, plate, phone):
        super().__init__(name, pas , sp)
        self.TypeCar = typeCar
        self.Plate = plate
        self.Phone = phone
    def __str__(self):
        return f"Car Type: {self.TypeCar}, Name: {self.Name}, Plate Number: {self.Plate}, Contact Number: {self.Phone}"

#-----------------------------Function-----------------------------

def create_login_interface():
    # Create main tkinter window
    root = tk.Tk()
    root.title("Login")
    root.geometry("200x200+20+20")

    # Variables to store the entered username and password
    username_var = tk.StringVar()
    password_var = tk.StringVar()

    logIn = tk.Label(root, text="Login Page:")
    logIn.grid(row=56, column=1)
    # Username and Password entry fields
    username_label = tk.Label(root, text="Username:")
    username_label.grid(row=0, column=0, sticky="e")
    username_entry = tk.Entry(root, textvariable=username_var)
    username_entry.grid(row=0, column=1)

    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=1, column=0, sticky="e")
    password_entry = tk.Entry(root, show="*", textvariable=password_var)
    password_entry.grid(row=1, column=1)

    def login_and_destroy():
        nonlocal username_var, password_var  # Use nonlocal keyword to update outer scope variables
        username = username_var.get()
        password = password_var.get()
        root.destroy()  # Close the tkinter window

    # Login button
    login_button = tk.Button(root, text="Login", command=login_and_destroy)
    login_button.grid(row=2, column=1, pady=10)

    # Run the tkinter event loop
    root.mainloop()

    # Return the entered username and password
    return username_var.get(), password_var.get()


def create_registration_interface():
    root = tk.Tk()
    root.title("Registration")
    root.geometry("200x200+20+20")

    # Variables to store the entered username, password, and service provider
    username_var = tk.StringVar()
    password_var = tk.StringVar()
    sp_var = tk.StringVar()

    register = tk.Label(root, text="Register Page:")
    register.grid(row=0, column=1)
    # Username, Password, and Service Provider entry fields
    username_label = tk.Label(root, text="Username:")
    username_label.grid(row=0, column=0, sticky="e")
    username_entry = tk.Entry(root, textvariable=username_var)
    username_entry.grid(row=0, column=1)

    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=1, column=0, sticky="e")
    password_entry = tk.Entry(root, show="*", textvariable=password_var)
    password_entry.grid(row=1, column=1)

    '''sp_label = tk.Label(root, text="Service Provider (A/C/U):")
    sp_label.grid(row=2, column=0, sticky="e")
    sp_entry = tk.Entry(root, textvariable=sp_var)
    sp_entry.grid(row=2, column=1)'''

    def register_and_destroy():
        nonlocal username_var, password_var, sp_var
        username = username_var.get()
        password = password_var.get()
        sp = "U"
        try:
            new_user = User(username, password, sp)
            UserData.append(new_user)
            messagebox.showinfo("Success", "Registration successful!")
            root.destroy()  # Close the tkinter window
            MainFunction()  # Call MainFunction again to resume login process
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Register button
    register_button = tk.Button(root, text="Register", command=register_and_destroy)
    register_button.grid(row=3, column=1, pady=10)

    # Run the tkinter event loop
    root.mainloop()

def ModifyUserNameData(UserNameModify, NewName, NewPass, NewSP):
    ExistUser = False 
    for User in UserData:
        if User.Name == UserNameModify:
            ExistUser = True
    
    if ExistUser:
        for user in UserData:
            if user.Name == UserNameModify:
                # Display current user data
                current_data_message = f"Current data for user '{UserNameModify}':\n"
                current_data_message += f"Username: {user.Name}\n"
                current_data_message += f"Password: {user.getPassword()}\n"
                current_data_message += f"Service Provider: {user.SP}"

                # Modify user data
                if NewName and NewName != user.Name:
                    user.Name = NewName
                    messagebox.showinfo("Username updated successfully!", "Username updated successfully!")
                    print("Username updated successfully!")

                if NewPass and NewPass != user.getPassword():
                    user.setPassword(NewPass)
                    messagebox.showinfo("Password updated successfully!", "Password updated successfully!")
                    print("Password updated successfully!")

                if NewSP and NewSP not in {"A", "C", "U"}:
                    messagebox.showerror("Invalid Input", "Enter service providers only A as Admin, C as Captain, or U as User")
                    print("Invalid Input: Enter service providers only A as Admin, C as Captain, or U as User")
                elif NewSP:
                    user.SP = NewSP
                    messagebox.showinfo("Service Provider updated successfully!", "Service Provider updated successfully!")
                    print("Service Provider updated successfully!")
                
                # Display updated data
                updated_data_message = f"\nUpdated data for user '{UserNameModify}':\n"
                updated_data_message += f"Username: {user.Name}\n"
                updated_data_message += f"Password: {user.getPassword()}\n"
                updated_data_message += f"Service Provider: {user.SP}"
                messagebox.showinfo("Updated Data", updated_data_message)
    else:
        messagebox.showerror("Error", "The username does not exist.")


def AdminPage():
    root = tk.Tk()
    root.title("Admin Page")

    # Create entry variables
    new_name = tk.StringVar()
    new_pass = tk.StringVar()
    new_sp = tk.StringVar()

    def view_all_users():
        # Function to display all users
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Information Users:\n")
        output_text.insert(tk.END, "UserName\tPassword\tServiceProvider\n")
        for user in UserData:
            output_text.insert(tk.END, f"{user.Name.ljust(20)}{user.getPassword().ljust(10)}{user.SP}\n")

    def modify_user_data():
        new_name_label = tk.Label(root, text="Enter new username:")
        new_name_label.pack()
        new_name_entry = tk.Entry(root, textvariable=new_name)
        new_name_entry.pack()

        new_pass_label = tk.Label(root, text="Enter new password:")
        new_pass_label.pack()
        new_pass_entry = tk.Entry(root, textvariable=new_pass)
        new_pass_entry.pack()

        new_sp_label = tk.Label(root, text="Enter new service provider:")
        new_sp_label.pack()
        new_sp_entry = tk.Entry(root, textvariable=new_sp)
        new_sp_entry.pack()
        # Function to modify user data
        username = username_entry.get()
        new_name_val = new_name.get()
        new_pass_val = new_pass.get()
        new_sp_val = new_sp.get()
        ModifyUserNameData(username, new_name_val, new_pass_val, new_sp_val)
        

    def add_new_user():
    # Function to add new user
        add_window = tk.Toplevel(root)
        add_window.title("Add New User")

        new_username_label = tk.Label(add_window, text="Enter new username:")
        new_username_label.pack()
        new_username_entry = tk.Entry(add_window)
        new_username_entry.pack()

        new_password_label = tk.Label(add_window, text="Enter new password:")
        new_password_label.pack()
        new_password_entry = tk.Entry(add_window)
        new_password_entry.pack()

        new_sp_label = tk.Label(add_window, text="Enter service provider (A for Admin, C for Captain, U for User):")
        new_sp_label.pack()
        new_sp_entry = tk.Entry(add_window)
        new_sp_entry.pack()

        def add_user():
            print("Add New User")
            while True:
                new_username = new_username_entry.get()
                new_password = new_password_entry.get()
                new_sp = new_sp_entry.get()

                # Check if username already exists
                exist_user = any(user.Name == new_username for user in UserData)
                if exist_user:
                    messagebox.showerror("Error", "This user exists and cannot be added")
                    return

                # Create new user and append to UserData list
                try:
                    new_user = User(new_username, new_password, new_sp)
                    UserData.append(new_user)
                    messagebox.showinfo("Success", "User added successfully!")
                    view_all_users()  # Refresh the displayed user list
                    add_window.destroy()
                    break
                except ValueError as e:
                    messagebox.showerror("Error", f"Error: {e}")
                    return
        
        add_button = tk.Button(add_window, text="Add User", command=add_user)
        add_button.pack()

    # Create GUI elements
    view_button = tk.Button(root, text="View all users", command=view_all_users)
    view_button.pack()

    username_label = tk.Label(root, text="Enter username to modify:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    ###################################

    modify_button = tk.Button(root, text="Modify user data", command=modify_user_data)
    modify_button.pack()

    add_button = tk.Button(root, text="Add new user", command=add_new_user)
    add_button.pack()

    output_text = tk.Text(root, height=10, width=50)
    output_text.pack()

    root.mainloop()
    

def MainFunction():
    print(30 * "-", "Welcome to FasterTaxi", 30 * "-")
    numChoose = 0

    while True:
        username, password = create_login_interface()
        numChoose += 1
        user_found = False

        for data in UserData:
            if data.Name == username and data.getPassword() == password:
                user_found = True
                if data.SP == "A": #page Admin
                    print(f"UserNmae : {data.Name}      ServiceProvider : {data.SP}")
                    AdminPage()
                elif data.SP == "C":
                    print("Captain")
                elif data.SP == "U":
                    print("User")
                break
        
        if not user_found:
            print("User not found or invalid username/password")
            if numChoose == 3:
                print("Please register : ")
                create_registration_interface()
                break
        else:
            break




#-----------------------------Main-----------------------------

try:  
    CaptainData = [] # data opject in class captain
    UserData = [] #data opject in class User
 

    C1 = captain("Raja Almadbouh", "123456" , "C" ,"Toyota Avalon", "80081", "0796329390") # Captain Information 
    CaptainData.append(C1)  # add C1 to list (CaptainData)
    C2 = captain( "Montasr Asmer" , "123456" , "C" , "Chevrolet Menlo", "17785", "0772182104")
    CaptainData.append(C2)

    U1 = User(C1.Name,C1.getPassword(),"C") # User Information 
    UserData.append(U1) # add C1 to list (UsernData)
    U2 = User(C2.Name,C2.getPassword(),"C")
    UserData.append(U2)
    U3 = User("Rand","123456","U")
    UserData.append(U3)
    U4 = User("Mohammed","123456","U")
    UserData.append(U4)
    U5 = User("Admin","123456","A")
    UserData.append(U5)
except ValueError as e:
    print(e)


MainFunction()









"""def ModifyUserNameData(UserNameModify):
    ExistUser = False # this value checking if can Username Exist or not
    for User in UserData:
        if User.Name == UserNameModify:
            ExistUser = True
    
    if ExistUser:
        for user in UserData:
            if user.Name == UserNameModify:
                print(f"Current data for user '{UserNameModify}':")
                print("Username:", user.Name)
                print("Password:", user.getPassword())
                print("Service Provider:", user.SP)

                print("---------------------------------")
                print(""""""Note  :  
                      Each attribute will be modified
                      , but if you do not want to modify a specific attribute, press (Enter) :""" """)

                NewName = input("Enter new username: ")
                NewPass = input("Enter new password: ")
                NewSP   = input("Enter new service provider: ")

                if NewName == "":
                    user.Name = user.Name
                else:
                    user.Name = NewName
                    print("Username updated successfully!")

                if NewPass == "":
                    user.setPassword(user.getPassword())
                else:
                    user.setPassword(NewPass)
                    print("Password updated successfully!")

                if NewSP == "":
                    user.SP = user.SP
                else:
                    while True:
                        print("Enter service providers only A as Admin or C as Captain or U as User")
                        NewSP   = input("Enter new service provider: ")
                        if NewSP in {"A" , "C" , "U"}:
                            user.SP = NewSP
                            print("Service Provider updated successfully!")
                            break
                        else:
                            print("Invalid Input!!!!!!!")
                
                print("---------------------------------")

                print("Updated data:")
                print("Username:", user.Name)
                print("Password:", user.getPassword())
                print("Service Provider:", user.SP)

                
    else:
        print("The UserName is not exist")


def AdminPage():
    while True:
        print("Admin Page")
        print("1. View all users")
        print("2. Modify user data")
        print("3. Add new user")
        print("4. Delete user")
        print("0. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Information Users : ")
            print("UserName\tPassword\tServiceProvider")
            for user in UserData:
                print(f"{user.Name.ljust(20)}{user.getPassword().ljust(10)}{user.SP}")
        elif choice == "2":
            # Implement modification of user data
            UserNameModify = input("Enter username to modify: ")
            ModifyUserNameData(UserNameModify)
            
        elif choice == "3":
            # Implement addition of new user
            pass
        elif choice == "4":
            # Implement deletion of user
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice")"""

"""
 184 - 218

def modify_user_data():
        # Function to modify user data
        username = username_entry.get()
        new_name_val = new_name.get()
        new_pass_val = new_pass.get()
        new_sp_val = new_sp.get()
        ModifyUserNameData(username, new_name_val, new_pass_val, new_sp_val)

    # Create GUI elements
    view_button = tk.Button(root, text="View all users", command=view_all_users)
    view_button.pack()

    username_label = tk.Label(root, text="Enter username to modify:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    new_name_label = tk.Label(root, text="Enter new username:")
    new_name_label.pack()
    new_name_entry = tk.Entry(root, textvariable=new_name)
    new_name_entry.pack()

    new_pass_label = tk.Label(root, text="Enter new password:")
    new_pass_label.pack()
    new_pass_entry = tk.Entry(root, textvariable=new_pass)
    new_pass_entry.pack()

    new_sp_label = tk.Label(root, text="Enter new service provider:")
    new_sp_label.pack()
    new_sp_entry = tk.Entry(root, textvariable=new_sp)
    new_sp_entry.pack()

    modify_button = tk.Button(root, text="Modify user data", command=modify_user_data)
    modify_button.pack()"""