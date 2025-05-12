def my_generator():
    test_data = [1, 2, 3, 4, 5]
    
    for num in test_data:
        if num % 2 == 0:
            yield num * num

for num in my_generator():
    print(num)
