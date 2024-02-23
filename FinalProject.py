``import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


#-----------------------------Class-----------------------------
class User():
    def __init__(self,name,pas,sp):
        self.Name = name#self.chickName(name)
        self._Password =pas
        if sp not in {"A", "C", "U"}:
            raise ValueError("Invalid input. Service provider must be A (Admin), C (Captain), or U (User).")
        self.SP = sp
    
    """def chickName(self,name):
        for U in UserData:
            if U.Name == name:
                print(f"This User :: ({name}) is exist in DataBase , can not add")
                return None
        return name"""
         
    def __str__(self):
        return f"UserName : {self.Name} \n Password : {self.getPassword()}"
    
    def getPassword(self):
        return self._Password
    
    def setPassword(self,newPassword):
        self._Password = newPassword


class captain(User):
    def __init__(self, name, pas, sp, typeCar, plate, phone):
        super().__init__(name, pas, sp)
        self.SP = "C"
        self.TypeCar = typeCar
        self.Plate = plate
        self.Phone = phone
        self.addUserData()

    def addUserData(self):
        for user in UserData:
            if user.Name == self.Name:
                print(f"This User ({self.Name}) is already in the database. Cannot add")
                return
        new_user = User(self.Name, self._Password, self.SP)
        UserData.append(new_user)

    def __str__(self):
        return f"Name: {self.Name}, Car Type: {self.TypeCar}, Plate Number: {self.Plate}, Contact Number: {self.Phone}"


#-----------------------------Function-----------------------------
# This function LogIn Page
    
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
        #username = username_var.get()
        #password = password_var.get()
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

    
    # Function to informtion User and all access Admin (User)
    def InformtionUser():
        AddUserWindow = tk.Toplevel(root)
        AddUserWindow.title("Informtion User")

        

        # Function to display all users
        def view_all_users():
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Information Users:\n")
            output_text.insert(tk.END, "UserName\t\tPassword\t\tServiceProvider\n")
            output_text.insert(tk.END, "---------\t\t--------\t\t---------------\n")
            for user in UserData:
                output_text.insert(tk.END, f"{user.Name.ljust(18)}{user.getPassword().ljust(18)}{user.SP}\n")
        def modify_user_data():
            new_name_label = tk.Label(AddUserWindow, text="Enter new username:")
            new_name_label.pack()
            new_name_entry = tk.Entry(AddUserWindow, textvariable=new_name)
            new_name_entry.pack()

            new_pass_label = tk.Label(AddUserWindow, text="Enter new password:")
            new_pass_label.pack()
            new_pass_entry = tk.Entry(AddUserWindow, textvariable=new_pass)
            new_pass_entry.pack()

            new_sp_label = tk.Label(AddUserWindow, text="Enter new service provider:")
            new_sp_label.pack()
            new_sp_entry = tk.Entry(AddUserWindow, textvariable=new_sp)
            new_sp_entry.pack()

            username = username_entry.get()
            new_name_val = new_name.get()
            new_pass_val = new_pass.get()
            new_sp_val = new_sp.get()
            ModifyUserNameData(username, new_name_val, new_pass_val, new_sp_val)

        def add_new_user():
            add_window = tk.Toplevel(AddUserWindow)
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

                    exist_user = any(user.Name == new_username for user in UserData)
                    if exist_user:
                        messagebox.showerror("Error", "This user exists and cannot be added")
                        return

                    try:
                        new_user = User(new_username, new_password, new_sp)
                        UserData.append(new_user)
                        messagebox.showinfo("Success", "User added successfully!")
                        view_all_users()
                        add_window.destroy()
                        break
                    except ValueError as e:
                        messagebox.showerror("Error", f"Error: {e}")
                        return

            add_button = tk.Button(add_window, text="Add User", command=add_user)
            add_button.pack()

        def delete_user():
            username_delete = username_delete_entry.get()
            deleted = False
            for user in UserData:
                if user.Name == username_delete:
                    UserData.remove(user)
                    messagebox.showinfo("Success", f"User '{username_delete}' deleted successfully!")
                    view_all_users()
                    deleted = True
                    break
            if not deleted:
                messagebox.showerror("Error", f"User '{username_delete}' not found.")

        def Back():
            AddUserWindow.destroy()
            AdminPage()

        view_button = tk.Button(AddUserWindow, text="View all users", command=view_all_users)
        view_button.pack()

        username_label = tk.Label(AddUserWindow, text="Enter username to modify:")
        username_label.pack()
        username_entry = tk.Entry(AddUserWindow)
        username_entry.pack()

        modify_button = tk.Button(AddUserWindow, text="Modify user data", command=modify_user_data)
        modify_button.pack()

        add_button = tk.Button(AddUserWindow, text="Add new user", command=add_new_user)
        add_button.pack()

        username_delete_label = tk.Label(AddUserWindow, text="Enter username to delete:")
        username_delete_label.pack()
        username_delete_entry = tk.Entry(AddUserWindow)
        username_delete_entry.pack()

        delete_button = tk.Button(AddUserWindow, text="Delete user", command=delete_user)
        delete_button.pack()

        Back_button = tk.Button(AddUserWindow, text="Back", command=Back)
        Back_button.pack()

        output_text = tk.Text(AddUserWindow, height=10, width=50)
        output_text.pack()
    

    # Informtion Captain
    def InformtionCaptain():
        CaptainWindow = tk.Toplevel(root)
        CaptainWindow.title("Information Captain")

        CaptainWindow.geometry("600x600")

        # Create entry variables
        new_name = tk.StringVar()
        new_password = tk.StringVar()
        new_sp = tk.StringVar()
        new_typeCar = tk.StringVar()
        new_plate = tk.StringVar()
        new_phone = tk.StringVar()

        # Function to display all captains
        def view_all_captains():
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Captain Information:\n")
            output_text.insert(tk.END, "Name\t\tCar Type\t\tPlate Number\t\tContact Number\n")
            for captain in CaptainData:
                output_text.insert(tk.END, f"{captain.Name.ljust(20)}{captain.TypeCar.ljust(18)}{captain.Plate.ljust(10)}{captain.Phone}\n")


        # Function to add new captain
        def add_new_captain():
            add_window = tk.Toplevel(CaptainWindow)
            add_window.title("Add New Captain")

            new_name_label = tk.Label(add_window, text="Enter captain's name:")
            new_name_label.pack()
            new_name_entry = tk.Entry(add_window, textvariable=new_name)
            new_name_entry.pack()

            
            new_password_label = tk.Label(add_window, text="Enter password:")
            new_password_label.pack()
            new_password_entry = tk.Entry(add_window, textvariable=new_password)
            new_password_entry.pack()
            

            new_typeCar_label = tk.Label(add_window, text="Enter car type:")
            new_typeCar_label.pack()
            new_typeCar_entry = tk.Entry(add_window, textvariable=new_typeCar)
            new_typeCar_entry.pack()

            new_plate_label = tk.Label(add_window, text="Enter plate number:")
            new_plate_label.pack()
            new_plate_entry = tk.Entry(add_window, textvariable=new_plate)
            new_plate_entry.pack()

            new_phone_label = tk.Label(add_window, text="Enter contact number:")
            new_phone_label.pack()
            new_phone_entry = tk.Entry(add_window, textvariable=new_phone)
            new_phone_entry.pack()


            def add_captain():

                new_name_val = new_name.get()

                for c in CaptainData:
                    if c.Name == new_name_val:
                        print(f"This User ({new_name_val}) is already in the database. Cannot add.")
                        messagebox.showinfo("Error", f"This User ({new_name_val}) is already in the database. Cannot add.")        
                        return
                    
                
                
                new_password_val = new_password.get()
                new_SP_val = "C"
                new_phone_val = new_phone.get()
                new_typeCar_val = new_typeCar.get()
                new_plate_val = new_plate.get()
                new_phone_val = new_phone.get()

                # Create new opject in class Captain object and add it to CaptainData
                new_captain = captain(new_name_val , new_password_val , new_SP_val , new_typeCar_val, new_plate_val, new_phone_val)
                CaptainData.append(new_captain)

                # Display success message
                messagebox.showinfo("Success", "Captain added successfully!")
                view_all_captains()
                add_window.destroy()
            add_button = tk.Button(add_window, text="Add Captain", command=add_captain)
            add_button.pack()

        # Function to modify captain data
        def ModifyCaptain():
            captain_name_entry = None
            def apply_changes():
                nonlocal captain_name_entry  # Use nonlocal to access the global variable
                captainName = captain_name_entry.get()

                def ModifyAtt():
                    modifyWindow = tk.Toplevel(CaptainWindow)
                    modifyWindow.title("Modify Captain Data")

                    new_name_label = tk.Label(modifyWindow, text="New Name:")
                    new_name_label.grid(row=1, column=0)
                    new_name_entry = tk.Entry(modifyWindow)
                    new_name_entry.grid(row=1, column=1)

                    new_password_label = tk.Label(modifyWindow, text="New Password:")
                    new_password_label.grid(row=2, column=0)
                    new_password_entry = tk.Entry(modifyWindow)
                    new_password_entry.grid(row=2, column=1)

                    new_typeCar_label = tk.Label(modifyWindow, text="New Car Type:")
                    new_typeCar_label.grid(row=3, column=0)
                    new_typeCar_entry = tk.Entry(modifyWindow)
                    new_typeCar_entry.grid(row=3, column=1)

                    new_plate_label = tk.Label(modifyWindow, text="New Plate Number:")
                    new_plate_label.grid(row=4, column=0)
                    new_plate_entry = tk.Entry(modifyWindow)
                    new_plate_entry.grid(row=4, column=1)

                    new_phone_label = tk.Label(modifyWindow, text="New Contact Number:")
                    new_phone_label.grid(row=5, column=0)
                    new_phone_entry = tk.Entry(modifyWindow)
                    new_phone_entry.grid(row=5, column=1)

                    def apply_changes():  # Define apply_changes within ModifyAtt
                        newName = new_name_entry.get()
                        newPassword = new_password_entry.get()
                        newTypeCar = new_typeCar_entry.get()
                        newPlate = new_plate_entry.get()
                        newPhone = new_phone_entry.get()

                        for captain in CaptainData:
                            if captain.Name == captainName:
                                if newName:
                                    captain.Name = newName
                                if newPassword:
                                    captain.setPassword(newPassword)
                                if newTypeCar:
                                    captain.TypeCar = newTypeCar
                                if newPlate:
                                    captain.Plate = newPlate
                                if newPhone:
                                    captain.Phone = newPhone
                                messagebox.showinfo("Success", "Captain data updated successfully!")
                                view_all_captains()
                                modifyWindow.destroy()
                                break
                        else:
                            messagebox.showerror("Error", "Captain not found!")

                    # Apply button to confirm changes
                    apply_button = tk.Button(modifyWindow, text="Apply Changes", command=apply_changes)
                    apply_button.grid(row=6, column=0, columnspan=2)

                for captain in CaptainData:
                    if captain.Name == captainName:
                        ModifyAtt()
                        break
                else:
                    messagebox.showerror("Error", "Captain not found!")

            modifyWindow = tk.Toplevel(CaptainWindow)
            modifyWindow.title("Modify Captain Data")

            captain_name_label = tk.Label(modifyWindow, text="Captain's Name:")
            captain_name_label.grid(row=0, column=0)
            captain_name_entry = tk.Entry(modifyWindow)
            captain_name_entry.grid(row=0, column=1)

            apply_button = tk.Button(modifyWindow, text="Apply Changes", command=apply_changes)
            apply_button.grid(row=6, column=0, columnspan=2)


            #------------End ModifyCaptain---------------


        #Function to Delete captain data
        def DeleteCaptain():

            deleteWindow = tk.Toplevel(CaptainWindow)
            deleteWindow.title("Delete Captain")

            nameLabel = tk.Label(deleteWindow, text="Enter the name of the captain you want to delete:")
            nameLabel.pack()

            nameEntry = tk.Entry(deleteWindow)
            nameEntry.pack()

            def confirmDelete():
                getName = nameEntry.get()
                Delete = False # F => Captain not Exist  , T => Captain Exist
                
                for D in CaptainData:
                    if D.Name == getName :
                        CaptainData.remove(getName)
                        messagebox.showinfo("Success", f"Captain {getName} deleted successfully!")
                        view_all_captains()
                        Delete = True # Captain Exis
                        break
                if not Delete:
                    messagebox.showerror("Error", f"Captain {getName} not found.")
                
                deleteWindow.destroy()

            deleteButton = tk.Button(deleteWindow, text="Delete", command=confirmDelete)
            deleteButton.pack()


        # Options available to the administrator (Captain)
        view_button = tk.Button(CaptainWindow, text="View all captains", command=view_all_captains)
        view_button.pack()

        add_captain_button = tk.Button(CaptainWindow, text="add New Captain", command=add_new_captain)
        add_captain_button.pack()

        modify_button = tk.Button(CaptainWindow, text="Modify Captain Data", command=ModifyCaptain)
        modify_button.pack()
        
        delete_button = tk.Button(CaptainWindow, text="Delete Captain Data", command=DeleteCaptain)
        delete_button.pack()

        output_text = tk.Text(CaptainWindow, height=20, width=80)
        output_text.pack()

    

    # Function to log out and close the window
    def log_out():
        root.destroy()
        MainFunction()

    
    InformtionUser_button = tk.Button(root, text="Informtion User", command=InformtionUser)
    InformtionUser_button.pack()

    InformtionCaptain_button = tk.Button(root, text="Informtion Captain", command=InformtionCaptain)
    InformtionCaptain_button.pack()

    logout_button = tk.Button(root, text="Log Out", command=log_out)
    logout_button.pack()

    """output_text = tk.Text(root, height=10, width=50)
    output_text.pack()
"""
    root.mainloop()
    

#----------------------------Main Function----------------------------

def MainFunction():
    Main = tk.Tk()
    Main.title("Page Home")
    Main.geometry("300x200")  

    
    style = ttk.Style(Main)

    """def close_main_window():
        Main.destroy()"""
    
    # Configure the style for labels
    style.configure("TLabel", foreground="blue", font=("Helvetica", 12))

    # Configure the style for buttons
    style.configure("TButton", foreground="white", background="blue", font=("Helvetica", 10))

    # Create and style labels
    welcome_label = ttk.Label(Main, text="Welcome to FasterTaxi", style="TLabel")
    welcome_label.pack(pady=10)

    # Schedule closing of the main window after 4 seconds
    #Main.after(4000, close_main_window)

    # Variable to count login attempts
    numChoose = 0

    while True:
        username, password = create_login_interface()
        numChoose += 1
        user_found = False

        # Assume UserData is a placeholder list
        #UserData = []  # Placeholder list
        for data in UserData:
            if data.Name == username and data.getPassword() == password:
                user_found = True
                if data.SP == "A":
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

    Main.mainloop()


#-----------------------------Main-----------------------------

try:  
    CaptainData = [] # data opject in class captain
    UserData = [] #data opject in class User
 

    C1 = captain("Raja Almadbouh", "123456" , "C" ,"Toyota Avalon", "80081", "0796329390") # Captain Information 
    CaptainData.append(C1)  # add C1 to list (CaptainData)
    C2 = captain( "Montasr Asmer" , "123456" , "C" , "Chevrolet Menlo", "17785", "0772182104")
    CaptainData.append(C2)


 
    C3 = captain( "Ahmad Asmer" , "123456" , "C" , "Chevrolet Menlo", "17785", "0772182104")
    CaptainData.append(C3)

    """U1 = User(C1.Name,C1.getPassword(),"C") # User Information 
    UserData.append(U1) # add C1 to list (UsernData)
    U2 = User(C2.Name,C2.getPassword(),"C")
    UserData.append(U2)"""
    U3 = User("Rand","123456","U")
    UserData.append(U3)
    U4 = User("Mohammed","123456","U")
    UserData.append(U4)
    U5 = User("Admin","123456","A")
    UserData.append(U5)
    U6 = User("Sabah","123456","C")
    UserData.append(U6)
except ValueError as e:
    print(e)


MainFunction()
``