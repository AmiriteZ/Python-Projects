from datetime import datetime

def calculateAge(dOB):
    #get current date
    today = datetime.today()

    #calculate age by subtracting the year of birth from the current year
    age = today.year - dOB.year

    #check if birthday has occured yet, if not subtract 1 from age
    if (today.month, today.day) < (dOB.month, dOB.day):
        age =- 1
    
    return age

def getDOB():
    #get the users date of birth
    dob = input("Enter your date of birth in the format DD/MM/YYYY: ")

    #check if the date is in the correct format
    try:
        #try to convert the date to a datetime object
        dob = datetime.strptime(dob, "%d/%m/%Y")
    except:
        #if the date is not in the correct format, print an error message and call the function again
        print("Invalid date format")
        return getDOB()
    
    return dob

print(f"you are {calculateAge(getDOB())} years old") #print the users age	
