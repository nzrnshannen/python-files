# monotonic: always increasing/decreasing

def check_list(num_list):
    incr = decr = False
    monotonic = True
    itr = 0
    
    # for increasing
    if num_list[itr] < num_list[itr+1]:
        incr = True
        monotonic = True
        while monotonic and itr < len(num_list)-1:
            if num_list[itr] >= num_list[itr+1]:
                monotonic = False
            itr+=1
    # for decreasing
    elif num_list[itr] > num_list[itr+1]: 
        decr = True
        monotonic = True
        while monotonic and itr < len(num_list)-1:
            if num_list[itr] <= num_list[itr+1]:
                monotonic = False
            itr+=1
    else:
        monotonic = False 
        
    if incr and monotonic:
        return "Increasing"
    elif decr and monotonic:
        return "Decreasing"
    else:
        return "Not a monotonic sequence!"    
            
numbers = input("Enter numbers separated by spaces: ")

if len(numbers.split()) < 2:
    print("Input at least 2 numbers!")
else:
    num_list = list(map(int, numbers.split()))
    print("Result = ", check_list(num_list))
