print("***** Python Foundation Lab Started *****")

product = "Laptop"
quantity = 5
unitPrice = 1650.00
inStock = True

print("***** Variables Values *****")
print("Product Name:", product)
print("Quantity:", quantity)
print("Unit Price:", unitPrice)
print("In Stock:", inStock)

print("***** Variables Types *****")
print("Product Name Type:", type(product))
print("Quantity Type:", type(quantity))
print("Unit Price Type:", type(unitPrice))
print("In Stock Type:", type(inStock))

totalSales = quantity * unitPrice
print("***** Sales Calculations *****")
print("Product Name:", product)
print("Quantity:", quantity)
print("Unit Price:", unitPrice)
print("Total Sales Amount:", totalSales)

if totalSales >= 2000:
    print("Sales target achieved.")
else:
    print("Sales target not achieved. Keep trying!")

sales = [1200, 850, 2400, 1750, 3200]
print("****** Processing Multiple Sales ******")
for sale in sales:
    if sale >= 2000:
        print(f"Sale amount {sale} - Target achieved!")
    else:
        print(f"Sale amount {sale} - Target not achieved. Keep trying!")