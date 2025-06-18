from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from salesanalytics import sales_analytics
from supplymanager import SupplyManager
from product_manager import get_all_products, add_product
from balance_manager import add_expense, get_expenses, get_balance_summary
from database_handler import database_handler
import ast

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dbh = database_handler()
dbh.connect()
sales = sales_analytics()
supply_manager = SupplyManager(dbh)

@app.get("/api/dashboard/summary")
def dashboard_summary():
    return sales.dashboard_summary()

@app.get("/api/transactions/recent")
def recent_transactions():
    return sales.recent_transactions()

@app.get("/api/products")
def api_get_products():
    return get_all_products()

@app.post("/api/products")
def api_add_product(product: dict):
    return add_product(product)

@app.post("/api/sales")
def api_insert_sale(sale: dict):
    return sales.insert_sale(sale, supply_manager)

@app.get("/api/supplies")
def api_get_supplies():
    return supply_manager.get_supplies()

@app.post("/api/supplies/update")
def api_update_supplies(updates: dict):
    return supply_manager.update_supplies(updates)

@app.post("/api/expenses")
def api_insert_expense(expense: dict):
    return add_expense(expense)

@app.get("/api/expenses")
def api_get_expenses():
    return get_expenses()

@app.get("/api/balance/summary")
def api_get_balance_summary():
    return get_balance_summary()

@app.get("/")
def root():
    return {"message": "Shaman API is running. See /docs for API documentation."}

@app.get("/api/supplies/usage/{supply_id}")
def api_get_supply_usage(supply_id: int, months: int = 1):
    return {"total_used": supply_manager.get_supply_usage_for_period(supply_id, months)}

@app.get("/api/supplies/avg-usage/{supply_id}")
def api_get_avg_monthly_usage(supply_id: int, months: int = 1):
    return {"avg_monthly_used": supply_manager.get_avg_monthly_usage(supply_id, months)}

@app.get("/api/supplies/shopping-suggestion/{supply_id}")
def api_get_shopping_suggestion(supply_id: int, months: int = 1):
    return supply_manager.get_shopping_suggestion(supply_id, months)

@app.get("/api/supplies/shopping-list")
def api_get_shopping_list(months: int = 1):
    return supply_manager.usage_manager(months)
