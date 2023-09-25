import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import base
import Friends_Page
import json
from datetime import datetime


class homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Home Page")
        self.geometry('900x500+300+200')
        self.configure(bg="#100426")
        
        self.create_widgets()

    def create_widgets(self):
        friends_button = tk.Button(self, width=6, text='Friends', border=0, bg='#131313', cursor='hand2', fg='#FF5B31', command=self.open_friends_page)
        friends_button.place(x=238, y=60)

        post_label = tk.Label(self, text="أكتب منشورك هنا:", bg="#100426", fg="white", font=("Arial", 14))
        post_label.place(x=50, y=150)

        self.post_entry = tk.Text(self, width=40, height=5, wrap=tk.WORD)
        self.post_entry.place(x=200, y=150)

        publish_button = tk.Button(self, text="نشر", bg='#FF5B31', fg='white', command=self.publish_post)
        publish_button.place(x=400, y=200)

        self.post_text = tk.Text(self, width=80, height=20, bg="white", selectbackground="#FF5B31")
        self.post_text.place(x=50, y=250)

        self.load_posts()
    def open_friends_page(self):
        self.destroy()
        Friends_Page.friend_page()

    def publish_post(self):
        post_text = self.post_entry.get("1.0", tk.END)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_post = f"تاريخ النشر: {current_time}\n{post_text}\n{'*' * 50}\n"
            
        self.post_text.insert(tk.END, formatted_post)
        
        with open('posts.txt', 'a', encoding='utf-8') as file:
            file.write(formatted_post)
        
        self.post_entry.delete("1.0", tk.END)
    def load_posts(self):
        try:
            with open('posts.txt', 'r', encoding='utf-8') as file:
                posts_data = file.read()
                self.post_text.insert(tk.END, posts_data)
        except FileNotFoundError:
            pass



if __name__ == '__main__':
    ROOT = homepage()
    ROOT.mainloop()
