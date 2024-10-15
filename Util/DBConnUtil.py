import pyodbc

class DBConnUtil:
    __connection = None

    def getConnection():
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                    'Server=LAPTOP-9SK29CK2\SQLEXPRESS;'
                    'Database=TechShop_NEW;'
                    'Trusted_Connection=yes;')
            
            # print("DB Connected Successfully")
            return connection
        except Exception as error:
            print("ERROR:  {}".format(error))

o= DBConnUtil
o.getConnection()
