def sum_string(input_str):
    sum = 0
    for ch in input_str:
        sum += ord(ch) if ord(ch) >= 65 and ord(ch) <= 95 else 0
    return sum

input_str = input("Enter a string: ")
sum_string(input_str)

print("Sum = ", sum_string(input_str))