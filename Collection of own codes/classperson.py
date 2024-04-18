class Person:
    def __init__(self, name, age):
        # Initialize a Person object with a name and age
        self.name = name
        self.age = age

# Create an instance of Person
person1 = Person("Alice", 30)

# Print the person's name and age
print(f"{person1.name} is {person1.age} years old.")
