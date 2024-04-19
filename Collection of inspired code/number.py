# Input a number
num = int(input("Enter a number: "))

# Initialize variables
is_prime = True
i = 2  

# Check if the number is prime using a while loop
while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1

# Output the result
if is_prime and num > 1:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
