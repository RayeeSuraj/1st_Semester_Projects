import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
import Number_Operator as op  # Importing functions from Number_Operator.py


class NumberAnalyzerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Number Analyzer")

        # Layout for the main window
        main_layout = QVBoxLayout()

        # Input section with Analyze button beside the input box
        input_layout = QHBoxLayout()
        self.number_label = QLabel("Enter a Number:")
        self.number_input = QLineEdit()
        self.analyze_button = QPushButton("Analyze")
        self.analyze_button.clicked.connect(self.analyze_number)

        input_layout.addWidget(self.number_label)
        input_layout.addWidget(self.number_input)
        input_layout.addWidget(self.analyze_button)  # Place the button beside the input box

        main_layout.addLayout(input_layout)

        # Output section
        self.result_labels = {
            "square": QLabel(""),
            "square_root": QLabel(""),
            "cube": QLabel(""),
            "cube_root": QLabel(""),
            "prime": QLabel(""),
            "palindrome": QLabel(""),
            "armstrong": QLabel(""),
        }

        for label in self.result_labels.values():
            main_layout.addWidget(label)

        # Set main layout to the window
        self.setLayout(main_layout)

    def is_number_valid(self, input_string):
        """Validate input using ASCII codes to check for numeric characters."""
        for char in input_string:
            if not (48 <= ord(char) <= 57):  # ASCII range for 0-9
                return False
        return True

    def clear_results(self):
        """Clear all result labels."""
        for label in self.result_labels.values():
            label.setText("")  # Clear the text
            label.hide()       # Hide the label until needed

    def analyze_number(self):
        user_input = self.number_input.text()

        # Clear all previous results
        self.clear_results()

        # Validate input using ASCII codes
        if not self.is_number_valid(user_input):
            QMessageBox.warning(self, "Invalid Input", "Please enter only a number.")
            return

        # Convert to integer for analysis
        number = int(user_input)

        # Perform checks and update the output labels
        self.result_labels["square"].setText(
            f"Perfect Square: {'YES' if op.check_square(number) else 'NO'}"
        )
        self.result_labels["square"].show()

        if op.check_square(number):
            self.result_labels["square_root"].setText(f"Square Root of {number}: {int(pow(number, 0.5))}")
            self.result_labels["square_root"].show()

        self.result_labels["cube"].setText(
            f"Perfect Cube: {'YES' if op.check_cube(number) else 'NO'}"
        )
        self.result_labels["cube"].show()

        if op.check_cube(number):
            self.result_labels["cube_root"].setText(f"Cubic Root of {number}: {int(round(pow(number, 1/3)))}")
            self.result_labels["cube_root"].show()

        self.result_labels["prime"].setText(f"Prime Number: {'YES' if op.check_prime(number) else 'NO'}")
        self.result_labels["prime"].show()

        # Palindrome logic with error for single-digit numbers
        if number < 10:  # Single-digit number
            self.result_labels["palindrome"].setText("Palindrome Number: Error! Invalid single-digit number.")
        else:
            self.result_labels["palindrome"].setText(
                f"Palindrome Number: {'YES' if op.check_palindrome(number) else 'NO'}"
            )
        self.result_labels["palindrome"].show()

        armstrong_result = op.check_armstrong(number)
        self.result_labels["armstrong"].setText(
            f"Armstrong Number: {armstrong_result if isinstance(armstrong_result, str) else 'YES' if armstrong_result else 'NO'}"
        )
        self.result_labels["armstrong"].show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    analyzer = NumberAnalyzerApp()
    analyzer.resize(400, 300)
    analyzer.show()
    sys.exit(app.exec())