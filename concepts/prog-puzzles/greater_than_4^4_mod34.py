def checkFunc(num):
    return True if num > 256 and num%34 == 4 else False

num = int(input("Enter a number: "))

print("Result = ", checkFunc(num))