# Function to calculate the total cost of items in the cart
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item[1] * item[2]  # Price * Quantity
    return total

# Main program
if __name__ == "__main__":
    # Initialize an empty list to store items in the cart
    cart = []

    # Add items to the cart
    while True:
        item_name = input("Enter the name of the item (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        price = float(input("Enter the price of the item: "))
        quantity = int(input("Enter the quantity of the item: "))
        cart.append((item_name, price, quantity))

    # Calculate and print the total cost of items in the cart
    total_cost = calculate_total(cart)
    print(f"The total cost of items in the cart is: ${total_cost:.2f}")

    # Print the items in the cart
    print("Items in the cart:")
    for item in cart:
        print(f"Item: {item[0]}, Price: ${item[1]:.2f}, Quantity: {item[2]}")
