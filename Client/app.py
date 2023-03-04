from tkinter import *
from tkinter import messagebox
from loginSystem import LoginSystem

class App:
    def __init__(self, serverIP, serverPort):
        try:
            self.loginSystem = LoginSystem(serverIP, serverPort)
        except:
            messagebox.showwarning(title="Connection error", message="Could't connect to the server")
            exit(-1)
        self.init_gui()


    def init_gui(self): 
        self.window = Tk()
        self.window.geometry("250x270")
        self.window.resizable(0, 0)
        self.window.title("Login page")
        self.window.config(background="light blue")
        # When the user presses 'x' call self.exit to terminate the connection properly
        self.window.protocol("WM_DELETE_WINDOW", self.exit)

        self.username_label = Label(self.window,
                                    text="Username: ",
                                    bg="light blue",
                                    pady=30
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

        self.register_button = Button(self.buttons_frame, text="Register", cursor="hand2", command=self.register)
        self.register_button.grid(row=2, column=0, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # if nothing is typed, do nothing
        if username == "" or password == "":
            return

        if self.loginSystem.login(username, password) == True:
            messagebox.showinfo(title="Login successful", message=f"Welcome {username}")
            self.exit()
        else:
            messagebox.showerror(title="Login unsuccessful", message="Wrong credentials")


    def register(self):
        register_window = Toplevel()
        Button(register_window, text="hello").pack()
        

    def exit(self):
        # Terminate the session with the server
        self.loginSystem.exit()
        # Close the window
        self.window.destroy()

    def run(self):
        self.window.mainloop()


app = App("localhost", 5050)
app.run()