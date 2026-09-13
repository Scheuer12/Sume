import sys
import types
import unittest


sys.modules.setdefault("pyodbc", types.SimpleNamespace())

from backend.database_handler import database_handler


class RecordingCursor:
    def __init__(self):
        self.calls = []

    def execute(self, query, data):
        self.calls.append((query, data))


class RecordingConnection:
    def __init__(self):
        self.commits = 0

    def commit(self):
        self.commits += 1


class TestDatabaseHandlerInsert(unittest.TestCase):
    def test_insert_validates_columns_and_commits(self):
        handler = database_handler()
        handler.cursor = RecordingCursor()
        handler.connection = RecordingConnection()
        handler.get_valid_tables = lambda: setattr(handler, "valid_tabs", ["sales"])
        handler.get_valid_columns = lambda table: setattr(
            handler, "valid_cols", ["dateSales", "totalSales"]
        )

        handler.insert(
            "sales",
            ("dateSales", "totalSales"),
            ("2026-09-12", 4200),
        )

        query, data = handler.cursor.calls[0]
        self.assertIn("INSERT INTO sales (dateSales, totalSales)", query)
        self.assertEqual(data, ("2026-09-12", 4200))
        self.assertEqual(handler.connection.commits, 1)

    def test_insert_rejects_invalid_table_before_loading_columns(self):
        handler = database_handler()
        handler.cursor = RecordingCursor()
        handler.connection = RecordingConnection()
        handler.get_valid_tables = lambda: setattr(handler, "valid_tabs", ["sales"])

        def fail_if_called(table):
            self.fail(f"Column lookup should not run for invalid table: {table}")

        handler.get_valid_columns = fail_if_called

        handler.insert(
            "invalid_table",
            ("dateSales", "totalSales"),
            ("2026-09-13", 4200),
        )

        self.assertEqual(handler.cursor.calls, [])
        self.assertEqual(handler.connection.commits, 0)


if __name__ == "__main__":
    unittest.main()
