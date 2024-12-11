# Hurricane Guard
Hurricane Guard in Python using object-oriented programming (OOP) as a project for our 
CMPSC 132-002: Programming and Computation II: Data Structures course, taught by 
Professor Janghoon Yang. This project aims to develop a disaster relief resource management
system to assist in hurricane relief efforts.

## HOW TO ACCESS
1. Go to: [Github Repository](https://github.com/Xiaohe041109/Project-2)
2. Click on the green "Code" button.
3. Select "Download ZIP" from the dropdown menu.
4. Extract the ZIP file to your desired location on your computer.
5. Open the project folder to access the files.
6. Run the Python scripts directly using your Python environment.

## USAGE & INSTRUCTIONS
## Install PySide6
```python
pip install pyside6
```
## Importing Proper Components
```python
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from mainwindow import MainWindow
import sys    

```
## Setting Up Your Location (REPLACE WITH DESIRED LATITUDE & LONGITUDE)
```python
latitude = 40.8448
longitude = -73.8648
```
## Running The GUI
```python
app = QApplication(sys.argv)

main_window = MainWindow(app, latitude, longitude)
main_window.show()

app.exec()
```
