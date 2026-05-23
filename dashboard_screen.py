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

        self.frame = tk.Frame(
            parent,
            bg="#F6EEDC"
        )

        self.build_ui()

    # =====================================================
    # BUILD UI
    # =====================================================

    def build_ui(self):

        self.frame.pack(fill="both", expand=True)

        # =================================================
        # HEADER
        # =================================================

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

        # =================================================
        # MAIN CARD
        # =================================================

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

        # =================================================
        # TOP SECTION
        # =================================================

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
            text="⌕",
            bg="white",
            fg="#666666",
            font=("Arial", 12)
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

        # =================================================
        # TABLE SECTION
        # =================================================

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
            height=6
        )

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

        self.tree.pack(fill="both", expand=True)

        # =================================================
        # STATS SECTION
        # =================================================

        stats_frame = tk.Frame(
            main_card,
            bg="#F8F1DD"
        )

        stats_frame.pack(
            fill="x",
            padx=16,
            pady=(0, 12)
        )

        stats = [
            ("12", "Total Searches"),
            ("8", "Resources Identified"),
            ("4", "This Week"),
            ("5", "Categories")
        ]

        for number, text in stats:

            stat_card = tk.Frame(
                stats_frame,
                bg="#F6EEDC",
                bd=1,
                relief="solid",
                width=95,
                height=72
            )

            stat_card.pack(
                side="left",
                expand=True,
                padx=5
            )

            stat_card.pack_propagate(False)

            stat_number = tk.Label(
                stat_card,
                text=number,
                bg="#F6EEDC",
                fg="#2B0A05",
                font=("Poppins", 16, "bold")
            )

            stat_number.pack(pady=(10, 0))

            stat_text = tk.Label(
                stat_card,
                text=text,
                bg="#F6EEDC",
                fg="#555555",
                font=("Poppins", 8)
            )

            stat_text.pack()

        # =================================================
        # FOOTER NAVIGATION
        # =================================================

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

    # =====================================================
    # SHOW
    # =====================================================

    def show(self):

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.load_history()

    # =====================================================
    # HIDE
    # =====================================================

    def hide(self):

        self.frame.pack_forget()

    # =====================================================
    # LOAD HISTORY
    # =====================================================

    def load_history(self):

        # CLEAR EXISTING TABLE
        for item in self.tree.get_children():

            self.tree.delete(item)

        categories = {
            "cassava": "Agricultural",
            "palm oil": "Agricultural",
            "sand": "Mineral",
            "plastic bottles": "Waste",
            "bambara nut": "Agricultural"
        }

        count = 0

        try:

            with open(
                "search_history.csv",
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.reader(file)

                next(reader)

                for i, row in enumerate(reader, start=1):

                    if len(row) >= 5:

                        resource = row[1].lower()

                        category = categories.get(
                            resource,
                            "General"
                        )

                        self.tree.insert(
                            "",
                            "end",
                            values=(
                                i,
                                row[1].title(),
                                category,
                                row[2],
                                row[0],
                                "🗑"
                            )
                        )

                        count += 1

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