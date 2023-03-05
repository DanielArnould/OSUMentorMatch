import sys
import os
import tkinter as otk
import tkinter.font as tkFont
from tkinter import *  
import customtkinter as tk
import OAuthCheck   


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
                

                OAuthCheck.check_OAuth()
                f2.pack(fill="both", expand=True, padx=0, pady=0)
                f1.pack_forget()
                Profile()
                
            
            

            def Login():
                    
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    lbl_Login=tk.CTkLabel(f1)
                    lbl_Login["anchor"] = "center"
                    lbl_Login["font"] = ft
                    lbl_Login["fg"] = "#333333"
                    lbl_Login["justify"] = "center"
                    lbl_Login["text"] = "Login"
                    lbl_Login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

                    btn_Login=tk.CTkButton(f1)
                    btn_Login["bg"] = "#e9e9ed"
                    btn_Login["font"] = ft
                    btn_Login["fg"] = "#000000"
                    btn_Login["justify"] = "center"
                    btn_Login["text"] = "Login With Osu"
                    btn_Login.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
                    btn_Login["command"] = runProfile
                        
                


                        
            def Profile():
                

                    lbl_playerStats=tk.Message(f2)
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    lbl_playerStats["font"] = ft
                    lbl_playerStats["fg"] = "#333333"
                    lbl_playerStats["justify"] = "center"
                    lbl_playerStats["text"] = "Player Information"
                    lbl_playerStats.place(x=20,y=30,width=307,height=341)

                    btn_logout=tk.Button(f2)
                    btn_logout["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    btn_logout["font"] = ft
                    btn_logout["fg"] = "#000000"
                    btn_logout["justify"] = "center"
                    btn_logout["text"] = "Logout"
                    btn_logout.place(x=270,y=60,width=70,height=25)
                    btn_logout["command"] = runLogin

                    lbl_userData=tk.Message(f2)
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    lbl_userData["font"] = ft
                    lbl_userData["fg"] = "#333333"
                    lbl_userData["justify"] = "center"
                    lbl_userData["text"] = "UserData"
                    lbl_userData.place(x=240,y=0,width=128,height=66)

                    btn_matcher=tk.Button(f2)
                    btn_matcher["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family='TkDefaultFont',size=10)
                    btn_matcher["font"] = ft
                    btn_matcher["fg"] = "#000000"
                    btn_matcher["justify"] = "center"
                    btn_matcher["text"] = "Mentor Matcher"
                    btn_matcher.place(x=120,y=370,width=120,height=32)
                    btn_matcher["command"] = runMatcher

                    

            def Matcher():
                lbl_playerStats=tk.Message(f3)
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                lbl_playerStats["font"] = ft
                lbl_playerStats["fg"] = "#333333"
                lbl_playerStats["justify"] = "center"
                lbl_playerStats["text"] = "Player Information"
                lbl_playerStats.place(x=120,y=130,width=196,height=214)

                btn_playWith=tk.Button(f3)
                btn_playWith["bg"] = "#e9e9ed"
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                btn_playWith["font"] = ft
                btn_playWith["fg"] = "#000000"
                btn_playWith["justify"] = "center"
                btn_playWith["text"] = "Play"
                btn_playWith.place(x=60,y=200,width=48,height=122)
                btn_playWith["command"] = runMatcher  

                btn_SkipPlayer=tk.Button(f3)
                btn_SkipPlayer["bg"] = "#e9e9ed"
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                btn_SkipPlayer["font"] = ft
                btn_SkipPlayer["fg"] = "#000000"
                btn_SkipPlayer["justify"] = "center"
                btn_SkipPlayer["text"] = "Skip"
                btn_SkipPlayer.place(x=320,y=200,width=51,height=129)
                btn_SkipPlayer["command"] = runMatcher

                btn_logout=tk.Button(f3)
                btn_logout["bg"] = "#e9e9ed"
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                btn_logout["font"] = ft
                btn_logout["fg"] = "#000000"
                btn_logout["justify"] = "center"
                btn_logout["text"] = "Logout"
                btn_logout.place(x=360,y=50,width=70,height=25)
                btn_logout["command"] = runLogin

                lbl_userData=tk.Message(f3)
                ft = tkFont.Font(family='TkDefaultFont',size=10)
                lbl_userData["font"] = ft
                lbl_userData["fg"] = "#333333"
                lbl_userData["justify"] = "center"
                lbl_userData["text"] = "UserData"
                lbl_userData.place(x=330,y=0,width=128,height=66)

                lbx_Leaderboard=tk.Listbox(f3)
                lbx_Leaderboard["borderwidth"] = "1px"
                lbx_Leaderboard["font"] = ft
                lbx_Leaderboard["fg"] = "#333333"
                lbx_Leaderboard["justify"] = "center"
                lbx_Leaderboard.place(x=60,y=340,width=358,height=102)


            
                    

            Login()








if __name__ == "__main__":
    root = tk.CTk()
    app = App(root)
    root.mainloop()
    
