# n stones

def num_stone_piles(n):
    ret_list = [n]
    x = 2

    for x in range(n-1):
        ret_list.append(ret_list[-1] + 2)

    return ret_list

input_pile = int(input("Enter n stone piles: "))

print("Result = ", num_stone_piles(input_pile))
