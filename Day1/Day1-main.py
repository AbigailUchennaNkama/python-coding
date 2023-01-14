#EXERCISE 1
"""Write a program in main.py that prints: "Day 1 - Python Print Function
   The function is declared like this:
   print('what to print')
"""

#Print Function👇
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

#EXERCISE 2
""""There are errors in all of the lines of code. Fix the code so that it runs without errors.
#Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
"""
#Fixing/deburging the code.
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#EXERCISE 3
"""Write a program that prints the number of characters in a user's name."""

print(len(input("What is your name? ")))

#EXERCISE 4
"""Write a program that switches the values stored in the variables a and b."""
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c
print("a: " + a)
print("b: " + b)
