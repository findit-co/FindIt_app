"""
Dashboard Screen - Professional Table View
Developer: Tochi
"""
import tkinter as tk
from tkinter import ttk
import csv

class DashboardScreen:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#f0f0f0")
        self.build_ui()
    
    def build_ui(self):
        # Header
        title = tk.Label(self.frame, text="FIND IT", font=("Poppins", 16, "bold"), bg="#f0f0f0", fg="#5A1207")
        title.pack(pady=10)
        
        # Main title
        main_title = tk.Label(self.frame, text="Search History", font=("Poppins", 28, "bold"), bg="#f0f0f0")
        main_title.pack(pady=10)
        
        # Subtitle
        subtitle = tk.Label(self.frame, text="View your previous resource searches.", font=("Poppins", 12), bg="#f0f0f0")
        subtitle.pack(pady=(0, 20))
        
        # Table frame
        table_frame = tk.Frame(self.frame, bg="#f0f0f0")
        table_frame.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Treeview table
        columns = ("ID", "Resource", "Category", "Location", "Date & Time")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)
        
        # Column headings
        self.tree.heading("ID", text="#")
        self.tree.heading("Resource", text="Resource")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Date & Time", text="Date & Time")
        
        # Column widths
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Resource", width=150)
        self.tree.column("Category", width=130)
        self.tree.column("Location", width=130)
        self.tree.column("Date & Time", width=200)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Total searches
        self.total_label = tk.Label(self.frame, text="Total Searches: 0", font=("Poppins", 12, "bold"), bg="#f0f0f0", fg="#5A1207")
        self.total_label.pack(pady=15)
        
        # Buttons
        button_frame = tk.Frame(self.frame, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        refresh_btn = tk.Button(button_frame, text="REFRESH", font=("Poppins", 10, "bold"), bg="#1565C0", fg="white", padx=20, pady=5, command=self.load_history)
        refresh_btn.pack(side="left", padx=10)
        
        home_btn = tk.Button(button_frame, text="HOME", font=("Poppins", 10, "bold"), bg="#757575", fg="white", padx=20, pady=5, command=lambda: self.controller.show_screen("home"))
        home_btn.pack(side="left", padx=10)
        
        new_btn = tk.Button(button_frame, text="NEW SEARCH", font=("Poppins", 10, "bold"), bg="#2E7D32", fg="white", padx=20, pady=5, command=lambda: self.controller.show_screen("input"))
        new_btn.pack(side="left", padx=10)
    
    def show(self):
        self.frame.pack(fill="both", expand=True)
        self.load_history()
    
    def hide(self):
        self.frame.pack_forget()
    
    def load_history(self):
        # Clear existing
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Category mapping
        categories = {
            "cassava": "Agricultural", "plastic": "Waste", "sand": "Mineral", 
            "palm oil": "Agricultural", "palm oil": "Agricultural"
        }
        
        count = 0
        try:
            with open("search_history.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for i, row in enumerate(reader, 1):
                    if len(row) >= 5:
                        resource = row[1].lower()
                        category = categories.get(resource, "General")
                        self.tree.insert("", "end", values=(i, row[1].title(), category, row[2], row[0]))
                        count += 1
        except FileNotFoundError:
            self.tree.insert("", "end", values=("—", "No data available", "—", "—", "Perform a search first"))
        
        self.total_label.config(text=f"Total Searches: {count}")