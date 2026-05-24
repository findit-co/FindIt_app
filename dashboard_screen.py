import tkinter as tk
from tkinter import ttk
import csv


class DashboardScreen:

    def __init__(self, parent, controller):

        self.parent = parent
        self.controller = controller
        self.all_history = []  # Store all history for searching

        self.frame = tk.Frame(
            parent,
            bg="#F6EEDC"
        )

        self.build_ui()

    # The build_Ui method

    def build_ui(self):

        self.frame.pack(fill="both", expand=True)

      # Header frame

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

        #Main card

        main_card = tk.Frame(
            self.frame,
            bg="#F8F1DD",
            bd=1,
            relief="solid"
        )

        main_card.pack(
            fill="both",
            expand=True,
            padx=14,
            pady=10
        )

       # This section is for the top frame

        top_frame = tk.Frame(
            main_card,
            bg="#F8F1DD"
        )

        top_frame.pack(
            fill="x",
            padx=16,
            pady=(14, 8)
        )

        # LEFT SIDE
        left_top = tk.Frame(
            top_frame,
            bg="#F8F1DD"
        )

        left_top.pack(side="left")

        title = tk.Label(
            left_top,
            text="Search History",
            bg="#F8F1DD",
            fg="#2B0A05",
            font=("Poppins", 18, "bold")
        )

        title.pack(anchor="w")

        subtitle = tk.Label(
            left_top,
            text="View your previous resource searches.",
            bg="#F8F1DD",
            fg="#555555",
            font=("Poppins", 9)
        )

        subtitle.pack(anchor="w")

        # RIGHT SEARCH BAR
        search_frame = tk.Frame(
            top_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        search_frame.pack(
            side="right",
            ipadx=6,
            ipady=2
        )

        search_icon = tk.Label(
            search_frame,
            text="🔍",
            bg="white",
            fg="#666666",
            font=("Arial", 10)
        )

        search_icon.pack(side="right", padx=(5, 6))

        self.search_entry = tk.Entry(
            search_frame,
            bd=0,
            relief="flat",
            font=("Poppins", 9),
            width=24
        )

        self.search_entry.pack(
            side="left",
            padx=(8, 2),
            pady=4
        )

        self.search_entry.insert(0, "Search history...")

        # Bind search events
        self.search_entry.bind("<FocusIn>", self._clear_search_placeholder)
        self.search_entry.bind("<FocusOut>", self._restore_search_placeholder)
        self.search_entry.bind("<KeyRelease>", self._search_history)

        #The section for history table

        table_frame = tk.Frame(
            main_card,
            bg="#F8F1DD"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=16,
            pady=(0, 12)
        )

        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        columns = (
            "#",
            "Resource",
            "Category",
            "Location",
            "Date & Time",
            "Action"
        )

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview",
            background="white",
            foreground="#333333",
            rowheight=32,
            fieldbackground="white",
            borderwidth=0,
            font=("Poppins", 9)
        )

        style.configure(
            "Treeview.Heading",
            background="#6B0F0F",
            foreground="white",
            relief="flat",
            font=("Poppins", 9, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#EADBC8")]
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=6,
            yscrollcommand=scrollbar.set
        )

        scrollbar.config(command=self.tree.yview)

        # HEADINGS
        self.tree.heading("#", text="#")
        self.tree.heading("Resource", text="Resource")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Date & Time", text="Date & Time")
        self.tree.heading("Action", text="Action")

        # COLUMN WIDTHS
        self.tree.column("#", width=40, anchor="center")
        self.tree.column("Resource", width=150)
        self.tree.column("Category", width=130)
        self.tree.column("Location", width=130)
        self.tree.column("Date & Time", width=170)
        self.tree.column("Action", width=70, anchor="center")

        self.tree.pack(fill="both", expand=True, side="left")

        #This is the frame for statistics

        stats_frame = tk.Frame(
            main_card,
            bg="#F8F1DD"
        )

        stats_frame.pack(
            fill="x",
            padx=16,
            pady=(0, 12)
        )

        self.total_label = tk.Label(
            stats_frame,
            text="0",
            bg="#F6EEDC",
            fg="#2B0A05",
            font=("Poppins", 16, "bold")
        )

        self.total_label.pack(side="left", padx=20)

        total_text = tk.Label(
            stats_frame,
            text="Total Searches",
            bg="#F8F1DD",
            fg="#555555",
            font=("Poppins", 10)
        )

        total_text.pack(side="left")

        # Refresh button
        refresh_btn = tk.Button(
            stats_frame,
            text="🔄 REFRESH",
            bg="#6B0F0F",
            fg="white",
            relief="flat",
            font=("Poppins", 9, "bold"),
            cursor="hand2",
            padx=15,
            pady=5,
            command=self.load_history
        )

        refresh_btn.pack(side="right")

        # the section for footer navigation

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
            ("📷\nInput", "input"),
            ("📄\nResults", "results"),
            ("📊\nDashboard", "dashboard")
        ]

        for text, screen in nav_items:

            bg_color = "white"
            fg_color = "#444444"

            if screen == "dashboard":
                bg_color = "#6B0F0F"
                fg_color = "white"

            btn = tk.Button(
                nav_inner,
                text=text,
                font=("Poppins", 8),
                bg=bg_color,
                fg=fg_color,
                bd=0,
                cursor="hand2",
                justify="center",
                activebackground=bg_color,
                activeforeground=fg_color,
                command=lambda s=screen:
                self.controller.show_screen(s)
            )

            btn.pack(
                side="left",
                padx=18,
                pady=5,
                ipadx=10,
                ipady=2
            )

    # Search placeholder methods
    def _clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search history...":
            self.search_entry.delete(0, tk.END)

    def _restore_search_placeholder(self, event):
        if self.search_entry.get().strip() == "":
            self.search_entry.insert(0, "Search history...")

    def _search_history(self, event):
        """Filter history based on search query"""
        query = self.search_entry.get().strip().lower()
        
        if query == "" or query == "search history...":
            self._display_history(self.all_history)
        else:
            filtered = [
                item for item in self.all_history 
                if query in item["resource"].lower() 
                or query in item["location"].lower()
                or query in item["category"].lower()
            ]
            self._display_history(filtered)

    def _display_history(self, history_list):
        """Display history items in the table"""
        # Clear existing table
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, item in enumerate(history_list, start=1):
            self.tree.insert(
                "",
                "end",
                values=(
                    i,
                    item["resource"],
                    item["category"],
                    item["location"],
                    item["date"],
                    "🗑"
                )
            )

# Show method to ensure smooth switching of screens

    def show(self):

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.load_history()

    #The hide method

    def hide(self):

        self.frame.pack_forget()

  # Load History

    def load_history(self):

        # CLEAR EXISTING TABLE
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.all_history = []

        categories = {
            "cassava": "Agricultural",
            "palm oil": "Agricultural",
            "sand": "Mineral",
            "plastic": "Waste/Recycling",
            "plastic bottle": "Waste/Recycling",
            "bambara nut": "Agricultural",
            "coconut": "Agricultural",
            "maize": "Agricultural",
            "timber": "Timber/Wood",
            "scrap metal": "Scrap/Metal",
            "charcoal": "Fuel/Energy",
            "groundnut": "Agricultural",
            "vegetables": "Agricultural",
            "carpet grass": "Agricultural/Landscaping"
        }

        count = 0

        try:
            with open("search_history.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header

                for i, row in enumerate(reader, start=1):
                    if len(row) >= 5:
                        resource = row[1].lower()
                        
                        # Find category
                        category = "General"
                        for key, cat in categories.items():
                            if key in resource:
                                category = cat
                                break
                        
                        history_item = {
                            "resource": row[1].title(),
                            "category": category,
                            "location": row[2],
                            "date": row[0]
                        }
                        
                        self.all_history.append(history_item)
                        
                        self.tree.insert(
                            "",
                            "end",
                            values=(
                                i,
                                history_item["resource"],
                                history_item["category"],
                                history_item["location"],
                                history_item["date"],
                                "🗑"
                            )
                        )
                        count += 1

            # Update total label
            self.total_label.config(text=str(count))

            if count == 0:
                self.tree.insert(
                    "",
                    "end",
                    values=(
                        "-",
                        "No search history",
                        "-",
                        "-",
                        "-",
                        "-"
                    )
                )

        except FileNotFoundError:
            self.tree.insert(
                "",
                "end",
                values=(
                    "-",
                    "No search history",
                    "-",
                    "-",
                    "-",
                    "-"
                )
            )
            self.total_label.config(text="0")