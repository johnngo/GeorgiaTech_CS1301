#Write a function called average_file. average_file should
#have one parameter: a filename.
#
#The file should have an integer on each line. average_file
#should return the average of these integers. However, if
#any of the lines of the file are _not_ integers,
#average_file should return the string "Error reading file!"
#
#Remember, by default, every time you read a line from a
#file, it's interpreted as a string.
#Add your function here!
def average_file(filename):
    read_file = open(filename, "r")
    
    result = 0
    fileslength = 0
    
    try:
        for line in read_file:
            result += int(line)
            fileslength += 1
        return result/ fileslength
    except:
        return "Error reading file!"
    
    files.close()
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5.0, then Error reading file!
#
#You can select valid_file.txt and invalid_file.txt from
#the dropdown in the top left to preview their contents.
print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))



#First, we define the function with its one parameter:
def average_file(filename):
    
    #Because we're reading from a file, we then need to open
    #the file. We don't need to specify "r" as the mode
    #because "r" is the default value for the "mode" keyword
    #parameter (however, we could also include "r" if we
    #wanted to):
    file = open(filename)
    
    #Because we're calculating an average, we're going to
    #need two things: the sum of all the numbers, and the
    #count of all the numbers:
    total = 0
    count = 0
    
    #Recall that if _any_ line of the file is not an integer,
    #then we return an error. So, we would wrap the entire
    #logic of calculating the average into the try block:
    try:
        
        #Then, we want to go through each line in the file...
        for line in file:
            
            #Convert the line to an integer... this is the line
            #that will cause an error if the line doesn't
            #contain an integer!
            value = int(line)
            
            #And then we add the value to our running total...
            total += value
            
            #And increment the count:
            count += 1
    
    #The only error that could occur on the lines above is a
    #ValueError on line 28. So, we catch ValueErrors:
    except ValueError:
        file.close()
        return "Error reading file!"
    
    #If no errors occurred, then we return the average:
    else:
        file.close()
        return total / count
    
    #Notice that we close the file in both the except and
    #the else block: only one of these blocks will run,
    #but we also must close before we return, so we need
    #to close in both.
    #
    #If we wanted to instead skip lines that didn't
    #contain integers, we would put the try/except block
    #inside the loop instead.
    #
    #Note that if the file was empty, there would be an
    #uncaught ZeroDivisionError here because we would be
    #trying to return 0 / 0. We aren't checking your code
    #for that case, but if we wanted to, we would include
    #the average calculation in the try block, and add an
    #extra except block to catch ZeroDivisionErrors.



print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))
