# Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

def len_chckr(list):
    return trav_list(list) if len(list) >= 8 else False

def trav_list(list):
    itr = 0
    for item in list:
        if list[4] == item:
            itr+=1
    
    return True if itr == 3 else False

input_list = input("Enter numbers separated by spaces: ")
list = list(map(int, input_list.split()))

print("List: ", list)
print("Result = ", len_chckr(list))
