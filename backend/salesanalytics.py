import ast
import datetime as dt
from collections import Counter
from database_handler import database_handler as DBHandler


class sales_analytics:

    def __init__(self):
        self.dbh = DBHandler()
        self.dbh.connect()
        self.sales_data = None
        self.counter = Counter()
        self.total_sales = 0




    def data_import(self, expression = "WHERE MONTH(dateSales) = MONTH(CURDATE()) AND YEAR(dateSales) = YEAR(CURDATE())"):

        if expression == "*":
            self.sales_data = self.dbh.read("sales", "*")
        else:
            self.sales_data = self.dbh.read("sales", "*", expression)

        if not self.sales_data:
            print("[ERRO] Nenhum dado retornado de vendas.")
            return {
                "success": False,
                "message": "Couldnt retrieve sales data.",
                "data": None
                }
        
        else:
            return {
                "success": True,
                "message": "Full unprocessed data sales",
                "data": self.sales_data
                }
        


    
    def sales_list(self, exp):
        self.data_import(exp)

        if not self.sales_data:
            return {
                "success": False,
                "message": "No sales data available.",
                "data": None
            }

        sales_list = []
        for item in self.sales_data:
            date = item[1] if isinstance(item[1], str) else item[1].strftime("%Y-%m-%d")
            try:
                sold_products = ast.literal_eval(item[2])
            except Exception as e:
                print(f"[ERRO] Falha ao interpretar salesData: {e}")
                sold_products = {}
            sales = [[prod, amt] for prod, amt in sold_products.items()]
            sales_list.append({
                "date": date,
                "sales": sales
            })

        return {
            "success": True,
            "message": "Sales list retrieved successfully.",
            "data": sales_list
        }
        

        

    def maxmin(self):

        if not self.sales_data:
            return {
                "success": False,
                "message": "No sales data available.",
                "data": None
            }
        # Count total amount sold per product across all days
        counter = Counter()
        for item in self.sales_data:
            # item[2] is the salesData column (stringified dict)
            sales_data_str = item[2]
            try:
                sold_products = ast.literal_eval(sales_data_str)
            except Exception as e:
                print(f"[ERRO] Falha ao interpretar salesData: {e}")
                sold_products = {}
            for product, amount_sold in sold_products.items():
                counter[product] += amount_sold
        if not counter:
            return {
                "success": False,
                "message": "No sales to analyze.",
                "data": None
            }
        most_common = counter.most_common(1)[0]
        less_common = counter.most_common()[-1]
        print(f"Produto mais vendido: {most_common[0]}, com {most_common[1]} unidades vendidas.")
        print(f"Produto menos vendido: {less_common[0]}, com {less_common[1]} unidades vendidas.")
        return {
            "success": True,
            "message": "Lists: [Product, Amount Sold]",
            "data": {
                "most_common": most_common,
                "less_common": less_common
            }
        }




    def total_sales(self, exp):

        self.data_import(exp)
        self.total_sales = 0  # Reset before calculation
        if not self.sales_data:
            return {
                "success": False,
                "message": "No sales data available.",
                "data": 0
            }
        for item in self.sales_data:
            self.total_sales += item[3]

        return {
            "success": True,
            "message": "Cash in cents",
            "data": self.total_sales
            }
