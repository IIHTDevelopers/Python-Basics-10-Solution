# Warehouse Management System
# Topics: Control Flow, Tuples, Dictionaries, If-Else

def initialize_inventory():
    # Initialize warehouse inventory with tuples (Item Name, Quantity, Price per Unit)
    return {
        "W101": ("Laptops", 50, 800),
        "W102": ("Smartphones", 100, 500),
        "W103": ("Headphones", 200, 50),
        "W104": ("Keyboards", 150, 30),
        "W105": ("Monitors", 75, 200)
    }

def most_expensive_item(inventory):
    # Find the most expensive item in inventory
    return max(inventory.values(), key=lambda item: item[2])

def monitor_stock(inventory):
    # Get the stock and price details of Monitors
    if "W105" in inventory:
        item_name, quantity, price = inventory["W105"]
        return f"Product: {item_name}, Stock: {quantity}, Price: ${price} per unit"
    else:
        return "Monitors not found in inventory."

def total_items_in_warehouse(inventory):
    # Calculate total stock in warehouse
    return sum(item[1] for item in inventory.values())

# Main Execution
inventory = initialize_inventory()


print("Most Expensive Item:", most_expensive_item(inventory))
print("Monitor Stock:", monitor_stock(inventory))
print("Total Items in Warehouse:", total_items_in_warehouse(inventory))
