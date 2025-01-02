# Import necessary modules from PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QMessageBox, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

# Import the Section_Student module
import Section_Student                                                        

class StringAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Set window title and size
        self.setWindowTitle('STUDENT DETAIL VIEWER :')
        self.resize(800, 600)
        
        # Create input section
        self.name_label = QLabel('Enter Your First Name')
        self.name_input = QLineEdit()
        
        # Create section check section with checkboxes
        self.section_check_label = QLabel('Section Check:')
        self.section_yes = QCheckBox('Yes')
        self.section_no = QCheckBox('No')
        
        # Create palindrome check section with checkboxes
        self.palindrome_label = QLabel('Palindrome Word:')
        self.palindrome_yes = QCheckBox('Yes')
        self.palindrome_no = QCheckBox('No')
        
        # Create analyze button and connect it to analyze_name function
        self.analyze_button = QPushButton('Check Details')
        self.analyze_button.clicked.connect(self.analyze_name)
        
        # Spacer to maintain alignment
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        
        # Add section check layout
        hbox_section = QHBoxLayout()
        hbox_section.setAlignment(Qt.AlignCenter)
        hbox_section.addWidget(self.section_check_label)
        hbox_section.addWidget(self.section_yes)
        hbox_section.addWidget(self.section_no)
        layout.addLayout(hbox_section)
        
        # Add palindrome check layout
        hbox_palindrome = QHBoxLayout()
        hbox_palindrome.setAlignment(Qt.AlignCenter)
        hbox_palindrome.addWidget(self.palindrome_label)
        hbox_palindrome.addWidget(self.palindrome_yes)
        hbox_palindrome.addWidget(self.palindrome_no)
        layout.addLayout(hbox_palindrome)
        
        # Add spacer and analyze button
        layout.addItem(spacer)
        layout.addWidget(self.analyze_button)
        
        # Set the layout for the main window
        self.setLayout(layout)
    
    def analyze_name(self):
        # Get the user input name
        user_name = self.name_input.text()
        
        # Clear previous checks
        self.section_yes.setChecked(False)
        self.section_no.setChecked(False)
        self.palindrome_yes.setChecked(False)
        self.palindrome_no.setChecked(False)
        self.section_yes.setStyleSheet('')
        self.section_no.setStyleSheet('')
        self.palindrome_yes.setStyleSheet('')
        self.palindrome_no.setStyleSheet('')
        
        # Check if the name is a palindrome and display the result first
        if Section_Student.palindrome_checker(user_name):
            self.palindrome_yes.setChecked(True)
            self.palindrome_yes.setStyleSheet('color: green')
            self.palindrome_no.setStyleSheet('')
        else:
            self.palindrome_no.setChecked(True)
            self.palindrome_no.setStyleSheet('color: red')
            self.palindrome_yes.setStyleSheet('')
        
        # Then check if the name is in the section and display the result
        if Section_Student.section_checker(user_name):
            self.section_yes.setChecked(True)
            self.section_yes.setStyleSheet('color: green')
            self.section_no.setStyleSheet('')
            details = Section_Student.details_viewer(user_name)
            QMessageBox.information(self, 'Student Details:', details)
        else:
            self.section_no.setChecked(True)
            self.section_no.setStyleSheet('color: red')
            self.section_yes.setStyleSheet('')
            QMessageBox.information(self, 'Student Details:', Section_Student.other_section(user_name))

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StringAnalyzer()
    ex.show()
    sys.exit(app.exec_())
