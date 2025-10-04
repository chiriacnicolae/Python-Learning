def apply_discount(price, discount=0.10):
    return price * (1 - discount)

final_price = apply_discount(100)
print(final_price)