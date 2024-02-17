import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def clear_UI():
    email_label.destroy()
    email_entry.destroy()
    password_label.destroy()
    password_entry.destroy()
    login_button.destroy()


def login_clicked():
    msg = f"Your Email: {email.get()}\nPassword: {password.get()}"

    if email.get() == "R" and password.get() == "12345":
        showinfo(title="Information", message=msg)
        #root.attributes('-fullscreen', False)# Make the window fullscreen
        getEmail = email.get()
        userName = getEmail.split("@")[0]
        clear_UI()
        userNameLabel = ttk.Label(root,text=f"User Name : {userName}")
        userNameLabel.pack()

        noteApp = "This program is characterized by a variety of wonderful services and reasonable prices"
        noteLable = ttk.Label(root,text=noteApp,padding=(10, 10))
        noteLable.pack(padx=10, pady=10, fill='x', expand=True)

        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_height()}++")

    else:
        showinfo(title="Information", message="Invalid Email Or Password")


#---------------------Main----------------------
root = tk.Tk()
root.title('FasterTaxi')
root.geometry("600x400+50+50")

email = tk.StringVar()
password = tk.StringVar()

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text="Email:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)



login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

# After Login User
root.mainloop()


