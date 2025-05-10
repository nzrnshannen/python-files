student = {
    "name": "Shannen",
    "age": 22,
    "grade": 3
}

for value in student.values():
    print(value, end = " ")

print()

for key, value in student.items():
    print(f"{key}: {value}")
    
car = {
    "brand": "Toyota",
    "year": 2020
}

car.update({"color": "red"})
print(car)