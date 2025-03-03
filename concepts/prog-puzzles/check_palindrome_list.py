def check_str(str):
    # Other solution:
    # orig_str = str.lower()
    # rev_str = str[::-1].lower()
    # return True if orig_str == rev_str else False
    
    if str == "":
        return True
    
    rev_list = []
    iter = len(str)-1
    
    while(iter >= 0): # copy string reversely 
        rev_list.append(str[iter])
        iter-=1
        
    rev = "".join(rev_list) # list to string for successful comparison
    
    return True if rev == str else False

def print_results(list):
    results = []
    for str in list:
        results.append(check_str(str.lower()))
        
    print(results)
    
    
str_list = input("Input a series of strings separate by spaces: ").split()
print_results(str_list)

# ISSUE: should return True if string is ''