import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import json
import base
import Home 

class LoginPage(base.BasePage):
    def __init__(self):
        super().__init__("Login Page", '900x500+300+200')
        self.create_widgets()

    def create_widgets(self):
        self.admin_data = {
            "mail": "admin@gmail.com",
            "password": "admin123"
        }

        self.bg_image = tk.PhotoImage(file="login001.png")
        bg_label = tk.Label(self, image=self.bg_image, bg='#100426')
        bg_label.place(x=420, y=10)

        self.configure(bg='#100426')

        frame = Frame(self, width=350, height=350, bg="#100426" )
        frame.place(x=50, y=55)

        heading = Label(frame, text='Sign in', fg='white', bg='#100426', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        self.user = Entry(frame, width=35, fg='white', borderwidth=1, bg="#100426", font=('Microsoft YaHei UI Light', 11),bd=5)
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)

        Frame(frame, width=295, height=3, bg='#100426').place(x=25, y=107)

        self.password = Entry(frame, width=35, fg='white', borderwidth=1, bg="#100426", font=('Microsoft YaHei UI Light', 11), show="*",bd=5)
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', self.on_enter_password)
        self.password.bind('<FocusOut>', self.on_leave_password)

        Frame(frame, width=295, height=2, bg='#100426').place(x=25, y=177)

        show_password_button = Button(frame, width=14, text="Show Password", border=0, bg='#100426', cursor='hand2', fg='#57a1f8', command=self.toggle_password_visibility)
        show_password_button.place(x=26, y=189)

        login_button = Button(frame, font=('Microsoft YaHei UI Light', 11), width=30, pady=10, text='Login', bg='#FF5B31', fg='white', border=0, command=self.login)
        login_button.place(x=35, y=215)
        label = Label(frame, width=39, pady=7, text="Don't have an account?", fg='white', bg='#100426', font=('Microsoft YaHei UI Light', 9))
        label.place(x=20, y=269)
        register_button = Button(frame, width=6, text='Register', border=0, bg='#100426', cursor='hand2', fg='#FF5B31', command=self.open_register_page)
        register_button.place(x=225, y=276)

    def on_enter_user(self, e):
        self.user.delete(0, 'end')

    def on_leave_user(self, e):
        name = self.user.get()
        if not name:
            self.user.insert(0, 'Username')

    def on_enter_password(self, e):
        self.password.delete(0, 'end')

    def on_leave_password(self, e):
        name = self.password.get()
        if not name:
            self.password.insert(0, 'Password')

    def toggle_password_visibility(self):
        current_password = self.password.get()
        if self.password.cget("show") == "":
            self.password.config(show="*")
        else:
            self.password.config(show="")
        self.password.delete(0, 'end')
        self.password.insert(0, current_password)

    def open_register_page(self):
        from Register import RegisterPage
        self.destroy()
        RegisterPage()
    def open_home_page(self):
        self.destroy()
        Home.homepage()
    def login(self):
        username = self.user.get()
        user_password = self.password.get()

        if not username or not user_password:
            messagebox.showerror("Login Failed", "Please enter both username and password.")
            return

        try:
            with open('user_data.json', 'r') as json_file:
                data = json.load(json_file)
                if not isinstance(data, list):
                    raise TypeError("The data is not a list")
        except FileNotFoundError:
            messagebox.showerror("Login Failed", "User data file not found.")
            self.clear_fields()
            return
        except Exception as e:
            messagebox.showerror("Login Failed", f"An error occurred: {str(e)}")
            self.clear_fields()
            return

        is_admin = False

        for user_data in data:
            if username == self.admin_data["mail"] and user_password == self.admin_data["password"]:
                is_admin = True
                break

        if is_admin:
            messagebox.showinfo("Login", "Login Successful as an Admin")
        else:
            for user_data in data:
                user_key = list(user_data.keys())[0]
                if username == user_data[user_key]["username"] and user_password == user_data[user_key]["password"]:
                    global id
                    id = user_key
                    messagebox.showinfo("Login", "Login Successful as a Normal User")
                    self.open_home_page()
                    break
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password.")
                self.clear_fields()

    def clear_fields(self):
        self.user.delete(0, 'end')
        self.password.delete(0, 'end')

root = LoginPage()
root.mainloop()
