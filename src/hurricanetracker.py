import requests
import json

class HurricaneTracker:
    def __init__(self, lat, long):
        self.BASE_URL = "https://api.weather.gov"
        self.latitude = lat
        self.longitude = long
        
        self.heyy = 2
        self.params = {
            "point": "40.8448,-73.8648",
            "event": "Hurricane"
        }
        self.headers = {
            "User-Agent": "Hurricane Gaurd/1.0"
        }
    
    # Retrieves the gridpoint information for a specific latitude & longitude
    def get_gridpoint(self):
        endpoint = f"{self.BASE_URL}/points/{self.latitude},{self.longitude}"
        self.heyy += 2
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data
    
    # Retrieves the weather forecast for a specific gridpoint
    def get_forecast(self):
        gridpoint_data = self.get_gridpoint()
        params = {
            
        }
        
        if gridpoint_data:
            office = gridpoint_data["properties"]["gridId"]
            gridX = gridpoint_data["properties"]["gridX"]
            gridY = gridpoint_data["properties"]["gridY"]
        
        endpoint = f"{self.BASE_URL}/gridpoints/{office}/{gridX},{gridY}/forecast"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        if data:
            periods = data["properties"]["periods"]

            for period in periods:
                    if period['number'] == 1:
                        params = {"temperature": period['temperature'],
                                  "description": period['shortForecast']
                            } 
                    elif period['number'] == 2:
                        params["tomorrows_temperature"] = period['temperature']
                        params["tomorrows_description"] = period['shortForecast']
            
        return params

    # Retrieves active hurricanes
    def get_active_hurricanes(self):
        endpoint = f"{self.BASE_URL}/alerts"
        
        # Make the GET request
        response = requests.get(endpoint, params=self.params)
        data = response.json()
        
        if data.get('features', {}):
            return f"{data.get('features', {})}"
        else:
            return f"There are no ACTIVE Hurricanes!"
  
