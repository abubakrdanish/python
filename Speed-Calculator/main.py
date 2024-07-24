from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys

class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        name_label = QLabel("Distance:")
        self.name_line_edit = QLineEdit()

        self.dropdown = QComboBox()
        self.dropdown.addItem("Metric (km)")
        self.dropdown.addItem("Imperial (miles)")

        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(self.dropdown, 0, 2)
        grid.addWidget(time_label,1,0)
        grid.addWidget(self.time_line_edit, 1,1)
        grid.addWidget(calculate_button,2,1)
        grid.addWidget(self.output_label,3,0,1,3)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.name_line_edit.text())
        time = float(self.time_line_edit.text())
        unit = self.dropdown.currentText()

        if unit == "Metric (km)":
            speed = distance / time
            self.output_label.setText(f"Average speed: {speed} km/h")
        elif unit == "Imperial (miles)":
            speed = distance / time
            speed = round(speed * 0.621371,2)
            self.output_label.setText(f"Average speed: {speed} miles/h")
        else:
            self.output_label.setText("Invalid unit selected")

app = QApplication(sys.argv)
speed_calculator = AverageSpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())