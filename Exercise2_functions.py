def calculate_sales(quantity, unitPrice):
    return quantity * unitPrice 

result = calculate_sales(5, 1650.00)
print("***** Sales Calculation using Function *****")
print("Total Sales Amount:", result)

print("****** Reusing Function with Different Values ******")
print("Total Sales for 5 units at $1500.75 each:", calculate_sales(5, 1500.75))
print("Total Sales for 2 units at $800.00 each:", calculate_sales(2, 800.00))
print("Total Sales for 10 units at $250.25 each:", calculate_sales(10, 250.25))

print("")
print("****** Data Type Check and Conversion ******")
quantity = "5" # string variable
print("Original quantity (string):", quantity)
quantity = int(quantity) # convert string to integer
print("Converted quantity (int):", quantity)
print("Total Sales after conversion:", calculate_sales(quantity, 500))

sales = [1200, 850, 2400, 1750, 3200]
print("")
print("****** Store multiple values in a  list")
print("Sales:", sales)
print("First sale:", sales[0]) #indexing
print("Number of sales:", len(sales))

order = {
    "OrderID": "ORD001", # key and value pair
    "Product": "Laptop",
    "Quantity": 2,
    "UnitPrice": 850
}
 
total = calculate_sales(order["Quantity"], order["UnitPrice"])
print("")
print("****** Create and Process a Dictionary ******")
print("Product:", order["Product"])
print("Total Sales:", total)