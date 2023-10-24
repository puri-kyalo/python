# Data type

number = 100 #int
second = 56.78 #float
text = "Hello there" #string
ispythonintresting = True #boolean

# storing Multiple values in a variable
#types of data types
cars = ["toyota", "nissan", "benz"] #list in python and its order can be changed
fruits = ("banana", "oranges", "apple") # Tuple ,the order is unchangable
countries = {"Kenya", "Uganda", "Tanzania", "DRC"} # a set in python, is unorderd and unchangable
details = {
     "firstname" : "Purity",
     "age" : 20,
"course" : "web developer",
"nationality" : "Kenyan"
 } # Dictionary, it stores element in form of a key and value
print(details["firstname"])
print(details)
print(details["age"])
print(second)
print(text)
print(cars)
print(countries)
print(ispythonintresting)


# determine data type
print(type(text))
print(type(countries))
print(type(details))

 # Typecasting - conveting one data type to another
print(float(number))
print(int(second))
