import math
import json

class DisasterReliefSystem:
    def __init__(self, initial_date=None):
        # Initialize the system with initial data or an empty structure
        self.resources_data = initial_date or {"supplies": [],"shelters": []}

    @staticmethod
    def calculate_distance(loc1, loc2):
        # Calculate the Haversine distance between two locations (latitude, longitude)
        R = 6371 #Radius of the Earth in km
        lat1, lon1 = loc1
        lat2, lon2 = loc2
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = (math.sin(delta_phi/2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def find_nearest_resources(self, user_location, resources_types):
        # Find the nearest resources of the specified type to the user's location
        resources = self.resources_data.get(resources_types, [])
        resources_sorted = sorted(resources, key=lambda r: self.calculate_distance(user_location, r["location"]))
        return resources_sorted

    def update_inventory(self, resource_name, location, new_stock):
        # Update the stock of a specific resource
        for resource in self.resources_data["supplies"]:
            if resource["name"] == resource_name and resource["location"] == location:
                resource["stock"] = new_stock
                print(f"Updated {resource_name} at {location} to {new_stock} items.")
                return
        print("Resource not found.")

    def add_new_resource(self, resource_name, location, stock):
        # Add a new resource to the inventory
        self.resources_data["supplies"].append({"name": resource_name, "location": location, "stock": stock})
        print(f"Added {resource_name} with {stock} items at location {location}.")

    def save_data_to_file(self, filename="resources.json"):
        # Save resources data to a JSON file
        with open(filename, "w") as file:
            json.dump(self.resources_data, file)
        print(f"Data saved to {filename}.")

    def load_data_from_file(self, filename="resource.json"):
        # Load resources data from a JSON file
        try:
            with open(filename, "r") as file:
                self.resources_data = json.load(file)
                print(f"Data loaded from {filename}.")
        except FileNotFoundError:
            print(f"{filename} not found. Using initial data.")

# Sample initial data
initial_data = {"supplies": [{"name":"Water Bottles", "location":(40.1247, -75.1161), "stock": 15000},
                 {"name":"First Aid Kits", "location":(40.1236, -75.1175), "stock": 10000},
                 {"name":"Canned Food", "location":(40.1181, -75.1211), "stock": 25000}],
                  "shelters": [{"name": "Woodland Shelter", "location": (40.1173, -75.1123)},
                               {"name": "Lares Shelter", "location": (40.1168, -75.1088)}]}

if __name__ == '__main__':
    system = DisasterReliefSystem(initial_data)
    user_location = (40.1165, -75.1083) # User's location at Penn State Abington

    # Find nearest supplies
    print("Nearest supplies:")
    nearest_supplies = system.find_nearest_resources(user_location, "supplies")
    for resource in nearest_supplies:
        distance = system.calculate_distance(user_location, resource["location"])
        print(f"{resource['name']} - {resource['stock']} in stock - {distance:.2f} km away.")

    # Find nearest shelters
    print("\nNearest shelters:")
    nearest_shelters = system.find_nearest_resources(user_location, "shelters")
    for shelter in nearest_shelters:
        distance = system.calculate_distance(user_location, shelter["location"])
        print(f"{shelter['name']} - {distance:.2f} km away")

    # Update inventory
    system.update_inventory("Water Bottles", (40.1247, -75.1161), 1200)

    # Add a new resource
    system.add_new_resource("Blankets", (40.1144, -75.1114), 1100)

    # Save data to file
    system.save_data_to_file("resources.json")

    # Load data from file
    system.load_data_from_file("resources.json")


