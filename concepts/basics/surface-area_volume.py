# 5: program allows user the enter a value for one edge of a cube
#   The program calculates the surface area of one side for the cube, the surface area of the cube, and its volume

#              FORMULAS
#---------------------------------------
# one side of the cube = a**2           
# surface area of the cube = 6 * a**2
# volume of cube = a**3
#---------------------------------------

while True:
    try:
        user_input = input("Enter a number: ")
        
        if "." in user_input:
            num = float(user_input)
        else:
            num = int(user_input)
            
        if num <= 0:
            print("Please enter a positive integer/floating point number.\n")
        else:
            surfarea_oneside = num **2
            surfarea_cube = 6 * num**2
            vol_cube = num ** 3
            print("============================================")
            print("Surface area of one side of the cube = " + str(surfarea_oneside))
            print("Surface area of the cube = " + str(surfarea_cube))
            print("Volume of the cube = " + str(vol_cube))
            break
        
    except ValueError:
        print("Invalid input. Try again!\n")
        