import pyodbc
from Util.DBConnUtil import DBConnUtil

class BaseDB:
    def __init__(self):
        self.db_connector = DBConnUtil()
        self.connection = self.db_connector.getConnection()
        self.cursor = self.connection.cursor()

    def execute_query(self, sql_query, params=None):
        try:
            self.__init__()
            if params:
                self.cursor.execute(sql_query, params)
            else:
                self.cursor.execute(sql_query)

            query_type = sql_query.strip().split()[0].upper()

            if query_type == 'SELECT':
                rows = self.cursor.fetchall()
                return rows
            else:
                return True  

        except pyodbc.Error as err:
            print("Error executing query: ", err)
            return None  

        finally:
            self.connection.commit()
