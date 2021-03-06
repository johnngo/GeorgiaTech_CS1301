#Write a function called attendance_check. attendance_check
#should have two parameters: roster and present. Both roster
#and present will be lists of strings. Return a list (sorted
#alphabetically) of all strings in the list roster that are
#not in the list present. In other words, if roster is a
#list of students enrolled in a class and present is a list
#of students in class today, return a list of students that
#are absent.
#
#You may assume that every item in each list will be a
#string. You may also assume that every name in the list
#present will be in the list roster. If no students are
#absent, return an empty list.


#Write your function here!
def attendance_check(roster, present):
    result = []
    for i in roster:
        if i not in present:
            result.append(i)
    result.sort()
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['Ferguson', 'Winston']
test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))


def attendance_check(roster, present):
    
    #There are some fancy ways to do this, but we're going
    #to focus on doing this with what we know so far:
    #lists and loops.
    #
    #One way to do this would be to remove the names in
    #present from roster -- at the end, roster would hold
    #only the absent students. However, that modifies the
    #value of the list, which we want to avoid doing. So,
    #instead, if we're going to return a list of students
    #who were absent, then we need to create a new list to
    #hold those names!
    
    absent = []
    
    #Next, we want to check which names on roster are also
    #in present. So, we iterate over the names in roster...
    
    for name in roster:
        
        #...and check if each name is in present:
        
        if not name in present:
            
            #If it's not, then we add that name to absent.
            
            absent.append(name)
    
    #When we're done, we sort absent:
    
    absent.sort()
    
    #And return it:
    
    return absent



test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))