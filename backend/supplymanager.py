import pyodbc
import ast
from datetime import datetime, timedelta

class SupplyManager:
    def __init__(self, db_handler):
        self.dbh = db_handler
        self.dbh.connect()




    def update_product_stock(self, product_id, new_amount):
        self.dbh.update("products", {"availableAmount": new_amount}, {"ProductId": product_id})
        return {"success": True, "ProductId": product_id, "newAmount": new_amount}




    def adjust_product_stock(self, product_id, delta):
        # Get current amount
        self.dbh.cursor.execute("SELECT availableAmount FROM products WHERE ProductId = ?", product_id)
        row = self.dbh.cursor.fetchone()
        if not row:
            return {"error": "Product not found"}
        new_amount = row[0] + delta
        self.dbh.update("products", {"availableAmount": new_amount}, {"ProductId": product_id})
        return {"success": True, "ProductId": product_id, "delta": delta}




    def deduct_supplies(self, sales_data):

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
                    # Deduct from supplies.availableAmount using update()
                    self.dbh.cursor.execute("SELECT availableAmount FROM supplies WHERE supplyID = ?", supplyFK)
                    row = self.dbh.cursor.fetchone()
                    if not row:
                        continue
                    new_amount = row[0] - qty_per_unit * amount_sold
                    self.dbh.update("supplies", {"availableAmount": new_amount}, {"supplyID": supplyFK})
        print("[INFO] Supplies deducted from stock based on sales.")





    def get_supply_usage_for_period(self, supplyID, months=1):
        """Calculate total usage of a supply in the last N months."""
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
                product_id = self.dbh.cursor.execute(
                    "SELECT ProductId FROM products WHERE ProductName = ?", product
                ).fetchone()
                if not product_id:
                    continue
                product_id = product_id[0]
                qty_row = self.dbh.cursor.execute(
                    "SELECT qty FROM suppliesbyproduct WHERE productFK = ? AND supplyFK = ?",
                    product_id, supplyID
                ).fetchone()
                if qty_row:
                    total_used += qty_row[0] * amount
        return total_used




    def get_avg_monthly_usage(self, supplyID, months=1):
        """Get average monthly usage for a supply."""
        total_used = self.get_supply_usage_for_period(supplyID, months)
        return total_used / months




    def get_shopping_suggestion(self, supplyID, months=1):
        """Suggest purchase amount for a supply based on usage and current stock."""
        avg_monthly_used = self.get_avg_monthly_usage(supplyID, months)
        row = self.dbh.cursor.execute(
            "SELECT supplyName, availableAmount FROM supplies WHERE supplyID = ?", supplyID
        ).fetchone()
        if not row:
            return None
        supplyName, availableAmount = row
        suggested_purchase = max(0, avg_monthly_used - availableAmount)
        return {
            "supplyName": supplyName,
            "avg_monthly_used": avg_monthly_used,
            "availableAmount": availableAmount,
            "suggested_purchase": suggested_purchase
        }




    def usage_manager(self, months=1):
        """Aggregate shopping suggestions for all supplies."""
        supplies = self.dbh.cursor.execute("SELECT supplyID FROM supplies").fetchall()
        shopping_list = []
        for (supplyID,) in supplies:
            suggestion = self.get_shopping_suggestion(supplyID, months)
            if suggestion:
                shopping_list.append(suggestion)
        return shopping_list
    



    def stock_warning(self, threshold=10):

        query = "SELECT supplyName, availableAmount FROM supplies WHERE availableAmount <= ?"
        return self.dbh.cursor.execute(query, threshold).fetchall()




    def get_product_stock(self, product_id):
        self.dbh.cursor.execute("SELECT availableAmount FROM products WHERE ProductId = ?", product_id)
        row = self.dbh.cursor.fetchone()
        if row:
            return {"ProductId": product_id, "availableAmount": row[0]}
        else:
            return {"error": "Product not found"}
