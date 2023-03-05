import customtkinter
import OAuthCheck


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        

        # checkbox = customtkinter.CTkCheckBox(self, text="Remember Me")
        # checkbox.pack(pady=12, padx=10)



class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=300, corner_radius=0)

        self.login_label = customtkinter.CTkLabel(self, text="Sidebar!", font=("Roboto", 24))
        self.login_label.grid(row=0, column=0, padx=50)


class ScrollableMentorFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="See Profile", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 20), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 20), padx=10)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return




def login():
    print("Test")

