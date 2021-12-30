###### TASK #1: Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)

####### TASK #2:  Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)

######## TASK #3 Counting, the Dojo Way - Print integers 1 to 100. 
######## If divisible by 5, print "Coding" instead. 
######## If divisible by 10, print "Coding Dojo".

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
        continue
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

######## TASK #4 Whoa. That Sucker's Huge - 
######## Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(1, 500000, 2):
    # print(i)
    sum = sum + i
print(sum)

######### TASK #5 Countdown by Fours - 
######### Print positive numbers starting at 2018, counting down by fours.
y = 2018
while y > 0:
    if y % 4 == 0:
        print(y)
    y = y - 1

######### TASK #6 Flexible Counter - Set three variables: lowNum, highNum, mult. 
######### Starting at lowNum and going through highNum, 
######### print only the integers that are a multiple of mult. 
######### For example, if lowNum=2, highNum=9, and mult=3, 
######### the loop should print 3, 6, 9 (on successive lines)
def flexible_counter(lowNum, highNum, multi):
    for i in range(lowNum, highNum + 1):
        if i % multi == 0:
            print(i)
        

flexible_counter(2, 21, 2)