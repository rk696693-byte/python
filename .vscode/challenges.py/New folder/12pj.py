customers = int(input("Enter number of customers: "))
for i in range(customers):
    print("\nCustomer", i + 1)
    items = int(input("Enter number of items: "))
    total = 0
    for j in range(items):
        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        total = total + price
    print("Total Bill =", total)
print("Report")
categories = ["Fruits", "Vegetables", "Snacks"]
for category in categories:
    print(category)
    for i in range(3):
        print(Item, i+1)