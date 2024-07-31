#4:  allows the user to enter a value and the program divides it by 2

while True:
    try:
        user_input = input("Enter a number: ") # input() returns String type (so typecast is a must)
        if "." in user_input: # the .isin() method does not exist for strings
            num = float(user_input) # converting String to float
            res = num/2
        else:
            num = int(user_input) # convertig String to int
            res = round(num/2) # eliminate floating point after dividing by 2 
        
        print("Answer: " + str(res))
        break

    except ValueError: # if user enters non-numeric value
        print("That's not a valid number!\n")