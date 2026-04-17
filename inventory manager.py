
#Project 1 ->> Simple E-commerce Inventory Analyzer 

inventory = [
    {"id": 101, "name": "Wireless Mouse", "category": "Electronics", "price": 750, "stock_quantity": 12, "is_on_sale": True},
    {"id": 102, "name": "Python Handbook", "category": "Books", "price": 900, "stock_quantity": 5, "is_on_sale": False},
    {"id": 103, "name": "Coffee Mug", "category": "Kitchenware", "price": 400, "stock_quantity": 25, "is_on_sale": True},
    {"id": 104, "name": "Bluetooth Speaker", "category": "Electronics", "price": 2500, "stock_quantity": 8, "is_on_sale": False},
    {"id": 105, "name": "Data Science Intro", "category": "Books", "price": 1100, "stock_quantity": 3, "is_on_sale": True}
]

print('=' * 40)
print(f"{'-----Inventory Analysis Report------':^40}")
print('=' * 40)

#Section 1 Total Inventory Value
 
total_value = 0
lis1=[]
for i in inventory:
    item_value= i["price"] * i ["stock_quantity"]
    total_value +=item_value
print('\n Total inventory Value:',total_value)

#Section 2 Low Stock Product

low_stock_products=[]
for product in inventory:
    if product["stock_quantity"]<10:
        low_stock_products.append(product["name"])
print("\n Stock Products:",low_stock_products)

#Section 3 Electonics Category

electronic_p =[]
for product in inventory:
    if product["category"] == "Electronics":
        electronic_p.append(product["name"])
print("\n Products in Electronics Category:",electronic_p)

#Section 4 On Sale Items

on_sale_items = [item["name"] for item in inventory if item["is_on_sale"]]
print("\n On sale Items:", on_sale_items)
print('\n')

print('=' * 40)
print(f"{'-----------End of Report----------' :^40}")
print('=' *40)