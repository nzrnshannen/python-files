# Finding a list of integers with exactly two occurences of nineteen and at least three occurrences of five

def checkFunc(list):
    chckr = False
    itr = 0
    for i in list:
        if i == 19:
            itr+=1
            
    if itr == 2:
        itr = 0
        chckr = True
        for j in list:
            if j == 5:
                itr+=1
                
    return True if itr >= 3 and chckr else False
    

input_list = input("Enter numbers separated by spaces: ")
list = list(map(int, input_list.split()))

print("List: ", list)

print("Result = ", checkFunc(list))
