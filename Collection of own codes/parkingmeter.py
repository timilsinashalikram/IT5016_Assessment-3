
print("Kia Ora, this is a parking meter")

# Set the initial parking time to 4 hours
park_time = 4
print("park_time is", park_time, "hours.")

# Set the parking rate (cost per hour)
rate = 4

# Initialize the total cost
cost = 0

# Check if the parking time is greater than 3 hours
if park_time > 3:
# Calculate the cost for the first 3 hours
    cost = rate * 3
# Decrease the rate by $2 for additional hours
    rate -= 2
# Calculate the remaining parking time
    park_time -= 3
 # Add the cost for the remaining time
    cost += rate * park_time
    print("The cost of parking is $", cost)
else:
# Calculate the cost directly for 3 hours or less
    cost = rate * park_time
    print("The cost of parking is $", cost)
