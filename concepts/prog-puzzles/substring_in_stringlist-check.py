# Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.

def str_chckr(list):
    return True if list[-2] in list[-1] else False


string_list = input("Enter a series of strings separated by space: ").split()


print("Result = ", str_chckr(string_list))