import pyodbc

class connection:

    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database: str
        self.valid_tabs = []
        self.valid_cols = []



    def connect(self):

        self.database = "FinanceControl"

        self.connection_data = (
            f"DRIVER=MySQL ODBC 9.3 ANSI Driver;"
            "SERVER=localhost;"
            "DATABASE={self.database};"
            "UID=root;"
            "PWD=;"
            "OPTION=3;"
        )
        
        self.connection = pyodbc.connect(self.connection_data)
        self.cursor = connection.cursor()



    def close(self):
        self.cursor.close()
        self.connection.close()



    
    def get_valid_columns(self, table_name):
        self.cursor.execute(f"DESCRIBE {table_name}")
        result = self.cursor.fetchall()
        self.valid_cols = [line[0] for line in result]
    


    
    def get_valid_tables(self):
        query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = %s
        """
        self.cursor.execute(query, (self.database,))
        result = self.cursor.fetchall()
        self.valid_tabs = [line[0] for line in result]
    


    
    def insert(self, table, columns: tuple, data: tuple):
        if len(columns) != len(data):
            print("Please check data x column count and try again.")
        else:
            self.get_valid_tables()
            self.get_valid_columns(self, table)

            try:           
                if table in self.valid_tabs and all(item in self.valid_cols for item in columns):

                    cols = ", ".join(columns)
                    placeholders = ", ".join(["%s"] * len(columns))
                    query = (f"""
                    INSERT INTO {table} ({cols}) 
                    VALUES ({placeholders})
                    """)

                    self.cursor.execute(query, data)
                    self.connection.commit()

                else:
                    print("Os dados de estrutura fornecidos são inválidos. Verifique os nomes de tabelas e colunas.")
                    return
            except Exception as e:
                print(f"Erro: {e}")