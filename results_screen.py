
import tkinter as tk
from tkinter import messagebox
import csv
import os


class ResultsScreen:

    def __init__(self, parent, controller):

        self.parent = parent
        self.controller = controller
        self.current_results = None

        self.frame = tk.Frame(
            parent,
            bg="#F6EEDC"
        )

        self.build_ui()

   # Build_Ui method

    def build_ui(self):

        self.frame.pack(fill="both", expand=True)

        # Header method

        header_frame = tk.Frame(
            self.frame,
            bg="white",
            height=38
        )

        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        header_label = tk.Label(
            header_frame,
            text="FIND IT",
            bg="white",
            fg="#2B0A05",
            font=("Poppins", 13, "bold")
        )

        header_label.pack(side="left", padx=18)

     #Main card method

        self.main_card = tk.Frame(
            self.frame,
            bg="#F8F1DD",
            bd=1,
            relief="solid"
        )

        self.main_card.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=10
        )

      # Top section

        top_frame = tk.Frame(
            self.main_card,
            bg="#F8F1DD"
        )

        top_frame.pack(
            fill="x",
            padx=18,
            pady=(15, 10)
        )

         # Resource image

        image_frame = tk.Frame(
            top_frame,
            bg="#EADBC8",
            width=95,
            height=95,
            bd=1,
            relief="solid"
        )

        image_frame.pack(
            side="left",
            padx=(0, 15)
        )

        image_frame.pack_propagate(False)

        self.resource_image = tk.Label(
            image_frame,
            text="🌱",
            bg="#EADBC8",
            font=("Arial", 38)
        )

        self.resource_image.pack(expand=True)
        #Resource details

        details_frame = tk.Frame(
            top_frame,
            bg="#F8F1DD"
        )

        details_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        resource_text = tk.Label(
            details_frame,
            text="Resource Identified",
            bg="#F8F1DD",
            fg="#444444",
            font=("Poppins", 10)
        )

        resource_text.pack(anchor="w")

        self.resource_label = tk.Label(
            details_frame,
            text="--",
            bg="#F8F1DD",
            fg="#2B0A05",
            font=("Poppins", 22, "bold")
        )

        self.resource_label.pack(anchor="w")

        # Income card

        income_card = tk.Frame(
            top_frame,
            bg="#F7E9BE",
            width=200,
            height=95,
            bd=1,
            relief="solid"
        )

        income_card.pack(side="right")

        income_card.pack_propagate(False)

        income_title = tk.Label(
            income_card,
            text="Income Potential",
            bg="#F7E9BE",
            fg="#5A1207",
            font=("Poppins", 10, "bold")
        )

        income_title.pack(pady=(16, 5))

        self.income_label = tk.Label(
            income_card,
            text="--",
            bg="#F7E9BE",
            fg="#5A1207",
            font=("Poppins", 12, "bold")
        )

        self.income_label.pack()

        income_subtitle = tk.Label(
            income_card,
            text="Monthly Estimate",
            bg="#F7E9BE",
            fg="#555555",
            font=("Poppins", 8)
        )

        income_subtitle.pack(pady=(3, 0))

       

        grid_frame = tk.Frame(
            self.main_card,
            bg="#F8F1DD"
        )

        grid_frame.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=5
        )

        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)

        # INDUSTRIAL USES CARD
        uses_card = tk.Frame(
            grid_frame,
            bg="#F8F1DD",
            bd=1,
            relief="solid"
        )

        uses_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8),
            pady=(0, 10)
        )

        uses_title = tk.Label(
            uses_card,
            text="🏭  Industrial Uses",
            bg="#F8F1DD",
            fg="#5A1207",
            font=("Poppins", 11, "bold")
        )

        uses_title.pack(anchor="w", padx=14, pady=(12, 8))

        self.uses_label = tk.Label(
            uses_card,
            text="--",
            justify="left",
            anchor="w",
            bg="#F8F1DD",
            fg="#333333",
            font=("Poppins", 9)
        )

        self.uses_label.pack(
            anchor="w",
            padx=18,
            pady=(0, 14)
        )

        # CREATIVE USES CARD
        creative_card = tk.Frame(
            grid_frame,
            bg="#F8F1DD",
            bd=1,
            relief="solid"
        )

        creative_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8, 0),
            pady=(0, 10)
        )

        creative_title = tk.Label(
            creative_card,
            text="💡  Creative / Local Uses",
            bg="#F8F1DD",
            fg="#5A1207",
            font=("Poppins", 11, "bold")
        )

        creative_title.pack(anchor="w", padx=14, pady=(12, 8))

        self.creative_label = tk.Label(
            creative_card,
            text="--",
            justify="left",
            anchor="w",
            bg="#F8F1DD",
            fg="#333333",
            font=("Poppins", 9)
        )

        self.creative_label.pack(
            anchor="w",
            padx=18,
            pady=(0, 14)
        )

        # BUSINESS IDEAS CARD
        business_card = tk.Frame(
            grid_frame,
            bg="#F8F1DD",
            bd=1,
            relief="solid"
        )

        business_card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 8)
        )

        business_title = tk.Label(
            business_card,
            text="💼  Business Ideas",
            bg="#F8F1DD",
            fg="#5A1207",
            font=("Poppins", 11, "bold")
        )

        business_title.pack(anchor="w", padx=14, pady=(12, 8))

        self.business_label = tk.Label(
            business_card,
            text="--",
            justify="left",
            anchor="w",
            bg="#F8F1DD",
            fg="#333333",
            font=("Poppins", 9)
        )

        self.business_label.pack(
            anchor="w",
            padx=18,
            pady=(0, 14)
        )

        # LOCAL RELEVANCE CARD
        local_card = tk.Frame(
            grid_frame,
            bg="#F8F1DD",
            bd=1,
            relief="solid"
        )

        local_card.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(8, 0)
        )

        local_title = tk.Label(
            local_card,
            text="📍  Local Relevance",
            bg="#F8F1DD",
            fg="#5A1207",
            font=("Poppins", 11, "bold")
        )

        local_title.pack(anchor="w", padx=14, pady=(12, 8))

        self.local_label = tk.Label(
            local_card,
            text="--",
            justify="left",
            anchor="w",
            bg="#F8F1DD",
            fg="#333333",
            font=("Poppins", 9)
        )

        self.local_label.pack(
            anchor="w",
            padx=18,
            pady=(0, 14)
        )

        # BUTTON SECTION
        button_frame = tk.Frame(
            self.main_card,
            bg="#F8F1DD"
        )

        button_frame.pack(
            fill="x",
            padx=18,
            pady=(12, 16)
        )

        new_btn = tk.Button(
            button_frame,
            text="⟳  NEW SEARCH",
            bg="white",
            fg="#333333",
            relief="solid",
            bd=1,
            font=("Poppins", 10, "bold"),
            cursor="hand2",
            command=lambda: self.controller.show_screen("input")
        )

        new_btn.pack(
            side="left",
            ipadx=18,
            ipady=8
        )

        save_btn = tk.Button(
            button_frame,
            text="💾  SAVE TO HISTORY",
            bg="#6B0F0F",
            fg="white",
            relief="flat",
            font=("Poppins", 10, "bold"),
            cursor="hand2",
            command=self.save_search
        )

        save_btn.pack(
            side="right",
            ipadx=18,
            ipady=8
        )

        # FOOTER NAVIGATION
        nav_frame = tk.Frame(
            self.frame,
            bg="white",
            height=52
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
            ("📝\nInput", "input"),
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
            btn.pack(side="left", padx=28, pady=4)

   # The show method

    def show(self):
        self.frame.pack(fill="both", expand=True)
        self.refresh()

    #The hide method
    def hide(self):
        self.frame.pack_forget()

   # Refresh result

    def refresh(self):
        if self.controller.current_resource and self.controller.resource_engine:
            resource = self.controller.current_resource.get("name", "Unknown")
            location = self.controller.current_resource.get("location", "Lagos")

            result = self.controller.resource_engine.find_resource(resource, location)

            # STORE THE RESULTS FOR SAVING - THIS WAS THE PROBLEM
            self.current_results = result

            if result and "error" not in result:
                self.resource_label.config(text=result.get("resource", resource).title())
                self.income_label.config(text=result.get("income_estimate", "₦0 - ₦0"))

                uses = result.get("uses", [])
                if isinstance(uses, list):
                    uses_text = "\n\n".join([f"• {u}" for u in uses])
                else:
                    uses_text = f"• {uses}"
                self.uses_label.config(text=uses_text)

                business = result.get("business_ideas", [])
                if isinstance(business, list):
                    business_text = "\n\n".join([f"• {b}" for b in business])
                else:
                    business_text = f"• {business}"
                self.business_label.config(text=business_text)

                self.local_label.config(text=result.get("location_specific", "Information not available"))

                if isinstance(uses, list) and len(uses) >= 2:
                    creative_text = "\n\n".join([f"• {uses[0]}", f"• {uses[1]}"])
                else:
                    creative_text = "• Information available in Industrial Uses"
                self.creative_label.config(text=creative_text)

            else:
                self.resource_label.config(text=resource.title())
                self.income_label.config(text="Data not available")
                self.uses_label.config(text="• Information not found\n• Try another resource")
                self.creative_label.config(text="• No creative uses found")
                self.business_label.config(text="• No business ideas available")
                self.local_label.config(text="No local relevance data available")
        else:
            self.resource_label.config(text="No Resource Selected")
            self.income_label.config(text="--")
            self.uses_label.config(text="• Please search for a resource first")
            self.creative_label.config(text="• Go to Input Screen")
            self.business_label.config(text="• Enter a resource name")
            self.local_label.config(text="Then click ANALYZE RESOURCES")
            self.current_results = None

    #save search feature

    def save_search(self):
        print(f"DEBUG: current_results = {self.current_results}")
        print(f"DEBUG: current_resource = {self.controller.current_resource}")
        
        if self.controller.current_resource and self.current_results:
            success = self.controller.save_search_history()
            if success:
                messagebox.showinfo("Success", "Search saved to history! ✅")
            else:
                # Manual save as fallback
                try:
                    file_exists = os.path.isfile("search_history.csv")
                    with open("search_history.csv", "a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        if not file_exists:
                            writer.writerow(["timestamp", "resource", "location", "business_idea", "income"])
                        
                        # Extract business idea
                        business = self.current_results.get("business_ideas", "")
                        if isinstance(business, list):
                            business = business[0] if business else ""
                        
                        writer.writerow([
                            self.controller.current_resource.get("timestamp", ""),
                            self.controller.current_resource.get("name", ""),
                            self.controller.current_resource.get("location", ""),
                            business,
                            self.current_results.get("income_estimate", "")
                        ])
                    messagebox.showinfo("Success", "Search saved to history! ✅")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not save: {e}")
        else:
            messagebox.showwarning(
                "Nothing to Save", 
                f"No search results to save.\n\nCurrent Results: {self.current_results is not None}\nCurrent Resource: {self.controller.current_resource is not None}"
            )