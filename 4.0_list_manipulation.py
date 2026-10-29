"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list containing eight monthly investment amounts in euros.
# 2. Process: Display the list, select one amount, sort the amounts from lowest to highest, and calculate the total invested.
# 3. Out: The complete list, the selected amount, the sorted list, and the total investment.
# 4. What my list is about, and what I computed from it: The list represents eight monthly investment contributions. I calculated the total amount invested to understand how much money was contributed over the period.


# Your code below
investments = [500, 650, 400, 750, 600, 900, 550, 800]

print("All investments:", investments)

print("Third month:", investments[2])

print("Sorted investments:", sorted(investments))

print("Total invested:", sum(investments))

print("First three months:", sum(investments[:3]))


# TEST RESULTS
# First three amounts: 500 + 650 + 400 = 1550.
# Python gives 1550, which is correct.
# The full list contains 8 investments.
# The sorted list is in ascending order.
# The total invested is 5150, as expected.
