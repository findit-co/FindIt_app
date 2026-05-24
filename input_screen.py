
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

   # Image Identufucation method

    def identify_resource_enhanced(self, image_path):
        """
        Analyze image using color, texture, and shape detection
        Returns: (resource_name, confidence, details)
        """
        
        img = cv2.imread(image_path)
        if img is None:
            return "Unknown", 0, {}
        
        # Extract all features
        features = self._extract_features(img)
        
        # Score each resource
        scores = self._calculate_resource_scores(features)
        
        # Get best match
        best_match = max(scores.items(), key=lambda x: x[1])
        resource, score = best_match
        
        # Get confidence percentage (30-95 range)
        confidence = min(95, max(30, int(score * 100)))
        
        # Get top 3 alternatives for display
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        alternatives = [f"{r}: {int(s*100)}%" for r, s in sorted_scores[1:3] if s > 0.2]
        
        return resource, confidence, alternatives
    
    def _extract_features(self, img):
        """Extract multiple features from image"""
        
        # Convert to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # 1. Average color
        avg_color = cv2.mean(img_rgb)[:3]
        r, g, b = avg_color
        
        # 2. Color dominance
        color_dominance = max(r, g, b)
        color_is_green = g > r and g > b and g > 100
        color_is_brown = r > 100 and r > g and g > b
        color_is_gray = (r > 80 and r < 180 and g > 80 and g < 180 and b > 80 and b < 180)
        color_is_white = r > 200 and g > 200 and b > 200
        color_is_orange = r > 150 and g > 80 and g < 150 and b < 80
        
        # 3. Texture analysis
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Variance (smooth vs rough)
        texture_variance = np.var(gray)
        is_smooth = texture_variance < 500
        is_rough = texture_variance > 1000
        
        # 4. Edge detection
        edges = cv2.Canny(gray, 50, 150)
        edge_density = np.sum(edges > 0) / edges.size
        has_many_edges = edge_density > 0.15
        has_few_edges = edge_density < 0.05
        
        # 5. Shape detection (circles/round objects)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50,
                                   param1=50, param2=30, minRadius=10, maxRadius=200)
        has_circles = circles is not None
        
        # 6. Detect organic shapes (leaf-like patterns)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        organic_texture = np.var(laplacian) > 200
        
        return {
            'color': (r, g, b),
            'color_is_green': color_is_green,
            'color_is_brown': color_is_brown,
            'color_is_gray': color_is_gray,
            'color_is_white': color_is_white,
            'color_is_orange': color_is_orange,
            'is_smooth': is_smooth,
            'is_rough': is_rough,
            'has_many_edges': has_many_edges,
            'has_few_edges': has_few_edges,
            'has_circles': has_circles,
            'organic_texture': organic_texture,
            'edge_density': edge_density
        }
    
    def _calculate_resource_scores(self, features):
        """Calculate match score for each resource"""
        scores = {
            'Cassava': 0,
            'Plastic': 0,
            'Sand': 0,
            'Palm Oil': 0,
            'Scrap Metal': 0,
            'Wood': 0
        }
        
        # ===== CASSAVA =====
        if features['color_is_brown']:
            scores['Cassava'] += 35
        if features['organic_texture']:
            scores['Cassava'] += 25
        if features['is_rough']:
            scores['Cassava'] += 20
        if not features['has_circles']:
            scores['Cassava'] += 10
        
        # ===== PLASTIC =====
        if features['color_is_white'] or (features['color'][0] > 150 and features['color'][1] > 150):
            scores['Plastic'] += 30
        if features['is_smooth']:
            scores['Plastic'] += 25
        if features['has_circles']:
            scores['Plastic'] += 25
        if features['has_few_edges']:
            scores['Plastic'] += 10
        
        # ===== SAND =====
        if features['color_is_gray'] or (features['color'][0] > 120 and features['color'][1] > 100 and features['color'][2] < 150):
            scores['Sand'] += 35
        if 0.08 < features['edge_density'] < 0.2:
            scores['Sand'] += 25
        if not features['has_circles']:
            scores['Sand'] += 15
        if not features['is_smooth']:
            scores['Sand'] += 15
        
        # ===== PALM OIL =====
        if features['color_is_orange'] or (features['color'][0] > 150 and features['color'][1] < 120 and features['color'][2] < 80):
            scores['Palm Oil'] += 45
        if features['is_smooth']:
            scores['Palm Oil'] += 20
        if features['organic_texture']:
            scores['Palm Oil'] += 15
        if not features['has_circles']:
            scores['Palm Oil'] += 10
        
        # ===== SCRAP METAL =====
        if features['color_is_gray']:
            scores['Scrap Metal'] += 30
        if features['has_many_edges']:
            scores['Scrap Metal'] += 30
        if features['is_smooth']:
            scores['Scrap Metal'] += 15
        if features['has_circles']:
            scores['Scrap Metal'] += 15
        
        # ===== WOOD =====
        if features['color_is_brown']:
            scores['Wood'] += 35
        if features['organic_texture']:
            scores['Wood'] += 25
        if features['is_rough']:
            scores['Wood'] += 20
        if features['has_many_edges']:
            scores['Wood'] += 10
        
        # Normalize scores to 0-1 range
        max_score = max(scores.values()) if max(scores.values()) > 0 else 1
        for resource in scores:
            scores[resource] = scores[resource] / max_score
        
        return scores

   # Build_ui house

    def build_ui(self):

        self.frame.pack(fill="both", expand=True)

      #Header frame

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

        header_label.pack(side="left", padx=15, pady=8)

       #Title frame

        title_label = tk.Label(
            self.frame,
            text="Identify a Resource",
            bg="#F6EEDC",
            fg="#2B0A05",
            font=("Poppins", 24, "bold")
        )

        title_label.pack(pady=(10, 2))

        subtitle_label = tk.Label(
            self.frame,
            text="Tell us what resource you have around you",
            bg="#F6EEDC",
            fg="#555555",
            font=("Poppins", 10)
        )

        subtitle_label.pack(pady=(0, 10))

        # Main white container Frame

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

        # Inner content frame

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

        # Input method title

        method_label = tk.Label(
            inner_frame,
            text="Choose Input Method",
            bg="white",
            fg="#333333",
            font=("Poppins", 11, "bold")
        )

        method_label.pack(anchor="w", pady=(0, 8))

        #Card container

        cards_frame = tk.Frame(
            inner_frame,
            bg="white"
        )

        cards_frame.pack(fill="x", pady=(0, 10))

        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        # The camera card section

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

        camera_icon.pack(pady=(12, 2))
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

       # Section for upload card

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

        upload_icon.pack(pady=(12, 2))
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

        #The preview label

        self.preview_label = tk.Label(
            inner_frame,
            text="",
            bg="white",
            fg="#666666",
            font=("Poppins", 9)
        )
        self.preview_label.pack(pady=(0, 5))

      #Divider

        divider = tk.Frame(
            inner_frame,
            bg="#DDDDDD",
            height=1
        )

        divider.pack(fill="x", pady=8)

       # Details label

        details_label = tk.Label(
            inner_frame,
            text="Or Enter Details (Optional)",
            bg="white",
            fg="#333333",
            font=("Poppins", 11, "bold")
        )

        details_label.pack(anchor="w", pady=(0, 8))

       #Resource Entry

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

        self.resource_entry.bind("<FocusIn>", self.clear_placeholder)
        self.resource_entry.bind("<FocusOut>", self.restore_placeholder)

       #The dropdown container

        dropdown_container = tk.Frame(
            inner_frame,
            bg="white"
        )

        dropdown_container.pack(fill="x", pady=(0, 10))

       #Labels frame

        labels_frame = tk.Frame(
            dropdown_container,
            bg="white"
        )

        labels_frame.pack(side="left")

        category_label = tk.Label(
            labels_frame,
            text="Category (Optional):",
            bg="white",
            fg="#333333",
            font=("Poppins", 10)
        )

        category_label.pack(anchor="w", pady=(0, 12))

        location_label = tk.Label(
            labels_frame,
            text="Your Location (Optional):",
            bg="white",
            fg="#333333",
            font=("Poppins", 10)
        )

        location_label.pack(anchor="w")

        #The second dropdown frame

        dropdowns_frame = tk.Frame(
            dropdown_container,
            bg="white"
        )

        dropdowns_frame.pack(side="right")

        self.category_var = tk.StringVar(value="Select Category")
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

        self.category_dropdown.pack(pady=(0, 8), ipady=2)

        self.location_var = tk.StringVar(value="Select Location")
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

        self.location_dropdown.pack(ipady=2)

        #Analyze button

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

      # Navigation bar

        nav_frame = tk.Frame(
            self.frame,
            bg="white",
            height=58
        )

        nav_frame.pack(fill="x", side="bottom")
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
                command=lambda s=screen: self.controller.show_screen(s)
            )
            btn.pack(side="left", padx=45, pady=5)

    # Integration camera fucntionality

    def open_camera(self, event=None):
        """Open webcam, capture image, and auto-identify"""
        
        camera_window = tk.Toplevel(self.frame)
        camera_window.title("Capture Image")
        camera_window.geometry("640x580")
        camera_window.configure(bg="#F6EEDC")
        
        video_label = tk.Label(camera_window, bg="black")
        video_label.pack(pady=10)
        
        status_label = tk.Label(camera_window, text="Position camera and click CAPTURE", 
                                bg="#F6EEDC", font=("Poppins", 10))
        status_label.pack(pady=5)
        
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
        
        self.webcam = cv2.VideoCapture(0)
        
        def update_frame():
            ret, frame = self.webcam.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_resized = cv2.resize(frame_rgb, (640, 480))
                img = ImageTk.PhotoImage(Image.fromarray(frame_resized))
                video_label.config(image=img)
                video_label.image = img
                self.current_frame = frame
            
            if self.webcam and self.webcam.isOpened():
                camera_window.after(30, update_frame)
        
        def capture_image():
            if hasattr(self, 'current_frame'):
                status_label.config(text="Analyzing image...", fg="orange")
                camera_window.update()
                
                cv2.imwrite("captured_image.jpg", self.current_frame)
                self.captured_image = "captured_image.jpg"
                
                # AUTO-IDENTIFY THE RESOURCE
                resource_name, confidence, alternatives = self.identify_resource_enhanced("captured_image.jpg")
                
                camera_window.destroy()
                
                self.resource_entry.delete(0, tk.END)
                self.resource_entry.insert(0, resource_name)
                self.resource_entry.config(fg="black")
                
                if alternatives:
                    self.preview_label.config(
                        text=f"✓ Identified: {resource_name} (confidence: {confidence}%) | Also could be: {', '.join(alternatives)}", 
                        fg="green"
                    )
                else:
                    self.preview_label.config(
                        text=f"✓ Identified: {resource_name} (confidence: {confidence}%)", 
                        fg="green"
                    )
        
        capture_btn.config(command=capture_image)
        update_frame()
        
        def on_close():
            if self.webcam and self.webcam.isOpened():
                self.webcam.release()
            camera_window.destroy()
        
        camera_window.protocol("WM_DELETE_WINDOW", on_close)

    # Integrating image uplad functionality

    def upload_image(self, event=None):
        """Upload image and auto-identify"""
        
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.captured_image = file_path
            
            self.preview_label.config(text="Analyzing image...", fg="orange")
            self.frame.update()
            
            # AUTO-IDENTIFY THE RESOURCE
            resource_name, confidence, alternatives = self.identify_resource_enhanced(file_path)
            
            self.resource_entry.delete(0, tk.END)
            self.resource_entry.insert(0, resource_name)
            self.resource_entry.config(fg="black")
            
            if alternatives:
                self.preview_label.config(
                    text=f"✓ Identified: {resource_name} (confidence: {confidence}%) | Also could be: {', '.join(alternatives)}", 
                    fg="green"
                )
            else:
                self.preview_label.config(
                    text=f"✓ Identified: {resource_name} (confidence: {confidence}%)", 
                    fg="green"
                )

  #Placeholder methods

    def clear_placeholder(self, event):
        if self.resource_entry.get() == "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)":
            self.resource_entry.delete(0, tk.END)
            self.resource_entry.config(fg="black")

    def restore_placeholder(self, event):
        if self.resource_entry.get().strip() == "":
            self.resource_entry.insert(0, "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)")
            self.resource_entry.config(fg="#888888")

   # Submit method

    def submit(self):
        resource = self.resource_entry.get().strip()

        if resource == "" or resource == "Enter Resource (e.g Cassava, Sand, Plastic Bottles, Palm Oil)":
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

        self.controller.set_resource_input(resource, category, location)
        self.controller.show_screen("results")

 # Show method

    def show(self):
        self.frame.pack(fill="both", expand=True)

    # Hide method

    def hide(self):
        self.frame.pack_forget()