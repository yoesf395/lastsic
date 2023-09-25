#run from her
import tkinter as tk
from tkinter import Frame, Label, Button, messagebox, LabelFrame, Canvas, Scrollbar
import json
import sys
import login

class design_friend_card(Frame):
    def __init__(self, parent, friend_name, image, user_key_friend_id):
        super().__init__(parent)
        self.configure(bg="white")
        self.user_id = login.id
        self.user_key_friend_id = user_key_friend_id
        self.friend_name = friend_name
        self.image = image
        self.is_following = False
        self.bol_test = False

        friend_card = LabelFrame(self, text='', width=200, height=300, bg='#e0dede', bd=0, relief=tk.RAISED)
        friend_card.pack(padx=10, pady=5, side=tk.LEFT)

        friend_image = tk.PhotoImage(file=self.image)
        image_label = Label(friend_card, image=friend_image, bg='#e0dede')
        image_label.image = friend_image
        image_label.pack(pady=10)

        data_to_follow = {
            "Username": self.friend_name,
            "usid": self.user_key_friend_id,
        }

        def follow_friend():
            with open('user_data.json', 'r') as json_file:
                data = json.load(json_file)
            for data_for_check in data:
                user_key = list(data_for_check.keys())[0]
                if user_key == self.user_id:
                    usernameq = data_for_check[user_key]["username"]
            try:
                with open("users_data/{}/people_I_follow.json".format(usernameq), "r") as file:
                    file_data = json.load(file)
            except FileNotFoundError:
                file_data = []
            if not self.is_following:
                file_data.append(data_to_follow)
                messagebox.showinfo("Follow", "You are now following this friend!")
                follow_button.config(text="Unfollow")
                self.is_following = True
            else:
                new_file_data = []
                for item in file_data:
                    if item != data_to_follow:
                        new_file_data.append(item)
                file_data = new_file_data

                messagebox.showinfo("Unfollow", "You have unfollowed this friend.")
                follow_button.config(text="Follow")
                self.is_following = False

            with open("users_data/{}/people_I_follow.json".format(usernameq), "w") as file:
                json.dump(file_data, file, indent=4)

        friend_name_label = Label(friend_card, text=self.friend_name, font=('Helvetica', 14), bg='#e0dede')
        friend_name_label.pack(pady=10)

        with open('user_data.json', 'r') as json_file:
            data = json.load(json_file)

        for data_for_check in data:
            user_key = list(data_for_check.keys())[0]
            if user_key == self.user_id:
                usernameq = data_for_check[user_key]["username"]

        with open("users_data/{}/people_I_follow.json".format(usernameq), "r") as file:
            file_data = json.load(file)

        for item in file_data:
            if item["Username"] == self.friend_name:
                self.bol_test = True
                break  
        follow_button_text = "Unfollow" if self.bol_test else "Follow"
        follow_button = Button(friend_card, width=20, text=follow_button_text, bg='#18B495', fg='white', command=follow_friend)
        follow_button.pack(pady=15, padx=15)


class friend_page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Friend Page")
        self.geometry('900x500+300+200')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.check_hobby()
        



    def check_hobby(self):
        self.user_id = login.id
        try:
            with open('user_data.json', 'r') as json_file:
                data = json.load(json_file)
                if not isinstance(data, list):
                    raise TypeError("The data is not a list")
        except FileNotFoundError:
            messagebox.showerror("Login Failed", "User data file not found.")
            return
        except Exception as e:
            messagebox.showerror("Login Failed", f"An error occurred: {str(e)}")
            return
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        friend_frame = Frame(self, bg='gray', width=screen_width, height=screen_height)
        friend_frame.pack(padx=0, pady=0)




        canvas = Canvas(friend_frame, bg='white', width=screen_width, height=screen_height)
        scrollbar = Scrollbar(friend_frame, orient="vertical", command=canvas.yview)
        card_frame = Frame(canvas, bg='white', padx=100)

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=card_frame, anchor="nw")
        card_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        row_cards = []
        for data_for_check in data :
            user_key = list(data_for_check.keys())[0]
            if user_key == self.user_id:
                hobby1_user = data_for_check[user_key]["First_Hobby"]
                hobby2_user = data_for_check[user_key]["Second_Hobby"]
            
        for data_for_check in data:
            user_key = list(data_for_check.keys())[0]
            
            if self.user_id != user_key:
                    if hobby1_user == data_for_check[user_key]["First_Hobby"] or hobby2_user == data_for_check[user_key]["Second_Hobby"]:
                        friend_name = data_for_check[user_key]["username"]
                        image = "male_photo.png" if data_for_check[user_key]["gender"] == "Male" else "famale_photo.png"
                        user_key_friend_id = user_key

                        card = design_friend_card(card_frame, friend_name, image, user_key_friend_id)
                        card.grid(row=len(row_cards) // 3, column=len(row_cards) % 3, padx=10, pady=10, sticky="nsew")
                        row_cards.append(card)

        card_frame.grid_columnconfigure(0, weight=1)
        card_frame.grid_columnconfigure(1, weight=1)
        card_frame.grid_columnconfigure(2, weight=1)
        card_frame.update_idletasks() 
        canvas.config(scrollregion=canvas.bbox("all"))  

    def on_closing(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            sys.exit()

if __name__ == "__main__":
    ROOT = friend_page()
    ROOT.mainloop()
