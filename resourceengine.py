import csv
from difflib import get_close_matches


class ResourceEngine:
    def __init__(self, csv_file="resources.csv"):
        """
        Initialize engine and load CSV data.
        """
        self.csv_file = csv_file
        self.resources = self._load_resources()
        self.all_resources_list = self._get_unique_resources()

        print(f"ResourceEngine loaded {len(self.resources)} resources")

    def _load_resources(self):
        """
        Load all resources from CSV file.
        """
        resources = []

        try:
            with open(self.csv_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    resources.append(row)

        except FileNotFoundError:
            print(f"ERROR: {self.csv_file} not found")

        return resources

    def _get_unique_resources(self):
        """
        Get list of unique resource names for fuzzy matching.
        """
        unique = set()
        for resource in self.resources:
            unique.add(resource["resource"].lower())
        return sorted(list(unique))

    def find_resource(self, resource_name, location):
        """
        Find matching resource by name and location.

        Args:
            resource_name: Resource user searched for
            location: User's selected city/location

        Returns:
            Dictionary with matching resource data
        """

        resource_name = resource_name.lower()
        location = location.lower()

        # FIRST: Try exact match
        for resource in self.resources:
            csv_resource = resource["resource"].lower()
            csv_location = resource["location"].lower()

            if csv_resource == resource_name and csv_location == location:
                return {
                    "resource": resource["resource"],
                    "uses": resource["uses"].split(","),
                    "business_ideas": resource["business_idea"],
                    "income_estimate": resource["income_estimate"],
                    "location_specific":
                        f"{resource['resource']} is profitable in {resource['location']} due to local demand."
                }

        # SECOND: Try exact match in any location
        for resource in self.resources:
            csv_resource = resource["resource"].lower()
            if csv_resource == resource_name:
                return {
                    "resource": resource["resource"],
                    "uses": resource["uses"].split(","),
                    "business_ideas": resource["business_idea"],
                    "income_estimate": resource["income_estimate"],
                    "location_specific":
                        f"{resource['resource']} is profitable in {resource['location']}. Apply these ideas to your location.",
                    "note": f"Showing results for '{resource_name}' (data from {resource['location']})"
                }

        # THIRD: Try fuzzy match (similar resource names)
        close_matches = get_close_matches(resource_name, self.all_resources_list, n=3, cutoff=0.6)

        if close_matches:
            suggested = close_matches[0]
            for resource in self.resources:
                if resource["resource"].lower() == suggested and resource["location"].lower() == location:
                    return {
                        "resource": resource["resource"],
                        "uses": resource["uses"].split(","),
                        "business_ideas": resource["business_idea"],
                        "income_estimate": resource["income_estimate"],
                        "location_specific":
                            f"Did you mean '{resource['resource']}'? {resource['resource']} is profitable in {resource['location']}.",
                        "note": f"Did you mean '{suggested.title()}'?"
                    }

        # FOURTH: Return suggestions when no match found
        suggestions = get_close_matches(resource_name, self.all_resources_list, n=5, cutoff=0.4)
        
        if suggestions:
            suggestion_text = ", ".join([s.title() for s in suggestions[:5]])
            return {
                "error": f"No matching resource found for '{resource_name}' in {location}",
                "suggestions": f"Did you mean: {suggestion_text}?",
                "uses": ["Try searching for one of the suggested resources"],
                "business_ideas": [f"Try: {suggestion_text}"],
                "income_estimate": "N/A",
                "location_specific": f"We couldn't find '{resource_name}'. Try searching for: {suggestion_text}"
            }
        else:
            return {
                "error": f"No matching resource found for '{resource_name}' in {location}",
                "suggestions": "Try: Cassava, Plastic, Sand, Palm Oil, Scrap Metal, Coconut, Maize, Timber, Charcoal",
                "uses": ["No data available for this search"],
                "business_ideas": ["Try searching for: Cassava, Plastic, Sand, Palm Oil, Scrap Metal"],
                "income_estimate": "N/A",
                "location_specific": "We couldn't find that resource. Try searching for common resources like Cassava, Plastic, or Sand."
            }


# Example Usage
engine = ResourceEngine("resources.csv")

result = engine.find_resource("plastic", "Lagos")

print(result)