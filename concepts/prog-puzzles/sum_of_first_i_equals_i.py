num_list = list(map(int, input("Enter a series of numbers separated by space: ").split()))

def sum_check(list):
    sum = 0
    for item in list:
        sum+=item
    
    return True if sum == len(list) else False

print("Result = ", sum_check(num_list))