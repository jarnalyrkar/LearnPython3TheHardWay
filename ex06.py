# Assigns a variable
types_of_people = 10
#puts the int variable inside a string
x = f"There are {types_of_people} types of people."


binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assigns a boolean value.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# prints the booleen "hilarious" using .format on another string
print(joke_evaluation.format(hilarious))

#Assigns two string variables
w = "This is the left side of..."
e = "a string with a right side."

#Concatinates the strings with +
print(w + e)