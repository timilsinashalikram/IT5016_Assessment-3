# Initialize boolean variables
is_driver_licensed = False
is_driver_insured = True
is_fuel_in_tank = True  

# Print a message indicating the purpose of the program
print("This program determines whether you can have a car or a driver.\n")

# Evaluate the expression
result = is_fuel_in_tank or is_driver_licensed and is_driver_insured

# Test case assertion 1: result should be True
print("Program output is", result, "\n")

# Remove all the fuel (set is_fuel_in_tank to False)
is_fuel_in_tank = False

# Re-evaluate the expression with updated value of is_fuel_in_tank
result = is_fuel_in_tank or is_driver_licensed and is_driver_insured

# Test case assertion 2: result should be False
print("Program output is now", result, "\n")
