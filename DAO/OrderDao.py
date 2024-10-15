from Model.Order import Order
from Exception.exceptions import InvalidDataException
from Util.DBConnUtil import DBConnUtil
import pyodbc

class OrderDao():

    def insert_order(self, customer_id, total_amount=0):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            new_order = Order(None, customer_id, total_amount)
            sql_query = "INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?)"
            cursor.execute(sql_query, (new_order.customer, new_order.order_date, new_order.total_amount))
            connection.commit()
            print("Order inserted successfully.")

        except Exception as e:
            print("Error inserting order:", e)
        finally:
            connection.close()

    def get_order_details(self, order_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()

            sql_query = """
                        SELECT Products.ProductName, OrderDetails.Quantity, Orders.Status
                        FROM OrderDetails
                        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
                        WHERE OrderDetails.OrderID = ?
                        """
            cursor.execute(sql_query, (order_id,))
            order_details = cursor.fetchall()

            if order_details:
                print("Order Details for Order ID:", order_id)
                for product_name, quantity, status in order_details:
                    print(f"Product: {product_name}, Quantity: {quantity}, Status: {status}")
            else:
                print("No details found for Order ID:", order_id)
        except Exception as e:
            print("Error getting order details:", e)
        finally:
            connection.close()

    def update_order_status(self, order_id, new_status):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = "UPDATE Orders SET Status = ? WHERE OrderID = ?"
            cursor.execute(sql_query, (new_status, order_id))
            connection.commit()
            print("Order status updated successfully.")
        except Exception as e:
            print("Error updating order status:", e)
        finally:
            connection.close()

    def cancel_order(self, order_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = "UPDATE Orders SET Status = 'Cancelled' WHERE OrderID = ?"
            cursor.execute(sql_query, (order_id,))
            connection.commit()
            print("Order cancelled successfully !")
        except Exception as e:
            print("Error cancelling order:", e)
        finally:
            connection.close()

    def calculate_total_amount(self, order_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()

            sql_query = """
                        SELECT SUM(Products.Price * OrderDetails.Quantity) AS TotalAmount
                        FROM OrderDetails
                        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        WHERE OrderDetails.OrderID = ?
                        """
            cursor.execute(sql_query, (order_id,))
            total_amount = cursor.fetchone()[0]

            update_query = "UPDATE Orders SET TotalAmount = ? WHERE OrderID = ?"
            cursor.execute(update_query, (total_amount, order_id))
            
            connection.commit() 

            print("Total Amount calculated and updated successfully.")
        except Exception as e:
            connection.rollback()
            print("Error calculating total amount:", e)
        finally:
            connection.close()

    def fetch_sales_data(self, start_date, end_date):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT o.OrderID, o.OrderDate, o.TotalAmount, od.ProductID, od.Quantity
                        FROM Orders o
                        INNER JOIN OrderDetails od ON o.OrderID = od.OrderID
                        WHERE o.OrderDate BETWEEN ? AND ?
                        """
            cursor.execute(sql_query, (start_date, end_date))
            sales_data = cursor.fetchall()

            # Fetching column names
            column_names = [i[0] for i in cursor.description]

            print("\t".join(column_names))

            # Printin data with column names
            for row in sales_data:
                print("\t".join(str(val) for val in row))

        except Exception as e:
            print("Error fetching sales data:", e)
        finally:
            connection.close()
