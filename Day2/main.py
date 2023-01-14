
#EXERCISE 1
"""Write a program that adds the digits
in a 2 digit number. e.g. if the input
was 35, then the output should be 3 + 5 = 8
"""
two_digit_number = input("Type a two digit number: ")
two_digit_number = str(two_digit_number)
a = int(two_digit_number[1])
b = int(two_digit_number[0])
print(a + b)


#EXERCISE 2 - BMI Calculator
"""Write a program that calculates the Body Mass Index (BMI) from a  user's weight and height"""
# BMI = weight / height^2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = int(weight) / (float(height) * float(height))
print(round(BMI))


#EXERCISE 3 - Life span calculator
""" Create a program using maths and f-Strings
    that tells us how many days, weeks, months and
    years we have left if we live until 90 years old.
    It will take your current age as the input and output
    a message with our time left in this format:
    You have x days, y weeks, and z months left.
"""

age = input("What is your current age? ")
Years_left = 90 - int(age)
days_left = 365 * int(Years_left)
weeks_left = 52 * int(Years_left)
months_left = 12 * int(Years_left)

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months and {Years_left} years left")



#EXERCISE 4 - Tip Calculator
"""
    Creat a program that calculates the individual bill of each person
    of a group of friends at a restaurant including the tip splited
    amongs them.
"""

bill = float(input("Enter bill: "))
tip = float(input("How much would you want to tip?(5%, 10%, 12%): "))
num_of_people = int(input("For how many people?: "))
tip_per_person = ((tip / 100) * bill) / num_of_people
Each_person = (bill / num_of_people) + tip_per_person
print(f"The bill for each person is {round(Each_person,2)}")
