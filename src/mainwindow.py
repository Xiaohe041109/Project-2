from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QMainWindow, QSizePolicy
from PySide6.QtGui import QDesktopServices, QFont
from ui_mainwindow import Ui_MainWindow
from hurricanetracker import HurricaneTracker

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, lat, long):
        self.latitude = lat
        self.longitude = long
        
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Hurricane Gaurd")
        
        #self.showFullScreen()
        
        self.hidden.setHidden(True)
        
        # Setting up GitHub & About file menu action buttons
        self.actionGitHub.triggered.connect(self.open_github)
        self.actionAbout.triggered.connect(self.open_github_about)
        
        # Connects hidden menu buttons to pages
        self.pushButton_3.clicked.connect(self.switch_to_home_page)
        self.pushButton_4.clicked.connect(self.switch_to_tracker_page)
        self.pushButton_5.clicked.connect(self.switch_to_prep_page)
        
        self.pushButton_6.clicked.connect(self.open_github)
        self.pushButton_7.clicked.connect(self.open_github_about)
        
        # Connects shown menu buttons to pages
        self.pushButton_8.clicked.connect(self.switch_to_home_page)
        self.pushButton_9.clicked.connect(self.switch_to_tracker_page)
        self.pushButton_10.clicked.connect(self.switch_to_prep_page)
        
        self.pushButton_11.clicked.connect(self.open_github)
        self.pushButton_12.clicked.connect(self.open_github_about)
        
        # Sets current temperature information
        font = QFont()
        font.setPointSize(200)
        self.label_6.setFont(font)
        self.label_6.setText(self.get_temperature())
        
        font2 = QFont()
        font2.setPointSize(10)
        self.label_7.setFont(font2)
        self.label_7.setText(self.get_temperature_description())

        # Sets tomorrows temperature information
        font3 = QFont()
        font3.setPointSize(75)
        self.label_10.setFont(font3)
        self.label_10.setText(self.get_tomorrows_temperature())
        
        self.label_9.setText(self.get_tomorrows_temperature_description())
        
        # Sets active hurricane information
        self.label_11.setText(self.get_active_hurricane_info())

    def switch_to_home_page(self):
        self.pages.setCurrentIndex(0)
    
    def switch_to_tracker_page(self):
        self.pages.setCurrentIndex(1)
    
    def switch_to_prep_page(self):
        self.pages.setCurrentIndex(2)
        
    def open_github(self):
        url = "https://github.com/Xiaohe041109/Project-2/tree/main"
        
        QDesktopServices.openUrl(url)
    
    def open_github_about(self):
        url = "https://github.com/Xiaohe041109/Project-2/blob/main/README.md"
        
        QDesktopServices.openUrl(url)
    
    def get_temperature(self):
        x = HurricaneTracker(self.latitude, self.longitude)
        
        params = x.get_forecast()
        return str(params["temperature"])

    def get_temperature_description(self):
        x = HurricaneTracker(self.latitude, self.longitude)
        
        params = x.get_forecast()
        return str(params["description"])
    
        #formatted_description = params["description"].replace(". ", ".\n")
        #return str(formatted_description)
    
    def get_tomorrows_temperature(self):
        x = HurricaneTracker(self.latitude, self.longitude)
        
        params = x.get_forecast()
        return str(params["tomorrows_temperature"])
    
    def get_tomorrows_temperature_description(self):
        x = HurricaneTracker(self.latitude, self.longitude)
        
        params = x.get_forecast()
        return str(params["tomorrows_description"])
    
    def get_active_hurricane_info(self):
        x = HurricaneTracker(self.latitude, self.longitude)
        
        return x.get_active_hurricanes()