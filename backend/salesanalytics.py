import ast
import datetime as dt
from collections import Counter
from database_handler import database_handler as DBHandler


class salesanalytics:

    def __init__(self):
        self.dbh = DBHandler()
        self.dbh.connect()
        self.sales_data = None
        self.counter = Counter()
        self.salesdict = ast.literal_eval(self.sales_data)
        self.total_sales = 0




    def data_import(self, expression = "WHERE MONTH(dateSales) = MONTH(CURDATE()) AND YEAR(dateSales) = YEAR(CURDATE())"):

        if expression == "*":
            self.sales_data = self.dbh.read("sales",  "*")
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
        

        

    def maxmin(self):

        #Most sold product
        for _, _, sales, _ in self.sales_data:
            self.counter.update(self.salesdict)

        most_common = self.counter.most_common(1)[0]
        print(f"Produto mais vendido: {most_common[0]}, com {most_common[1]} unidades vendidas.")

        #Irrelevant Product
        less_common = self.counter.most_common()[len(self.counter)-1]
        print(f"Produto menos vendido: {less_common[0]}, com {less_common[1]} unidades vendidas.")

        return {
            "success": True,
            "message": "Lists: [Item, Amount Sold]",
            "data": {
                "most_common": most_common,
                "less_common": less_common
            }
            }




    def totalsales(self, exp):

        self.data_import(exp)
        for item in self.sales_data:
            self.total_sales += item[3]

        return {
            "success": True,
            "message": "Cash in cents",
            "data": self.total_sales
            }
        