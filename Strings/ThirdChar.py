#Write function called third_character that accepts a
#string as an argument and returns the third character
#of the string. If the user inputs a string with fewer than
#3 characters, return "Too short". 


#Write your function here!
def third_character(a):
    if len(a) > 2:
        return a[2]
    else:
        return "Too short"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 1, o, and "Too short", each on a different line.
print(third_character("CS1301"))
print(third_character("Georgia Tech"))
print(third_character("GT"))

#There are two ways we could approach this. They're both
#pretty short, so we'll do both in this file. Either way,
#the trick is to remember that the third character in the
#string is at index 2 because Python is zero-indexed: the
#first character is at index 0, the second at index 1, etc.
#
#First, we could use a conditional to check the length of
#the string, and only return the third character if it's
#long enough:

def third_character(input_string):
    if len(input_string) > 2:
        return input_string[2]
    else:
        return "Too short"
    
    
#Or, we can try to return the third character, and catch
#the error that may arise:

def third_character(input_string):
    try:
        return input_string[2]
    except IndexError:
        return "Too short"
    
