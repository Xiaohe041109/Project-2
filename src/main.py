import json
from HurricaneTracker import HurricaneTracker

latitude = 40.8448  # Latitude for Bronx, NY
longitude = -73.8648  # Longitude for Bronx, NY

# Calls the hurricane tracker class
x = HurricaneTracker()

# Testing hurricane tracker class
active_hurricanes_data = x.fetch_active_hurricanes()
print(json.dumps(active_hurricanes_data, indent=4))
#print(active_hurricanes_data["type"])

# state = gridpoint_data.get('properties', {}).get('relativeLocation', {}).get('properties', {}).get('state', 'State not found')
# print(state)


"""# Testing hurricane tracker gridpoint method
gridpoint_data = x.get_gridpoint(latitude, longitude)

if gridpoint_data:
    office = gridpoint_data["properties"]["gridId"]
    gridX = gridpoint_data["properties"]["gridX"]
    gridY = gridpoint_data["properties"]["gridY"]

    print(f"Office: {office}, GridX: {gridX}, GridY: {gridY}")

# Testing hurricane tracker forecast method
forecast_data = x.get_forecast(office, gridX, gridY)

if forecast_data:
    periods = forecast_data["properties"]["periods"]

    for period in periods:
        print(f"{period['name']}: {period['detailedForecast']}")"""

