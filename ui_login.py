import sys
import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  



class App:
    def __init__(self, root):
            
            
            global f1
            f1 = Frame(width=500, height=500, background="#D3D3D3")
            f1.pack(fill="both", expand=True, padx=0, pady=0)
            
            f2 = Frame(width=500, height=500, background="#D3D3D3")
            f2.pack(fill="both", expand=True, padx=0, pady=0)

            f3 = Frame(width=500, height=500, background="#D3D3D3")
            f3.pack(fill="both", expand=True, padx=0, pady=0)



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


            def runMatcher():
                f3.pack(fill="both", expand=True, padx=0, pady=0)
                f2.pack_forget()
                Matcher()
            
            
            def runLogin():
                f1.pack(fill="both", expand=True, padx=0, pady=0)
                f2.pack_forget()
                f3.pack_forget()
                Login()
            
            
            def runProfile():
                f2.pack(fill="both", expand=True, padx=0, pady=0)
                f1.pack_forget()
                Profile()
                
            
            

            def Login():
                    
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    GLabel_502=tk.Label(f1)
                    GLabel_502["anchor"] = "center"
                    GLabel_502["font"] = ft
                    GLabel_502["fg"] = "#333333"
                    GLabel_502["justify"] = "center"
                    GLabel_502["text"] = "Login"
                    GLabel_502.place(x=220,y=30,width=70,height=25)

                    GButton_304=tk.Button(f1)
                    GButton_304["bg"] = "#e9e9ed"
                    
                    GButton_304["font"] = ft
                    GButton_304["fg"] = "#000000"
                    GButton_304["justify"] = "center"
                    GButton_304["text"] = "Login With Osu"
                    GButton_304.place(x=80,y=90,width=250,height=50)
                    GButton_304["command"] = runProfile
                        
                


                        
            def Profile():
                

                    GMessage_338=tk.Message(f2)
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    GMessage_338["font"] = ft
                    GMessage_338["fg"] = "#333333"
                    GMessage_338["justify"] = "center"
                    GMessage_338["text"] = "Player Information"
                    GMessage_338.place(x=20,y=30,width=307,height=341)

                    GButton_472=tk.Button(f2)
                    GButton_472["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    GButton_472["font"] = ft
                    GButton_472["fg"] = "#000000"
                    GButton_472["justify"] = "center"
                    GButton_472["text"] = "Logout"
                    GButton_472.place(x=270,y=60,width=70,height=25)
                    GButton_472["command"] = runLogin

                    GMessage_659=tk.Message(f2)
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    GMessage_659["font"] = ft
                    GMessage_659["fg"] = "#333333"
                    GMessage_659["justify"] = "center"
                    GMessage_659["text"] = "UserData"
                    GMessage_659.place(x=240,y=0,width=128,height=66)

                    GButton_902=tk.Button(f2)
                    GButton_902["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    GButton_902["font"] = ft
                    GButton_902["fg"] = "#000000"
                    GButton_902["justify"] = "center"
                    GButton_902["text"] = "Mentor Matcher"
                    GButton_902.place(x=120,y=370,width=120,height=32)
                    GButton_902["command"] = runMatcher

                    

            def Matcher():
                GMessage_338=tk.Message(f3)
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                GMessage_338["font"] = ft
                GMessage_338["fg"] = "#333333"
                GMessage_338["justify"] = "center"
                GMessage_338["text"] = "Player Information"
                GMessage_338.place(x=120,y=130,width=196,height=214)

                GButton_20=tk.Button(f3)
                GButton_20["bg"] = "#e9e9ed"
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                GButton_20["font"] = ft
                GButton_20["fg"] = "#000000"
                GButton_20["justify"] = "center"
                GButton_20["text"] = "Play"
                GButton_20.place(x=60,y=200,width=48,height=122)
                GButton_20["command"] = runMatcher

                GButton_769=tk.Button(f3)
                GButton_769["bg"] = "#e9e9ed"
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                GButton_769["font"] = ft
                GButton_769["fg"] = "#000000"
                GButton_769["justify"] = "center"
                GButton_769["text"] = "Skip"
                GButton_769.place(x=320,y=200,width=51,height=129)
                GButton_769["command"] = runMatcher

                GButton_472=tk.Button(f3)
                GButton_472["bg"] = "#e9e9ed"
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                GButton_472["font"] = ft
                GButton_472["fg"] = "#000000"
                GButton_472["justify"] = "center"
                GButton_472["text"] = "Logout"
                GButton_472.place(x=360,y=50,width=70,height=25)
                GButton_472["command"] = runLogin

                GMessage_659=tk.Message(f3)
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                GMessage_659["font"] = ft
                GMessage_659["fg"] = "#333333"
                GMessage_659["justify"] = "center"
                GMessage_659["text"] = "UserData"
                GMessage_659.place(x=330,y=0,width=128,height=66)


            
                    

            Login()








if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
