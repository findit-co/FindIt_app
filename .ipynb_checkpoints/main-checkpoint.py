from tarfile import data_filter
import tkinter as tk
from tkinter import ttk,messagebox
import csv
from datetime import datetime
from HomePage import HomeScreen
from input_screen import InputScreen
from results_screen import ResultsScreen
from dashboard_screen import DashboardScreen
from resource_engine import ResourceEngine

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

    #shared data between screens
        self.current_resource = None # stores input from InputScreen
        self.search_results = None # Stores results from ResourceEngine
        # Initialize components(teammates will create these)
        self.resource_engine = ResourceEngine("resources.csv")
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
    def set_resource_input(self, resource_name, location):
        """ Store resource input from InputScreen.
        called by Kennedy's InputScreen when user submits.
        Args:
            resource_name: The resource user entered
            location: Selected location (Lagos, Aba, Kano)"""
        self.current_resource = {
                    "name": resource_name,
                    "location": location,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                }

        def get_resource_result_results(self):
            """ Get results for current resource.called by Udo's ResultsScreen to display results.
              Returns:
                    Dictionary with results or None"""

            if self.currrent_resource and self.resource_engine:
                # Dilibe's ResourceEngine will process this
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
                """ Load all previous searches.called by Tochi's DashboardScreen.

                Returns:
                    List of previous searches
                    """

                if self.data_manager:
                    return self.data_manager.load_history()
                    return []


                


      
    def build_ui(self):
        """Override this in child classes.
        each screen implements their own UI here."""
        raise
    NotImplementedError("subclass must implement build_ui()")


class InputScreen(BaseScreen):
    """
    Input Screen - Resource entry
    Developer: Kennedy (Input Systems Engineer)
    """
    
    def build_ui(self):
        # PLACEHOLDER - Kennedy will implement
        pass
    
    def show(self):
        """Show this screen"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide this screen"""
        self.frame.pack_forget()
        
class ResultsScreen(BaseScreen):
    """
    Results Screen - Display resource information
    Developer: Udo (Output & Presentation Engineer)
    """
    
    def build_ui(self):
        # PLACEHOLDER - Udo will implement
        pass
    
    def show(self):
        """Show this screen"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide this screen"""
        self.frame.pack_forget()



class DashboardScreen(BaseScreen):
    """
    Dashboard Screen - Search history
    Developer: Tochi (Assistant Data & Persistence Engineer)
    """
    
    def build_ui(self):
        # PLACEHOLDER - Tochi will implement
        pass
    
    def show(self):
        """Show this screen"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide this screen"""
        self.frame.pack_forget()





class ResourceEngine:
    """
    Resource matching engine
    Developer: Dilibe (Core Logic Engineer)
    """
    
    def __init__(self, csv_file="resources.csv"):
        """
        DILIBE: Initialize your engine.
        
        Args:
            csv_file: Path to resources CSV file
        """
        self.csv_file = csv_file
        # DILIBE: Load CSV data here
        # self.resources = self._load_resources()
        print(f"ResourceEngine initialized (Dilibe: Load {csv_file} here)")
    
    def find_resource(self, resource_name, location):
        """
        DILIBE: Implement resource matching logic.
        
        Args:
            resource_name: Name of resource to find
            location: User's selected location
        
        Returns:
            Dictionary with format:
            {
                "resource": "Sand",
                "uses": ["Construction", "Glass making", "Landscaping"],
                "business_ideas": [
                    "Start sand supply business",
                    "Partner with construction companies"
                ],
                "income_estimate": "₦50,000 - ₦200,000/month",
                "location_specific": "High demand in Lagos construction"
            }
        """
        # PLACEHOLDER - Dilibe will implement
        # 1. Search CSV for resource_name
        # 2. Filter by location if needed
        # 3. Return formatted results
        
        print(f"ResourceEngine: Finding '{resource_name}' in {location}")
        
        return {
            "resource": resource_name,
            "uses": ["DILIBE: Add uses here", "Use 2", "Use 3"],
            "business_ideas": [
                "DILIBE: Add business idea 1",
                "DILIBE: Add business idea 2"
            ],
            "income_estimate": "DILIBE: Add income estimate",
            "location_specific": f"DILIBE: Add {location}-specific info"
        }


class DataManager:
    """
    Data persistence manager
    Developer: Kene (Data & Persistence Engineer)
    """
    
    def __init__(self, history_file="search_history.csv"):
        """
        KENE: Initialize data manager.
        
        Args:
            history_file: Path to history CSV file
        """
        self.history_file = history_file
        # KENE: Create file if doesn't exist
        # self._initialize_file()
        print(f"DataManager initialized (Kene: Setup {history_file} here)")
    
    def save_search(self, resource_input, results):
        """
        KENE: Save search to CSV.
        
        Args:
            resource_input: Dict with name, location, timestamp
            results: Dict with uses, business_ideas, income
        """
        # PLACEHOLDER - Kene will implement
        # 1. Open CSV in append mode
        # 2. Write new row with all data
        # 3. Handle errors gracefully
        
        print(f"DataManager: Saving search for '{resource_input['name']}'")
        print("KENE: Implement CSV writing here")
    
    def load_history(self):
        """
        KENE: Load all search history.
        
        Returns:
            List of dictionaries, each representing a search
            Format:
            [
                {
                    "timestamp": "2024-01-15 10:30:00",
                    "resource": "Sand",
                    "location": "Lagos",
                    "business_ideas": "...",
                    "income": "..."
                },
                ...
            ]
        """
        # PLACEHOLDER - Kene will implement
        # 1. Open CSV file
        # 2. Read all rows
        # 3. Return as list of dictionaries
        
        print("DataManager: Loading history")
        print("KENE: Implement CSV reading here")
        
        return [
            {
                "timestamp": "2024-01-15 10:30:00",
                "resource": "Sand",
                "location": "Lagos",
                "business_ideas": "Construction supply",
                "income": "₦50,000/month"
            },
            {
                "timestamp": "2024-01-15 11:00:00",
                "resource": "Cassava",
                "location": "Aba",
                "business_ideas": "Garri processing",
                "income": "₦80,000/month"
            }
        ]



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