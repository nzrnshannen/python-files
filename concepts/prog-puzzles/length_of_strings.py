def length_func(str):
    str_len = []
    for item in str:
        str_len.append(len(item))
    return str_len
    

input_strings = input("Enter strings separated by a space: ").split()
print("Input: ", input_strings)
print("Result = ", length_func(input_strings))

# should accept an empty string => len 0