########################################################################################
############################## ASSIGNMENT NUMBER ONE ###################################
########################################################################################
x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#1 # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def changeNum(num):
    print("x is currently: " +str(num))
    num[1][0] = 15
    print("x is now: " +str(num))

changeNum(x)


#2 # Change the last_name of the first student from 'Jordan' to 'Bryant'
def changeName(names):
    print("students is currently: " +str(names))
    names[0]['last_name'] = "Bryant"
    print("students is now: " +str(names))

changeName(students)


#3 # In the sports_directory, change 'Messi' to 'Andres'
def sports_figures(figures):
    print(figures)
    figures["soccer"][0] = "Andres"
    print(figures)

sports_figures(sports_directory)


#4 # Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]

def changeY(obj):
    print(obj)
    obj[0]['y'] = 30
    print(obj)

changeY(z)

########################################################################################
############################## ASSIGNMENT NUMBER TWO ###################################
########################################################################################

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and 
# prints each key and the associated value. For example, given the following list:

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(listNames):
    print(listNames)
    for i in listNames:
        print('first_name ' + '- ' +i['first_name'] + ', ' 'last_name ' + '- ' +i['last_name']  )

iterateDictionary(students) 



########################################################################################
############################## ASSIGNMENT NUMBER THREE #################################
########################################################################################

# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel
def iterateDictionary2(key, list):
    for i in list:
        print(i[key])

iterateDictionary2('last_name', students)


########################################################################################
############################## ASSIGNMENT NUMBER FOUR ##################################
########################################################################################

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. 
# For example:

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(list):
    count_locations = 0
    for i in list['locations']:
        print(i)
        count_locations += 1
    print('LOCATIONS: ' +str(count_locations))
    count_instructors = 0
    print(count_locations)
    for i in list['instructors']:
        print(i)
        count_instructors += 1
    print('LOCATIONS: ' +str(count_instructors))

printInfo(dojo)