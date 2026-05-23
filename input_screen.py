"""
Input Screen - Resource entry
Developer: Kennedy (Input Systems Engineer)
With Camera, Upload, and Basic Image Recognition
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import cv2
from PIL import Image, ImageTk
import os
import numpy as np


class InputScreen:
    def __init__(self, parent, controller):

        self.parent = parent
        self.controller = controller
        self.captured_image = None
        self.webcam = None

        self.frame = tk.Frame(
            parent,
            bg="#F6EEDC"
        )

        self.build_ui()

    # ==========================================
    # IMAGE RECOGNITION FUNCTION
    # ==========================================

    def analyze_image(self, image_path):
        """
        Analyze image to identify possible resource
        Returns: (detected_resource, confidence)
        """
        
        # Read image
        img = cv2.imread(image_path)
        
        if img is None:
            return None, 0
        
        # Calculate average color
        avg_color = cv2.mean(img)[:3]
        r, g, b = avg_color
        
        # Color to resource mapping
        color_mapping = [
            # Brown/Yellow tones - Cassava, Yam, Garri
            (r > 100 and r < 200 and g > 80 and g < 180 and b > 30 and b < 100, "Cassava"),
            # Green tones - Leaves, Vegetables, Palm fronds
            (g > 100 and g < 200 and r < g and b < g, "Palm Oil / Vegetables"),
            # Gray/Brown - Sand, Stones, Construction materials
            (r > 80 and r < 180 and g > 80 and g < 180 and b > 80 and b < 180, "Sand / Construction"),
            # Dark/Black - Charcoal, Coal, Black soil
            (r < 80 and g < 80 and b < 80, "Charcoal / Coal"),
            # White/Cream - Garri, Flour, Salt
            (r > 180 and g > 180 and b > 180, "Garri / Flour / Salt"),
            # Orange/Brown - Palm Oil, Clay
            (r > 150 and r < 220 and g > 80 and g < 150 and b < 80, "Palm Oil"),
            # Yellow - Corn, Maize, Golden products
            (r > 180 and r < 230 and g > 150 and g < 210 and b < 100, "Maize / Corn"),
        ]
        
        for condition, resource in color_mapping:
            if condition:
                return resource, 75
        
        # If no color match, check for edges/shapes
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        edge_count = np.sum(edges > 0)
        
        if edge_count > 50000:
            return "Scrap Metal / Plastic", 60
        
        return "General Resource", 40

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
            fill="both",
            expand=True,
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
            fill="both",
            expand=True,
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

        self.camera_card = tk.Frame(
            cards_frame,
            bg="white",
            bd=1,
            relief="solid",
            height=120,
            cursor="hand2"
        )

        self.camera_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.camera_card.grid_propagate(False)
        self.camera_card.bind("<Button-1>", self.open_camera)

        camera_icon = tk.Label(
            self.camera_card,
            text="📷",
            bg="white",
            fg="#6B0F0F",
            font=("Segoe UI Emoji", 26)
        )

        camera_icon.pack(
            pady=(12, 2)
        )
        camera_icon.bind("<Button-1>", self.open_camera)

        camera_title = tk.Label(
            self.camera_card,
            text="Use Camera",
            bg="white",
            fg="#222222",
            font=("Poppins", 11, "bold")
        )

        camera_title.pack()
        camera_title.bind("<Button-1>", self.open_camera)

        camera_subtitle = tk.Label(
            self.camera_card,
            text="Capture image using\nyour webcam",
            bg="white",
            fg="#777777",
            justify="center",
            font=("Poppins", 8)
        )

        camera_subtitle.pack()
        camera_subtitle.bind("<Button-1>", self.open_camera)

        # ==========================================
        # UPLOAD CARD
        # ==========================================

        self.upload_card = tk.Frame(
            cards_frame,
            bg="white",
            bd=1,
            relief="solid",
            height=120,
            cursor="hand2"
        )

        self.upload_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        self.upload_card.grid_propagate(False)
        self.upload_card.bind("<Button-1>", self.upload_image)

        upload_icon = tk.Label(
            self.upload_card,
            text="↑",
            bg="white",
            fg="#6B0F0F",
            font=("Poppins", 28)
        )

        upload_icon.pack(
            pady=(12, 2)
        )
        upload_icon.bind("<Button-1>", self.upload_image)

        upload_title = tk.Label(
            self.upload_card,
            text="Upload Image",
            bg="white",
            fg="#222222",
            font=("Poppins", 11, "bold")
        )

        upload_title.pack()
        upload_title.bind("<Button-1>", self.upload_image)

        upload_subtitle = tk.Label(
            self.upload_card,
            text="Choose image from\nyour device",
            bg="white",
            fg="#777777",
            justify="center",
            font=("Poppins", 8)
        )

        upload_subtitle.pack()
        upload_subtitle.bind("<Button-1>", self.upload_image)

        # ==========================================
        # PREVIEW LABEL
        # ==========================================

        self.preview_label = tk.Label(
            inner_frame,
            text="",
            bg="white",
            fg="#666666",
            font=("Poppins", 9)
        )
        self.preview_label.pack(pady=(0, 5))

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
    # CAMERA FUNCTIONALITY WITH RECOGNITION
    # ==========================================

    def open_camera(self, event=None):
        """Open webcam and capture image"""
        
        # Create camera window
        camera_window = tk.Toplevel(self.frame)
        camera_window.title("Capture Image")
        camera_window.geometry("640x580")
        camera_window.configure(bg="#F6EEDC")
        
        # Video label
        video_label = tk.Label(camera_window, bg="black")
        video_label.pack(pady=10)
        
        # Button frame
        btn_frame = tk.Frame(camera_window, bg="#F6EEDC")
        btn_frame.pack(pady=10)
        
        capture_btn = tk.Button(
            btn_frame,
            text="📸 CAPTURE",
            bg="#7A0C0C",
            fg="white",
            font=("Poppins", 12, "bold"),
            padx=20,
            pady=5,
            cursor="hand2"
        )
        capture_btn.pack(side="left", padx=10)
        
        cancel_btn = tk.Button(
            btn_frame,
            text="CANCEL",
            bg="#999999",
            fg="white",
            font=("Poppins", 12, "bold"),
            padx=20,
            pady=5,
            cursor="hand2",
            command=camera_window.destroy
        )
        cancel_btn.pack(side="left", padx=10)
        
        # Start webcam
        self.webcam = cv2.VideoCapture(0)
        
        def update_frame():
            ret, frame = self.webcam.read()
            if ret:
                # Convert to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize
                frame_resized = cv2.resize(frame_rgb, (640, 480))
                # Convert to PhotoImage
                img = ImageTk.PhotoImage(Image.fromarray(frame_resized))
                video_label.config(image=img)
                video_label.image = img
                # Store current frame for capture
                self.current_frame = frame
            
            if self.webcam and self.webcam.isOpened():
                camera_window.after(30, update_frame)
        
        def capture_image():
            if hasattr(self, 'current_frame'):
                # Save captured image
                cv2.imwrite("captured_image.jpg", self.current_frame)
                self.captured_image = "captured_image.jpg"
                camera_window.destroy()
                
                # Analyze the image
                detected, confidence = self.analyze_image("captured_image.jpg")
                
                # Show analysis result
                message = f"Analysis complete!\n\nDetected: {detected}\nConfidence: {confidence}%\n\nThe resource name has been auto-filled. You can edit it if needed."
                
                result = messagebox.askquestion("Image Analysis", message + "\n\nUse this resource?")
                
                if result == 'yes':
                    self.resource_entry.delete(0, tk.END)
                    self.resource_entry.insert(0, detected)
                    self.resource_entry.config(fg="black")
                
                self.preview_label.config(text=f"✓ Image captured: {detected} ({confidence}% confidence)", fg="green")
        
        capture_btn.config(command=capture_image)
        
        # Start video feed
        update_frame()
        
        # Clean up when closed
        def on_close():
            if self.webcam and self.webcam.isOpened():
                self.webcam.release()
            camera_window.destroy()
        
        camera_window.protocol("WM_DELETE_WINDOW", on_close)

    # ==========================================
    # UPLOAD FUNCTIONALITY WITH RECOGNITION
    # ==========================================

    def upload_image(self, event=None):
        """Upload image from device and recognize it"""
        
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.captured_image = file_path
            
            # Analyze the image
            detected, confidence = self.analyze_image(file_path)
            
            # Extract filename for resource entry
            filename = os.path.basename(file_path).split('.')[0]
            
            # Show analysis result
            message = f"Image loaded: {filename}\n\nAnalysis result:\nDetected: {detected}\nConfidence: {confidence}%"
            
            result = messagebox.askquestion("Image Analysis", message + "\n\nUse this resource?")
            
            if result == 'yes':
                self.resource_entry.delete(0, tk.END)
                self.resource_entry.insert(0, detected)
                self.resource_entry.config(fg="black")
            else:
                self.resource_entry.delete(0, tk.END)
                self.resource_entry.insert(0, filename.replace('_', ' ').title())
                self.resource_entry.config(fg="black")
            
            self.preview_label.config(text=f"✓ Image loaded: {detected} ({confidence}% confidence)", fg="green")

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
                "Please enter a resource name or use Camera/Upload"
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