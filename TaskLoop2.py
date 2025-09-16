# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
# Loop through each item in the inventory
for product, detail in inventory.items():
    #print(f"Product: {product}")
    #print(f"  Stock: {detail}")
    if(detail[0] < 30):
        print(f"{product} need restocking.")
    elif detail[0] > 100:
        print(f"{product} should be sold at the discounted price of {detail[2]}.")
    else:
        print(f"{product} should be sold at the regular price of {detail[1]}.")