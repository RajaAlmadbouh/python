import tkinter as tk
from tkinter import messagebox

#-----------------------------Class-----------------------------
class User():
    def __init__(self,name,pas,sp):
        self.Name = name
        self._Password =pas
        if sp not in {"A", "C", "U"}:
            raise ValueError("Invalid input. Service provider must be A (Admin), C (Captain), or U (User).")
        self.SP = sp
         
    def __str__(self):
        return f"UserName : {self.Name} \n "
    
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
                if data.SP == "A":
                    print("Admin")
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

