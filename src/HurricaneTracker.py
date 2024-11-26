import requests

class HurricaneTracker:
    def __init__(self):
        self.BASE_URL = "https://api.weather.gov"
        self.params = {
            "event": "hurricane"
        }
        self.headers = {
            "User-Agent": "Hurricane Gaurd/1.0 stevensblantrice@gmail.com"
        }
    
    # Retrieves the gridpoint information for a specific latitude & longitude.
    def get_gridpoint(self, latitude, longitude):
        endpoint = f"{self.BASE_URL}/points/{latitude},{longitude}"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data
    
    # Retrieves the weather forecast for a specific gridpoint.
    def get_forecast(self, office, gridX, gridY):
        endpoint = f"{self.BASE_URL}/gridpoints/{office}/{gridX},{gridY}/forecast"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data
    
    def fetch_active_hurricanes(self):
        endpoint = f"{self.BASE_URL}/alerts"
        
        # Make the GET request
        response = requests.get(endpoint)
        data = response.json()
        return data
  
