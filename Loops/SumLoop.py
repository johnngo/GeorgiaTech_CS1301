mystery_int = 7

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Use a loop to find the sum of all numbers between 0 and
#mystery_int, including bounds (meaning that if
#mystery_int = 7, you add 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7).
#
#However, there's a twist: mystery_int might be negative.
#So, if mystery_int was -4, you would -4 + -3 + -2 + -1 + 0.
#
#There are a lot of different ways you can do this. Most of
#them will involve using a conditional to decide whether to
#add or subtract 1 from mystery_int.
#
#You may use either a for loop or a while loop to solve this,
#although we recommend using a while loop.

my_summ =0

while mystery_int < 0 or mystery_int > 0:
    if mystery_int < 0:
#        print(mystery_int)   
        my_summ +=mystery_int
        mystery_int +=1
    if mystery_int >0:
#        print(mystery_int)
        my_summ +=mystery_int
        mystery_int -=1
    
print(my_summ)

#sample #1
mystery_int = 7

#-----------------------------------------------------------
#There are lots of ways we could do this. The simplest ways
#are going to involve basically writing two different
#answers: one for where mystery_int is positive, the other
#for when it's negative. Then, we use a conditional to
#switch between them.
#
#Here's what that would look like with a while loop:

current_sum = 0
if mystery_int > 0:
    while mystery_int > 0:
        current_sum += mystery_int
        mystery_int -= 1
else:
    while mystery_int < 0:
        current_sum += mystery_int
        mystery_int += 1
print(current_sum)

#And here it is with a for loop. Note that it's a little
#more complex than we might have expected: we have to put
#mystery_int as the first argument if it's negative
#because Python requires ranges to go from lowest to
#highest.

current_sum = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        current_sum += i
else:
    for i in range(mystery_int, 0):
        current_sum += i
print(current_sum)

#Or, we could also run the same for loop in reverse by
#putting -1 as our step:
current_sum = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        current_sum += i
else:
    for i in range(0, mystery_int - 1, -1):
        current_sum += i
print(current_sum)

#However, in all these, notice we have a decent amount
#of repeated code: really, all that's changing is the sign
#on a couple of values. Can't we do this more efficiently?
#We can! Check out sample_answer_2.py to see how.

#sample#2
mystery_int = 7

#The more efficient solutions to this would have one overall
#loop, and use some logic inside the loop to design which
#ways to iterate.
#
#Here's a solution with a while loop. Here, we're always
#going to be approaching 0 whether mystery_int is positive
#or negative, so we run our loop while mystery_int is not 0:

current_sum = 0
while not mystery_int == 0:
    #Then, we add the current mystery_int to the sum:
    current_sum += mystery_int
    
    #Then, we need to either add one or subtract one from
    #mystery_int to move it toward 0:
    if mystery_int < 0:
        mystery_int += 1
    else:
        mystery_int -= 1
print(current_sum)

#This way, mystery_int will always be moving in the direction
#of 0, and it can't pass 0 without equaling 0, guaranteeing
#the loop will terminate.
#
#Note, though, that the conditional on lines 18 to 21 will
#always have the same result. So, why not just check that
#first?

if mystery_int < 0:
    change = 1
else:
    change = -1

current_sum = 0
while not mystery_int == 0:
    current_sum += mystery_int
    mystery_int += change
print(current_sum)

#We always want to either add 1 or subtract 1, so we can
#calculate which we'll do and store it. Then, we just add
#that value each time the loop runs.
#
#That same logic can let us do this with a for loop. See
#sample_answer_3.py for that.

#sample3
mystery_int = 7

#That same logic can let us do this with a for loop,
#although it gets a little weird. First, we have to use
#the opposite values for change because we're running from
#0 to mystery_int, not from mystery_int to 0:

if mystery_int < 0:
    change = -1
else:
    change = 1

#Then, because range() is exclusive of the second bound,
#we need to either run our loop to mystery_int + 1 if
#mystery_int is positive, or mystery_int - 1 if
#mystery_int is negative. We can do that by running it
#to mystery_int + change either way, and using change
#as our step argument, too:  

current_sum = 0
for i in range(0, mystery_int + change, change):
    current_sum += i
print(current_sum)

#Finally, there's one more way we could do this, but it
#uses something we haven't covered yet. Check out
#sample_answer_4.py if you want to see!

#sample4
mystery_int = 7

#In every solution we've shown, we've had to use a
#conditional to decide whether to add or subtract one each
#time the loop iterates. Isn't there an easier way?
#
#There is! We can find the sign of mystery_int by dividing
#it by its absolute value, which lets us do this:

current_sum = 0
while not mystery_int == 0:
    current_sum += mystery_int
    mystery_int -= mystery_int // abs(mystery_int)
print(current_sum)

#Line 13 divides mystery_int by its absolute value, using
#the abs() function. This will be 1 if mystery_int is
#positive, -1 if it's negative. So, we can just add the
#result, and voila: we have a solution in only 5 lines.
#
#Note that we use the floor division function to force
#mystery_int to stay an integer instead of becoming a
#float. We could also use regular division and typecast
#the result to an integer.
