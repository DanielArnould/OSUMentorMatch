import customtkinter
import OAuthCheck


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        

        # checkbox = customtkinter.CTkCheckBox(self, text="Remember Me")
        # checkbox.pack(pady=12, padx=10)



class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class ScrollableMentorFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.username_list = []
        self.button_list = []
        self.similarity_scores =[]

    def add_mentor(self, username, similarity_score, pfp=None):
        username_label = customtkinter.CTkLabel(self, text=username, image=pfp, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="See Profile", width=100, height=24)
        similarity_label = customtkinter.CTkLabel(self, text=similarity_score, padx=20, anchor="e")
        if self.command is not None:
            button.configure(command=lambda: self.command(username))
        username_label.grid(row=len(self.username_list), column=0, pady=(0, 20), sticky="w")
        similarity_label.grid(row=len(self.similarity_scores), column=1, pady=(0, 20), sticky="e")
        button.grid(row=len(self.button_list), column=2, pady=(0, 20), padx=10)
        self.username_list.append(username_label)
        self.similarity_scores.append(similarity_label)
        self.button_list.append(button)





def login():
    print("Test")

