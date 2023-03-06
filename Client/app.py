from tkinter import *
from tkinter import messagebox
from loginSystem import LoginSystem

INFOLEN = 128

"""
    The login application. Responsible for the gui and the user input. Also
    creates an instance of the LoginSystem class and through it communicates
    with the server.
"""
class LoginApp:
    def __init__(self, serverIP, serverPort):
        # Try to connect to the server
        try:
            self.loginSystem = LoginSystem(serverIP, serverPort)
        except:
            messagebox.showwarning(title="Connection error", message="Could't connect to the server")
            exit(-1)

        self.init_gui()
        self.access_granted = False

    # Makes the basic login window
    def init_gui(self): 
        self.window = Tk()
        self.window.geometry("250x250")
        self.window.resizable(0, 0)
        self.window.title("Login page")
        self.window.config(background="light blue")

        # When the user presses 'x' call self.exit to terminate the connection properly
        self.window.protocol("WM_DELETE_WINDOW", self.exit)

        self.username_label = Label(self.window,
                                    text="Username: ",
                                    bg="light blue",
                                    pady=20
                                    )
        self.username_label.grid(row=0, column=0)
        
        self.password_label = Label(self.window,
                                    text="Password: ",
                                    bg="light blue",
                                    pady=10
                                    )
        self.password_label.grid(row=1, column=0)

        self.username_entry = Entry(self.window)
        self.username_entry.grid(row=0, column=1)

        self.password_entry = Entry(self.window, show='*')
        self.password_entry.grid(row=1, column=1)

        self.buttons_frame = Frame(self.window, bg="light blue")
        self.buttons_frame.grid(row=2, column=0, columnspan=2)

        self.login_button = Button(self.buttons_frame, text="Login", cursor="hand2", command=self.login)
        self.login_button.grid(row=0, column=0, pady=10)

        self.register_label = Label(self.buttons_frame,
                                    text="Register if you don't\nhave an account",
                                    bg="light blue")
        self.register_label.grid(row=1, column=0)

        self.register_button = Button(self.buttons_frame, text="Register", cursor="hand2", command=self.create_register_page)
        self.register_button.grid(row=2, column=0, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        # if nothing is typed, do nothing
        if username == "" or password == "":
            return
        
        max_len = INFOLEN / 2
        if len(username) > max_len or len(password) > max_len:
            messagebox.showerror(title="Login unsuccessful", message="Your username/password shouldn't be that big")
            return

        if self.loginSystem.login(username, password) == True:
            messagebox.showinfo(title="Login successful", message=f"Welcome {username}")
            # if the login is successful exit the app
            self.access_granted = True
            self.exit()
        else:
            messagebox.showerror(title="Login unsuccessful", message="Wrong credentials")

    # Creates the GUI for the register page
    def create_register_page(self):
        self.register_window = Toplevel()
        self.register_window.title("Register page")
        self.register_window.geometry("350x180")
        self.register_window.resizable(0, 0)
        self.register_window.config(background="light yellow")
        # Call exit_register() when closing the register page
        self.register_window.protocol("WM_DELETE_WINDOW", self.close_register_page)

        # Disable register button, we don't want multiple register windows
        self.register_button.config(state=DISABLED)
        
        self.r_username_label = Label(self.register_window,
                                    text="Username: ",
                                    bg="light yellow",
                                    pady=10
                                    )
        self.r_username_label.grid(row=0, column=0)
        
        self.r_password_label = Label(self.register_window,
                                    text="Password: ",
                                    bg="light yellow",
                                    pady=10
                                    )
        self.r_password_label.grid(row=1, column=0)

        self.r_password_label2 = Label(self.register_window,
                                    text="Password Verification: ",
                                    bg="light yellow",
                                    pady=10
                                    )
        self.r_password_label2.grid(row=2, column=0)

        self.r_username_entry = Entry(self.register_window)
        self.r_username_entry.grid(row=0, column=1)

        self.r_password_entry = Entry(self.register_window, show='*')
        self.r_password_entry.grid(row=1, column=1)

        self.r_password_entry2 = Entry(self.register_window, show='*')
        self.r_password_entry2.grid(row=2, column=1)

        self.r_register_button = Button(self.register_window, text="Register", cursor="hand2", command=self.register)
        self.r_register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def register(self):
        username = self.r_username_entry.get()
        password = self.r_password_entry.get()
        password2 = self.r_password_entry2.get()

        if password != password2:
            messagebox.showwarning(title="Error", message="The passwords don't match", parent=self.register_window)
            return
        
        # if nothing is typed, do nothing
        if username == "" or password == "":
            return
        
        max_len = INFOLEN / 2
        if len(username) > max_len or len(password) > max_len:
            messagebox.showerror(title="Registration unsuccessful", message="Your username/password shouldn't be that big", parent=self.register_window)
            return
        
        if self.loginSystem.register(username, password) == True:
            messagebox.showinfo(title="Thank you", message="Registration successful", parent=self.register_window)
            self.close_register_page()
        else:
            messagebox.showwarning(title="Error", message="Username already in use", parent=self.register_window)
        

    def exit(self):
        # Terminate the session with the server
        self.loginSystem.exit()
        # Close the window
        self.window.destroy()

    def close_register_page(self):
        # Reactivate register button
        self.register_button.config(state=ACTIVE)
        # Close the window
        self.register_window.destroy()

    def run(self):
        self.window.mainloop()
        return self.access_granted


app = LoginApp("localhost", 5050)
app.run()