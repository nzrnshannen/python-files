# Generate a list and tuple with comma-separated numbers
# exampl: 6,5,7,8
numbers = input("Please input series of numbers: ")

# .split(delimiter)
list = numbers.split(",")

# tuple() -> convert list to tuple
tuple = tuple(list)

print("Original string = ", numbers)
print("List = ", list)
print("Tuple = ", tuple)