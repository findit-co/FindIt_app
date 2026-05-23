from tarfile import data_filter
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime
from HomePage import HomeScreen
from input_screen import InputScreen
from results_screen import ResultsScreen 
from dashboard_screen import DashboardScreen
from resourceengine import ResourceEngine
from DataManager import DataManager
class BaseScreen:
    """
    Base class for all screens - enables polymorphism.
    All screen classes(Home, Input, Results, dashboard) inherit from this. """

    def __init__(self, parent, controller):
        """Initialize base screen.
        args:
            parent:The main window(tk.Tk object)
            controller:Reference to FinfItApp for navigathion"""
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent)
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

        # shared data between screens
        self.current_resource = None  # stores input from InputScreen
        self.search_results = None    # Stores results from ResourceEngine
        
        # Initialize components (teammates will create these)
        self.resource_engine = ResourceEngine("resources.csv")
        self.data_manager = None      # Kene will create DataManager
        
        # Initialize all screens
        self.screens = {}
        self._create_screens()

        # show home screen first
        self.show_screen("home")

    def _create_screens(self):
        """Create all screen objects and store in dictionary."""
        self.screens["home"] = HomeScreen(self.root, self)
        self.screens["input"] = InputScreen(self.root, self)
        self.screens["results"] = ResultsScreen(self.root, self)
        self.screens["dashboard"] = DashboardScreen(self.root, self)

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
    
    def set_resource_input(self, resource_name, category, location):
        """ Store resource input from InputScreen.
        called by Kennedy's InputScreen when user submits.
        Args:
            resource_name: The resource user entered
            category: Selected category (Agriculture, Mining, etc.)
            location: Selected location (Lagos, Aba, Kano)"""
        self.current_resource = {
            "name": resource_name,
            "category": category,
            "location": location,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def get_resource_results(self):
        """ Get results for current resource. Called by Udo's ResultsScreen to display results.
          Returns:
                Dictionary with results or None"""
        if self.current_resource and self.resource_engine:
            results = self.resource_engine.find_resource(
                self.current_resource["name"],
                self.current_resource["location"]
            )
            self.search_results = results
            return results
        return None

    def save_search_history(self):
        """ Save current search to CSV. 
        called after displaying results.
        Uses Kene's DataManager."""
        if self.current_resource and self.search_results and self.data_manager:
            self.data_manager.save_search(
                self.current_resource,
                self.search_results
            )

    def load_search_history(self):
        """ Load all previous searches. Called by Tochi's DashboardScreen.

        Returns:
            List of previous searches
        """
        if self.data_manager:
            return self.data_manager.load_history()
        return []


def main():
    """
    Main entry point for the application.
    Creates the window and starts the app.
    """
    root = tk.Tk()
    app = FindItApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()