import tkinter as tk
from tkinter import ttk,messagebox
import csv
from datetime import datetime

class BaseScreen:
    """
    Base class for all screens - enables polymorphism.
    All screen classes(Home, Input, Results, dashboard) inherit from this. """

    def __init__(self, parent, controller):
        """Initialize base screen.
        args:
            parent:The main window(tk.Tk object)
            controller:Reference to FinfItApp for navigathion"""
        self.parent= parent
        self.controller = controller
        self.frame = tk.Frame(Parent)
        self.build_ui()


class FindItApp:
    """Main application controller. Manages all screens, navigation, and dataflow."""
    def __init__(self, root):
        """ Initialize the application.
        Args:
          root: The main tkinter window"""
        self.root = root
        self.root.title("FIND IT- Resource Intelligence App")
        self.root.geometry("1250x800")
        self.root.configure(bg="#f0f0f0")

    #shared data between screens
        self.current_resource = None # stores input from InputScreen
        self.search_results = None # Stores results from ResourceEngine
        # Initialize components(teammates will create these)
        self.resource_engine = None #Dilibe will create ResourceEngine
        self.data_manager = None  # Kene will create DataManager
        #Initialize all screens
        self.screens = {}
        self._create_screens()

        # show home screen first
        self.show_screen("home")

    def _create_screens(self):
        """Create all screen objects and store in dictionary."""
        self.screens["home"] = HomeScreen(self.root,self)
        self.screens["input"] = InputScreen(self.root,self)
        self.screens["results"] = ResultsScreen(self.root,self)
        self.screens["dashboard"] = DashboardScreen(self.root,self)


    def show_screen(self, screen_name):
        """ navigate to a specific screen.
             Args:
                 screen_name: Name of screen ("home", "input", "results", "dashboard")"""

        # Hide all screens first
        for screen in self.screens.values():
            screen.hide()

        # Show requested screen
        if screen_name in self.screens:
            self.screens[screen_name].show()
                


      
    def build_ui(self):
        """Override this in child classes.
        each screen implements their own UI here."""
        raise
    NotImplementedError("subclass must implement build_ui()")
    

    def show(self):
        """Show this screen by packing its frame."""
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        """Hide this screen by unpacking its frame."""
        self.frame.pack_forget()