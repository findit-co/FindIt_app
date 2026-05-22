import tkinter as tk

class HomeScreen: 
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent)
        self.build_ui()
        
    def show(self):
        #to display screen frame
        self.frame.pack(fill="both", expand=True)
        
    def hide(self):
        # to hide the screen frame
        self.frame.pack_forget()

    def build_ui(self):
        #  Home screen ui design
        
        # colour scheme 
        bg_cream = "#EADBC8"       #background colour for most parts
        fg_dark = "#4A1512"        # deep brownish red for buttons and other elements
        
        self.frame.configure(bg=bg_cream)
        
        # to keep things centered horizontally
        self.frame.columnconfigure(0, weight=1)
        
        #putting in logo
        try:
            self.logo_img = tk.PhotoImage(file="logo.png")
            self.logo_img = self.logo_img.subsample(6, 6)  # resize logo
            
            logo_label = tk.Label(
                self.frame, 
                image=self.logo_img, 
                bg=bg_cream
            )
            logo_label.pack(pady=(60, 10))
        except Exception:
            # incase theres any issue, but the file is already in this folder
            logo_label = tk.Label(
                self.frame, 
                text="🔍\n[ kindly make sure youve placed logo.png in your project folder ]", 
                font=("Poppins", 14, "italic"), 
                bg=bg_cream, 
                fg=fg_dark,
                pady=20
            )
            logo_label.pack(pady=(30, 10))
        
        # title w brand name
        # title_text = tk.Label(
        #     self.frame,
        #     text="FIND IT",
        #     font=("Poppins", 42, "bold"),
        #     bg=bg_cream,
        #     fg=fg_dark
        # )
        # title_text.pack()

        # catchy tagline
        headline_label = tk.Label(
            self.frame, 
            text="Turn what you can see into\nwhat you can create.", 
            font=("Poppins", 22, "bold"), 
            bg=bg_cream, 
            fg=fg_dark,
            justify="center"
        )
        headline_label.pack(pady=(5, 20))
        
        #straight line across page for decorarive purposes
        line_across = tk.Frame(self.frame, bg=fg_dark, height=1, width=500)
        line_across.pack(pady=10)
        
        #mini explanation
        body_label = tk.Label(
            self.frame, 
            text="Empowering you to discover the value, uses and\nincome opportunities in the resources around you.", 
            font=("Poppins", 13), 
            bg=bg_cream, 
            fg="#2C1B18",
            justify="center"
        )
        body_label.pack(pady=(10, 40))
        
        #callto action button frame container 
        btn_container = tk.Frame(self.frame, width=300, height=100, bg=bg_cream)
        btn_container.pack_propagate(False) #freezing the layout
        btn_container.pack()

        #  link button to show_screen("input")(kennedys page)
        get_started_btn = tk.Button(
            btn_container, 
            text="Get Started", 
            font=("Poppins", 16, "bold"), 
            bg=fg_dark,        
            fg="white", 
            activebackground="#330E0C", 
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_screen("input")
        )
        get_started_btn.pack(expand=True, fill="both")