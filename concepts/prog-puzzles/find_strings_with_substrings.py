def find_strings(substring, strlist):
    ret_list = []
    for str in strlist:
        if substring in str:
            ret_list.append(str)
    return ret_list


input_strings = input("Enter strings separated by spaces: ").split()
substr = input("Enter the substring: ")

print("Input: ", input_strings)
print("Output: ", find_strings(substr, input_strings))