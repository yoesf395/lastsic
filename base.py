import tkinter as tk
import sys
class BasePage(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.configure(bg='#131313')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            sys.exit()