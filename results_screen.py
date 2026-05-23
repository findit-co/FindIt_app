"""
Results Screen - Displays Resource Intelligence
Developer: Udo (Output & Presentation Engineer)
"""

import tkinter as tk
from tkinter import messagebox
import csv
import os

class ResultsScreen:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#f0f0f0")
        self.build_ui()
    
    def build_ui(self):
        # Header
        header_frame = tk.Frame(self.frame, bg="#5A1207", height=60)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text="FIND IT", font=("Arial", 18, "bold"), bg="#5A1207", fg="white")
        title.pack(pady=15)
        
        # Main content with scrolling
        canvas = tk.Canvas(self.frame, bg="#f0f0f0", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main container
        main_frame = tk.Frame(self.scrollable_frame, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=50, pady=30)
        
        # Resource name
        self.resource_label = tk.Label(main_frame, text="", font=("Arial", 32, "bold"), bg="#f0f0f0", fg="#3B0D06")
        self.resource_label.pack(pady=(0, 20))
        
        # Income section
        income_card = tk.Frame(main_frame, bg="#EADBC8", relief="solid", bd=1)
        income_card.pack(fill="x", pady=10)
        
        income_inner = tk.Frame(income_card, bg="#EADBC8")
        income_inner.pack(pady=15, padx=20)
        
        income_label = tk.Label(income_inner, text="INCOME POTENTIAL", font=("Arial", 14, "bold"), bg="#EADBC8", fg="#3B0D06")
        income_label.pack()
        
        self.income_label = tk.Label(income_inner, text="", font=("Arial", 20, "bold"), bg="#EADBC8", fg="#2E7D32")
        self.income_label.pack(pady=(5, 0))
        
        # Two-column layout
        columns_frame = tk.Frame(main_frame, bg="#f0f0f0")
        columns_frame.pack(fill="both", expand=True, pady=20)
        
        # LEFT COLUMN
        left_col = tk.Frame(columns_frame, bg="#f0f0f0")
        left_col.pack(side="left", fill="both", expand=True, padx=10)
        
        # Uses section
        uses_frame = tk.Frame(left_col, bg="white", relief="solid", bd=1)
        uses_frame.pack(fill="x", pady=5)
        
        uses_header = tk.Frame(uses_frame, bg="#5A1207", height=35)
        uses_header.pack(fill="x")
        uses_header.pack_propagate(False)
        
        uses_title = tk.Label(uses_header, text="POSSIBLE USES", font=("Arial", 12, "bold"), bg="#5A1207", fg="white")
        uses_title.pack(pady=8)
        
        self.uses_label = tk.Label(uses_frame, text="", font=("Arial", 11), bg="white", justify="left", anchor="w")
        self.uses_label.pack(pady=15, padx=15)
        
        # RIGHT COLUMN
        right_col = tk.Frame(columns_frame, bg="#f0f0f0")
        right_col.pack(side="left", fill="both", expand=True, padx=10)
        
        # Business Ideas section
        business_frame = tk.Frame(right_col, bg="white", relief="solid", bd=1)
        business_frame.pack(fill="x", pady=5)
        
        business_header = tk.Frame(business_frame, bg="#5A1207", height=35)
        business_header.pack(fill="x")
        business_header.pack_propagate(False)
        
        business_title = tk.Label(business_header, text="BUSINESS IDEAS", font=("Arial", 12, "bold"), bg="#5A1207", fg="white")
        business_title.pack(pady=8)
        
        self.business_label = tk.Label(business_frame, text="", font=("Arial", 11), bg="white", justify="left", anchor="w")
        self.business_label.pack(pady=15, padx=15)
        
        # Location Specific section
        location_frame = tk.Frame(right_col, bg="white", relief="solid", bd=1)
        location_frame.pack(fill="x", pady=5)
        
        location_header = tk.Frame(location_frame, bg="#5A1207", height=35)
        location_header.pack(fill="x")
        location_header.pack_propagate(False)
        
        location_title = tk.Label(location_header, text="LOCAL RELEVANCE", font=("Arial", 12, "bold"), bg="#5A1207", fg="white")
        location_title.pack(pady=8)
        
        self.location_label = tk.Label(location_frame, text="", font=("Arial", 11), bg="white", wraplength=400, justify="left")
        self.location_label.pack(pady=15, padx=15)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        new_btn = tk.Button(button_frame, text="NEW SEARCH", font=("Arial", 11, "bold"), bg="#757575", fg="white", padx=25, pady=8, command=lambda: self.controller.show_screen("input"))
        new_btn.pack(side="left", padx=10)
        
        save_btn = tk.Button(button_frame, text="SAVE TO HISTORY", font=("Arial", 11, "bold"), bg="#5A1207", fg="white", padx=25, pady=8, command=self.save_search)
        save_btn.pack(side="left", padx=10)
        
        dashboard_btn = tk.Button(button_frame, text="VIEW DASHBOARD", font=("Arial", 11, "bold"), bg="#1565C0", fg="white", padx=25, pady=8, command=lambda: self.controller.show_screen("dashboard"))
        dashboard_btn.pack(side="left", padx=10)
        
        # Footer navigation
        footer_frame = tk.Frame(self.frame, bg="#EADBC8", height=40)
        footer_frame.pack(fill="x", side="bottom")
        footer_frame.pack_propagate(False)
        
        footer_inner = tk.Frame(footer_frame, bg="#EADBC8")
        footer_inner.pack(pady=10)
        
        for name, screen in [("HOME", "home"), ("INPUT", "input"), ("RESULTS", "results"), ("DASHBOARD", "dashboard")]:
            btn = tk.Button(footer_inner, text=name, font=("Arial", 9), bg="#EADBC8", fg="#3B0D06", bd=0, cursor="hand2", command=lambda s=screen: self.controller.show_screen(s))
            btn.pack(side="left", padx=20)
    
    def show(self):
        self.frame.pack(fill="both", expand=True)
        self.refresh()
    
    def hide(self):
        self.frame.pack_forget()
    
    def refresh(self):
        """Get results from Dilibe's ResourceEngine"""
        if self.controller.current_resource and self.controller.resource_engine:
            resource = self.controller.current_resource["name"]
            location = self.controller.current_resource["location"]
            
            # Call Dilibe's find_resource method
            result = self.controller.resource_engine.find_resource(resource, location)
            
            # Check if result has an error
            if "error" in result:
                self.resource_label.config(text="Not Found")
                self.income_label.config(text="N/A")
                self.uses_label.config(text=f"• {result['error']}")
                self.business_label.config(text="• Try: Cassava, Plastic, Sand, or Palm Oil")
                self.location_label.config(text=f"Check spelling or try a different resource")
                self.controller.search_results = None
            else:
                # Display results from Dilibe's engine
                self.resource_label.config(text=result["resource"])
                self.income_label.config(text=result["income_estimate"])
                
                # Handle uses (could be list or string)
                if isinstance(result["uses"], list):
                    uses_text = "\n".join(f"• {u.strip()}" for u in result["uses"])
                else:
                    uses_text = f"• {result['uses']}"
                self.uses_label.config(text=uses_text)
                
                # Handle business ideas
                business_text = f"• {result['business_ideas']}"
                self.business_label.config(text=business_text)
                
                # Location specific info
                self.location_label.config(text=result["location_specific"])
                
                self.controller.search_results = result
    
    def save_search(self):
        """Save current search to CSV history"""
        if self.controller.current_resource and self.controller.search_results and self.controller.data_manager:
            success = self.controller.data_manager.save_search(
                self.controller.current_resource,
                self.controller.search_results
            )
            if success:
                messagebox.showinfo("Success", "Search saved to history!")
            else:
                messagebox.showerror("Error", "Could not save to history")