"""
Input Screen - Resource entry
Developer: Kennedy (Input Systems Engineer)
Design matches Figma exactly
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
        header_frame = tk.Frame(self.frame, bg="white", height=50)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(
            header_frame,
            text="FIND IT",
            bg="white",
            fg="#5A1207",
            font=("Poppins", 18, "bold")
        )
        header_label.pack(side="left", padx=25, pady=12)
        
        # ========== TITLE SECTION ==========
        title_frame = tk.Frame(self.frame, bg="#F2D9B0")
        title_frame.pack(fill="x", side="top")
        
        title_label = tk.Label(
            title_frame,
            text="Identify a Resource",
            bg="#F2D9B0",
            fg="#3B0D06",
            font=("Poppins", 32, "bold")
        )
        title_label.pack(pady=(15, 5))
        
        subtitle_label = tk.Label(
            title_frame,
            text="Tell us what resource you have around you",
            bg="#F2D9B0",
            fg="#333333",
            font=("Poppins", 16)
        )
        subtitle_label.pack(pady=(0, 15))
        
        # ========== MAIN CONTENT (NO SCROLL) ==========
        main_frame = tk.Frame(self.frame, bg="#FDF5E0")
        main_frame.pack(fill="both", expand=True, padx=50, pady=10)
        
        # "Choose Input Method" title
        method_label = tk.Label(
            main_frame,
            text="Choose Input Method",
            bg="#FDF5E0",
            fg="#3B0D06",
            font=("Poppins", 18, "bold")
        )
        method_label.pack(anchor="w", pady=(0, 10))
        
        # Camera and Upload cards - side by side
        cards_frame = tk.Frame(main_frame, bg="#FDF5E0")
        cards_frame.pack(fill="x", pady=(0, 15))
        
        # Camera Card
        camera_card = tk.Frame(
            cards_frame,
            bg="white",
            relief="solid",
            bd=1,
            width=320,
            height=130
        )
        camera_card.pack(side="left", padx=(0, 40), expand=True, fill="x")
        camera_card.pack_propagate(False)
        
        camera_icon = tk.Label(
            camera_card,
            text="📷",
            bg="white",
            fg="#5A1207",
            font=("Segoe UI Symbol", 32)
        )
        camera_icon.pack(pady=(20, 5))
        
        camera_title = tk.Label(
            camera_card,
            text="Use Camera",
            bg="white",
            fg="#3B0D06",
            font=("Poppins", 14, "bold")
        )
        camera_title.pack()
        
        camera_subtitle = tk.Label(
            camera_card,
            text="Capture image using your webcam",
            bg="white",
            fg="#888888",
            font=("Poppins", 10)
        )
        camera_subtitle.pack(pady=(5, 15))
        
        # Upload Card
        upload_card = tk.Frame(
            cards_frame,
            bg="white",
            relief="solid",
            bd=1,
            width=320,
            height=130
        )
        upload_card.pack(side="left", expand=True, fill="x")
        upload_card.pack_propagate(False)
        
        upload_icon = tk.Label(
            upload_card,
            text="🖼️",
            bg="white",
            fg="#5A1207",
            font=("Segoe UI Symbol", 32)
        )
        upload_icon.pack(pady=(20, 5))
        
        upload_title = tk.Label(
            upload_card,
            text="Upload Image",
            bg="white",
            fg="#3B0D06",
            font=("Poppins", 14, "bold")
        )
        upload_title.pack()
        
        upload_subtitle = tk.Label(
            upload_card,
            text="Choose image from your device",
            bg="white",
            fg="#888888",
            font=("Poppins", 10)
        )
        upload_subtitle.pack(pady=(5, 15))
        
        # Divider line
        divider = tk.Frame(main_frame, bg="#CCCCCC", height=1)
        divider.pack(fill="x", pady=10)
        
        # "Or Enter Details (Optional)" section
        details_label = tk.Label(
            main_frame,
            text="Or Enter Details (Optional)",
            bg="#FDF5E0",
            fg="#3B0D06",
            font=("Poppins", 16, "bold")
        )
        details_label.pack(anchor="w", pady=(10, 10))
        
        # Resource Entry Field
        resource_frame = tk.Frame(main_frame, bg="#FDF5E0")
        resource_frame.pack(fill="x", pady=(0, 15))
        
        self.resource_entry = tk.Entry(
            resource_frame,
            bg="white",
            fg="#888888",
            font=("Poppins", 12),
            relief="solid",
            bd=1
        )
        self.resource_entry.pack(fill="x", ipady=10)
        self.resource_entry.insert(0, "Enter Resource (e.g. Cassava, Sand, Plastic Bottles, Palm Oil)")
        
        # Bind placeholder behavior
        self.resource_entry.bind("<FocusIn>", self.clear_placeholder)
        self.resource_entry.bind("<FocusOut>", self.restore_placeholder)
        
        # Category and Location row (side by side)
        row_frame = tk.Frame(main_frame, bg="#FDF5E0")
        row_frame.pack(fill="x", pady=(0, 15))
        
        # Category (left side)
        category_frame = tk.Frame(row_frame, bg="#FDF5E0")
        category_frame.pack(side="left", fill="x", expand=True, padx=(0, 20))
        
        category_label = tk.Label(
            category_frame,
            text="Category (Optional)",
            bg="#FDF5E0",
            fg="#333333",
            font=("Poppins", 12)
        )
        category_label.pack(anchor="w", pady=(0, 5))
        
        self.category_var = tk.StringVar(value="Select Category")
        self.category_dropdown = ttk.Combobox(
            category_frame,
            textvariable=self.category_var,
            values=["Agriculture", "Mining", "Recycling", "Manufacturing", "Waste"],
            font=("Poppins", 11),
            state="readonly"
        )
        self.category_dropdown.pack(fill="x", ipady=5)
        
        # Location (right side)
        location_frame = tk.Frame(row_frame, bg="#FDF5E0")
        location_frame.pack(side="left", fill="x", expand=True)
        
        location_label = tk.Label(
            location_frame,
            text="Your Location (Optional)",
            bg="#FDF5E0",
            fg="#333333",
            font=("Poppins", 12)
        )
        location_label.pack(anchor="w", pady=(0, 5))
        
        self.location_var = tk.StringVar(value="Select Location")
        self.location_dropdown = ttk.Combobox(
            location_frame,
            textvariable=self.location_var,
            values=["Lagos", "Abuja", "Port Harcourt", "Kano", "Aba", "Enugu", "Ibadan"],
            font=("Poppins", 11),
            state="readonly"
        )
        self.location_dropdown.pack(fill="x", ipady=5)
        
        # ANALYZE RESOURCES Button
        analyze_btn = tk.Button(
            main_frame,
            text="ANALYZE RESOURCES",
            bg="#5A1207",
            fg="white",
            font=("Poppins", 14, "bold"),
            relief="flat",
            cursor="hand2",
            padx=40,
            pady=12,
            command=self.submit
        )
        analyze_btn.pack(pady=(10, 20))
        
        # ========== BOTTOM NAVIGATION ==========
        nav_frame = tk.Frame(self.frame, bg="#EADBC8", height=45)
        nav_frame.pack(fill="x", side="bottom")
        nav_frame.pack_propagate(False)
        
        nav_inner = tk.Frame(nav_frame, bg="#EADBC8")
        nav_inner.pack(expand=True)
        
        # Navigation buttons matching Figma
        nav_items = [
            ("Home", "home"),
            ("Input", "input"),
            ("Results", "results"),
            ("Dashboard", "dashboard")
        ]
        
        for text, screen in nav_items:
            btn = tk.Button(
                nav_inner,
                text=text,
                font=("Poppins", 11),
                bg="#EADBC8",
                fg="#3B0D06" if screen != "input" else "#5A1207",
                bd=0,
                cursor="hand2",
                command=lambda s=screen: self.controller.show_screen(s)
            )
            btn.pack(side="left", padx=25, pady=10)
    
    def clear_placeholder(self, event):
        """Clear placeholder text when user clicks"""
        if self.resource_entry.get() == "Enter Resource (e.g. Cassava, Sand, Plastic Bottles, Palm Oil)":
            self.resource_entry.delete(0, tk.END)
            self.resource_entry.config(fg="black")
    
    def restore_placeholder(self, event):
        """Restore placeholder if field is empty"""
        if self.resource_entry.get().strip() == "":
            self.resource_entry.insert(0, "Enter Resource (e.g. Cassava, Sand, Plastic Bottles, Palm Oil)")
            self.resource_entry.config(fg="#888888")
    
    def submit(self):
        """Get user input and send to controller"""
        resource = self.resource_entry.get().strip()
        
        # Check if it's placeholder or empty
        if resource == "" or resource == "Enter Resource (e.g. Cassava, Sand, Plastic Bottles, Palm Oil)":
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