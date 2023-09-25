import json
import tkinter as tk
from tkinter import ttk
import pandas as pd
import base64
from Register import RegisterPage
import login
from Friends_Page import friend_page
class item():
    def __init__(self, name, model_year, age, gender, category,type1):
        self.name = name
        self.age = age
        self.model_year = model_year
        self.gender = gender
        self.category = category
        self.type=type1
    def jsson(self):
        self.item1 = {"name": self.name, "age": self.age, "model_year": self.model_year, "gender": self.gender,
                      "category": self.category,"type":self.type}
        with open("data_base.json", "r") as file:
            file_data = json.load(file)
        file_data.append(self.item1)
        with open("data_base.json", "w") as file:
            json.dump(file_data, file, indent=2)
books1 = (item("adventure_story", 2023, "kids", "all", "books","text"))
books1.jsson()
books2 = (item("cinderella_story", 2023, "kids", "female", "books","text"))
books2.jsson()
books3 = (item("nagib mahfouz_novel", 2005, ">15", "all", "books","text"))
books3.jsson()
books4 = (item("space_science", 2023, ">15", "all", "books","text"))
books4.jsson()
books5 = (item("Taha hessen_novel", 2002, ">15", "all", "books","text"))
books4.jsson()
books6 = (item("chemistry", 2011, ">15", "all", "books","text"))
books6.jsson()
fashion1 = (item("shirt", 2021, "youths", "male", "fashion","text"))
fashion1.jsson()
fashion2 = (item("shirt", 2021, "youths", "female", "fashion","text"))
fashion2.jsson()
fashion3 = (item("shirt", 2021, "kids", "all", "fashion","text"))
fashion3.jsson()
fashion4 = (item("shirt", 2021, "adults", "male", "fashion","text"))
fashion4.jsson()
fashion5 = (item("shirt", 2021, "adults", "female", "fashion","text"))
fashion5.jsson()
fashion6 = (item("shoes", 2023, "kids", "female", "fashion","text"))
fashion6.jsson()
fashion7 = (item("shoes", 2023, "kids", "male", "fashion","text"))
fashion7.jsson()
fashion8 = (item("shoes", 2023, "youths", "male", "fashion","text"))
fashion8.jsson()
fashion9 = (item("shoes", 2023, "youths", "female", "fashion","text"))
fashion9.jsson()
fashion10 = (item("shoes", 2023, "adults", "male", "fashion","text"))
fashion10.jsson()
fashion11 = (item("shoes", 2023, "adults", "female", "fashion","text"))
fashion11.jsson()
fashion12 = (item("pants", 2020, "youths", "male", "fashion","text"))
fashion12.jsson()
fashion13 = (item("pants", 2020, "youths", "female", "fashion","text"))
fashion13.jsson()
fashion14 = (item("pants", 2020, "kids", "male", "fashion","text"))
fashion14.jsson()
fashion15 = (item("pants", 2020, "kids", "female", "fashion","text"))
fashion15.jsson()
fashion16 = (item("pants", 2020, "adults", "male", "fashion","text"))
fashion16.jsson()
fashion17 = (item("pants", 2020, "adults", "female", "fashion","text"))
fashion17.jsson()
fashion18 = (item("skirt", 2020, "adults", "female", "fashion","text"))
fashion18.jsson()
fashion19 = (item("skirt", 2020, "youths", "female", "fashion","text"))
fashion19.jsson()
fashion20 = (item("skirt", 2020, "kids", "female", "fashion","text"))
fashion20.jsson()
sports1 = (item("racket", 2022, "all", "all", "sports","text"))
sports1.jsson()
sports2 = (item("swimsuit", 2022, "youths", "male", "sports","text"))
sports2.jsson()
sports3 = (item("swimsuit", 2022, "kids", "female", "sports","text"))
sports3.jsson()
sports4 = (item("swimsuit", 2022, "kids", "male", "sports","text"))
sports4.jsson()
sports5 = (item("swimsuit", 2022, "youths", "female", "sports","text"))
sports5.jsson()
sports6 = (item("swimsuit", 2022, "adults", "female", "sports","text"))
sports6.jsson()
sports7 = (item("swimsuit", 2022, "adults", "male", "sports","text"))
sports7.jsson()
sports8 = (item("ball", 2022, "all", "all", "sports","text"))
sports8.jsson()
movie1 = (item("cindralla", 2022, "kids", "female", "movie","text"))
movie1.jsson()
movie2 = (item("spider_man", 2022, "kids", "male", "movie","text"))
movie2.jsson()
movie3 = (item("koko", 2022, "kids", "all", "movie","text"))
movie3.jsson()
movie4 = (item("welle wanka", 2022, "all", "all", "movie","text"))
movie4.jsson()
movie5 = (item("action_film", 2022, "youths", "all", "movie","text"))
movie5.jsson()
movie6 = (item("comedy_film", 2022, "youths", "all", "movie","text"))
movie6.jsson()
movie7 = (item("classic_film", 2022, "adults", "all", "movie","text"))
movie7.jsson()
class store_image:
    def __init__(self,category,input_path):
        self.category=category
        self.input_path=input_path
    def imagetojson(self):
        with open(self.input_path, "rb") as img_file:
           self.item1= base64.b64encode(img_file.read()).decode('utf-8')
        with open("task_manager_data.json", "r") as file:
            file_data2 = json.load(file)
        file_data2.append(self.item1)
        with open("task_manager_data.json", "w") as file:
            json.dump(file_data2, file, indent=2)
# image1=store_image("sports","C:\Users\HP VIP\Desktop\project - Copy - Copy\Sports_in_Dubai_ar2023.jpg")
# image1.imagetojson()
# image2=store_image("sports","C:\Users\HP VIP\Desktop\project - Copy - Copy\Youth-soccer-indiana.jpg")
# image2.imagetojson()
# image3=store_image("books","C:\Users\HP VIP\Desktop\project - Copy - Copy\images (1).jpg")
# image3.imagetojson()
# image4=store_image("books","C:\Users\HP VIP\Desktop\project - Copy - Copy\images (2).jpg")
# image4.imagetojson()
# image5=store_image("fashion","C:\Users\HP VIP\Desktop\project - Copy - Copy\7421.jpg")
# image5.imagetojson()
# image6=store_image("fashion","C:\Users\HP VIP\Desktop\project - Copy - Copy\images.jpg")
# image6.imagetojson()
# image7=store_image("fashion","C:\Users\HP VIP\Desktop\project - Copy - Copy\757736ede7c2504c5a8e5ba97945cc82.jpg")
# image7.imagetojson()
# image8=store_image("movies","C:\Users\HP VIP\Desktop\project - Copy - Copy\images (3).jpg")
# image8.imagetojson()
# image9=store_image("movies","C:\Users\HP VIP\Desktop\project - Copy - Copy\images (4).jpg")
# image9.imagetojson()
# image10=store_image("movies","C:\Users\HP VIP\Desktop\project - Copy - Copy\images.jpg")
# image10.imagetojson()
class Home_page():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x6000")
        self.button1 = tk.Button(self.root, text="about me", font=("Arial", 18),bg="red",activebackground="green")
        self.button1.place(x=50, y=80)
        self.button2 = tk.Button(self.root, text="add friend", font=("Arial", 18),bg="red",activebackground="green",command=self.my_friends)
        self.button2.place(x=410, y=80)
        self.button4 = tk.Button(self.root, text="my friend", font=("Arial", 18), bg="red", activebackground="green")
        self.button4.place(x=410, y=100)
        self.label = tk.Label(self.root, text="Enter your post", font=('Arial', 10),fg="gray")
        self.label.place(x=250,y=170)
        self.textBox = tk.Text(self.root, height=5,width=30, font=('Arial', 18),foreground="blue")
        self.textBox.place(x=100, y=200)
        self.text_widget = tk.Text(self.root,width=50,foreground="black")
        self.text_widget.pack(side=tk.LEFT,fill=tk.BOTH)
        self.scroll_bar = tk.Scrollbar(self.root)
        self.scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
        self.long_text=self.get_hobbies()
        self.text_widget.insert(tk.END,self.long_text)
        self.scroll_bar.pack(side=tk.RIGHT)
        self.scroll_bar.config(command=self.text_widget.yview())
        self.button3=ttk.Button(self.root, text="post", width=20,command=self.post_json)
        self.button3.place(x=230,y=340)
        self.button4=ttk.Button(self.root, text="log out", width=20, command=self.log_out())
        self.button4.place(x=230, y=500)
        self.root.mainloop()
    def books(self):
        books = pd.read_csv("Books.csv")
        books.dropna()
        return books
    def sports(self):
        sports = pd.read_csv("sports.csv")
        sports.dropna()
        return sports
    def post_json(self):
        return self.textBox.get
    def get_hobbies(self):
        with open("post_data.json", "r") as file:
            file_datas2 = json.load(file)
        with open("data_base.json", "r") as file:
            file_data2 = json.load(file)
        with open("task_manager_data.json", "r") as file:
            file_data3 = json.load(file)
        for i in range(0, 2):
            if file_datas2["user_id"]["First_Hobby"] == "books" or file_datas2["user_id"]["second_Hobby"] == "books":
                return file_data2["books"], file_data3["books"], self.books()
            elif file_datas2["user_id"]["First_Hobby"] == "fashion" or file_datas2["user_id"][
                "second_Hobby"] == "fashion":
                return file_data2["fashion"], file_data3["fashion"]
            elif file_datas2["user_id"]["First_Hobby"] == "sports" or file_datas2["user_id"][
                "second_Hobby"] == "sports":
                return file_data2["sports"], file_data3["sports"], self.sports()
            elif file_datas2["user_id"]["First_Hobby"] == "movies" or file_datas2["user_id"][
                "second_Hobby"] == "movies":
                return file_data2["movies"], file_data3["movies"]
    def log_out(self):
        self.destroy()
        RegisterPage()
    def my_friends(self):
        self.destroy
        friend_page()

    def log_out(self):
        self.destroy()
        RegisterPage()

    def my_friends(self):
        self.destroy
        friend_page()
Home_page()
