import tkinter as tk
from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, messagebox
import json
import re
import os 
import random
import sys
import login
import base


class RegisterPage(base.BasePage):
    def __init__(self):
        super().__init__("Register Page", '900x500+300+200')

        self.email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        self.password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!#%*?&]{8,20}$"
        self.password_hidden = True

        self.create_widgets()

    def create_widgets(self):
        self.bg_image = tk.PhotoImage(file="login001.png")
        self.bg_label = tk.Label(self, image=self.bg_image, bg='#100426')
        self.bg_label.place(x=420, y=10)

        self.frame = Frame(self, width=400, height=450, bg="#100426")
        self.frame.place(x=0, y=50)
        
        self.configure(bg='#100426')

        self.heading = Label(self.frame, text='Sign up', fg='white', bg='#100426', font=('Microsoft YaHei UI Light', 28, 'bold'))
        self.heading.place(x=120, y=0)

        self.fields = [
            {'text': 'Username', 'x': 30, 'y': 90},
            {'text': 'Mail', 'x': 30, 'y': 150},
            {'text': 'Password', 'x': 230, 'y': 90},
            {'text': 'Age', 'x': 230, 'y': 150},
        ]

        self.genders = ['Male', 'Female']
        self.First_Hobby = ['hobby1', 'hobby2', 'hobby3', 'Aswan', 'Luxor', 'Other']
        self.Second_Hobby = ['hobby4', 'hobby5', 'hobby6', 'Aswan', 'Luxor', 'Other']

        self.entries = []
        for field in self.fields:
            entry = Entry(self.frame, width=20, fg='white', borderwidth=0, bg="#100426", font=('Microsoft YaHei UI Light', 11),bd=5)
            entry.default_text = field['text']
            entry.place(x=field['x'], y=field['y'])
            entry.insert(0, field['text'])
            entry.bind('<FocusIn>', self.on_enter)
            entry.bind('<FocusOut>', self.on_leave)
            self.entries.append(entry)

            Frame(self.frame, width=170, height=2, bg='#100426').place(x=field['x'], y=field['y'] + 27)

        self.gender_var = self.create_option_menu(self.frame, self.genders, 130, 215)
        self.First_Hobby_var = self.create_option_menu(self.frame, self.First_Hobby, 30, 280)
        self.Second_Hobby_var = self.create_option_menu(self.frame, self.Second_Hobby, 230, 280)

        self.toggle_password_button = Button(self.frame, width=14, text="Show Password", border=0, bg='#100426', cursor='hand2', fg='#57a1f8', command=self.toggle_password_visibility)
        self.toggle_password_button.place(x=250, y=125)

        self.register_button = Button(self.frame, font=('Microsoft YaHei UI Light', 11), width=30, pady=10, text='Register', bg='#FF5B31', fg='white', border=0, command=self.register_but_check)
        self.register_button.place(x=85, y=350)

        self.label = Label(self.frame, width=39, pady=7, text="Already a member?", fg='white', bg='#100426', font=('Microsoft YaHei UI Light', 9))
        self.label.place(x=45, y=53)

        self.login_button = Button(self.frame, width=6, text='login', border=0, bg='#100426', cursor='hand2', fg='#FF5B31', command=self.open_login_page)
        self.login_button.place(x=238, y=60)

    def on_enter(self, e):
        entry = e.widget
        if entry.get() == entry.default_text:
            entry.delete(0, 'end')
            entry.config(fg='white')
            if entry.default_text == 'Password':
                entry.config(show="*")

    def on_leave(self, e):
        entry = e.widget
        if not entry.get():
            entry.insert(0, entry.default_text)
            entry.config(fg='red')
            if entry.default_text == 'Password':
                entry.config(show="")

    def toggle_password_visibility(self):
        for entry in self.entries:
            if entry.default_text == 'Password':
                if self.password_hidden:
                    entry.config(show="")
                else:
                    entry.config(show="*")
        self.password_hidden = not self.password_hidden

    def create_option_menu(self, parent, options, x, y):
        variable = StringVar(parent)
        variable.set(options[0])
        option_menu = OptionMenu(parent, variable, *options)
        option_menu.config(width=16, bg="#100426", borderwidth=1, font=('Microsoft YaHei UI Light', 11), fg='white')
        option_menu.place(x=x, y=y)
        return variable

    def validate_data(self, data):
        email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!#%*?&]{8,20}$"

        user_data = list(data.values())[0]

        if not re.match(email_pattern, user_data["mail"]):
            messagebox.showerror("Registration failed", "Invalid email format.")
            return False

        if not re.match(password_pattern, user_data["password"]):
            messagebox.showerror("Registration failed", "Invalid password format.")
            return False

        if not user_data["username"] or not user_data["mail"] or not user_data["password"] or not user_data["age"] :
            messagebox.showerror("Registration failed", "All fields must be filled.")
            return False

        if not user_data["age"].isdigit():
            messagebox.showerror("Registration failed", "Age must be a number.")
            return False
        
        return True

    def register_but_check(self):
        user_id = str(random.randint(0, 9000000000))

        data = {
            user_id: {
                "username": self.entries[0].get(),
                "mail": self.entries[1].get(),
                "password": self.entries[2].get(),
                "age": self.entries[3].get(),
                "gender": self.gender_var.get(),
                "First_Hobby": self.First_Hobby_var.get(),
                "Second_Hobby": self.Second_Hobby_var.get()
            }
        }

        if self.validate_data(data):
            try:
                with open("user_data.json", "r") as file:
                    file_data = json.load(file)
            except FileNotFoundError:
                file_data = []

            file_data.append(data)

            with open("user_data.json", "w") as file:
                json.dump(file_data, file, indent=4)

            messagebox.showinfo("Registration successful", "Your data has been saved in user_data.json")
            path = os.getcwd()
            path += "/users_data/{}".format(data[user_id]["username"])

            os.mkdir(path)
            print("Directory '% s' created" % path)
            file_data = []
            with open("users_data/{}/people_I_follow.json".format(data[user_id]["username"]), "w") as file:
                    json.dump(file_data, file)

    def open_login_page(self):
        self.destroy()
        login.LoginPage()
       


        
                
if __name__ == "__main__":
    root = RegisterPage()
    root.mainloop()
    
