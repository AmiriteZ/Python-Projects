def main():
    # String manipulation
    strInput = "The quick brown fox jumps over the lazy dog"
    print(f"The string is: {strInput}")
    
    print(f"1.  {strInput[0]} is the first character of the string")
    print(f"2.  {strInput[-1]} is the last character of the string")
    print(f"3.  {strInput[3:]} is the string without the first three characters")
    print(f"4.  {strInput[:5]} is the first five characters of the string")
    print(f"5.  {strInput[-6:]} is the last six characters of the string")
    print(f"6.  {strInput[:-9]} is the string without the last nine characters")
    print(f"7.  {strInput[3:8]} is the characters between the 4th and 9th characters")
    print(f"8.  {strInput[::2]} is every other character of the string")
    print(f"9.  {strInput[::-1]} is the string in reverse order")
    print("10.  ",strInput[0:2] + strInput[7:15] , " is the first two characters and the characters between the 8th and 16th characters")
    print(f"11.  {strInput.upper()} is the string in uppercase")
    print(f"12.  {strInput.lower()} is the string in lowercase")
    print(f"13.  {strInput.title()} is the string with the first letter of each word capitalized")
    print(f"14.  {strInput.swapcase()} is the string with the case of each letter swapped")
    print(f"15.  {strInput.capitalize()} is the string with the first letter capitalized")
    print(f"16. {strInput.replace('fox', 'cat')} is the string with 'fox' replaced with 'cat'")
    print(f"17. {strInput.strip()} is the string with leading and trailing whitespace removed")
    print(f"18. {strInput.center(50)}\nis the string centered in a field of 50 characters")
    print(f"19. {strInput.find('fox')} is the index of the first occurrence of 'fox'")
    print(f"20. {strInput.rfind('fox')} is the index of the last occurrence of 'fox'")
    print(f"21. {strInput.index('fox')} is the index of the first occurrence of 'fox'")
    print(f"22. {strInput.rindex('fox')} is the index of the last occurrence of 'fox'")
    print(f"23. {strInput.count('fox')} is the number of occurrences of 'fox'")
    print("24. use variable.startswith(word) to check if the string starts with a specific word")
    print("25. use variable.endswith(word) to check if the string ends with a specific word")
    print("26. use variable.isalnum() to check if the string is alphanumeric, returns True or False, (false if it contains spaces or special characters)")
    print("27. use variable.isalpha() to check if the string is alphabetic, returns True or False (false if it contains spaces or special characters)")
    print("28. use variable.isdigit() to check if the string is a digit, returns True or False")
    print("29. use variable.islower() to check if the string is in lowercase, returns True or False")
    print("30. use variable.isupper() to check if the string is in uppercase, returns True or False")
    print("31. use variable.isspace() to check if the string contains only whitespace, returns True or False")
    print("32. use variable.istitle() to check if the string is in title case, returns True or False")
    print("33. use variable.split() to split the string into a list of words")
    print("34. use variable.splitlines() to split the string into a list of lines")
    print("35. use variable.split('<character>') to split the string at a specific character")
    print("36 use strInput.join([list of items]) to join the items in a list with the string that already exists")
    

    



main()