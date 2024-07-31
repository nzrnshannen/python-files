#6: program allows user to enter two values and outputs the product of the two values

# Note: input() always returns a string so it is important to typecast it

print("Enter two values\n--------")

isValid = False
num1 = num2 = 0
res = 0

while isValid == False:
    
    # validating first input
    while True:
        input_a = input("a: ")
        try:
            if "." in input_a:
                num1 = float(input_a)
            else:
                num1 = int(input_a)
                break # exit loop after entering num1 input
        except ValueError:
            print("Invalid input for variable num1!\n")
        
    # validating second input
    while True:
        input_b = input("b: ")
        try:
            if "." in input_b:
                num2 = float(input_b)
            else:
                num2 = int(input_b)
            break # exit loop after entering num2 and performing calculation
        except ValueError:
            print("Invalid input for variable num2!\n")
        
    res = num1 * num2
    isValid = True
    
print("Answer: " + str(num1) + " * " + str(num2) + " = " + str(res))