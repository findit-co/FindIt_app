# 🤝 FIND IT App - Teammate Integration Guide
## How to Plug Your Code Into the App

---

## 📋 Quick Start for All Teammates

### Step 1: Get the Main File
Ruth has created `main.py` with your placeholder class already set up.

### Step 2: Find Your Class
Search for your name in `main.py`:
- **Ekenem** → `class HomeScreen`
- **Kennedy** → `class InputScreen`
- **Udo** → `class ResultsScreen`
- **Tochi** → `class DashboardScreen`
- **Dilibe** → `class ResourceEngine`
- **Kene** → `class DataManager`

### Step 3: Implement Your Method
Replace the placeholder code in your `build_ui()` method (or other methods).

### Step 4: Test Your Screen
Run `python main.py` and navigate to your screen to test.

---

## 👥 Individual Integration Instructions

### 🎨 Ekenem - Home Screen Developer

**Your Class:** `HomeScreen`  
**Your Method:** `build_ui()`

**What to Keep:**
```python
class HomeScreen(BaseScreen):  # Don't change this line
    def build_ui(self):        # Don't change this line
```

**What to Replace:**
Everything inside `build_ui()` method

**Requirements:**
1. Create welcome UI matching your Figma design
2. Add "Start" button that calls: `self.controller.show_screen("input")`
3. Use `self.frame` as parent for all widgets

**Example Navigation:**
```python
tk.Button(
    self.frame,
    text="Start",
    command=lambda: self.controller.show_screen("input")
).pack()
```

**Test Your Work:**
- Run app → Should see your home screen
- Click Start → Should go to input screen

---

### ⌨️ Kennedy - Input Screen Developer

**Your Class:** `InputScreen`  
**Your Method:** `build_ui()`

**What to Keep:**
```python
class InputScreen(BaseScreen):  # Don't change this line
    def build_ui(self):         # Don't change this line
```

**What to Replace:**
Everything inside `build_ui()` method

**Requirements:**
1. Text input field for resource name
2. Dropdown for location (Lagos, Aba, Kano)
3. Submit button with validation
4. Back button to home

**Critical: Data Passing**
Before navigating to results, you MUST call:
```python
# Get values from your widgets
resource_name = self.resource_entry.get()
location = self.location_combo.get()

# Validate
if not resource_name or not location:
    messagebox.showerror("Error", "Please fill all fields")
    return

# Pass data to controller
self.controller.set_resource_input(resource_name, location)

# Then navigate
self.controller.show_screen("results")
```

**Store Your Widgets:**
```python
def build_ui(self):
    # Store as instance variables so you can access later
    self.resource_entry = tk.Entry(self.frame, ...)
    self.location_combo = ttk.Combobox(self.frame, ...)
```

**Test Your Work:**
- Enter resource name
- Select location
- Click Submit → Should go to results screen
- Check terminal for "ResourceEngine: Finding..." message

---

### 📊 Udo - Results Screen Developer

**Your Class:** `ResultsScreen`  
**Your Methods:** `build_ui()` and `show()`

**What to Keep:**
```python
class ResultsScreen(BaseScreen):  # Don't change this line
    def build_ui(self):           # Don't change this line
    def show(self):               # Don't change this line
        super().show()            # Don't remove this line
```

**What to Replace:**
Everything else inside both methods

**Requirements:**
1. Display resource name
2. Show possible uses (list)
3. Show business ideas (list)
4. Show income estimate
5. Save button, Back button, View History button

**Critical: Getting Results**
In your `show()` method, get results like this:
```python
def show(self):
    super().show()  # Don't remove this!
    
    # Get results from controller
    results = self.controller.get_resource_results()
    
    if results:
        # Update your labels with results
        self.resource_label.config(text=f"Resource: {results['resource']}")
        
        # Format uses as bullet points
        uses_text = "\n".join([f"• {use}" for use in results['uses']])
        self.uses_label.config(text=f"Possible Uses:\n{uses_text}")
        
        # Same for business ideas
        ideas_text = "\n".join([f"• {idea}" for idea in results['business_ideas']])
        self.ideas_label.config(text=f"Business Ideas:\n{ideas_text}")
        
        self.income_label.config(text=f"Income: {results['income_estimate']}")
```

**Store Your Labels:**
```python
def build_ui(self):
    # Store labels as instance variables
    self.resource_label = tk.Label(self.frame, ...)
    self.uses_label = tk.Label(self.frame, ...)
    self.ideas_label = tk.Label(self.frame, ...)
    self.income_label = tk.Label(self.frame, ...)
```

**Save Button:**
```python
tk.Button(
    self.frame,
    text="Save to History",
    command=self.save_search
).pack()

def save_search(self):
    self.controller.save_search_history()
    messagebox.showinfo("Success", "Search saved to history!")
```

**Test Your Work:**
- Navigate from input screen
- Should see results displayed
- Click Save → Should see success message
- Click View History → Should go to dashboard

---

### 📈 Tochi - Dashboard Screen Developer

**Your Class:** `DashboardScreen`  
**Your Methods:** `build_ui()` and `show()`

**What to Keep:**
```python
class DashboardScreen(BaseScreen):  # Don't change this line
    def build_ui(self):              # Don't change this line
    def show(self):                  # Don't change this line
        super().show()               # Don't remove this line
```

**What to Replace:**
Everything else inside both methods

**Requirements:**
1. Display search history in table format
2. Use `ttk.Treeview` for professional look
3. Columns: Date, Resource, Location, Business Ideas
4. Back button to home
5. Refresh button (optional)

**Critical: Getting History**
In your `show()` method, load history like this:
```python
def show(self):
    super().show()  # Don't remove this!
    
    # Get history from controller
    history = self.controller.load_search_history()
    
    # Clear existing items in table
    for item in self.tree.get_children():
        self.tree.delete(item)
    
    # Add history items to table
    for search in history:
        self.tree.insert("", "end", values=(
            search["timestamp"],
            search["resource"],
            search["location"],
            search["business_ideas"]
        ))
```

**Create Treeview:**
```python
def build_ui(self):
    # Create Treeview
    columns = ("Date", "Resource", "Location", "Ideas")
    self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
    
    # Set column headings
    for col in columns:
        self.tree.heading(col, text=col)
        self.tree.column(col, width=150)
    
    self.tree.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Add scrollbar
    scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
    scrollbar.pack(side="right", fill="y")
    self.tree.configure(yscrollcommand=scrollbar.set)
```

**Test Your Work:**
- Navigate to dashboard
- Should see table with history
- Click Refresh → Should reload data
- Click Back → Should go to home

---

### 🧠 Dilibe - Resource Engine Developer

**Your Class:** `ResourceEngine`  
**Your Methods:** `__init__()` and `find_resource()`

**What to Keep:**
```python
class ResourceEngine:                    # Don't change this line
    def __init__(self, csv_file="resources.csv"):  # Don't change this line
    def find_resource(self, resource_name, location):  # Don't change this line
```

**What to Replace:**
Everything inside both methods

**Requirements:**
1. Load resources from CSV file
2. Search for resource by name
3. Filter by location if needed
4. Return results in specific format

**CSV File Structure:**
Create `resources.csv` with these columns:
```csv
resource,uses,business_ideas,income_estimate,lagos_info,aba_info,kano_info
Sand,"Construction;Glass making;Landscaping","Sand supply business;Partner with construction companies","₦50,000 - ₦200,000/month","High demand in construction","Growing construction sector","Desert sand processing"
Cassava,"Garri;Flour;Starch","Garri processing;Cassava flour production","₦80,000 - ₦150,000/month","Urban market demand","Traditional processing hub","Agricultural processing"
```

**Implementation Example:**
```python
def __init__(self, csv_file="resources.csv"):
    self.csv_file = csv_file
    self.resources = {}
    self._load_resources()

def _load_resources(self):
    try:
        with open(self.csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.resources[row['resource'].lower()] = row
    except FileNotFoundError:
        print(f"Warning: {self.csv_file} not found")

def find_resource(self, resource_name, location):
    resource_key = resource_name.lower()
    
    if resource_key not in self.resources:
        return None
    
    resource = self.resources[resource_key]
    
    # Get location-specific info
    location_key = f"{location.lower()}_info"
    location_info = resource.get(location_key, "No specific info for this location")
    
    return {
        "resource": resource['resource'],
        "uses": resource['uses'].split(';'),
        "business_ideas": resource['business_ideas'].split(';'),
        "income_estimate": resource['income_estimate'],
        "location_specific": location_info
    }
```

**Test Your Work:**
- Create `resources.csv` with sample data
- Run app and search for a resource
- Check if results appear correctly
- Try different locations

---

### 💾 Kene - Data Manager Developer

**Your Class:** `DataManager`  
**Your Methods:** `__init__()`, `save_search()`, `load_history()`

**What to Keep:**
```python
class DataManager:                                    # Don't change this line
    def __init__(self, history_file="search_history.csv"):  # Don't change this line
    def save_search(self, resource_input, results):   # Don't change this line
    def load_history(self):                           # Don't change this line
```

**What to Replace:**
Everything inside all methods

**Requirements:**
1. Create CSV file if doesn't exist
2. Save searches with all details
3. Load all previous searches
4. Handle errors gracefully

**CSV File Structure:**
Create `search_history.csv` with these columns:
```csv
timestamp,resource,location,uses,business_ideas,income_estimate
```

**Implementation Example:**
```python
def __init__(self, history_file="search_history.csv"):
    self.history_file = history_file
    self._initialize_file()

def _initialize_file(self):
    try:
        with open(self.history_file, 'r') as file:
            pass  # File exists
    except FileNotFoundError:
        # Create file with headers
        with open(self.history_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'resource', 'location', 'uses', 'business_ideas', 'income_estimate'])

def save_search(self, resource_input, results):
    try:
        with open(self.history_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                resource_input['timestamp'],
                resource_input['name'],
                resource_input['location'],
                '; '.join(results['uses']),
                '; '.join(results['business_ideas']),
                results['income_estimate']
            ])
    except Exception as e:
        print(f"Error saving search: {e}")

def load_history(self):
    history = []
    try:
        with open(self.history_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                history.append(row)
    except FileNotFoundError:
        pass  # Return empty list
    return history
```

**Test Your Work:**
- Run app and make a search
- Click Save on results screen
- Check if `search_history.csv` is created
- Navigate to dashboard and verify data appears

---

## 🔧 Integration with Ruth's Controller

### How to Access Controller Methods

From any screen class, you can access:

```python
# Navigate to another screen
self.controller.show_screen("screen_name")

# Store input data (Kennedy)
self.controller.set_resource_input(name, location)

# Get results (Udo)
results = self.controller.get_resource_results()

# Save to history (Udo)
self.controller.save_search_history()

# Load history (Tochi)
history = self.controller.load_search_history()
```

### How Ruth Connects Your Code

In `FindItApp.__init__()`, Ruth creates instances:
```python
# Your screen objects
self.screens["home"] = HomeScreen(self.root, self)
self.screens["input"] = InputScreen(self.root, self)
# ... etc

# Backend objects (Dilibe and Kene create these)
self.resource_engine = ResourceEngine()
self.data_manager = DataManager()
```

---

## ✅ Testing Checklist

### Before Integration:
- [ ] Read this guide completely
- [ ] Understand your requirements
- [ ] Know which methods to implement
- [ ] Have sample data ready (if needed)

### During Integration:
- [ ] Keep class and method signatures unchanged
- [ ] Use `self.frame` as parent for widgets
- [ ] Store widgets as instance variables if you need to update them
- [ ] Test navigation commands
- [ ] Add error handling

### After Integration:
- [ ] Run `python main.py`
- [ ] Navigate to your screen
- [ ] Test all buttons and inputs
- [ ] Check for errors in terminal
- [ ] Test with teammates' code

---

## 🐛 Common Issues and Solutions

### Issue 1: "NameError: name 'tk' is not defined"
**Solution:** Make sure imports are at the top of `main.py`:
```python
import tkinter as tk
from tkinter import ttk, messagebox
```

### Issue 2: "AttributeError: 'NoneType' object has no attribute..."
**Solution:** Check if you're calling controller methods before data is set:
```python
# Bad
results = self.controller.get_resource_results()
print(results['resource'])  # Error if results is None

# Good
results = self.controller.get_resource_results()
if results:
    print(results['resource'])
```

### Issue 3: Widgets not showing up
**Solution:** Make sure you're using `self.frame` as parent:
```python
# Bad
tk.Label(text="Hello").pack()

# Good
tk.Label(self.frame, text="Hello").pack()
```

### Issue 4: Navigation not working
**Solution:** Use controller's show_screen method:
```python
# Bad
self.show_screen("input")

# Good
self.controller.show_screen("input")
```

---

## 📞 Communication Protocol

### When You're Done:
1. Test your code thoroughly
2. Notify Ruth: "My [screen/component] is ready for integration"
3. Share any issues you encountered
4. Document any changes you made

### When You Need Help:
1. Check this guide first
2. Ask Ruth (she's the integration lead)
3. Check with teammate working on related component
4. Review the main plan document

---

## 🎯 Success Criteria

Your integration is successful when:
- [ ] Your code runs without errors
- [ ] Navigation to/from your screen works
- [ ] Data passing works correctly
- [ ] Your UI matches requirements
- [ ] Code is commented and clean
- [ ] You've tested with other teammates' code

---

## 🚀 Final Notes

**Remember:**
- Ruth has created the backbone - you're adding the muscles!
- Don't change class names or method signatures
- Use `self.controller` to access app functionality
- Test incrementally as you build
- Communicate with your team

**You've got this!** 💪

Each of you is building a critical piece of the puzzle. When we put it all together, we'll have an amazing app! 🎉

---

**Questions?** Ask Ruth - she's your integration lead and technical guide! 👩‍💻