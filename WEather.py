import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget,   QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter the city name: ",self)
    self.city_input = QLineEdit(self)
    self.get_weather_buton = QPushButton("Get Weather",self)



if __name__ == "__main__":
  app = QApplication(sys.argv)
  weather_app = WeatherApp()
  weather_app.show()
  sys.exit(app.exec_())