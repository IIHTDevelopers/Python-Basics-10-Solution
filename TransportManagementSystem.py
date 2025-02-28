# Transport Management System
# Topics: Operators, Control Flow, Functions

# Static data: Transport records stored as a dictionary
transport_data = {
    "T101": {"route": "New York - Boston", "passengers": 40, "fare_per_passenger": 15},
    "T102": {"route": "Los Angeles - San Francisco", "passengers": 30, "fare_per_passenger": 20},
    "T103": {"route": "Chicago - Detroit", "passengers": 25, "fare_per_passenger": 25},
    "T104": {"route": "Houston - Dallas", "passengers": 50, "fare_per_passenger": 10},
    "T105": {"route": "Miami - Orlando", "passengers": 20, "fare_per_passenger": 30}
}

def calculate_trip_revenue(trip_id):
    """Calculate the total revenue for a given trip."""
    if trip_id in transport_data:
        trip = transport_data[trip_id]
        revenue = trip["passengers"] * trip["fare_per_passenger"]  # Using multiplication operator
        return f"Revenue for {trip['route']}: ${revenue}"
    else:
        return "Error: Trip ID not found."

def validate_trip(trip_id, min_passengers):
    """Check if the trip meets the minimum required passengers for operation."""
    if trip_id in transport_data:
        trip = transport_data[trip_id]
        if trip["passengers"] >= min_passengers:  # Using comparison operator
            return f"Trip {trip_id} is valid with {trip['passengers']} passengers."
        else:
            return f"Trip {trip_id} does not meet the minimum requirement of {min_passengers} passengers."
    else:
        return "Error: Trip ID not found."

def total_transport_revenue():
    """Calculate the total revenue generated from all trips."""
    total_revenue = sum(trip["passengers"] * trip["fare_per_passenger"] for trip in transport_data.values())  # Using sum operator
    return f"Total Transport Revenue: ${total_revenue}"

# Main Execution
print(calculate_trip_revenue("T102"))  # Get revenue for Trip T102
print(validate_trip("T104", 40))  # Check if Trip T104 meets the minimum requirement of 40 passengers
print(total_transport_revenue())  # Calculate total revenue from all trips
