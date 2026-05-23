import tkinter as tk
from tkinter import messagebox as msgbox

class InputScreen(BaseScreen):

    def build_ui(self):
        self.create_header()
        self.title_section()
        self.main_section()
        self.footer_navigation()
    
    #--------------------------------
    #HEADER SECTION

    def create_header(self):

        #This is the header frame
        self.header_frame = tk.Frame(
        self,
        bg = "white",
        height = 50
    )

    #Positioning the frame
    self.header_frame.pack(fill="x")

    #Find It title label
    self.header_label = tk.Label(
        self.header_frame,
        text = "FIND IT",
        bg = "white",
        fg = "black",
        font = ("Poppins", 16, "bold")
    )

    #Positioning the label inside the frame
    self.header_label.pack(
        side = "left",
        padx = 15,
        pady = 10
    )

    #--------------------------------
    #TITLE SECTION

    def title_section(self):

        #This is the title frame
        self.title_frame = tk.Frame(
        self,
        bg = "#F2D9B0"
        ) 

    #Positioning the frame
    self.title_frame.pack(fill="x")

    #"Identify a Resource" Title
    self.title_label = tk.Label(
        self.title_frame,
        text = "Identify a Resource",
        bg = "#F2D9B0",
        fg = "#3B0D06",
        font = ("Poppins", 30, "bold")
    )

    #Positioning the title inside the frame
    self.title_label.pack(
        padx = 25,
        pady = 20
    )

    #The subtitle
    self.subtitle_label = tk.Label(
        self.title_frame,
        text = "Tell us what resource you have around you",
        bg = "#F2D9B0",
        fg = "black",
        font = ("Poppins", 17)
    )

    #Positioning the subtitle inside the frame
    self.subtitle_label.pack(
        padx = 25,
        pady = 20
    )

    #----------------------------------
    #MAIN SECTION

    def main_section(self):

        # This is the main section frame
        self.main_section_frame = tk.Frame(
            self,
            bg= "#FDF5E0",
            bd = 1,
            relief = "spy inputpage.pyolid"
        )

        # Positioning the frame
        self.main_section_frame.pack(
            fill="both",
            padx=40,
            pady=20
        )

        #---------------------------------
        #"Choose Input Method" Frame 
        self.main_title_frame = tk.Frame(
            self.main_section_frame,
            bg = "#FDF5E0"
        )

        #Positioning the frame
        self.main_title_frame.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        #"Choose Input Method" Title
        self.main_title_label = tk.Label(
            self.main_title_frame,
            text = "Choose Input Method",
            bg = "#FDF5E0",
            fg = "#3B0D06",
            font = ("Poppins", 17, "bold")
        )

        #Positioning the title inside the frame
        self.main_title_label.pack(
            side = "left",
            padx = 15,
            pady = 10
        )

        #---------------------------------------------------
        #Container holding Use Camera and Upload Image Cards
        self.cards_container = tk.Frame(
            self.main_section_frame,
            bg = "#FDF5E0"
        )

        #Positioning the container
        self.cards_container.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

       #CAMERA CARD FRAME

        self.camera_card = tk.Frame(
            self.cards_container,
            bg = "#FDF5E0",
            bd = 1,
            relief = "solid",
            width = 300,
            height = 140
       )

        #Positioning camera card to the left
        self.camera_card.pack(
            side = "left",
            padx = 15,
            pady = 10
        )

        #This prevents the frame from shrinking
        self.camera_card.pack_propagate(False)

        #Camera title
        self.camera_title = tk.Label(
            self.camera_card,
            text = "Use Camera",
            bg = "#FDF5E0",
            fg = "black",
            font = ("Poppins", 14, "bold")
        )

        self.camera_title.pack(pady = (35, 5))

        #Camera subtitle
        self.camera_subtitle = tk.Label(
            self.camera_card,
            text = "Capture image using \n your webcam",
            bg = "#FDF5E0",
            fg = "black",
            font = ("Poppins", 10)
        )

        self.camera_subtitle.pack()

        #UPLOAD CARD FRAME

        self.upload_card = tk.Frame(
            self.cards_container,
            bg = "FDF5E0",
            bd = 1,
            relief = "solid",
            width = 300,
            height = 140
        )

        #This positions the upload card beside camera card
        self.upload_card.pack(
            side = "left",
            padx = 15,
            pady = 10
        ) 

        #This prevents the frame from shrinking
        self.upload_card.pack_propagate(False)

        #Upload title
        self.upload_title = tk.Label(
            self.upload_card,
            text = "Upload Gallery",
            bg = "#FDF5E0",
            fg = "black",
            font = ("Poppins", 14, "bold")
        )

        self.upload_title.pack(pady=(35, 5))

        #Upload subtitle
        self.upload_subtitle = tk.Label(
            self.upload_card,
            text = "Choose image from \n your device",
            bg = "#FDF5E0",
            fg = "black",
            font = ("Poppins", 10)
        )

        self.upload_subtitle.pack()

        #-----------------------------------------------------------
        #The dividing line that separates image input and text input
        self.divider_line = tk.Frame(
            self.main_section_frame,
            bg = "black",
            height = 1
        )

        #Positioning the frame
        self.divider_line.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        #----------------------------------
        #"Or Enter Details..." Frame
        self.details_section_frame = tk.Frame(
            self.main_section_frame,
            bg = "#FDF5E0"
        )

        #Positioning the Frame
        self.details_section_frame.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        #"Or Enter Details..." Title
        self.details_section_label = tk.Label(
            self.details_section_frame,
            text = "Or Enter Details (Optional)",
            bg = "#FDF5E0",
            fg = "#3B0D06",
            font = ("Poppins", 17, "bold")
        )

         #Positioning the title inside the frame
        self.details_section_label.pack(
            side = "left"
        )

        #--------------------
        #Resource Entry Field
        self.resource_entry = tk.Entry(
            self.details_section_frame,
            bg="white",
            fg="black",
            font=("Poppins", 12),
            relief="solid",
            bd=1
        )

        #Placeholder text
        self.resource_entry.insert(
            0,
            "Enter Resource (e.g. Cassava, Sand, Plastic Bottles, Palm Oil)"
        )

        #Positioning the entry field
        self.resource_entry.pack(
            fill="x",
            padx=15,
            pady=10,
            ipady=8
        )

        #------------------------------
        #Category and Location Dropdown
        self.dropdown_section = tk.Frame(
            self.main_section_frame,
            bg = "#FDF5E0"
        )

        #Positioning the container
        self.dropdown_section.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        #CATEGORY ROW

        self.category_row = tk.Frame(
            self.dropdown_section,
            bg="#FDF5E0"
        )

        #Positioning it in the frame
        self.category_row.pack(
            fill="x",
            pady=5
        )

        # Category label
        self.category_label = tk.Label(
            self.category_row,
            text="Category (Optional)",
            bg="#FDF5E0",
            fg="black",
            font=("Poppins", 12)
        )

        self.category_label.pack(
            side="left"
        )

        # Category dropdown
        self.category_dropdown = tk.OptionMenu(
            self.category_row,
            tk.StringVar(),
            "Agriculture",
            "Mining",
            "Recycling",
            "Manufacturing",
            #Other Categories could be added later
        )

        self.category_dropdown.pack(
            side="right"
        )

        #LOCATION ROW

        self.location_row = tk.Frame(
            self.dropdown_section,
            bg="#FDF5E0"
        )

        self.location_row.pack(
            fill="x",
            pady=5
        )

        #Location label
        self.location_label = tk.Label(
            self.location_row,
            text="Your Location (Optional)",
            bg="#FDF5E0",
            fg="black",
            font=("Poppins", 12)
        )

        self.location_label.pack(
            side="left"
        )

        # Location dropdown
        self.location_dropdown = tk.OptionMenu(
            self.location_row,
            tk.StringVar(),
            "Lagos",
            "Abuja",
            "Port Harcourt",
            "Kano",
            #Other locations could be added later
        )

        self.location_dropdown.pack(
                side="right"
        )

        #--------------------
        #Analyze Resources Button

        self.analyze_button_frame = tk.Frame(
            self.main_section_frame,
            bg="#FDF5E0"
        )
        
        # Positioning the frame
        self.analyze_button_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        # Analyze button
        self.analyze_button = tk.Button(
            self.analyze_button_frame,
            text="ANALYZE RESOURCES",
            bg="#5A1207",
            fg="white",
            font=("Poppins", 14, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        # Positioning the button
        self.analyze_button.pack(
            fill="x",
            ipady=12
        )

    # -----------------------------------
    #FOOTER NAVIGATION SECTION

    self.footer_frame = tk.Frame(
        self,
        bg="white",
        height=80
    )

    #Positioning the footer
    self.footer_frame.pack(
        fill="x",
        side="bottom"
    )

    #Prevent footer from shrinking
    self.footer_frame.pack_propagate(False)

    #Home Navigation Item
    self.home_nav = tk.Frame(
        self.footer_frame,
        bg="white"
    )

    #Positioning it
    self.home_nav.pack(
        side="left",
        expand=True,
        pady=10
    )

    #Home icon placeholder
    self.home_icon = tk.Label(
        self.home_nav,
        text="🏠",
        bg="white",
        font=("Arial", 20)
    )

    #Positioning it
    self.home_icon.pack()

    #Home text
    self.home_text = tk.Label(
        self.home_nav,
        text="Home",
        bg="white",
        fg="black",
        font=("Poppins", 10)
    )

    #Positioning it
    self.home_text.pack()

    #Input Navigation Item
    self.input_nav = tk.Frame(
        self.footer_frame,
        bg="white"
    )

    #Positioning it
    self.input_nav.pack(
        side="left",
        expand=True,
        pady=10
    )

    #Input icon placeholder
    self.input_icon = tk.Label(
        self.input_nav,
        text="📷",
        bg="white",
        font=("Arial", 20)
    )

    #Positioning it
    self.input_icon.pack()

    #Input text
    self.input_text = tk.Label(
        self.input_nav,
        text="Input",
        bg="white",
        fg="black",
        font=("Poppins", 10)
    )

    #Positioning it
    self.input_text.pack()

    #Results Navigation Item

    self.results_nav = tk.Frame(
        self.footer_frame,
        bg="white"
    )

    #Positioning it
    self.results_nav.pack(
        side="left",
        expand=True,
        pady=10
    )

    #Results icon placeholder
    self.results_icon = tk.Label(
        self.results_nav,
        text="📄",
        bg="white",
        font=("Arial", 20)
    )

    #Positioning it
    self.results_icon.pack()

    #Results text
    self.results_text = tk.Label(
        self.results_nav,
        text="Results",
        bg="white",
        fg="black",
        font=("Poppins", 10)
    )

    #Positioning it
    self.results_text.pack()

    #Dashboard Navigation Item

    self.dashboard_nav = tk.Frame(
        self.footer_frame,
        bg="white"
    )

    self.dashboard_nav.pack(
        side="left",
        expand=True,
        pady=10
    )

    #Dashboard icon placeholder
    self.dashboard_icon = tk.Label(
        self.dashboard_nav,
        text="📊",
        bg="white",
        font=("Arial", 20)
    )

    #Positioning it
    self.dashboard_icon.pack()

    # Dashboard text
    self.dashboard_text = tk.Label(
        self.dashboard_nav,
        text="Dashboard",
        bg="white",
        fg="black",
        font=("Poppins", 10)
    )

    #Positioning it
    self.dashboard_text.pack()







    

