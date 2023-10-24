class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Assign the 'name' argument to the 'name' attribute
        self.age = age    # Assign the 'age' argument to the 'age' attribute
        self.gender = gender  # Assign the 'gender' argument to the 'gender' attribute

    def details(self):
        print(self.name, "is studying")

# Create an instance of the Person class
p = Person(name="Joe", age=34, gender="male")

# Call the 'details' method on the 'p' object
p.details()