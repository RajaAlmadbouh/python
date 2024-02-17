# Tkinter fundamentals

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk() #create an instance of the tk.Tk class that will create the application window

root.title('Tkinter')

root.geometry("600x400+50+50")# window.geometry("widthxheigh+x+y")

#Tkinter Window - Center
'''
window_width = 300
window_height = 200

# get the screen dimension
#get the screen width and height using the winfo_screenwidth() and winfo_screenheight() methods.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
'''
#place a label on the root window
message = tk.Label(root,text="Raja")
message.pack()
message = ttk.Label(root,text="Madbouh").pack()

#Tkinter Button
# button = ttk.Button(master, text, command)
#The master : is the parent widget on which you place the button.
#The text : is the label of the button.
#The command : specifies a callback function that will be called automatically when the button is clicked.

# exit button
exitButton = ttk.Button(root,text="Exit",command=lambda:quit())
#is assigned to a lambda expression that closes the root window.
exitButton.pack()

def button_clicked():
    print('Button clicked')#print in console


button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

# display an image label
photo = tk.PhotoImage(file='./5.png')
image_label = ttk.Label(
    root,
    image=photo,
    text="python",
    padding=5
)
image_label.pack()

# download button
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


download_icon = tk.PhotoImage(file='./5.png')
download_button = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# download button handler
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


download_icon = tk.PhotoImage(file='./5.png')

download_button = ttk.Button(
    root,
    image=download_icon,
    text='Download',
    compound=tk.LEFT,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)



# Tkinter checkbox

agreement = tk.StringVar()

def agreement_changed():#define a function that will be called once the state of the checkbox changed. The function shows the value of the checkbox
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())

ttk.Checkbutton(root,text = "I agree",command=agreement_changed,
                variable=agreement , onvalue="agree",offvalue="disagree").pack()


label1 = tk.Label(master=root, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(master=root,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(master=root, text='Demo',bg='blue', fg='white')

label1.pack()
label2.pack()
label3.pack()


#Tkinter Entry

# store email address and password
email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    msg=f"Your Email:{email.get()}\n password: {password.get()}"
    showinfo(title="Information" , message=msg)

# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

#email
email_label = ttk.Label(signin,text="Email ")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)#create an email Entry widget and associate it with the email variable:
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)


# keep the window displaying
root.mainloop() #method of the main window object ,ensures the main window continues to display and run until you close it

