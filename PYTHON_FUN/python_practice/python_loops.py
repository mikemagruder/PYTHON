for i in range(5):
    print(i)

for i in range(3, 5):
    print(i)

for i in range(1, 10, 2):
    print(i)

for x in 'Mike':
    print(x)

################## FOR LOOPS WITH LISTS #####################
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i], 'hello world')
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz


################## FOR LOOPS WITH DICTIONARIES ################
my_dict = { "name": "Mike", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Mike", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


############## WHILE LOOPS ##############################
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1


############### ELSE STATEMENTS #######################
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")