import ast
from collections import Counter
from database_handler import database_handler as DBHandler

dbh = DBHandler()

dbh.connect()
dbh.get_valid_tables()

sales_data = dbh.read("sales",  "*")

counter = Counter()

for _, _, sales in sales_data:
    astdict = ast.literal_eval(sales)
    counter.update(astdict)

most_common = counter.most_common(1)[0]
print(f"Produto mais vendido: {most_common[0]}, com {most_common[1]} unidades vendidas.")