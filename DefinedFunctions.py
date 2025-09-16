# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
def calculate_revenue(prices, quantities_sold):
    revenu_list = []
    for index in range(len(prices)):
        revenu_list.append(prices[index] * quantities_sold[index])
    return revenu_list

def formatted_output(revenues):
    sorted_revenues = sorted(revenues)
    for index_revenue in range(len(revenues)):
        product_name = revenues[index_revenue][0]
        revenue = revenues[index_revenue][1]
        print(f"{product_name} has total revenue of ${revenue}")

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)
