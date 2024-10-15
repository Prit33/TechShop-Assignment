import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from DAO.CustomerDao import CustomerDao
from DAO.InventoryDao import InventoryDao
from DAO.OrderDao import OrderDao
from DAO.OrderDetailsDao import OrderDetailsDao
from DAO.ProductDao import ProductDao


def main():
    customer_obj = CustomerDao()
    product_obj = ProductDao()
    order_obj = OrderDao()
    orderdetails_obj = OrderDetailsDao()
    inventory_obj = InventoryDao()
    print("\n--------Welcome------------")
    while True:
        print(
            "\n1. Customers\n2. Products\n3. Orders\n4. OrderDetails\n5. Inventory\n6. Exit\n"
        )
        choice = input("Enter your choice: ")
                                        
        if choice == "1":
            while True:
                print(
                    "\n1. Insert Customer\n2. Delete Customer\n3. Calculate Total Orders\n4. Get Customer Details\n5. Update Customer Info\n6. Exit\n"
                )
                choice_customer = input("Enter your choice: ")
                if choice_customer == "1":
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    email = input("Enter Email: ")
                    phone = input("Enter Phone: ")
                    address = input("Enter Address: ")
                    print("\n")
                    customer_obj.insertCustomer(first_name, last_name, email, phone, address)
                elif choice_customer == "2":
                    customer_id = input("Enter Customer ID to delete: ")
                    print("\n")
                    customer_obj.deleteCustomer(customer_id)
                elif choice_customer == "3":
                    customer_id = input("Enter Customer ID: ")
                    print("\n")
                    customer_obj.calculateTotalOrders(customer_id)
                elif choice_customer == "4":
                    customer_id = input("Enter Customer ID: ")
                    print("\n")
                    customer_obj.getCustomerDetails(customer_id)
                elif choice_customer == "5":
                    customer_id = input("Enter Customer ID: ")
                    email = input("Enter New Email: ")
                    phone = input("Enter New Phone: ")
                    address = input("Enter New Address: ")
                    print("\n")
                    customer_obj.updateCustomerInfo(customer_id, email, phone, address)
                elif choice_customer == '6':
                    print("\n")
                    print("Exiting the Customer!!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                print(
                    "\n1. Get Product Details\n2. Insert Product\n3. Update Product Info\n4. Check Product Stock\n5. Exit\n"
                )
                choice_product = input("Enter your choice: ")
                if choice_product == "1":
                    product_id = input("Enter Product ID: ")
                    print("\n")
                    product_obj.get_product_details(product_id)
                elif choice_product == "2":
                    product_name = input("Enter Product Name: ")
                    description = input("Enter Product Description: ")
                    price = input("Enter Product Price: ")
                    print("\n")
                    product_obj.insert_product(product_name, description, price)
                elif choice_product == "3":
                    product_id = input("Enter Product ID: ")
                    price = input("Enter New Price: ")
                    description = input("Enter New Description: ")
                    print("\n")
                    product_obj.update_product_info(product_id, price, description)
                elif choice_product == "4":
                    product_id = input("Enter Product ID: ")
                    print("\n")
                    product_obj.is_product_in_stock(product_id)
                elif choice_product == '5':
                    print("\n")
                    print("Exiting the Product!!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                print(
                    "\n1. Insert Order\n2. Update Order Status\n3. Cancel Order\n4. Calculate total amount\n5. Get order details\n6. Exit\n"
                )
                choice_order = input("Enter your choice: ")
                if choice_order == "1":
                    customer_id = input("Enter Customer ID: ")
                    total_amount = input("Enter Total Amount: ")
                    print("\n")
                    order_obj.insert_order(customer_id, total_amount)
                elif choice_order == "2":
                    order_id = input("Enter Order ID: ")
                    new_status = input("Enter New Status: ")
                    print("\n")
                    order_obj.update_order_status(order_id, new_status)
                elif choice_order == "3":
                    order_id = input("Enter Order ID: ")
                    print("\n")
                    order_obj.cancel_order(order_id)
                elif choice_order == "4":
                    order_id = input("Enter Order ID: ")
                    print("\n")
                    order_obj.calculate_total_amount(order_id)
                elif choice_order == "5":
                    order_id = input("Enter Order ID: ")
                    print("\n")
                    order_obj.get_order_details(order_id)
                elif choice_order == '6':
                    print("\n")
                    print("Exiting the Order!!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                print(
                    "1. Calculate SubTotal\n"
                    + "2. Get Order Details\n"
                    + "3. Update Quantity\n"
                    + "4. Add Discount\n5. Exit"
                )
                choice_order_detail = input("Enter your choice: ")
                if choice_order_detail == "1":
                    order_detail_id = input("Enter Order Detail ID: ")
                    print("\n")
                    orderdetails_obj.calculate_subtotal(order_detail_id)
                elif choice_order_detail == "2":
                    order_detail_id = input("Enter Order Detail ID: ")
                    print("\n")
                    orderdetails_obj.get_order_detail_info(order_detail_id)
                elif choice_order_detail == "3":
                    order_detail_id = input("Enter Order Detail ID: ")
                    new_quantity = int(input("Enter new quantity: "))
                    print("\n")
                    orderdetails_obj.update_quantity(order_detail_id, new_quantity)
                elif choice_order_detail == "4":
                    try:
                        order_detail_id = input("Enter Order Detail ID: ")
                        totalAfterDiscount = int(input("Enter Discount Percentage: "))
                        print("\n")
                        orderdetails_obj.add_discount(order_detail_id, totalAfterDiscount)
                    except ValueError:
                        print("Invalid input. Discount must be number.")
                elif choice_order_detail == '5':
                    print("\n")
                    print("Exiting the Order details!!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "5":
            while True:
                print("\n")
                print(
                    "1. Get Product\n"
                    + "2. Get Quantity in Stock\n"
                    + "3. Add To Inventory\n"
                    + "4. Remove From Inventory\n"
                    + "5. Update Stock Quantity\n"
                    + "6. Product Available\n"
                    + "7. Get Inventory Value\n"
                    + "8. List Low Stock Products\n"
                    + "9. List Out Of Stock Products\n"
                    + "10. List All Products\n11. Exit\n"
                )
                choice_inventory = input("Enter your choice: ")
                if choice_inventory == "1":
                    inventory_id = int(input("Enter the inventory id: "))
                    product = inventory_obj.get_product(inventory_id)
                    print("\n")
                    print(product)
                elif choice_inventory == "2":
                    inventory_id = int(input("Enter the inventory id: "))
                    print("\n")
                    print("Quantity in Stock: ",inventory_obj.get_quantity_in_stock(inventory_id))
                elif choice_inventory == "3":
                    product_id = int(input("Enter the product id: "))
                    quantity_in_stock = int(input("Enter the quantity in stock: "))
                    last_stock_update = input("Enter the last stock update: ")
                    print("\n")
                    inventory_obj.insert_inventory(
                        product_id, quantity_in_stock, last_stock_update
                    )
                elif choice_inventory == "4":
                    inventory_id = int(input("Enter the inventory id: "))
                    quantity = int(input("Enter the quantity: "))
                    print("\n")
                    inventory_obj.remove_from_inventory(quantity, inventory_id)
                elif choice_inventory == "5":
                    inventory_id = int(input("Enter the inventory id: "))
                    new_quantity = int(input("Enter the new quantity: "))
                    print("\n")
                    inventory_obj.update_stock_quantity(inventory_id, new_quantity)
                elif choice_inventory == "6":
                    inventory_id = input("Enter Inventory ID: ")
                    quantity_to_check = int(input("Enter Quantity to Check: "))
                    print("\n")
                    if inventory_obj.is_product_available(inventory_id, quantity_to_check):
                        print("Product is available in inventory.")
                    else:
                        print("Product is not available in inventory.")
                elif choice_inventory == "7":
                    inventory_id = input("Enter Inventory ID: ")
                    print("\n")
                    print("Inventory value:",inventory_obj.get_inventory_value(inventory_id))
                elif choice_inventory == "8":
                    threshold = int(input("Enter the threshold for low stock: "))
                    print("\n")
                    inventory_obj.list_low_stock_products(threshold)
                elif choice_inventory == "9":
                    print("\n")
                    inventory_obj.list_out_of_stock_products()
                elif choice_inventory == "10":
                    print("\n")
                    inventory_obj.list_all_products()
                elif choice_inventory == '11':
                    print("\n")
                    print("Exiting from Inventory!!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '6':
            print("\n")
            print("Exiting from the system, Thank you !")
            break
        else:
            print("\n")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
