# Defines the function cheese_and_crackers which takes in two arguments; cheese_count and boxes_of_crackers
# It just prints out the two variables in a string-context.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
#We run the function from above, and directly pass numbers as arguments
cheese_and_crackers(20, 30)


print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Variables are set, and then sent with the function as arguments.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#math when setting arguments.
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# Variables with arithmetic, sent in as arguments.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# My own function:
# Calculates metric bmi
def bmiCalc(height, weight):
    bmi = (weight / (height*height)) * 10000
    print(f"Your BMI is {bmi}")

bmiCalc(171, 96)