# Balance management functions (incomes, expenses, cash flow)
from database_handler import database_handler

dbh = database_handler()
dbh.connect()



def add_expense(expense):
    dbh.cursor.execute(
        "INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)",
        expense["date"], expense["description"], expense["amount"]
    )
    dbh.connection.commit()
    return {"success": True}




def get_expenses():
    dbh.cursor.execute("SELECT date, description, amount FROM expenses")
    return [
        {"date": row[0], "description": row[1], "amount": row[2]} for row in dbh.cursor.fetchall()
    ]




def get_balance_summary():
    dbh.cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = dbh.cursor.fetchone()[0] or 0
    # Add similar logic for incomes if you have an incomes table
    return {"total_expenses": total_expenses}
