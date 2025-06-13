import pyodbc
import ast
from datetime import datetime, timedelta

class SupplyManager:
    def __init__(self, db_handler):
        self.dbh = db_handler
        self.dbh.connect()

    def deduct_supplies_from_sales(self, sales_data):
        """
        Deducts supplies from stock based on new sales data.
        sales_data: list of dicts, each with {"date": ..., "sales": [[product, amount], ...]}
        """
        for sale in sales_data:
            for product_name, amount_sold in sale["sales"]:
                # Get product ID
                product_query = "SELECT ProductId FROM products WHERE ProductName = ?"
                product_id = self.dbh.cursor.execute(product_query, product_name).fetchone()
                if not product_id:
                    print(f"[WARN] Product '{product_name}' not found in DB.")
                    continue
                product_id = product_id[0]
                # Get supplies and qty per product
                supplies_query = "SELECT supplyFK, qty FROM suppliesbyproduct WHERE productFK = ?"
                for supplyFK, qty_per_unit in self.dbh.cursor.execute(supplies_query, product_id):
                    # Deduct from supplies.availableAmount
                    update_query = "UPDATE supplies SET availableAmount = availableAmount - ? WHERE supplyID = ?"
                    total_deduct = qty_per_unit * amount_sold
                    self.dbh.cursor.execute(update_query, total_deduct, supplyFK)
        self.dbh.connection.commit()
        print("[INFO] Supplies deducted from stock based on sales.")

    def project_shopping_list(self, months=1):
        """
        Projects a shopping list for the next period (default: month) based on average past usage.
        Returns a list of dicts: [{supplyName, avg_monthly_used, availableAmount, suggested_purchase}]
        """
        # Get all supplies
        supplies = self.dbh.cursor.execute("SELECT supplyID, supplyName, availableAmount FROM supplies").fetchall()
        shopping_list = []
        for supplyID, supplyName, availableAmount in supplies:
            # Calculate average monthly usage from sales and suppliesbyproduct
            # Get all sales in the last N months
            since = (datetime.now() - timedelta(days=30*months)).strftime('%Y-%m-%d')
            sales = self.dbh.cursor.execute(
                "SELECT salesData FROM sales WHERE dateSales >= ?", since
            ).fetchall()
            total_used = 0
            for (salesData_str,) in sales:
                try:
                    sales_dict = ast.literal_eval(salesData_str)
                except Exception:
                    continue
                for product, amount in sales_dict.items():
                    # For each product, get how much of this supply is used
                    product_id = self.dbh.cursor.execute(
                        "SELECT ProductId FROM products WHERE ProductName = ?", product
                    ).fetchone()
                    if not product_id:
                        continue
                    product_id = product_id[0]
                    # Get qty of this supply per product
                    qty_row = self.dbh.cursor.execute(
                        "SELECT qty FROM suppliesbyproduct WHERE productFK = ? AND supplyFK = ?",
                        product_id, supplyID
                    ).fetchone()
                    if qty_row:
                        total_used += qty_row[0] * amount
            avg_monthly_used = total_used / months
            suggested_purchase = max(0, avg_monthly_used - availableAmount)
            shopping_list.append({
                "supplyName": supplyName,
                "avg_monthly_used": avg_monthly_used,
                "availableAmount": availableAmount,
                "suggested_purchase": suggested_purchase
            })
        return shopping_list

    def get_low_stock_supplies(self, threshold=10):
        """
        Returns a list of supplies where availableAmount <= threshold.
        """
        query = "SELECT supplyName, availableAmount FROM supplies WHERE availableAmount <= ?"
        return self.dbh.cursor.execute(query, threshold).fetchall()
