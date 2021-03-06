#Write a function called lucky_sevens that takes in one
#parameter, a string variable named a_string. Your function
#should return True if there are exactly three '7's in
#a_string. If there are less than three or more than three
#'7's, the function should return False.
#
#For example:
#  - lucky_sevens("happy777bday") should return True.
#  - lucky_sevens("h7app7ybd7ay") should also return True.
#  - lucky_sevens("happy77bday") should return False.
#  - lucky_sevens("h777appy777bday") should also return False.
#
#Hint: Remember in Chapter 3.3, we covered how to use a loop
#to look at each character in a string.

count =0
#Write your function here!
def lucky_sevens(a_string):
    count =0
    for i in a_string:
        for j in i:
            if j == "7":
                count +=1
                
    if count == 3:
        return True
    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, each on their own line.
print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))

#alternative
#We'll start with the function header: the function is
#called lucky_sevens, and it has one parameter: a_string.
def lucky_sevens(a_string):
    
    #Next, we're going to want to count something. So,
    #let's create a counter:
    count = 0
    
    #Next, we need to go through each letter one by one:
    for letter in a_string:
        
        #Finally, we need to check whether each letter is
        #the character "7":
        if letter == "7":
            
            #And if so, add to the counter:
            count += 1
    
    #Then, only once we've done everything else are we
    #ready to return. Notice that this line is 
    #indented once: it's inside the function, but not the
    #loop or conditional.
    #
    #count == 3 will resolve to True if count is 3, False
    #otherwise. So, we can just return it directly:
    
    return count == 3


#There are lots of other ways we could do this. We'll cover
#them more in Chapter 4.2.

print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))
