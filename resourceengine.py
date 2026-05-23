import csv


class ResourceEngine:
    """
    Resource matching engine
    Developer: Dilibe (Core Logic Engineer)
    """

    def __init__(self, csv_file="resources.csv"):
        """
        Initialize engine and load CSV data.
        """
        self.csv_file = csv_file
        self.resources = self._load_resources()

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

        return {
            "error": f"No matching resource found for '{resource_name}' in {location}"
        }


# Example Usage
engine = ResourceEngine("resources.csv")

result = engine.find_resource("plastic", "Lagos")

print(result)