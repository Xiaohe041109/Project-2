from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from mainwindow import MainWindow
import sys    

latitude = 40.8448
longitude = -73.8648

app = QApplication(sys.argv)

main_window = MainWindow(app, latitude, longitude)
main_window.show()

app.exec()

"""form_window.form_submitted.connect(
    lambda: [print("BUTTON CLICKED"), 
             main_window.show(),
             form_window.hide()]
)"""

"""main_window = MainWindow(app, latitude, longitude)
main_window.show()"""

"""
# Calls the HurricaneTracker class
x = HurricaneTracker(40.8448, -73.8648)
print(x.get_forecast())
#print(type(x.get_forecast()))
#print(x.get_active_hurricanes())

# Calls the MainWindow class
y = MainWindow(app)
print(y.get_active_hurricane_info())
print(type(y.get_active_hurricane_info()))
"""

"""
# Testing HurricaneTracker get_active_hurricanes method
active_hurricanes_data = x.get_active_hurricanes()
print(active_hurricanes_data)
"""

"""
# Testing HurricaneTracker gridpoint method
gridpoint_data = x.get_gridpoint(latitude, longitude)

#print(json.dumps(gridpoint_data, indent=4))
#state = gridpoint_data.get('properties', {}).get('relativeLocation', {}).get('properties', {}).get('state', 'State not found')
#print(state)

if gridpoint_data:
    office = gridpoint_data["properties"]["gridId"]
    gridX = gridpoint_data["properties"]["gridX"]
    gridY = gridpoint_data["properties"]["gridY"]
    
    print (f"Office: {office} GridX: {gridX} GridY: {gridY}")
"""

"""
# Testing HurricaneTracker get_forecast method
forecast_data = x.get_forecast()

if forecast_data:
    periods = forecast_data["properties"]["periods"]

    for period in periods:
            if period['number'] == 1:
                print(f"{period['name']}: {period['temperature']}")
"""

