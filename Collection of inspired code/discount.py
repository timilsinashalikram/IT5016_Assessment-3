# Input the total cost of the purchase
purchase_amount = float(input("Please enter the purchase amount: "))

# Determine the discount amount
discount = purchase_amount * 0.2 if purchase_amount >= 100 else 0

# Calculate the total after applying the discount
total_after_discount = purchase_amount - discount

# Display the results
print("\nPurchase Amount: $", purchase_amount)
print("Discount Applied: $", discount)
print("Amount Payable: $", total_after_discount)
