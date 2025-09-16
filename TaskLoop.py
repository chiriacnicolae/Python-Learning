# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

# Set the stock threshold for applying discounts
discount_threshold = 100
for item in inventory:
    print(f"Processing {item}...")
    current_stock = inventory[item][0]
    min_stock = inventory[item][1]
    restock_qty = inventory[item][2]
    on_sale = inventory[item][3]
    # Check if the current stock is below the minimum required stock
    while current_stock < min_stock:
        current_stock += restock_qty
    # Apply discount if stock exceeds the threshold
    if current_stock > discount_threshold and not on_sale:
        on_sale = True
        print(f"{item} stock has exceeded {discount_threshold} units. Discount applied.")
    elif on_sale == True:
        print(f"{item} is already discounted.")

    inventory[item][0] = current_stock
    inventory[item][3] = on_sale
print("\nFinal inventory Report")
for item in inventory:
    print(f"{item}: {inventory[item][0]} units (Min: {inventory[item][1]} units) - On sale: {inventory[item][3]}")



