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

        self.frame = tk.Frame(
            parent,
            bg="#F6EEDC"
        )

        self.build_ui()

    # ==========================================
    # BUILD UI
    # ==========================================

    def build_ui(self):

        self.frame.pack(fill="both", expand=True)

        # ==========================================
        # HEADER
        # ==========================================

        header_frame = tk.Frame(
            self.frame,
            bg="white",
            height=40
        )

        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        header_label = tk.Label(
            header_frame,
            text="FIND IT",
            bg="white",
            fg="#3B0D06",
            font=("Poppins", 14, "bold")
        )

        header_label.pack(
            side="left",
            padx=15,
            pady=8
        )

        # ==========================================
        # TITLE SECTION
        # ==========================================

        title_label = tk.Label(
            self.frame,
            text="Identify a Resource",
            bg="#F6EEDC",
            fg="#2B0A05",
            font=("Poppins", 24, "bold")
        )

        title_label.pack(
            pady=(10, 2)
        )

        subtitle_label = tk.Label(
            self.frame,
            text="Tell us what resource you have around you",
            bg="#F6EEDC",
            fg="#555555",
            font=("Poppins", 10)
        )

        subtitle_label.pack(
            pady=(0, 10)
        )

        # ==========================================
        # MAIN WHITE CONTAINER
        # ==========================================

        white_frame = tk.Frame(
            self.frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        white_frame.pack(
            fill="x",
            padx=70,
            pady=(0, 8)
        )

        # ==========================================
        # INNER CONTENT FRAME
        # ==========================================

        inner_frame = tk.Frame(
            white_frame,
            bg="white"
        )

        inner_frame.pack(
            fill="x",
            padx=20,
            pady=14
        )

        # ==========================================
        # INPUT METHOD TITLE
        # ==========================================

        method_label = tk.Label(
            inner_frame,
            text="Choose Input Method",
            bg="white",
            fg="#333333",
            font=("Poppins", 11, "bold")
        )

        method_label.pack(
            anchor="w",
            pady=(0, 8)
        )

        # ==========================================
        # CARDS CONTAINER
        # ==========================================

        cards_frame = tk.Frame(
            inner_frame,
            bg="white"
        )

        cards_frame.pack(
            fill="x",
            pady=(0, 10)
        )

        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        # ==========================================
        # CAMERA CARD
        # ==========================================

        camera_card = tk.Frame(
            cards_frame,
            bg="white",
            bd=1,
            relief="solid",
            height=120
        )

        camera_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        camera_card.grid_propagate(False)

        camera_icon = tk.Label(
            camera_card,
            text="📷",
            bg="white",
            fg="#6B0F0F",
            font=("Segoe UI Emoji", 26)
        )

        camera_icon.pack(
            pady=(12, 2)
        )

        camera_title = tk.Label(
            camera_card,
            text="Use Camera",
            bg="white",
            fg="#222222",
            font=("Poppins", 11, "bold")
        )

        camera_title.pack()

        camera_subtitle = tk.Label(
            camera_card,
            text="Capture image using\nyour webcam",
            bg="white",
            fg="#777777",
            justify="center",
            font=("Poppins", 8)
        )

        camera_subtitle.pack()

        # ==========================================
        # UPLOAD CARD
        # ==========================================

        upload_card = tk.Frame(
            cards_frame,
            bg="white",
            bd=1,
            relief="solid",
            height=120
        )

        upload_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        upload_card.grid_propagate(False)

        upload_icon = tk.Label(
            upload_card,
            text="↑",
            bg="white",
            fg="#6B0F0F",
            font=("Poppins", 28)
        )

        upload_icon.pack(
            pady=(12, 2)
        )

        upload_title = tk.Label(
            upload_card,
            text="Upload Image",
            bg="white",
            fg="#222222",
            font=("Poppins", 11, "bold")
        )

        upload_title.pack()

        upload_subtitle = tk.Label(
            upload_card,
            text="Choose image from\nyour device",
            bg="white",
            fg="#777777",
            justify="center",
            font=("Poppins", 8)
        )

        upload_subtitle.pack()

        # ==========================================
        # DIVIDER
        # ==========================================

        divider = tk.Frame(
            inner_frame,
            bg="#DDDDDD",
            height=1
        )

        divider.pack(
            fill="x",
            pady=8
        )

        # ==========================================
        # DETAILS LABEL
        # ==========================================

        details_label = tk.Label(
            inner_frame,
            text="Or Enter Details (Optional)",
            bg="white",
            fg="#333333",
            font=("Poppins", 11, "bold")
        )

        details_label.pack(
            anchor="w",
            pady=(0, 8)
        )

        # ==========================================
        # RESOURCE ENTRY
        # ==========================================

        self.resource_entry = tk.Entry(
            inner_frame,
            font=("Poppins", 10),
            relief="solid",
            bd=1,
            bg="white",
            fg="#888888"
        )

        self.resource_entry.pack(
            fill="x",
            ipady=7,
            pady=(0, 12)
        )

        self.resource_entry.insert(
            0,
            "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)"
        )

        self.resource_entry.bind(
            "<FocusIn>",
            self.clear_placeholder
        )

        self.resource_entry.bind(
            "<FocusOut>",
            self.restore_placeholder
        )

        # ==========================================
        # DROPDOWN CONTAINER
        # ==========================================

        dropdown_container = tk.Frame(
            inner_frame,
            bg="white"
        )

        dropdown_container.pack(
            fill="x",
            pady=(0, 10)
        )

        # ==========================================
        # LABELS FRAME
        # ==========================================

        labels_frame = tk.Frame(
            dropdown_container,
            bg="white"
        )

        labels_frame.pack(
            side="left"
        )

        category_label = tk.Label(
            labels_frame,
            text="Category (Optional):",
            bg="white",
            fg="#333333",
            font=("Poppins", 10)
        )

        category_label.pack(
            anchor="w",
            pady=(0, 12)
        )

        location_label = tk.Label(
            labels_frame,
            text="Your Location (Optional):",
            bg="white",
            fg="#333333",
            font=("Poppins", 10)
        )

        location_label.pack(anchor="w")

        # ==========================================
        # DROPDOWNS FRAME
        # ==========================================

        dropdowns_frame = tk.Frame(
            dropdown_container,
            bg="white"
        )

        dropdowns_frame.pack(
            side="right"
        )

        self.category_var = tk.StringVar(
            value="Select Category"
        )

        self.category_dropdown = ttk.Combobox(
            dropdowns_frame,
            textvariable=self.category_var,
            values=[
                "Agriculture",
                "Mining",
                "Recycling",
                "Manufacturing",
                "Waste"
            ],
            font=("Poppins", 9),
            state="readonly",
            width=32
        )

        self.category_dropdown.pack(
            pady=(0, 8),
            ipady=2
        )

        self.location_var = tk.StringVar(
            value="Select Location"
        )

        self.location_dropdown = ttk.Combobox(
            dropdowns_frame,
            textvariable=self.location_var,
            values=[
                "Lagos",
                "Abuja",
                "Port Harcourt",
                "Kano",
                "Aba",
                "Enugu",
                "Ibadan"
            ],
            font=("Poppins", 9),
            state="readonly",
            width=32
        )

        self.location_dropdown.pack(
            ipady=2
        )

        # ==========================================
        # ANALYZE BUTTON
        # ==========================================

        analyze_btn = tk.Button(
            inner_frame,
            text="🔍   ANALYZE RESOURCES",
            bg="#7A0C0C",
            fg="white",
            activebackground="#5A1207",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Poppins", 11, "bold"),
            command=self.submit
        )

        analyze_btn.pack(
            fill="x",
            pady=(22, 8),
            ipady=11
        )

        # ==========================================
        # BOTTOM NAVIGATION
        # ==========================================

        nav_frame = tk.Frame(
            self.frame,
            bg="white",
            height=58
        )

        nav_frame.pack(
            fill="x",
            side="bottom"
        )

        nav_frame.pack_propagate(False)

        nav_inner = tk.Frame(
            nav_frame,
            bg="white"
        )

        nav_inner.pack(expand=True)

        nav_items = [
            ("⌂\nHome", "home"),
            ("📷\nInput", "input"),
            ("📄\nResults", "results"),
            ("📊\nDashboard", "dashboard")
        ]

        for text, screen in nav_items:

            btn = tk.Button(
                nav_inner,
                text=text,
                font=("Poppins", 8),
                bg="white",
                fg="#444444",
                bd=0,
                cursor="hand2",
                justify="center",
                activebackground="white",
                command=lambda s=screen:
                self.controller.show_screen(s)
            )

            btn.pack(
                side="left",
                padx=45,
                pady=5
            )

    # ==========================================
    # PLACEHOLDER METHODS
    # ==========================================

    def clear_placeholder(self, event):

        if self.resource_entry.get() == \
                "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)":

            self.resource_entry.delete(0, tk.END)

            self.resource_entry.config(
                fg="black"
            )

    def restore_placeholder(self, event):

        if self.resource_entry.get().strip() == "":

            self.resource_entry.insert(
                0,
                "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)"
            )

            self.resource_entry.config(
                fg="#888888"
            )

    # ==========================================
    # SUBMIT
    # ==========================================

    def submit(self):

        resource = self.resource_entry.get().strip()

        if resource == "" or resource == \
                "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)":

            messagebox.showwarning(
                "Input Error",
                "Please enter a resource name"
            )

            return

        category = self.category_var.get()
        location = self.location_var.get()

        if category == "Select Category":
            category = "General"

        if location == "Select Location":
            location = "Lagos"

        self.controller.set_resource_input(
            resource,
            category,
            location
        )

        self.controller.show_screen("results")

    # ==========================================
    # SHOW SCREEN
    # ==========================================

    def show(self):
        self.frame.pack(fill="both", expand=True)

    # ==========================================
    # HIDE SCREEN
    # ==========================================

    def hide(self):
        self.frame.pack_forget()