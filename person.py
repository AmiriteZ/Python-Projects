genders = ["male", "female", "other", "prefer not to say"] 
gOptions = ["M", "F", "O", "PNTS"]

def print_user():
    fname = input("Enter your first name: ") #input function is used to take input from the user
    lname = input("Enter your last name: ") #input function is used to take input from the user
    age = input("Enter your age: ") #input function is used to take input from the user
    while not age.isdigit(): #if the input is not a digit, the loop will continue to run
        print("Invalid entry")
        age = input("Enter your age: ")
    
    age = int(age) #convert the age to an integer

    gender = input("What gender are you? \nEnter M for male, F for female, O for other, if you dont want to say type PNTS: ") #input function is used to take input from the user
    gender = gender.upper() #convert the input to uppercase

    while gender not in gOptions: #if the input is not in the list of options, the loop will continue to run
        print("Invalid entry")
        gender = input("What gender are you? \nEnter M for male, F for female, O for other, if you dont want to say type PNTS: ")
        
    if age < 18: #if the age is less than 18, the user is not eligible to use the service
        print("Sorry, you are not eligible to use this service")
        return
    
    print(f"Hello {fname} {lname} welcome to our service") #print the user's name and welcome message


print_user() #call the function