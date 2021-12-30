# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Mike"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)	# with a comma
print("Hello " + str(name))	# with a +	-- this one should give us an error!

first_name = "Mike"
last_name = "Magruder"

print(f"Hello my name is {first_name} {last_name}")
print("Hello my name is {} {}" .format(first_name, last_name))


# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}" .format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string