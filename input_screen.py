"""
Input Screen - Resource entry
Developer: Kennedy (Input Systems Engineer)
"""
import tkinter as tk
from tkinter import ttk, messagebox

class InputScreen:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#FDF5E0")
        self.build_ui()

    def build_ui(self):
        # Make frame fill entire window
        self.frame.pack(fill="both", expand=True)
        
        # ========== HEADER ==========
        header_frame = tk.Frame(self.frame, bg="white", height=45)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(
            header_frame,
            text="FIND IT",
            bg="white",
            fg="#5A1207",
            font=("Poppins", 16, "bold")
        )
        header_label.pack(side="left", padx=20, pady=10)
        
        # ========== TITLE SECTION ==========
        title_label = tk.Label(
            self.frame,
            text="Identify a Resource",
            bg="#FDF5E0",
            fg="#3B0D06",
            font=("Poppins", 28, "bold")
        )
        title_label.pack(pady=(15, 5))
        
        subtitle_label = tk.Label(
            self.frame,
            text="Tell us what resource you have around you",
            bg="#FDF5E0",
            fg="#333333",
            font=("Poppins", 13)
        )
        subtitle_label.pack(pady=(0, 15))
        
        # ========== WHITE FRAME FOR INPUT SECTION ==========
        white_frame = tk.Frame(
            self.frame,
            bg="white",
            relief="solid",
            bd=1
        )
        white_frame.pack(fill="both", expand=True, padx=60, pady=(0, 10))
        
        # Inner padding for white frame
        inner_frame = tk.Frame(white_frame, bg="white")
        inner_frame.pack(fill="both", expand=True, padx=25, pady=15)
        
        # ========== CHOOSE INPUT METHOD ==========
        method_label = tk.Label(
            inner_frame,
            text="Choose Input Method",
            bg="white",
            fg="#3B0D06",
            font=("Poppins", 16, "bold")
        )
        method_label.pack(anchor="w", pady=(0, 12))
        
        # Camera and Upload cards - side by side
        cards_frame = tk.Frame(inner_frame, bg="white")
        cards_frame.pack(fill="x", pady=(0, 15))
        
        # Camera Card
        camera_card = tk.Frame(
            cards_frame,
            bg="#F5F5F5",
            relief="solid",
            bd=1,
            height=100
        )
        camera_card.pack(side="left", padx=(0, 25), expand=True, fill="x")
        camera_card.pack_propagate(False)
        
        camera_icon = tk.Label(
            camera_card,
            text="📷",
            bg="#F5F5F5",
            fg="#5A1207",
            font=("Segoe UI Symbol", 28)
        )
        camera_icon.pack(pady=(12, 2))
        
        camera_title = tk.Label(
            camera_card,
            text="Use Camera",
            bg="#F5F5F5",
            fg="#3B0D06",
            font=("Poppins", 12, "bold")
        )
        camera_title.pack()
        
        camera_subtitle = tk.Label(
            camera_card,
            text="Capture image using webcam",
            bg="#F5F5F5",
            fg="#888888",
            font=("Poppins", 9)
        )
        camera_subtitle.pack(pady=(2, 10))
        
        # Upload Card
        upload_card = tk.Frame(
            cards_frame,
            bg="#F5F5F5",
            relief="solid",
            bd=1,
            height=100
        )
        upload_card.pack(side="left", expand=True, fill="x")
        upload_card.pack_propagate(False)
        
        upload_icon = tk.Label(
            upload_card,
            text="🖼️",
            bg="#F5F5F5",
            fg="#5A1207",
            font=("Segoe UI Symbol", 28)
        )
        upload_icon.pack(pady=(12, 2))
        
        upload_title = tk.Label(
            upload_card,
            text="Upload Image",
            bg="#F5F5F5",
            fg="#3B0D06",
            font=("Poppins", 12, "bold")
        )
        upload_title.pack()
        
        upload_subtitle = tk.Label(
            upload_card,
            text="Choose image from device",
            bg="#F5F5F5",
            fg="#888888",
            font=("Poppins", 9)
        )
        upload_subtitle.pack(pady=(2, 10))
        
        # Divider line
        divider = tk.Frame(inner_frame, bg="#CCCCCC", height=1)
        divider.pack(fill="x", pady=10)
        
        # ========== OR ENTER DETAILS ==========
        details_label = tk.Label(
            inner_frame,
            text="Or Enter Details (Optional)",
            bg="white",
            fg="#3B0D06",
            font=("Poppins", 14, "bold")
        )
        details_label.pack(anchor="w", pady=(8, 10))
        
        # Resource Entry Field
        resource_label = tk.Label(
            inner_frame,
            text="Resource Name:",
            bg="white",
            fg="#333333",
            font=("Poppins", 11)
        )
        resource_label.pack(anchor="w", pady=(0, 3))
        
        self.resource_entry = tk.Entry(
            inner_frame,
            bg="#F5F5F5",
            fg="#888888",
            font=("Poppins", 11),
            relief="solid",
            bd=1
        )
        self.resource_entry.pack(fill="x", ipady=8, pady=(0, 12))
        self.resource_entry.insert(0, "e.g., Cassava, Sand, Plastic Bottles")
        
        # Bind placeholder behavior
        self.resource_entry.bind("<FocusIn>", self.clear_placeholder)
        self.resource_entry.bind("<FocusOut>", self.restore_placeholder)
        
        # Category and Location row (side by side)
        row_frame = tk.Frame(inner_frame, bg="white")
        row_frame.pack(fill="x", pady=(0, 15))
        
        # Category (left side)
        category_frame = tk.Frame(row_frame, bg="white")
        category_frame.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        category_label = tk.Label(
            category_frame,
            text="Category (Optional)",
            bg="white",
            fg="#333333",
            font=("Poppins", 11)
        )
        category_label.pack(anchor="w", pady=(0, 3))
        
        self.category_var = tk.StringVar(value="Select Category")
        self.category_dropdown = ttk.Combobox(
            category_frame,
            textvariable=self.category_var,
            values=["Agriculture", "Mining", "Recycling", "Manufacturing", "Waste"],
            font=("Poppins", 10),
            state="readonly"
        )
        self.category_dropdown.pack(fill="x", ipady=3)
        
        # Location (right side)
        location_frame = tk.Frame(row_frame, bg="white")
        location_frame.pack(side="left", fill="x", expand=True)
        
        location_label = tk.Label(
            location_frame,
            text="Your Location (Optional)",
            bg="white",
            fg="#333333",
            font=("Poppins", 11)
        )
        location_label.pack(anchor="w", pady=(0, 3))
        
        self.location_var = tk.StringVar(value="Select Location")
        self.location_dropdown = ttk.Combobox(
            location_frame,
            textvariable=self.location_var,
            values=["Lagos", "Abuja", "Port Harcourt", "Kano", "Aba", "Enugu", "Ibadan"],
            font=("Poppins", 10),
            state="readonly"
        )
        self.location_dropdown.pack(fill="x", ipady=3)
        
        # ========== ANALYZE BUTTON ==========
        analyze_btn = tk.Button(
            inner_frame,
            text="ANALYZE RESOURCES",
            bg="#5A1207",
            fg="white",
            font=("Poppins", 13, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.submit
        )
        analyze_btn.pack(fill="x", pady=(8, 8), ipady=10)
        
        # ========== BOTTOM NAVIGATION BAR ==========
        nav_frame = tk.Frame(self.frame, bg="#EADBC8", height=42)
        nav_frame.pack(fill="x", side="bottom")
        nav_frame.pack_propagate(False)
        
        nav_inner = tk.Frame(nav_frame, bg="#EADBC8")
        nav_inner.pack(expand=True)
        
        # Navigation buttons
        nav_items = [
            ("HOME", "home"),
            ("INPUT", "input"),
            ("RESULTS", "results"),
            ("DASHBOARD", "dashboard")
        ]
        
        for text, screen in nav_items:
            btn = tk.Button(
                nav_inner,
                text=text,
                font=("Poppins", 10, "bold"),
                bg="#EADBC8",
                fg="#5A1207" if screen == "input" else "#3B0D06",
                bd=0,
                cursor="hand2",
                activebackground="#D4B896",
                command=lambda s=screen: self.controller.show_screen(s)
            )
            btn.pack(side="left", padx=30, pady=8)
    
    def clear_placeholder(self, event):
        """Clear placeholder text when user clicks"""
        if self.resource_entry.get() == "e.g., Cassava, Sand, Plastic Bottles":
            self.resource_entry.delete(0, tk.END)
            self.resource_entry.config(fg="black", bg="white")
    
    def restore_placeholder(self, event):
        """Restore placeholder if field is empty"""
        if self.resource_entry.get().strip() == "":
            self.resource_entry.insert(0, "e.g., Cassava, Sand, Plastic Bottles")
            self.resource_entry.config(fg="#888888", bg="#F5F5F5")
    
    def submit(self):
        """Get user input and send to controller"""
        resource = self.resource_entry.get().strip()
        
        # Check if it's placeholder or empty
        if resource == "" or resource == "e.g., Cassava, Sand, Plastic Bottles":
            messagebox.showwarning("Input Error", "Please enter a resource name")
            return
        
        category = self.category_var.get()
        location = self.location_var.get()
        
        # Validate category/location selections
        if category == "Select Category":
            category = "General"
        if location == "Select Location":
            location = "Lagos"
        
        # Send to controller
        self.controller.set_resource_input(resource, category, location)
        self.controller.show_screen("results")
    
    def show(self):
        """Show the screen"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide the screen"""
        self.frame.pack_forget()