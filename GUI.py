import customtkinter

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.login_label = customtkinter.CTkLabel(self, text="Login System", font=("Roboto", 24))
        self.login_label.pack(pady=12, padx=10)

        self.client_id_entry = customtkinter.CTkEntry(self, placeholder_text="Client ID", show="*")
        self.client_id_entry.pack(pady=12, padx=10)

        self.client_key_entry = customtkinter.CTkEntry(self, placeholder_text="Client Secret", show="*")
        self.client_key_entry.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="username")
        self.username_entry.pack(pady=12, padx=10)

        login_button = customtkinter.CTkButton(self, text="Login", command=login)
        login_button.pack(pady=12, padx=12)

        # checkbox = customtkinter.CTkCheckBox(self, text="Remember Me")
        # checkbox.pack(pady=12, padx=10)

class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=300, corner_radius=0)

        self.login_label = customtkinter.CTkLabel(self, text="Login System", font=("Roboto", 24))
        self.login_label.grid(row=0, column=0)


class ScrollableMentorFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(self, master, label_text="CTKScrollabelFrame")

        self.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
            
def login():
    print("Test")