import unittest
import sys
import os


# Adjusting the path to import TestUtils and the required modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from SchoolFeeManagementSystem import get_fees, display_fees, save_to_file
from TransportManagementSystem import calculate_trip_revenue, validate_trip, total_transport_revenue
from WarehouseManagementSystem import initialize_inventory, most_expensive_item, total_items_in_warehouse


class TestManagementSystems(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # ===== School Fee Management System =====
        save_to_file()  # Ensure the file is created with initial data

        # ===== Transport Management System =====
        self.trip_id = "T102"
        self.min_passengers = 40
        self.expected_revenue = "Revenue for Los Angeles - San Francisco: $600"
        self.expected_validation = "Trip T102 does not meet the minimum requirement of 40 passengers."
        self.expected_total_revenue = "Total Transport Revenue: $2925"

        # ===== Warehouse Management System =====
        self.inventory = initialize_inventory()
        self.expected_most_expensive = ("Laptops", 50, 800)
        self.expected_total_items = 575

    # ========== School Fee Management System Tests ==========
    def test_get_fees(self):
        """
        Test case for get_fees() function.
        """
        try:
            result = get_fees()
            expected_result = "Student: Emma, Grade: 9th, Fees Paid: $4000, Total Fees: $7000"
            if result == expected_result:
                self.test_obj.yakshaAssert("TestGetFees", True, "functional")
                print("TestGetFees = Passed")
            else:
                self.test_obj.yakshaAssert("TestGetFees", False, "functional")
                print("TestGetFees = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestGetFees", False, "functional")
            print(f"TestGetFees = Failed | Exception: {e}")

    def test_display_fees(self):
        """
        Test case for display_fees() function.
        """
        try:
            result = display_fees()
            # Check if the result contains the header and all student records
            expected_header = "ID,Name,Grade,Fees Paid,Total Fees"
            if expected_header in result and "S101" in result and "S105" in result:
                self.test_obj.yakshaAssert("TestDisplayFees", True, "functional")
                print("TestDisplayFees = Passed")
            else:
                self.test_obj.yakshaAssert("TestDisplayFees", False, "functional")
                print("TestDisplayFees = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDisplayFees", False, "functional")
            print(f"TestDisplayFees = Failed | Exception: {e}")

    # ========== Transport Management System Tests ==========
    def test_calculate_trip_revenue(self):
        """
        Test case for calculate_trip_revenue() function.
        """
        try:
            result = calculate_trip_revenue(self.trip_id)
            if result == self.expected_revenue:
                self.test_obj.yakshaAssert("TestCalculateTripRevenue", True, "functional")
                print("TestCalculateTripRevenue = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateTripRevenue", False, "functional")
                print("TestCalculateTripRevenue = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateTripRevenue", False, "functional")
            print(f"TestCalculateTripRevenue = Failed | Exception: {e}")

    def test_validate_trip(self):
        """
        Test case for validate_trip() function.
        """
        try:
            result = validate_trip(self.trip_id, self.min_passengers)
            if result == self.expected_validation:
                self.test_obj.yakshaAssert("TestValidateTrip", True, "functional")
                print("TestValidateTrip = Passed")
            else:
                self.test_obj.yakshaAssert("TestValidateTrip", False, "functional")
                print("TestValidateTrip = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestValidateTrip", False, "functional")
            print(f"TestValidateTrip = Failed | Exception: {e}")

    def test_total_transport_revenue(self):
        """
        Test case for total_transport_revenue() function.
        """
        try:
            result = total_transport_revenue()
            if result == self.expected_total_revenue:
                self.test_obj.yakshaAssert("TestTotalTransportRevenue", True, "functional")
                print("TestTotalTransportRevenue = Passed")
            else:
                self.test_obj.yakshaAssert("TestTotalTransportRevenue", False, "functional")
                print("TestTotalTransportRevenue = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalTransportRevenue", False, "functional")
            print(f"TestTotalTransportRevenue = Failed | Exception: {e}")

    # ========== Warehouse Management System Tests ==========
    def test_most_expensive_item(self):
        """
        Test case for most_expensive_item() function.
        """
        try:
            result = most_expensive_item(self.inventory)
            if result == self.expected_most_expensive:
                self.test_obj.yakshaAssert("TestMostExpensiveItem", True, "functional")
                print("TestMostExpensiveItem = Passed")
            else:
                self.test_obj.yakshaAssert("TestMostExpensiveItem", False, "functional")
                print("TestMostExpensiveItem = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestMostExpensiveItem", False, "functional")
            print(f"TestMostExpensiveItem = Failed | Exception: {e}")

    def test_total_items_in_warehouse(self):
        """
        Test case for total_items_in_warehouse() function.
        """
        try:
            result = total_items_in_warehouse(self.inventory)
            if result == self.expected_total_items:
                self.test_obj.yakshaAssert("TestTotalItemsInWarehouse", True, "functional")
                print("TestTotalItemsInWarehouse = Passed")
            else:
                self.test_obj.yakshaAssert("TestTotalItemsInWarehouse", False, "functional")
                print("TestTotalItemsInWarehouse = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalItemsInWarehouse", False, "functional")
            print(f"TestTotalItemsInWarehouse = Failed | Exception: {e}")


if __name__ == '__main__':
    unittest.main()
