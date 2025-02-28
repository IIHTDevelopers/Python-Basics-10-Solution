import os

# Static Data: Dictionary containing student fee records
student_fees = {
    "S101": {"name": "Alice", "grade": "5th", "fees_paid": 2000, "total_fees": 5000},
    "S102": {"name": "Bob", "grade": "6th", "fees_paid": 3500, "total_fees": 5000},
    "S103": {"name": "Charlie", "grade": "7th", "fees_paid": 5000, "total_fees": 5000},
    "S104": {"name": "David", "grade": "8th", "fees_paid": 1000, "total_fees": 6000},
    "S105": {"name": "Emma", "grade": "9th", "fees_paid": 4000, "total_fees": 7000}
}

# File to store student fee records
FILE_NAME = "fees_data.txt"

def save_to_file():
    """Save the student fee records to a file."""
    with open(FILE_NAME, "w") as file:
        file.write("ID,Name,Grade,Fees Paid,Total Fees\n")
        for student_id, data in student_fees.items():
            file.write(f"{student_id},{data['name']},{data['grade']},{data['fees_paid']},{data['total_fees']}\n")

def get_fees():
    """Retrieve and display Emma's fee details from the file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()[1:]  # Skip header
            for line in lines:
                student_id, name, grade, fees_paid, total_fees = line.strip().split(",")
                if name == "Emma":
                    return f"Student: {name}, Grade: {grade}, Fees Paid: ${fees_paid}, Total Fees: ${total_fees}"
    return "Error: Emma's record not found."

def display_fees():
    """Display all student fee records from the file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return file.read()
    return "Error: No data found."

# Save initial static data to file
save_to_file()

# Execute functions
print(get_fees())  # Get Emma's fee details
print(display_fees())  # Display all student fee records
