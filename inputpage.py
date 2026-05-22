import tkinter as tk
from tkinter import messagebox as msgbox

class InputScreen(BaseScreen):

    def build_ui(self):
        self.create_header()
        self.title_section()
        self.main_section()
        self.footer_navigation()

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

    def main_section(self):
        
       def main_section(self):

    # This is the main section frame
    self.main_section_frame = tk.Frame(
        self,
        bg= "#FDF5E0",
        bd = 1,
        relief = "solid"
    )

    # Positioning the frame
    self.main_section_frame.pack(
        fill="both",
        padx=40,
        pady=20
    )

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
            bg = ""#FDF5E0"",
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
            bg = #FDF5E0",
            fg = "black",
            font = ("Poppins", 14, "bold")
        )

        self.camera_title.pack(pady = (35, 5))

        #Camera subtitle
        self.camera_subtitle = tk.Label(
            self.camera_card,
            text = "Capture image using \n your webcam",
            bg = "#FDF5E0",
            fd = "black",
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
        

        print("Or Enter Details(Optional)")
        self.text_resource()
        self.dropdown_section()
        self.analyze_button()

    def camera_box(self):
        print("Use Camera")
        print("Capture image using your webcam")

    def upload_image(self):
        print("Upload Image")
        print("Choose image from your main device")

    def text_resource(self):
        print("Enter Resource (e.g. Cassava, Sand, Plastic Bottles, Palm Oil)")

    def footer_navigation(self):
        self.home_nav()
        self.input_nav()
        self.results_nav()
        self.dashboard_nav()

    

