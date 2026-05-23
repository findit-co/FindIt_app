"""
Loading Screen - Optional
"""
import tkinter as tk

class LoadingScreen:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#f0f0f0")
        self.build_ui()
    
    def build_ui(self):
        title = tk.Label(self.frame, text="FIND IT", font=("Poppins", 16, "bold"), bg="#f0f0f0", fg="#5A1207")
        title.pack(pady=50)
        
        loading = tk.Label(self.frame, text="Analyzing Resource...", font=("Poppins", 24, "bold"), bg="#f0f0f0")
        loading.pack(pady=40)
        
        message = tk.Label(self.frame, text="Please wait while we find the best uses and opportunities for you.", font=("Poppins", 12), bg="#f0f0f0")
        message.pack(pady=20)
        
        # Spinner animation (simple)
        self.spinner = tk.Label(self.frame, text="⏳", font=("Arial", 30), bg="#f0f0f0")
        self.spinner.pack(pady=20)
        
        # Navigation
        nav_frame = tk.Frame(self.frame, bg="#f0f0f0")
        nav_frame.pack(side="bottom", pady=20)
        
        for name in ["Home", "Input", "Results", "Dashboard"]:
            btn = tk.Button(nav_frame, text=name, font=("Poppins", 10), command=lambda n=name.lower(): self.controller.show_screen(n) if n != "results" else None)
            btn.pack(side="left", padx=15)
    
    def show(self):
        self.frame.pack(fill="both", expand=True)
        # Auto-redirect to results after 2 seconds
        self.frame.after(2000, lambda: self.controller.show_screen("results"))
    
    def hide(self):
        self.frame.pack_forget()