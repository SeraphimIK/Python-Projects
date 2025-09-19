
# Seraphim Ikuomola
# 
# Part 1: Fibonacci Sequence
# This program generates the first 10 Fibonacci numbers
# and displays them in a column and then on one line.
# 
# Assign individual variables for the Fibonacci sequence
first = 0
second = 1
third = first + second
fourth = second + third
fifth = third + fourth
sixth = fourth + fifth
seventh = fifth + sixth
eighth = sixth + seventh
ninth = seventh + eighth
tenth = eighth + ninth
# Display them in a column
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(ninth)
print(tenth)

print()  # blank line for readability
# Display them on one line separated by commas
print(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, sep=", ")
