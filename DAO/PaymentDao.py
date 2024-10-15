from Util.DBConnUtil import DBConnUtil
import pyodbc

class PaymentProcessingSystem:

    def record_payment(self, order_id, payment_method, amount):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        INSERT INTO payments (OrderID, PaymentMethod, Amount)
                        VALUES (?, ?, ?)
                        """
            cursor.execute(sql_query, (order_id, payment_method, amount))
            connection.commit()

            print("Payment recorded successfully")
        except pyodbc.Error as e:
            print("Error recording payment:", e)
            connection.rollback()  
        finally:
            connection.close()

    def validate_payment(self, order_id, payment_method, amount):
        valid_payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']
        
        if order_id not in self.orders:
            return f"Order ID {order_id} not found."

        if payment_method not in valid_payment_methods:
            return f"Invalid payment method: {payment_method}. Please use one of {valid_payment_methods}."

        total_order_amount = self.orders[order_id]
        if amount < total_order_amount:
            return f"Insufficient amount. The total amount for Order ID {order_id} is {total_order_amount}."

        return True  
