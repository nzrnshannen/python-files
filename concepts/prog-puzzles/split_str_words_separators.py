def toListFunc(str):
    return str.split()

def toListFuncExtract(str):
    return [char for char in str if char in extract]

input_str = input("Enter a string: ")
list_str = toListFunc(input_str)
extract = [' ', ',', ', ']

empt_list = toListFuncExtract(input_str)

fin_list = [list_str, empt_list]
print("Result:\n", fin_list)
