#Write a function called string_splitter that replicates the
#function of the string type's split() method, assuming that
#we're splitting at spaces. string_splitter should take as
#input a string, and return as output a list of the
#individual words from the string, assuming that words were
#divided by spaces. The spaces themselves should not be in
#the list that your function returns.
#
#You may assume that there will never be more than one space
#in a row, and that the string will neither start nor end
#with a space. However, you should not assume there will
#always be a space.
#
#You may not use Python's built-in split() method.
#
#For example:
#
#  string_splitter("Hello world") -> ['Hello', 'world']


#Write your function here!
def string_splitter(a_string):
    list = []
    string=""
    
    for s in a_string:
        print(s)
        if s == " ":
            
            list.append(string)
            string = ""
            
        else:
            string +=s
            
    if string:
        list.append(string)
    else:
        pass
    
    return list


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ['Hello', 'world']
print(string_splitter("Hello world"))


#There are a lot of different ways you could do this
#problem. The one below is probably one of the simplest,
#but there are lots of others.
#
#For this answer, we're going to basically follow this
#pattern:
#
#If there's currently a space in the string, then there
#are at least two words. So, grab the first word by
#finding the index of the first space, save the first
#word to the list, and remove the first word from the
#string. Repeat as long as there are spaces in the
#string. When all the spaces are gone, add whatever is
#left to the list.

def string_splitter(a_string):
    
    #First we initialize the list we'll end up returning:
    
    words = []
    
    #Then, we run a while loop as long as there is a
    #space in the string. If there's a space, there must
    #be at least two words:
    
    while " " in a_string:
        
        #So, if we're here, we know there's a space in
        #the string. So, the first word is the string
        #slice from the beginning until the index of the
        #first space.
        #
        #So, we find the index...
        
        index = a_string.find(" ")
        
        #...and add that slice to the list of words...
        
        words.append(a_string[:index])
        
        #...and remove that slice from a_string. To do
        #this last part, we set a_string equal to
        #itself, starting one character after the first
        #space.
        
        a_string = a_string[index + 1:]
        
        #If there are still spaces, the loop will repeat.
        #Each time the loop repeats, it'll get rid of
        #one space.
        
    #When there are no more spaces, then there is still
    #one word in the string: whatever was after the last
    #space. So, we add that to the list:
    
    words.append(a_string)
    
    #And return our result:
    
    return words


print(string_splitter("Hello, world"))

