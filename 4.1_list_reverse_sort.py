"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list containing eight monthly investment amounts in euros.
# 2. Process: Reorder the investments in four different ways while keeping the original list unchanged.
# 3. Out: Display the four reordered lists and the original list to verify that it has not changed.
# 4. My four orders, and which ones modify the original:
#Ascending order: Lowest to highest investment.
#Descending order: Highest to lowest investment.
#Reversed order: Last investment to first.
#Shifted order: Move the first investment to the end.


# Your code below
investments = [500, 650, 400, 750, 600, 900, 550, 800]

# Ascending order
ascending = sorted(investments)
print("Ascending:", ascending)

# Descending order
descending = investments.copy()
descending.sort(reverse=True)
print("Descending:", descending)

# Reversed order
reversed_list = investments.copy()
reversed_list.reverse()
print("Reversed:", reversed_list)

# Shifted order
shifted = investments[1:] + investments[:1]
print("Shifted:", shifted)

print("Original list:", investments)

# TEST RESULTS
# Ascending: Correctly sorted from lowest to highest.
# Descending: Correctly sorted from highest to lowest.
# Reversed: Correctly reversed the original order.
# Shifted: Correctly moved the first item to the end.
# The original list remained unchanged.