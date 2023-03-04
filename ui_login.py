import sys
import os
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Osu Mentory")
        #setting window size
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='TkDefaultFont',size=10)
        GLabel_502=tk.Label(root)
        GLabel_502["anchor"] = "center"
        GLabel_502["font"] = ft
        GLabel_502["fg"] = "#333333"
        GLabel_502["justify"] = "center"
        GLabel_502["text"] = "Login"
        GLabel_502.place(x=220,y=30,width=70,height=25)

        GButton_304=tk.Button(root)
        GButton_304["bg"] = "#e9e9ed"
        
        GButton_304["font"] = ft
        GButton_304["fg"] = "#000000"
        GButton_304["justify"] = "center"
        GButton_304["text"] = "Login With Osu"
        GButton_304.place(x=80,y=90,width=250,height=50)
        GButton_304["command"] = self.runLogin

    def runLogin(self):
        os.system('python main.py')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
