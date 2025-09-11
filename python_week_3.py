
def calculate_discount(price, discount_percent):
        if discount_percent >= 20:
            discount_amount = price * (discount_percent / 100)
            final_price = price - discount_amount
            return final_price
        else:
            return price

def main():
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)

        if final_price < original_price:
            print(f"Final price after a {discount_percentage}% discount: ${final_price:.2f}")
        else:
            print(f"Sorry, No discount applied. Original price: ${original_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount percentage.")

if __name__ == "__main__":
    main()