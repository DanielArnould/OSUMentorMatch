import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=350
        height=452
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_338=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_338["font"] = ft
        GMessage_338["fg"] = "#333333"
        GMessage_338["justify"] = "center"
        GMessage_338["text"] = "Player Information"
        GMessage_338.place(x=20,y=30,width=307,height=341)

        GButton_472=tk.Button(root)
        GButton_472["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_472["font"] = ft
        GButton_472["fg"] = "#000000"
        GButton_472["justify"] = "center"
        GButton_472["text"] = "Logout"
        GButton_472["relief"] = "sunken"
        GButton_472.place(x=270,y=60,width=70,height=25)
        GButton_472["command"] = self.GButton_472_command

        GMessage_659=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_659["font"] = ft
        GMessage_659["fg"] = "#333333"
        GMessage_659["justify"] = "center"
        GMessage_659["text"] = "UserData"
        GMessage_659["relief"] = "raised"
        GMessage_659.place(x=240,y=0,width=128,height=66)

        GButton_902=tk.Button(root)
        GButton_902["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_902["font"] = ft
        GButton_902["fg"] = "#000000"
        GButton_902["justify"] = "center"
        GButton_902["text"] = "Mentor Matcher"
        GButton_902.place(x=120,y=370,width=120,height=32)
        GButton_902["command"] = self.GButton_902_command

    def GButton_472_command(self):
        print("command")


    def GButton_902_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
