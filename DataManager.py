import csv
import os
from datetime import datetime

class DataManager:                                
    def __init__(self, history_file="search_history.csv"):  
        self.history_file = history_file
        self._initialize_file()

    def _initialize_file(self):
       #makes sure the file acc exists and the headers match our ui
        try:
            # checks if file exists by trying to open it
            with open(self.history_file, 'r', encoding='utf-8') as file:
                pass  
        except FileNotFoundError:
            # make the file with matching columns for rsults and dashboard screens
            with open(self.history_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'timestamp', 
                    'resource', 
                    'location', 
                    'uses', 
                    'business_ideas', 
                    'income_estimate'
                ])

    def save_search(self, resource_input, results):   
        #takes in what user selectss and some engine data, then appends them tothe CSV file
        try:
            # generate a timestamp if kennedy's controller input doesn't have one
            timestamp = resource_input.get('timestamp', datetime.now().strftime("%Y-%m-%d %H:%M"))
            
            #gets out clean string values from dictionary formats
            resource_name = resource_input.get('name', results.get('resource', 'Unknown Resource')).capitalize()
            location = resource_input.get('location', 'Unknown Location')
            
            # converts list data fields to strings so columns in our csv stay clean
            uses_list = results.get('uses', [])
            uses_str = "; ".join(uses_list) if isinstance(uses_list, list) else str(uses_list)
            
            ideas_list = results.get('business_ideas', [])
            ideas_str = "; ".join(ideas_list) if isinstance(ideas_list, list) else str(ideas_list)
            
            income = results.get('income_estimate', '₦0 - ₦0')

            # append the record to csv file
            with open(self.history_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    timestamp,
                    resource_name,
                    location,
                    uses_str,
                    ideas_str,
                    income
                ])
            print(f"[DataManager] Successfully saved history for: {resource_name}")
            return True
        except Exception as e:
            print(f"[DataManager] Error saving search to file cabinet: {e}")
            return False

    def load_history(self):                           
        #loads all previous searches from csv file to show in tochi's dashboard 
        history = []
        if not os.path.exists(self.history_file):
            return history
            
        try:
            with open(self.history_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    history.append(row)
        except Exception as e:
            print(f"[DataManager] Error reading records from file cabinet: {e}")
            
        return history