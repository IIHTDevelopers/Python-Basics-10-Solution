
import unittest
import sys
import os


# Adjusting the path to import TestUtils and the required modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from SchoolFeeManagementSystem import *
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
        self.min_passengers = 20
        self.expected_revenue = 600
        self.expected_validation = True
        self.expected_total_revenue = 2925

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
            result = get_fees("Emma")
            expected_result = 4000
            if result == expected_result:
                self.test_obj.yakshaAssert("TestGetFees", True, "functional")
                print("TestGetFees = Passed")
            else:
                self.test_obj.yakshaAssert("TestGetFees", False, "functional")
                print("TestGetFees = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestGetFees", False, "functional")
            print(f"TestGetFees = Failed")

    def test_is_total_fee_paid(self):
        """
        Test case for is_total_fee_paid() function.
        """
        try:
            result = is_total_fee_paid("Charlie")
           
            self.test_obj.yakshaAssert("TestIsTotalFeePaid", result, "functional")
            if result:   
                print("TestIsTotalFeePaid = Passed")
            else:
                print("TestIsTotalFeePaid = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestIsTotalFeePaid", False, "functional")
            print(f"TestIsTotalFeePaid = Failed")

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
            print(f"TestCalculateTripRevenue = Failed" )

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
            print(f"TestValidateTrip = Failed ")

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
            print(f"TestTotalTransportRevenue = Failed ")

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
            print(f"TestMostExpensiveItem = Failed ")

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
            print(f"TestTotalItemsInWarehouse = Failed")


if __name__ == '__main__':
    unittest.main()
