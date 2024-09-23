def checkinput(option):
    checker = True

    if not option.isdigit():
        print("Invalid entry")
        checker = False

    #return false to other functions if the input is invalid
    return checker

def basicCalc():
    validOption = False
    print("\n\nWelcome to the basic calculator")
    print("Select from the following options:")

    option1 = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Square root\n7. Back\ninput: ")

    while validOption == False:
        validOption = checkinput(option1)
        #check if option is a digit
        if validOption == False:
            option1 = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Square root\n7. Back\nInput:")
        else:
            break

        
    option1 = int(option1)

    #check if option is in corect range
    while option1 > 7 or option1 < 1:
        print("Invalid entry")
        option1 = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Square root\n7. Back\nInput:")

    option1 = int(option1)

    if option1 == 1:
        print("You have selected addition")

        #get the 1st number	
        num1 = input("Enter the first number: ")
        validOption = checkinput(num1)

        #check if option is a digit
        while validOption == False:
            num1 = input("Enter the first number: ")
            validOption = checkinput(num1)
        num1 = int(num1)

        #get the 2nd number
        num2 = input("Enter the second number: ")
        validOption = checkinput(num2)

        #check if option is a digit
        while validOption == False:
            num2 = input("Enter the second number: ")
            validOption = checkinput(num2)
        num2 = int(num2)

        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    #check if option is a digit

    elif option1 == 2:
        print("You have selected subtraction")

        #get the 1st number
        num1 = input("Enter the first number: ")
        validOption = checkinput(num1)

        #check if option is a digit
        while validOption == False:
            num1 = input("Enter the first number: ")
            validOption = checkinput(num1)
        num1 = int(num1)

        #get the 2nd number
        num2 = input("Enter the second number: ")
        validOption = checkinput(num2)

        #check if option is a digit
        while validOption == False:
            num2 = input("Enter the second number: ")
            validOption = checkinput(num2)
        num2 = int(num2)

        print(f"The difference between {num1} and {num2} is {num1 - num2}")

    elif option1 == 3:
        print("You have selected multiplication")

        #get the 1st number
        num1 = input("Enter the first number: ")
        validOption = checkinput(num1)

        #check if option is a digit
        while validOption == False:
            num1 = input("Enter the first number: ")
            validOption = checkinput(num1)
        num1 = int(num1)

        #get the 2nd number
        num2 = input("Enter the second number: ")
        validOption = checkinput(num2)

        #check if option is a digit
        while validOption == False:
            num2 = input("Enter the second number: ")
            validOption = checkinput(num2)
        num2 = int(num2)

        print(f"The product of {num1} and {num2} is {num1 * num2}")

    elif option1 == 4:
        print("You have selected division")

        #get the 1st number
        num1 = input("Enter the first number: ")
        validOption = checkinput(num1)

        #check if option is a digit
        while validOption == False:
            num1 = input("Enter the first number: ")
            validOption = checkinput(num1)
        num1 = int(num1)

        #get the 2nd number
        num2 = input("Enter the second number: ")
        validOption = checkinput(num2)

        #check if option is a digit
        while validOption == False:
            num2 = input("Enter the second number: ")
            validOption = checkinput(num2)
        num2 = int(num2)

        print(f"The quotient of {num1} and {num2} is {num1 / num2}")
    
    elif option1 == 5:
        print("You have selected power")

        #get the 1st number
        num1 = input("Enter the base number: ")
        validOption = checkinput(num1)

        #check if option is a digit
        while validOption == False:
            num1 = input("Enter the base number: ")
            validOption = checkinput(num1)
        num1 = int(num1)

        #get the 2nd number
        num2 = input("Enter the power: ")
        validOption = checkinput(num2)

        #check if option is a digit
        while validOption == False:
            num2 = input("Enter the power: ")
            validOption = checkinput(num2)
        num2 = int(num2)

        print(f"{num1} to the power of {num2} is {num1 ** num2}")

    elif option1 == 6:
        print("You have selected square root")

        #get the number
        num1 = input("Enter the number: ")
        validOption = checkinput(num1)

        #check if option is a digit
        while validOption == False:
            num1 = input("Enter the number: ")
            validOption = checkinput(num1)
        num1 = int(num1)

        print(f"The square root of {num1} is {num1 ** 0.5}")

    else:
        print("You have selected back")
        return
    
    return 
    
def averageCalc():
    validOption = False

    print("\n\nWelcome to the average calculator")
    amount = input("How many numbers would you like to calculate the average of: ")
    
    while validOption == False:
        validOption = checkinput(amount)
        #check if option is a digit
        if validOption == False:
            amount = input("How many numbers would you like to calculate the average of: ")
        else:
            break

    amount = int(amount)

    numbers = []
    for i in range(amount):
        num = input(f"Enter number {i + 1}:")
        validOption = checkinput(num)

        #check if option is a digit
        while validOption == False:
            num = input(f"Enter number {i + 1}:")
            validOption = checkinput(num)
        
        num = int(num)
        numbers.append(num)
    
    print(f"The average is {sum(numbers) / len(numbers)}")
    return

def areaCalc():
    validOption = False
    print("\n\nWelcome to the area calculator")
    print("Select from the following options:")
    option1 = input("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Back\nInput:")

    while validOption == False:
        validOption = checkinput(option1)
        #check if option is a digit
        if validOption == False:
            option1 = input("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Back\nInput:")
        else:
            break

    option1 = int(option1)

    #check if option is in corect range
    while option1 > 5 or option1 < 1:
        print("Invalid entry")
        option1 = input("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Back\nInput:")
    
    option1 = int(option1)

    if option1 == 1:
        print("You have selected square")

        #get the side length
        side = input("Enter the side length: ")
        validOption = checkinput(side)

        #check if option is a digit
        while validOption == False:
            side = input("Enter the side length: ")
            validOption = checkinput(side)
        side = int(side)

        print(f"The area of the square is {side ** 2}")
    
    elif option1 == 2:
        print("You have selected rectangle")

        #get the length
        length = input("Enter the length: ")
        validOption = checkinput(length)

        #check if option is a digit
        while validOption == False:
            length = input("Enter the length: ")
            validOption = checkinput(length)
        length = int(length)

        #get the width
        width = input("Enter the width: ")
        validOption = checkinput(width)

        #check if option is a digit
        while validOption == False:
            width = input("Enter the width: ")
            validOption = checkinput(width)
        width = int(width)

        print(f"The area of the rectangle is {length * width}")

    elif option1 == 3:
        print("You have selected triangle")

        #get the base
        base = input("Enter the base: ")
        validOption = checkinput(base)

        #check if option is a digit
        while validOption == False:
            base = input("Enter the base: ")
            validOption = checkinput(base)
        base = int(base)

        #get the height
        height = input("Enter the height: ")
        validOption = checkinput(height)

        #check if option is a digit
        while validOption == False:
            height = input("Enter the height: ")
            validOption = checkinput(height)
        height = int(height)

        print(f"The area of the triangle is {(base * height) / 2}")

    elif option1 == 4:
        print("You have selected circle")

        #get the radius
        radius = input("Enter the radius: ")
        validOption = checkinput(radius)

        #check if option is a digit
        while validOption == False:
            radius = input("Enter the radius: ")
            validOption = checkinput(radius)
        radius = int(radius)

        print(f"The area of the circle is {3.14159 * radius ** 2}")
    
    else:
        print("You have selected back")
        return
    
    return

def volumeCalc():
    validOption = False
    print("\n\nWelcome to the volume calculator")
    print("Select from the following options:")#
    option1 = input("1. Cube\n2. Cuboid\n3. Cylinder\n4. Sphere\n5. Back\nInput:")

    while validOption == False:
        validOption = checkinput(option1)
 
        #check if option is a digit
        if validOption == False:
            option1 = input("1. Cube\n2. Cuboid\n3. Cylinder\n4. Sphere\n5. Back\nInput:")
        else:
            break

    option1 = int(option1)

    #check if option is in corect range
    while option1 > 5 or option1 < 1:
        print("Invalid entry")
        option1 = input("1. Cube\n2. Cuboid\n3. Cylinder\n4. Sphere\n5. Back\nInput:")


    if option1 == 1:
        print("You have selected cube")

        #get the side length
        side = input("Enter the side length: ")
        validOption = checkinput(side)

        #check if option is a digit
        while validOption == False:
            side = input("Enter the side length: ")
            validOption = checkinput(side)
        side = int(side)

        print(f"The volume of the cube is {side ** 3}")

    elif option1 == 2:
        print("You have selected cuboid")

        #get the length
        length = input("Enter the length: ")
        validOption = checkinput(length)

        #check if option is a digit
        while validOption == False:
            length = input("Enter the length: ")
            validOption = checkinput(length)
        length = int(length)

        #get the width
        width = input("Enter the width: ")
        validOption = checkinput(width)

        #check if option is a digit
        while validOption == False:
            width = input("Enter the width: ")
            validOption = checkinput(width)
        width = int(width)

        #get the height
        height = input("Enter the height: ")
        validOption = checkinput(height)

        #check if option is a digit
        while validOption == False:
            height = input("Enter the height: ")
            validOption = checkinput(height)
        height = int(height)

        print(f"The volume of the cuboid is {length * width * height}")

    elif option1 == 3:
        print("You have selected cylinder")

        #get the radius
        radius = input("Enter the radius: ")
        validOption = checkinput(radius)

        #check if option is a digit
        while validOption == False:
            radius = input("Enter the radius: ")
            validOption = checkinput(radius)
        radius = int(radius)

        #get the height
        height = input("Enter the height: ")
        validOption = checkinput(height)

        #check if option is a digit
        while validOption == False:
            height = input("Enter the height: ")
            validOption = checkinput(height)
        height = int(height)

        print(f"The volume of the cylinder is {3.14159 * radius ** 2 * height}")

    elif option1 == 4:
        print("You have selected sphere")

        #get the radius
        radius = input("Enter the radius: ")
        validOption = checkinput(radius)

        #check if option is a digit
        while validOption == False:
            radius = input("Enter the radius: ")
            validOption = checkinput(radius)
        radius = int(radius)

        print(f"The volume of the sphere is {4 / 3 * 3.14159 * radius ** 3}")

    else:
        print("You have selected back")
        return
    
    return

def bmiCalc():
    validOption = False
    print("\n\nWelcome to the BMI calculator")

    #get the weight
    weight = input("Enter your weight in kg: ")

    validOption = checkinput(weight)
    
    #check if option is a digit
    while validOption == False:
        weight = input("Enter your weight in kg: ")
        validOption = checkinput(weight)
    
    weight = int(weight)

    #get the height
    height = input("Enter your height in cm: ")
    validOption = checkinput(height)

    #check if option is a digit
    while validOption == False:
        height = input("Enter your height in cm: ")
        validOption = checkinput(height)
    
    height = int(height)

    bmi = weight / (height*height) * 10000
    bmi = round(bmi, 2)

    print(f"Your BMI is {bmi}")

    if bmi < 18.5:
        print("You are underweight, please consult a doctor")

    elif bmi >= 18.5 and bmi < 24.9:
        print("You are healthy")

    elif bmi >= 24.9 and bmi < 29.9:
        print("You are overweight, try to exercise more or eat healthier")

    else:
        print("You are obese, please consult a doctor")
    
    return

def tempCalc():
    print("\n\nWelcome to the temperature calculator")
    print("Select from the following options:")
    option1 = input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Back\nInput:")
    validOption = checkinput(option1)
    
    #check if option is a digit
    while validOption == False:
        option1 = input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Back\nInput:")
        validOption = checkinput(option1)
    
    option1 = int(option1)

    #check if option is in corect range
    while option1 > 3 or option1 < 1:
        print("Invalid entry")
        option1 = input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Back\nInput:")
    
    option1 = int(option1)


    if option1 == 1:
        print("You have selected Celsius to Fahrenheit")

        #get the temperature
        temp = input("Enter the temperature in Celsius: ")
        validOption = checkinput(temp)

        #check if option is a digit
        while validOption == False:
            temp = input("Enter the temperature in Celsius: ")
            validOption = checkinput(temp)
        
        temp = int(temp)

        print(f"The temperature in Fahrenheit is {temp * 9/5 + 32}")

    elif option1 == 2:
        print("You have selected Fahrenheit to Celsius")

        #get the temperature
        temp = input("Enter the temperature in Fahrenheit: ")
        validOption = checkinput(temp)

        #check if option is a digit
        while validOption == False:
            temp = input("Enter the temperature in Fahrenheit: ")
            validOption = checkinput(temp)
        
        temp = int(temp)

        print(f"The temperature in Celsius is {(temp - 32) * 5/9}")

    else:
        print("You have selected back")
        return
    
def calcSelector():
    print ("Select a calculator from the following options: ")
    option1 = input("1. Basic calculator\n2. Average calculator\n3. Area calculator\n4. Volume calculator\n5. BMI calculator\n6. Temperature calculator\n7. Exit\nInput:")
    validOption = checkinput(option1)

    #check if option is a digit
    while validOption == False:
        option1 = input("1. Basic calculator\n2. Average calculator\n3. Area calculator\n4. Volume calculator\n5. BMI calculator\n6. Temperature calculator\n7. Exit\nInput:")
        validOption = checkinput(option1)

    option1 = int(option1)

    #check if option is in corect range
    while option1 > 7 or option1 < 1:
        print("Invalid entry")
        option1 = input("1. Basic calculator\n2. Average calculator\n3. Area calculator\n4. Volume calculator\n5. BMI calculator\n6. Temperature calculator\n7. Exit\nInput:")

    option1 = int(option1)

    if option1 == 1:
        basicCalc()

    elif option1 == 2:
        averageCalc()

    elif option1 == 3:
        areaCalc()

    elif option1 == 4:
        volumeCalc()

    elif option1 == 5:
        bmiCalc()
    
    elif option1 == 6:
        tempCalc()

    else:
        print("You have selected exit")
        return

def main():
    counter = 0 #counter to check if the user is a new or returning user
    goAgain = True #variable to check if the user wants to use the calculator again

    while goAgain == True: #loop to keep the calculator running

        if counter == 0:
            print("Welcome to Amir's calculator \nThere are a few calculators you might want to use")
        else :
            print("\n\nWelcome back to Amir's calculator \nWhat can i do for you this time?")

        calcSelector() #run the function to select a calculator

        #ask the user if they want to use the calculator again
        option = input("\n\nWould you like to use the calculator again? \nEnter Y for yes or N for no: ")
        option = option.upper()

        if option == "N":
            print("Thank you for using Amir's calculator, see you soon!")
            goAgain = False

        counter += 1

    return



main() #call the main function