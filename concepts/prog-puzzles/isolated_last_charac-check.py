def input_strings(strlist, listlen):
    print("Enter strings: ")
    for i in range(listlen):
        strlist.append(input())
        
def check_last_charac(strlist):
        return True if strlist[-2] == ' ' else False

def print_results(strlist):
    result_list = []
    for str in strlist:
        result_list.append(check_last_charac(str))

    print("Output: ", result_list)

list_len = int(input("Enter number of strings: "))
list_str = []

input_strings(list_str, list_len)
print("Input: ", list_str)

print_results(list_str)

