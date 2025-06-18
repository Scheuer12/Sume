import pyodbc
from typing import Union, Tuple

class database_handler:

    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database: str
        self.valid_tabs = []
        self.valid_cols = []



    def connect(self):

        self.database = "financecontrol"

        self.connection_data = (
            "DRIVER=MySQL ODBC 9.3 ANSI Driver;"
            "SERVER=localhost;"
            f"DATABASE={self.database};"
            "UID=root;"
            "PWD=;"
            "OPTION=3;"
        )
        
        self.connection = pyodbc.connect(self.connection_data)
        self.cursor = self.connection.cursor()



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
            WHERE table_schema = ?
        """
        self.cursor.execute(query, self.database)
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
                    placeholders = ", ".join(["?"] * len(data))
                    query = (f"""
                    INSERT INTO {table} ({cols})
                    VALUES ({placeholders})
                    """)

                    self.cursor.execute(query, data)
                    self.connection.commit()
                    print("Dados adicionados com sucesso.")

                else:
                    print("Os dados de estrutura fornecidos são inválidos. Verifique os nomes de tabelas e colunas.")
                    return
            except Exception as e:
                print(f"Erro: {e}")




    def read(self, table, columns: Union[str, Tuple[str, ...]], expression = None):
        self.get_valid_tables()
        self.get_valid_columns(table)
        if table in self.valid_tabs and (
            columns == "*" or all(item in self.valid_cols for item in columns)
            ):
            try:
                if columns == "*":
                    cols = "*"
                else:
                    cols = ", ".join(columns)
                
                if expression:
                    query = f"SELECT {cols} FROM {table} {expression}"
                    self.cursor.execute(query)
                else:
                    query = f"SELECT {cols} FROM {table}"
                    self.cursor.execute(query)

                read_data = self.cursor.fetchall()
                return(read_data)

            except Exception as e:
                print(f"Erro: {e}")
                return

        else:
            print("Os dados de estrutura fornecidos são inválidos. Verifique os nomes de tabelas e colunas.")
            return
        
    


    def update(self, table, columns=[], values=[], expression=None):

        edit_query_list = []
        
        for i, col in enumerate(columns):
            edit_query_list.append(f"{col} = ?")

        edit_query = ", ".join(edit_query_list)
        query = f"UPDATE {table} SET {edit_query}"

        if expression:
            query += f" WHERE {expression}"

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("UPDATE executado com sucesso.")
        except Exception as e:
            print(f"[ERRO] Falha ao executar UPDATE: {e}")




    def update_generic(self, table, set_dict, where_dict):
        """
        Update rows in a table.
        set_dict: dict of columns to update {col: value}
        where_dict: dict of WHERE clause {col: value}
        """
        set_clause = ', '.join([f"{col} = ?" for col in set_dict.keys()])
        where_clause = ' AND '.join([f"{col} = ?" for col in where_dict.keys()])
        values = list(set_dict.values()) + list(where_dict.values())
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.cursor.execute(query, values)
        self.connection.commit()




    def delete(self, table, expression=None):
        try:
            if expression:
                query = f"DELETE FROM {table} WHERE {expression}"
            else:
                print("[AVISO] DELETE sem cláusula WHERE não é permitido por segurança.")
                return

            self.cursor.execute(query)
            self.connection.commit()
            print("DELETE executado com sucesso.")
            
        except Exception as e:
            print(f"[ERRO] Falha ao executar DELETE: {e}")
