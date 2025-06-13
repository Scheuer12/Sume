# Example usage for SupplyManager
# This file demonstrates how to use the SupplyManager class

from database_handler import database_handler
from supplymanager import SupplyManager
import ast

if __name__ == "__main__":
    dbh = database_handler()
    manager = SupplyManager(dbh)

    # Example: Deduct supplies from a new sales list (simulate new sales)
    new_sales = [
        {"date": "2025-06-13", "sales": [["Pão Francês", 10], ["Bolo Chocolate", 2]]},
        {"date": "2025-06-13", "sales": [["Coxinha", 5]]}
    ]
    manager.deduct_supplies_from_sales(new_sales)

    # Example: Project shopping list for next month
    shopping_list = manager.project_shopping_list(months=1)
    print("\nShopping List for Next Month:")
    for item in shopping_list:
        print(item)

    # Example: Get low stock supplies
    low_stock = manager.get_low_stock_supplies(threshold=10)
    print("\nLow Stock Supplies:")
    for name, amount in low_stock:
        print(f"{name}: {amount}")
