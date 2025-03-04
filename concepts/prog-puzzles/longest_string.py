def check_longest_str(strlist):
    max = -1
    itr = 0
    index = 0
    for str in strlist:
        if max < len(str):
            max = len(str)
            index = itr
        itr+=1
        
    return strlist[index]

input_str = input("Enter strings separate by space: ").split()

print("Input: ", input_str)
print("Longest string: ", check_longest_str(input_str))

# should accept an empty string