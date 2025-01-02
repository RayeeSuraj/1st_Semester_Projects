# List of student details
students_details = [
    { "First_Name": "Suman", "Full_Name": "Suman Shrestha", "ID": 20244095, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Keshab", "Full_Name": "Keshab Xetrri", "ID": 20244097, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Raskin", "Full_Name": "Raskin Rai", "ID": 20244123, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Ramesh", "Full_Name": "Ramesh Kurmi Chaudhary", "ID": 20244093, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Farendra", "Full_Name": "Farendra Chaudhary", "ID": 20244113, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Joel", "Full_Name": "Joel Chaudhary", "ID": 20244096, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Anish", "Full_Name": "Anish Shrestha", "ID": 20244121, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Pragresh", "Full_Name": "Pragresh Shrestha", "ID": 20244099, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Uttam", "Full_Name": "Uttam Shrestha", "ID": 20244110, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Suraj1", "Full_Name": "Suraj Rai", "ID": 20244098, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Suraj2", "Full_Name": "Suraj Bishwokarma", "ID": 20244108, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Hari", "Full_Name": "Hari Narayan Gupta", "ID": 20244106, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Arpan", "Full_Name": "Arpan Karki", "ID": 20244109, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Bipan", "Full_Name": "Bipan Baram", "ID": 20244118, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Shiva", "Full_Name": "Shiva Khadka", "ID": 20244092, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Subash", "Full_Name": "Subash Karki", "ID": 20244101, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Surya", "Full_Name": "Surya KC", "ID": 20244125, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Saurav", "Full_Name": "Saurav Upadhaya", "ID": 20244100, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Samrit", "Full_Name": "Samrit", "ID": 20244101, "Gender": "Male", "Country": "Nepal"},
    { "First_Name": "Nasir", "Full_Name": "Nasir Ahamed", "ID": 20244107, "Gender": "Female", "Country": "Bangladesh"},
    { "First_Name": "Naim", "Full_Name": "Naim Muhammad", "ID": 20244105, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Shakib", "Full_Name": "Shakib Chowdhury", "ID": 20244094, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Lotypur", "Full_Name": "Lotypur Rahman", "ID": 20244116, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Rafi", "Full_Name": "Abdullah AI Rafi", "ID" : 20244102, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Siam", "Full_Name": "Md Ayeed Hosen Siam", "ID": 20244103, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Anas", "Full_Name": "Anas Ashraful Islam", "ID": 20244104, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Shanto", "Full_Name": "Shanto Mijanur Rahman", "ID": 20244120, "Gender": "Male", "Country": "Bangladesh"},
    { "First_Name": "Manisha", "Full_Name": "Manisha Thapa", "ID": 20244114, "Gender": "Female", "Country": "Nepal"},
    { "First_Name": "Niru", "Full_Name": "Niru Tamang", "ID": 20244089, "Gender": "Female", "Country": "Nepal"},
    { "First_Name": "Sophiya", "Full_Name": "Sophiya Rijal", "ID": 20244090, "Gender": "Female", "Country": "Nepal"},
    { "First_Name": "Shradha", "Full_Name": "Shradha Khad Thakuri", "ID": 20244122, "Gender": "Female", "Country": "Nepal"}
]

# Function to check if a student belongs to the section by first name with unique identifier
def section_checker(first_name):
    return any(first_name.lower() == student["First_Name"].lower()[:len(first_name)] for student in students_details)

# Function to return details of the student if they belong to the section
def details_viewer(first_name):
    student = next((s for s in students_details if first_name.lower() == s["First_Name"].lower()[:len(first_name)]), None)
    if student:
        return f"Full Name: {student['Full_Name']}\nGender: {student['Gender']}\nID no: {student['ID']}\nCountry: {student['Country']}"
    else:
        return other_section(first_name)

# Function to handle cases where the name is not in the section
def other_section(first_name):
    return f"Sorry, {first_name} is not from this section. So, there is no detail. Try again with another name."

# Function to check if a given word is a palindrome
def palindrome_checker(user_word):
    return user_word.lower() == user_word[::-1].lower()