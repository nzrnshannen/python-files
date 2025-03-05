def non_negatives(n):
    ret_string = ""
    for itr in range(0, n+1):
        ret_string += str(itr) + " "

    return ret_string

input_n = int(input("Enter n: "))

print("Output: ", non_negatives(input_n))