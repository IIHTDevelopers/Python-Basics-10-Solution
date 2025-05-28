# Transport Management System
# Topics: Dictionaries, Functions, Arithmetic Operations

# Initialize transport trip data
transport_data = {
    "T101": {"route": "New York - Boston", "passengers": 40, "fare_per_passenger": 15},
    "T102": {"route": "Los Angeles - San Francisco", "passengers": 30, "fare_per_passenger": 20},
    "T103": {"route": "Chicago - Detroit", "passengers": 25, "fare_per_passenger": 25},
    "T104": {"route": "Houston - Dallas", "passengers": 50, "fare_per_passenger": 10},
    "T105": {"route": "Miami - Orlando", "passengers": 20, "fare_per_passenger": 30}
}

def calculate_trip_revenue(trip_id):
    # Calculate revenue for a given trip
    if trip_id in transport_data:
        data = transport_data[trip_id]
        return data["passengers"] * data["fare_per_passenger"]
    return None

def validate_trip(trip_id, min_passengers):
    # Check if a trip meets minimum passenger requirement
    if trip_id in transport_data:
        return transport_data[trip_id]["passengers"] >= min_passengers
    return False

def total_transport_revenue():
    # Compute total revenue from all trips
    return sum(data["passengers"] * data["fare_per_passenger"] for data in transport_data.values())

# Main Execution
print("Revenue for T102:", calculate_trip_revenue("T102"))
print("Is T102 valid for min 20 passengers?:", validate
