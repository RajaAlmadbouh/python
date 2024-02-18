import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def button_clicked():
    print('Button clicked')

def download_clicked():
    showinfo(title='Information', message='Download button clicked!')

def agreement_changed():
    tk.messagebox.showinfo(title='Result', message=agreement.get())

def login_clicked():
    msg = f"Your Email: {email.get()}\nPassword: {password.get()}"
    showinfo(title="Information", message=msg)

root = tk.Tk()
root.title('Tkinter')
root.geometry("600x400+50+50")

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
frame = ttk.Frame(root)
frame.pack(expand=True)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Now let's add some widgets to the frame
label1 = tk.Label(frame, text='Tkinter', bg='red', fg='white')
label2 = tk.Label(frame, text='Pack Layout', bg='green', fg='white')
label3 = tk.Label(frame, text='Demo', bg='blue', fg='white')

label1.pack(pady=5, anchor="center")
label2.pack(pady=5, anchor="center")
label3.pack(pady=5, anchor="center")

# Add a button
button = ttk.Button(frame, text='Click Me', command=button_clicked)
button.pack()

# Add an image label
photo = tk.PhotoImage(file='./5.png')
image_label = ttk.Label(frame, image=photo, text="Python", padding=5)
image_label.place(relx=0.5, rely=0.5, anchor="center")

# Add a download button
download_icon = tk.PhotoImage(file='./5.png')
download_button = ttk.Button(frame, image=download_icon, command=download_clicked)
download_button.pack(ipadx=5, ipady=5, expand=True)

# Add a checkbox
agreement = tk.StringVar()
ttk.Checkbutton(frame, text="I agree", command=agreement_changed, variable=agreement, onvalue="agree", offvalue="disagree").pack()

# Add labels to the root window
label1 = tk.Label(root, text='Tkinter', bg='red', fg='white')
label2 = tk.Label(root, text='Pack Layout', bg='green', fg='white')
label3 = tk.Label(root, text='Demo', bg='blue', fg='white')

label1.pack()
label2.pack()
label3.pack()

# Add entry fields for email and password
email = tk.StringVar()
password = tk.StringVar()

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text="Email")
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

root.mainloop()

""""import tkinter as tk
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


"""
