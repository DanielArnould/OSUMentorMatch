import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=450
        height=450
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
        GMessage_338.place(x=120,y=130,width=196,height=214)

        GButton_20=tk.Button(root)
        GButton_20["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_20["font"] = ft
        GButton_20["fg"] = "#000000"
        GButton_20["justify"] = "center"
        GButton_20["text"] = "Play"
        GButton_20.place(x=60,y=200,width=48,height=122)
        GButton_20["command"] = self.GButton_20_command

        GButton_769=tk.Button(root)
        GButton_769["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_769["font"] = ft
        GButton_769["fg"] = "#000000"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "Skip"
        GButton_769.place(x=320,y=200,width=51,height=129)
        GButton_769["command"] = self.GButton_769_command

        GButton_472=tk.Button(root)
        GButton_472["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_472["font"] = ft
        GButton_472["fg"] = "#000000"
        GButton_472["justify"] = "center"
        GButton_472["text"] = "Logout"
        GButton_472["relief"] = "sunken"
        GButton_472.place(x=360,y=50,width=70,height=25)
        GButton_472["command"] = self.GButton_472_command

        GMessage_659=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_659["font"] = ft
        GMessage_659["fg"] = "#333333"
        GMessage_659["justify"] = "center"
        GMessage_659["text"] = "UserData"
        GMessage_659["relief"] = "raised"
        GMessage_659.place(x=330,y=0,width=128,height=66)

    def GButton_20_command(self):
        print("command")


    def GButton_769_command(self):
        print("command")


    def GButton_472_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
