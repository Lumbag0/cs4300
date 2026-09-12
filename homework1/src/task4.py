def calculate_discount(price: int | float, discount: int | float) -> float:
    discount_amount = (discount / 100) * price
    final_price = round((price - discount_amount),2)
    return final_price

def main():
    price = 5
    discount = 10
    print(f"${price} with an applied discount of {discount} is {calculate_discount(price, discount)}")

    price = 7.00
    discount = 10
    print(f"${price} with an applied discount of {discount} is {calculate_discount(price, discount)}")

    price = 10
    discount = 3.5
    print(f"${price} with an applied discount of {discount} is {calculate_discount(price, discount)}")

    price = 4.99
    discount = 20.5
    print(f"${price} with an applied discount of {discount} is {calculate_discount(price, discount)}")

if __name__ == "__main__":
    main()