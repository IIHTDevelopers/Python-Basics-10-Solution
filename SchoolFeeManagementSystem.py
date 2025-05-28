# School Fee Management System
# Topics: Dictionaries, Control Flow, File Handling

import os

# Initialize student fee data
student_fees = {
    "S101": {"name": "Alice", "grade": "5th", "fees_paid": 2000, "total_fees": 5000},
    "S102": {"name": "Bob", "grade": "6th", "fees_paid": 3500, "total_fees": 5000},
    "S103": {"name": "Charlie", "grade": "7th", "fees_paid": 5000, "total_fees": 5000},
    "S104": {"name": "David", "grade": "8th", "fees_paid": 1000, "total_fees": 6000},
    "S105": {"name": "Emma", "grade": "9th", "fees_paid": 4000, "total_fees": 7000}
}

def get_fees(name):
    # Return fees paid by student with given name
    for student in student_fees.values():
        if student["name"] == name:
            return student["fees_paid"]
    return None

def is_total_fee_paid(name):
    # Check if student has paid total fees
    for student in student_fees.values():
        if student["name"] == name:
            return student["fees_paid"] >= student["total_fees"]
    return False

def save_to_file():
    # Save fee details to file
    with open("fees_data.txt", "w") as file:
        file.write("ID,Name,Grade,Fees Paid,Total Fees\n")
        for sid, data in student_fees.items():
            file.write(f"{sid},{data['name']},{data['grade']},{data['fees_paid']},{data['total_fees']}\n")

# Main Execution
save_to_file()
print("Fees Paid by Emma:", get_fees("Emma"))
print("Has Charlie paid full fees?:", is_total_fee_paid("Charlie"))
